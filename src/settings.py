#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""
import logging
import os.path
from collections import OrderedDict
from logging.config import fileConfig

BASE_PATH = os.path.normpath(os.path.join(__file__, "../../"))
fileConfig(os.path.join(BASE_PATH, "etc/logger_config.ini"))

ALL_VECTOR = ['铝', '沪铝', '铝型材', '电解铝', '云铝股份', '铝制品', '铝质', '铝土', '铝厂', '铝合金', '铝箔', '铝棒', '铝业', '铝锭', '铝土矿', '铝板', '化铝', '铝制', '山铝业', '铝线', '氧化铝',
              '铜管', '纯铜', '阴极铜', '电解铜', '化铜', '铜精矿', '炼铜', '铜线', '铜业', '铜材', '铜合金', '废铜', '铜矿', '伦铜', '铜价', '氧化铜', '铜箔', '铜带', '铜厂', '粗铜', '沪铜', '硫酸铜', '炼铜厂', '铜板', '铜期货', '铜',
              '铅酸', '铅矿', '沪铅', '铅锌', '伦铅', '铅锌矿', '铅', '无铅',
              '锌板', '锌矿', '锌精矿', '铅锌', '锌粉', '氧化锌', '镀锌管', '锌锭', '锌', '镀锌', '镀锌板', '铅锌矿', '锌合金',
              'PVC', '塑料',
              '中铁', '钢铁股', '钢铁', '铁制', '高铁', '钢铁行业', '铁业', '铁轮', '钢铁业', '铁路', '炼铁', '铁板', '国际钢铁', '钢铁市场', '铁厂', '钢铁工业', '制铁', '铁路运输', '铁矿', '钢铁厂', '钢铁价格', '钢铁公司', '国铁', '钢铁工', '钢铁企业', '钢铁产业', '铁工', '铁', '铁矿石'
              ]
CLASSES_NUM = OrderedDict(Others=0, Al=1, Cu=2, Fe=3, PVC=4, Pb=5, Zn=6)
NUM_CLASS = {0: "Others", 1: "Al", 2: "Cu", 3: "Fe", 4: "PVC", 5: "Pb",
             6: "Zn"}

MONGO_DATABASE = {
    'host': '172.16.88.140',
    'port': 27017,
}

logging.info("读取settings文件完成")
