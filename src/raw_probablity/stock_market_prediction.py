#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-16

@author: Devin
"""
from src.settings import *
import datetime
import logging

import pandas_datareader.data as web

start = datetime.datetime(2017, 1, 1)
end = datetime.date.today()

apple = web.DataReader("AAPL", "google", start, end)

logging.debug("type(apple) {0}".format(str(type(apple))))

apple.head()
