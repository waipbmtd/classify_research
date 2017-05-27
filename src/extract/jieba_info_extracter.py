#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-25

@author: Devin
"""
import logging
import re
import traceback

from pymongo import MongoClient
from snownlp import SnowNLP

from src.settings import MONGO_DATABASE
from src.utils.jiebautil import jieba_extract_tags


def tags():
    """
    提取关键字
    :return:
    """
    client = MongoClient(**MONGO_DATABASE)
    db = client.data
    for it in db.news.find({"machine_tags": {"$exists": False}}):
        try:
            title = it.get("title") if it.get("title") else ""
            title = "".join(title) if type(title) == list else title
            wc_content = it.get("content_text") if it.get(
                "content_text") else ""
            content = title + wc_content
            wc_tags = []
            if content:
                wc_tags = jieba_extract_tags(content, top_k=10)
            tags = ",".join([t for t in wc_tags if not re.match("[\d\.]+", t)])
            logging.debug("content:{0}".format(content))
            logging.debug("tags:{0}".format(tags))

            db.news.update_one({"_id": it.get("_id")},
                               {"$set": {"machine_tags": tags}})
        except Exception as e:
            logging.error(
                "数据{0}提取关键词异常:{1}".format(content, traceback.format_exc()))
            continue


def summary():
    """
    简述提取
    :return:
    """
    client = MongoClient(**MONGO_DATABASE)
    db = client.data
    for it in db.news.find({"machine_summary": {"$exists": False}}):
        content = it.get("content_text")
        title = it.get("title")
        try:
            if content is not None and content != "":
                content = content.strip()
                snownlp = SnowNLP(content)
                summary = snownlp.summary(1)
                logging.debug("content:{0}".format(content))
                logging.debug("summary:{0}".format(summary))
            elif title:
                summary = title if type(title) == list else [title]
                logging.debug("title:{0}".format(summary[0]))
                logging.debug("summary:{0}".format(summary))
            db.news.update_one({"_id": it.get("_id")},
                               {"$set": {"machine_summary": summary[0]}})
        except Exception as e:
            logging.error(
                "数据{0}提取简述异常:{1}".format(content, traceback.format_exc()))
            continue
