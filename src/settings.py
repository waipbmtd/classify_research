#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""
import os.path
from logging.config import fileConfig

BASE_PATH = os.path.normpath(os.path.join(__file__, "../../"))

fileConfig(os.path.join(BASE_PATH, 'etc/logger_config.ini'))

ALL_CATEGORY = ['Al', 'Cu', 'Pb', 'Zn']
ALL_VECTOR = ['铝', '沪铝', '伦铝', '沪铜', '伦铜', '铜', '铅', '伦铅', '沪铅', '铅锌', '锌精矿',
              '锌']
