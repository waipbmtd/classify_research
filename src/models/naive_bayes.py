#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-11

@author: Devin
"""

import random

from src.utils.mathutil import mean, stdev, calculate_probability


def split_data_set(data_set, split_ratio):
    """
    收集的样本特征数据拆分成测试和回归数据集
    :param data_set:
    :param split_ratio:
    :return:
    """
    train_size = int(len(data_set) * split_ratio)
    train_set = []
    copy = list(data_set)
    while len(train_set) < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy.pop(index))
    return [train_set, copy]


def separate_by_class(data_set):
    """
    将特征数据按类别分类
    :param data_set:
    :return:
    """
    separated = {}
    for i in range(len(data_set)):
        vector = data_set[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def summarize(dataset):
    """
    计算高斯分布需要的平均值和标准差
    :param dataset:
    :return:
    """
    r_dataset = [x for x in zip(*dataset)][:-1]
    summaries = [(mean(attribute), stdev(attribute)) for attribute in
                 r_dataset]
    return summaries


def calculate_class_probabilities(summaries, inputVector):
    """
    计算向量属于各个类别的相对可能性
    :param summaries:
    :param inputVector:
    :return:
    """
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculate_probability(x, mean, stdev)
    return probabilities


def predict(summaries, input_vector):
    """
    获取最大概率类别
    :param summaries:
    :param input_vector:
    :return:
    """
    probabilities = calculate_class_probabilities(summaries, input_vector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def get_accuracy(test_set, predictions):
    """
    计算正确率
    :param test_set:
    :param predictions:
    :return:
    """
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_set))) * 100.0
