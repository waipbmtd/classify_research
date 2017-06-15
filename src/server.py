#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-06-15

@author: Devin
"""
import os
import sys
import redis
import logging

sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
os.chdir(os.path.abspath(os.path.join(__file__, "../")))

from src.settings import REDIS_URL
from src.classify.scikit import gnb_info_classfilter
from src.extract import jieba_info_extracter, raw_info_extracter


def run_classify():
    """
    启动分类
    :return:
    """
    gnb_info_classfilter.classify()


def run_extract():
    """
    启动提取
    :return:
    """
    jieba_info_extracter.tags()
    jieba_info_extracter.summary()
    raw_info_extracter.tags()


def run(*args):
    """

    :param kwargs:
    :return:
    """
    logging.info("接收到爬虫消息:%s" % args)
    run_classify()
    run_extract()
    logging.info("执行完到爬虫消息:%s" % args)


def main():
    r_client = redis.from_url(REDIS_URL)
    ps = r_client.pubsub()
    ps.subscribe(spider_test=run)
    [x for x in ps.listen()]

if __name__ == "__main__":
    main()
