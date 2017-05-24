#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-24

@author: Devin
"""
import logging
import math
import os
import random

from pymongo import MongoClient
from sklearn.naive_bayes import GaussianNB

from src.settings import ALL_VECTOR, CLASSES_NUM, MONGO_DATABASE, BASE_PATH, \
    NUM_CLASS
from src.utils import datasetutil
from src.utils.jiebautil import jieba_split, jieba_split_content

SAMPLE_DIR = os.path.join(BASE_PATH, "data/use_info_data")
DATASET_PATH = os.path.join(BASE_PATH, "data/use_info_data/data_set.csv")


def keyword_freq_vector(seq: list, keys: list, weight_1000: bool = False):
    """
    获取关键字词频向量
    :param seq:
    :param keys:
    :param weight_1000:
    :return:
    """
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


def read_content_vector(content, weight_1000=True):
    """
    读取文章特征量向量
    :param f_path:
    :param weight_1000:
    :return:
    """
    t_seg_list = [x for x in jieba_split_content(content)]
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
    sample_num = 0
    feature_num = len(ALL_VECTOR)

    for category in os.listdir(data_dir):
        category_dir = os.path.join(data_dir, category)
        if not os.path.isdir(category_dir):
            continue
        class_num = CLASSES_NUM.get(category)

        for parent, folders, files in os.walk(category_dir):
            logging.debug(
                "parent:{0},folders:{1},files:{2}".format(parent, folders,
                                                          files))
            sample_num += len(files)
            for t_file_name in files:
                t_file_path = os.path.join(parent, t_file_name)
                t_vector_freq = read_vector(t_file_path, True)
                yield ','.join(
                    [str(i) for i in t_vector_freq + [class_num]]) + "\n"
    yield ",".join(
        [str(sample_num), str(feature_num)] + list(CLASSES_NUM.keys())) + "\n"


def sample2dataset(sample_dir: str, dataset_path: str):
    """
    将样本转化为dataset
    :param sample_dir:
    :param dataset_path:
    :return:
    """
    with open(dataset_path, 'w') as f:
        sample_vectors = list(reade_data(sample_dir))
        sample_vectors.insert(0, sample_vectors.pop(-1))
        f.writelines(sample_vectors)


def gaussian_model(dataset_path: str):
    iris = datasetutil.load_info(dataset_path)
    return GaussianNB().fit(iris.data, iris.target)


def update_db_class(dataset_path: str):
    gnb = gaussian_model(dataset_path)

    client = MongoClient(**MONGO_DATABASE)
    db = client.data
    for it in db.news.find({"machine_class": {"$exists": False}}):
        wc_content = it.get("content_text")
        wc_vector = read_content_vector(wc_content)
        num_class = gnb.predict([wc_vector])
        str_class = NUM_CLASS.get(int(num_class))
        logging.debug("class:{0}, content:{1}".format(str_class, wc_content))

        db.news.update_one({"_id": it.get("_id")},
                           {"$set": {"machine_class": str_class}})


def train():
    sample2dataset(SAMPLE_DIR, DATASET_PATH)


def classify():
    update_db_class(DATASET_PATH)
