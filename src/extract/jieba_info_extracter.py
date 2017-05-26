#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-25

@author: Devin
"""
import logging
import traceback

from pymongo import MongoClient

from src.settings import MONGO_DATABASE
from src.utils.jiebautil import jieba_extract_tags


def tags():
    """
    提取关键字
    :return:
    """
    client = MongoClient(**MONGO_DATABASE)
    db = client.data
    for it in db.news.find({"machine_tags": {"$exists": False}}).limit(1):
        try:
            title = it.get("title") if it.get("title") else ""
            title = "".join(title) if type(title) == list else title
            wc_content = it.get("content_text") if it.get(
                "content_text") else ""
            content = title + wc_content
            wc_tags = ""
            if content:
                wc_tags = jieba_extract_tags(content, top_k=10)
            logging.debug("content:{0}, tags:{1}".format(content, wc_tags))

            # db.news.update_one({"_id": it.get("_id")},
            #                    {"$set": {"machine_tags": str_class}})
        except Exception as e:
            logging.error(
                "数据{0}提取关键词异常:{1}".format(content, traceback.format_exc()))
            continue


def resume():
    """
    简述提取
    :return:
    """
    logging.debug("extract:resume")
