#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import traceback
import logging

import pika

from settings import mq
from hanlder import run


class InfoServer(object):
    _connection = None
    _channel = None
    _conf = mq

    def __init__(self):
        self.handler = run

    def on_message(self, channel, method_frame, header_frame, body):
        logging.info('message arrive: %s' % body)
        try:
            self.handler(body)
        except Exception as e:
            logging.error("处理消息获得异常:%s", traceback.format_exc())
        finally:
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)


class SyncInfoServer(InfoServer):
    @property
    def channel(self):
        if not self._channel:
            self._channel = self.connection.channel()
            self._channel.exchange_declare(self._conf.get('exchange'),
                                           type=self._conf.get(
                                               'exchange_type'))
            self._channel.queue_declare(self._conf.get('queue'), exclusive=True)
            self._channel.queue_bind(exchange=self._conf.get('exchange'),
                                     routing_key=self._conf.get('routing_key'),
                                     queue=self._conf.get('queue'))
        return self._channel

    @property
    def connection(self):
        if not self._connection:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(self._conf.get('host')))
            self._connection = connection
        return self._connection

    def run(self):
        logging.debug('sync consumer...')
        while True:
            try:
                logging.info('start consuming...')
                self.channel.basic_consume(self.on_message,
                                           self._conf.get('queue'))
                self.channel.start_consuming()
            except pika.exceptions.ConnectionClosed:
                logging.error('lost connection...')
                logging.error('reconnect 5 seconds later...')
                self._channel = None
                self._connection = None
                time.sleep(5)
            except KeyboardInterrupt:
                logging.error('stop consuming...')
                self.channel.stop_consuming()
                self.channel.close()
                self.connection.close()
                break
            except Exception as e:
                logging.error(str(e))
                time.sleep(1)
            finally:
                pass