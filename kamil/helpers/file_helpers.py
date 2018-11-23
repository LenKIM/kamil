# -*- coding: utf-8 -*-
import re

from sklearn.feature_extraction.text import CountVectorizer


def get_total_text_from_files():
    with open('/Users/len/kamill/tests/textures/sentences.txt', 'r', encoding='utf8') as text_file:
        list = []
        origin_texts = []
        for index, line in enumerate(text_file):
            removed_special_char_line = re.sub('[^\w]', ' ', line)
            list.append(removed_special_char_line)
            origin_texts.append(line)
        return list, origin_texts


def get_frequent_counted_companies_from_file():
    removed_special_char, total_texts = get_total_text_from_files()
    texts = []
    for index, line in enumerate(removed_special_char):
        words = [word for word in line.split() if '효성' in word]
        new_str = ' '.join(words)
        texts.append(new_str)

    vect = CountVectorizer(ngram_range=(1, 1))
    matrix = vect.fit_transform(texts)
    freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]
    return freqs
