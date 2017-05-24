#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-23

@author: Devin
"""
from src.settings import MONGO_DATABASE
import logging


from pymongo import MongoClient

client = MongoClient(**MONGO_DATABASE)
db = client.data

logging.debug(db.news.find_one())
