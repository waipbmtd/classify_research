#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2017-05-12

@author: Devin
"""
import copy
import logging
import os
from operator import itemgetter

import jieba
import jieba.analyse
from jieba.analyse import TFIDF

from src.settings import BASE_PATH

# jieba加载用户自定义字典
jieba.load_userdict(
    os.path.join(BASE_PATH, "data/use_info_data/jieba_dict.txt"))


class USE_TFIDF(TFIDF):
    def extract_tags(self, sentence, topK=20, withWeight=False, allowPOS=(),
                     withFlag=False):
        """
        Extract keywords from sentence using TF-IDF algorithm.
        Parameter:
            - topK: return how many top keywords. `None` for all possible words.
            - withWeight: if True, return a list of (word, weight);
                          if False, return a list of words.
            - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v','nr'].
                        if the POS of w is not in this list,it will be filtered.
            - withFlag: only work with allowPOS is not empty.
                        if True, return a list of pair(word, weight) like posseg.cut
                        if False, return a list of words
        """
        if allowPOS:
            allowPOS = frozenset(allowPOS)
            words = self.postokenizer.cut(sentence)
        else:
            words = self.tokenizer.cut(sentence, cut_all=False, HMM=False)
        freq = {}
        for w in words:
            logging.debug("分词:{0}".format(w))
            if allowPOS:
                if w.flag not in allowPOS:
                    continue
                elif not withFlag:
                    w = w.word
            wc = w.word if allowPOS and withFlag else w
            if len(wc.strip()) < 2 or wc.lower() in self.stop_words:
                continue
            freq[w] = freq.get(w, 0.0) + 1.0
        total = sum(freq.values())
        for k in freq:
            kw = k.word if allowPOS and withFlag else k
            freq[k] *= self.idf_freq.get(kw, self.median_idf) / total

        if withWeight:
            tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
        else:
            tags = sorted(freq, key=freq.__getitem__, reverse=True)
        if topK:
            return tags[:topK]
        else:
            return tags


def jieba_split(f_path, cut_all=True):
    with open(f_path, 'rt', encoding='utf8') as f:
        content = f.read()
        seg_list = jieba.cut(content, cut_all=cut_all, HMM=False)
    return seg_list


def jieba_split_content(content, cut_all=True):
    return jieba.cut(content, cut_all=cut_all, HMM=False)


def jieba_extract_tags(sentence, top_k=20, with_weight=False, allow_pos=()):
    use_tfidf = USE_TFIDF()
    return use_tfidf.extract_tags(sentence, top_k, with_weight, allow_pos)
