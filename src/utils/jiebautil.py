#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-12

@author: Devin
"""
import os

import jieba
import jieba.analyse

from src.settings import BASE_PATH

jieba.load_userdict(
    os.path.join(BASE_PATH, "data/use_info_data/jieba_dict.txt"))


def jieba_split(f_path, cut_all=False):
    seg_list = []

    with open(f_path, 'rt', encoding='utf8') as f:
        content = f.read()
        seg_list = jieba.cut(content, cut_all=cut_all)
        # print("Full Mode: " + "/ ".join(seg_list))  # 全模式
        # tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True)
        # print("jieba.analyse.extract_tags: {0}".format(tags))
    return seg_list
