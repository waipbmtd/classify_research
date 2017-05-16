#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""
import math


def mean(numbers):
    """
    计算平均值
    :param numbers:
    :return:
    """
    return sum(numbers) / float(len(numbers))


def stdev(numbers):
    """
    计算标准差
    :param numbers:
    :return:
    """
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(
        len(numbers) - 1)
    return math.sqrt(variance)


def calculate_probability(x, mean, stdev):
    """
    高斯分布计算某个值的概率
    :param x:
    :param mean: 平均值
    :param stdev: 标准差
    :return:
    """
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent
