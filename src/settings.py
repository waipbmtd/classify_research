#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""
import logging
import os.path
from collections import OrderedDict
from logging.config import dictConfig, fileConfig


BASE_PATH = os.path.normpath(os.path.join(__file__, "../../"))
fileConfig(os.path.join(BASE_PATH,"etc/logger_config.ini"))


# LOGGING_CONFIG = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'loggers': {
#         'root': {
#             'handlers': ['info_file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'infologger': {
#             'handlers': ['info_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'errorlogger': {
#             'handlers': ['error_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         }
#     },
#
#     'handlers': {
#         'info_file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_PATH, 'logs/mylog_info.log'),
#             'backupCount': 5,
#             'maxBytes': 50 * 1024 * 1024,
#             'formatter': 'verbose',
#         },
#         'error_file': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_PATH, 'logs/mylog_error.log'),
#             'backupCount': 5,
#             'maxBytes': 50 * 1024 * 1024,
#             'formatter': 'verbose',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(pathname)s [%(lineno)d]: %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#
# }
#
# dictConfig(LOGGING_CONFIG)

ALL_VECTOR = ['铝', '沪铝', '伦铝', '氧化铝', '沪铜', '伦铜', '铜', '铅', '伦铅',
              '沪铅', '铅锌', '锌精矿', '锌', '铁', '钢铁', 'PVC']
CLASSES_NUM = OrderedDict(Others=0, Al=1, Cu=2, Fe=3, PVC=4, Pb=5, Zn=6)
NUM_CLASS = {0: "Others", 1: "Al", 2: "Cu", 3: "Fe", 4: "PVC", 5: "Pb",
             6: "Zn"}

MONGO_DATABASE = {
    'host': '172.16.88.140',
    'port': 27017,
}

logging.info("读取settings文件完成")