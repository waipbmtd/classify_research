#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-07-21

@author: Devin
"""
from settings import *
from server import SyncInfoServer


if __name__ == '__main__':
    logging.info("分析模块启动")
    SyncInfoServer().run()
    logging.info("分析模块结束")