#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""
import os.path
from collections import OrderedDict
from logging.config import fileConfig

BASE_PATH = os.path.normpath(os.path.join(__file__, "../../"))

fileConfig(os.path.join(BASE_PATH, 'etc/logger_config.ini'))

ALL_VECTOR = ['铝', '沪铝', '伦铝', '氧化铝', '沪铜', '伦铜', '铜', '铅', '伦铅',
              '沪铅', '铅锌', '锌精矿', '锌', '铁', '钢铁', 'PVC']
CLASSES_NUM = OrderedDict(Others=0, Al=1, Cu=2, Fe=3, PVC=4, Pb=5, Zn=6)
NUM_CLASS = {0:"Others", 1:"Al", 2:"Cu", 3:"Fe", 4:"PVC", 5:"Pb", 6:"Zn"}

MONGO_DATABASE = {
    'host': '172.16.88.140',
    'port': 27017,
}
