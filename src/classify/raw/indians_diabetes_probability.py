#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-12

@author: Devin
"""
import csv
import logging
import os

from src.models.naive_bayes import split_data_set, separate_by_class, summarize, \
    predict, get_accuracy
from src.settings import BASE_PATH


def load_csv(filename):
    lines = csv.reader(open(filename, "rt"))
    data_set = list(lines)
    for i in range(len(data_set)):
        data_set[i] = [float(x) for x in data_set[i]]
    return data_set


if __name__ == "__main__":
    filename = os.path.join(BASE_PATH,
                            'data/indians_diabetes_data/pima-indians-diabetes.data.csv')
    data_set = load_csv(filename)
    logging.info('Loaded data file {0} with {1} rows'.format(filename, len(data_set)))

    train, test = split_data_set(data_set, 0.67)
    logging.info('Split {0} rows into train with {1} and test with {2}'.format(
        len(data_set), len(train), len(test)))

    separated = separate_by_class(train)

    gaussian_feature = dict()
    for key, value in separated.items():
        summary = summarize(value)
        gaussian_feature[key] = summary
        logging.info('Class: {0}  Attribute summaries: {1}'.format(key, summary))

    probabilities = []
    for input_vector in test:
        probabilitie = predict(gaussian_feature, input_vector)
        logging.info('data {0} Probabilities for each class: {1}'.format(
            str(input_vector), probabilitie))
        probabilities.append(probabilitie)

    accuracy = get_accuracy(test, probabilities)
    logging.info('Accuracy: {0}'.format(accuracy))
