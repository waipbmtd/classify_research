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

# jieba加载用户自定义字典
jieba.load_userdict(
    os.path.join(BASE_PATH, "data/use_info_data/jieba_dict.txt"))


def jieba_split(f_path, cut_all=False):
    with open(f_path, 'rt', encoding='utf8') as f:
        content = f.read()
        seg_list = jieba.cut(content, cut_all=cut_all)
    return seg_list


def jieba_split_content(content, cut_all=False):
    return jieba.cut(content, cut_all=cut_all)