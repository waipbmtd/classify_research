#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-24

@author: Devin
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))
os.chdir(os.path.abspath(os.path.join(__file__, "../")))
from src.settings import logging

import argparse

from importlib import import_module


def parse_args():
    parser = argparse.ArgumentParser(description='机器学习小工具', epilog="机器学习小工具")
    parser.add_argument("-a", "--actions", nargs='?',
                        choices=["classify", "extract"],
                        required=True,
                        help="需要执行的操作, classifier:分类. extracter:提取关键词和简述")

    parser.add_argument("-c", '--classifier', choices=['raw', 'scikit'],
                        default="scikit", help="分类器选择")
    parser.add_argument("-als", '--algorithms', choices=['gnb'],
                        default="gnb", help="分类算法选择")
    parser.add_argument("-cd", '--class_do',
                        choices=["train", "classify", "regression"],
                        nargs='*', default=["train", "classify"],
                        help='机器分类的具体操作')

    parser.add_argument("-e", '--extracter', choices=["jieba"],
                        default="jieba", help="提取工具选择")
    parser.add_argument("-ed", '--extract_do', choices=["tags", "summary"],
                        default=["tags", "resume"], nargs='*',
                        help="提取具体操作")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    logging.info("开始")
    args = parse_args()
    actions = args.actions
    if "classify" in actions:
        classifier = args.classifier
        algorithms = args.algorithms
        does = args.class_do
        logging.debug("执行参数:classify %s %s %s", classifier, algorithms,
                      does)
        cf = import_module(
            "src.classify.%s.%s_info_classfilter" % (
                classifier, algorithms))
        [exec("cf.%s()" % s) for s in does]
    if "extract" in actions:
        extracter = args.extracter
        does = args.extract_do
        logging.debug("执行参数: extract {0} {1} ".format( extracter, does))
        et = import_module("src.extract.%s_info_extracter" % extracter)
        [exec("et.%s()" % s) for s in does]

    logging.debug("完成")
