# -*- coding: utf-8 -*-
from typing import List


def get_stopwords_from_file() -> List:
    """
    불용어만 따로 파일로 만든거 load
    :return:
    """
    with open('/Users/len/kamill/stopwords.txt', 'r', encoding='utf-8') as fp:
        return [a.strip() for a in fp.readlines()]