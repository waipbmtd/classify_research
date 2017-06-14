#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-06-14

@author: Devin
"""
import logging
import re
import traceback

from pymongo import MongoClient

from src.settings import MONGO_DATABASE, RAW_TAG_CORRESPOND_WORDS


def raw_extract_tags(content, top_k):
    raw_tags = dict()
    for k, v_list in RAW_TAG_CORRESPOND_WORDS.items():
        k_dict = dict()
        for v in v_list:
            if content.count(v) > 0:
                k_dict[v] = content.count(v)
        if k_dict:
            raw_tags[k] = k_dict
    return raw_tags


def tags():
    """
    提取关键字
    :return:
    """
    logging.info("raw提取关键字")
    client = MongoClient(**MONGO_DATABASE)
    db = client.data
    for it in db.news.find({"$or": [{"human_tags": {"$exists": False}},
                                    {"human_tags": {"$regex": "^ *$"}}]}):
        try:
            title = it.get("title") if it.get("title") else ""
            title = "".join(title) if type(title) == list else title
            wc_content = it.get("content_text") if it.get(
                "content_text") else ""
            content = title + wc_content
            wc_tags = {}
            if content:
                wc_tags = raw_extract_tags(content, top_k=10)
            if not wc_tags:
                logging.info("关键字字典为空,忽略!")
                continue
            logging.info("关键字为:%s" % wc_tags)
            tags = ",".join([t for t in wc_tags if not re.match("[\d\.]+", t)])
            logging.debug("raw 提取关键字:{0}".format(tags))

            db.news.update_one({"_id": it.get("_id")},
                               {"$set": {"human_tags": tags}})
        except Exception as e:
            logging.error(
                "数据{0}raw提取关键词异常:{1}".format(content, traceback.format_exc()))
            continue


def summary():
    """
    简述提取
    :return:
    """
    logging.info("raw提取简述没有实现")
    pass
