# -*- coding: utf-8 -*-
import re
from typing import List

from sklearn.feature_extraction.text import CountVectorizer


class ObviousWord:

    def __init__(self) -> None:
        texts = []
        related_company = ['효성', '더클래스효성', '에이에스씨', '효성티앤에스', '진흥기업', '효성아이티엑스', '효성itx', '에프엠케이', 'FMK', '효성굿스프링스',
                           '효성캐피탈', '효성인포메이션시스템', '효성트랜스월드', '갤럭시아디바이스', '신화인터텍', '신성자동차', '효성토요타', '신동진',
                           '갤럭시아커뮤니케이션즈', '더프리미엄효성', '갤럭시아일렉트로닉스', '엔에이치테크', '갤럭시아에스엠', '엔에이치씨엠에스', '갤럭시아코퍼레이션',
                           '효성에프엠에스', '효성프리미어모터스', '아이티엑스마케팅', '평창풍력발전', '세빛섬', '공덕개발', '광주일보사', '공덕경우개발',
                           '트리니티에셋매니지먼트', '에이티엠플러스', '행복두드리미', '태안솔라팜', '에브리쇼', '동륭실업', '아승오토모티브그룹', '효성투자개발', '효성중공업']

        with open('/Users/len/kamill/tests/textures/sentences.txt', 'r', encoding='utf8') as input_file:
            with open('stopwords.txt', 'r') as fp:

                for index, line in enumerate(input_file):
                    line = re.sub('[^\w]', ' ', line)
                    words = [word for word in line.split() if '효성' in word]
                    new_str = ' '.join(words)
                    texts.append(new_str)

                    vect = CountVectorizer(ngram_range=(1, 1), stop_words=['효성', '효성은'])
                    matrix = vect.fit_transform(texts)

            freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]



            stopwords = [l.strip() for l in fp.readlines()]
            print(len(stopwords))
            stopword_pat_str = '|'.join(stopwords)
            sss = []
            ordered_companies = sorted(related_company, key=lambda a: len(a), reverse=True)

            for comp in ordered_companies:
                test_pat_str = '^' + comp + f'({stopword_pat_str})?$'
                test_pat = re.compile(test_pat_str)
                for key, val in freqs:
                    if re.match(test_pat, key) is not None:
                        sss.append(key)

    def load_word(self) -> List:
        pass


class AmbiguousWord:

    def __init__(self) -> None:
        super().__init__()

    def load_word(self) -> List:
        pass
