#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-12

@author: Devin
"""
import csv
import logging
import math
import os
import random

from src.models.naive_bayes import split_data_set, separate_by_class, \
    summarize, \
    predict, get_accuracy
from src.settings import BASE_PATH, ALL_VECTOR
from src.utils.jiebautil import jieba_split


def load_csv(filename):
    lines = csv.reader(open(filename, "rt"))
    data_set = list(lines)
    for i in range(len(data_set)):
        data_set[i] = [float(x) for x in data_set[i][:-1]] + [data_set[i][-1]]
    return data_set


def keyword_freq_vector(seq: list, keys: list, weight_1000: bool = False,
                        correct=True):
    vector = [seq.count(k) for k in keys]
    if weight_1000:
        sum_vector = int(math.fsum(vector))
        if sum_vector == 0:
            sum_vector = 1
        vector = [math.ceil(v * 1000 / sum_vector) for v in vector]
    vector = [v if v else random.randint(0, 3) for v in vector]
    return vector


def read_vector(f_path, weight_1000=True):
    """
    读取文章特征量向量
    :param f_path:
    :param weight_1000:
    :return:
    """
    t_seg_list = [x for x in jieba_split(f_path)]
    t_vector_freq = keyword_freq_vector(t_seg_list, ALL_VECTOR,
                                        weight_1000)
    return t_vector_freq


def reade_data(data_dir: str):
    """
    读取文件夹下所有文件特征量向量
    :param data_dir:
    :param category_list:
    :return:
    """
    for category in os.listdir(data_dir):
        category_dir = os.path.join(data_dir, category)
        if not os.path.isdir(category_dir):
            continue
        for parent, folders, files in os.walk(category_dir):
            logging.debug(
                "parent:{0},folders:{1},files:{2}".format(parent, folders,
                                                          files))
            for t_file_name in files:
                t_file_path = os.path.join(parent, t_file_name)
                t_vector_freq = read_vector(t_file_path, True)
                yield ','.join(
                    [str(i) for i in t_vector_freq + [category]]) + "\n"


def write_sample():
    """
    样本收集
    :param category_list:
    :return:
    """
    data_dir = os.path.join(BASE_PATH, 'data/use_info_data')
    data_path = os.path.join(data_dir, "data.csv")
    with open(data_path, 'w') as f:
        f.writelines(reade_data(data_dir))


def regression_test():
    """
    基于样本分为样本和测试回归测试
    :return:
    """
    filename = os.path.join(BASE_PATH, 'data/use_info_data/data.csv')
    data_set = load_csv(filename)
    logging.debug(
        'Loaded data file {0} with {1} rows'.format(filename, len(data_set)))

    train, test = split_data_set(data_set, 0.67)
    logging.debug(
        'Split {0} rows into train with {1} and test with {2}'.format(
            len(data_set), len(train), len(test)))

    separated = separate_by_class(train)
    logging.debug('Separated instances: {0}'.format(separated))

    gaussian_feature = dict()
    for key, value in separated.items():
        summary = summarize(value)
        gaussian_feature[key] = summary
        logging.debug(
            'Class: {0}  Attribute summaries: {1}'.format(key, summary))

    probabilities = []
    for input_vector in test:
        probabilitie = predict(gaussian_feature, input_vector)
        logging.debug('data {0} Probabilities for each class: {1}'.format(
            str(input_vector), probabilitie))
        probabilities.append(probabilitie)

    accuracy = get_accuracy(test, probabilities)
    logging.debug('Accuracy: {0}'.format(accuracy))


def article_test(f_path):
    """
    基于样本测试文档分类
    :param f_path:
    :return:
    """
    filename = os.path.join(BASE_PATH, 'data/use_info_data/data.csv')
    data_set = load_csv(filename)
    logging.debug(
        'Loaded data file {0} with {1} rows'.format(filename, len(data_set)))

    separated = separate_by_class(data_set)

    gaussian_feature = dict()
    for key, value in separated.items():
        summary = summarize(value)
        gaussian_feature[key] = summary
        logging.info(
            'Class: {0}  Attribute summaries: {1}'.format(key, summary))

    input_vector = read_vector(f_path)
    probabilitie = predict(gaussian_feature, input_vector)
    logging.info('data {0} Probabilities for each class: {1}'.format(
        str(input_vector), probabilitie))


if __name__ == "__main__":
    write_sample()
    # regression_test()
    article_test(os.path.join(BASE_PATH, "data/use_info_data/test.txt"))
