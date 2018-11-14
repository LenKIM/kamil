import re
import unittest

from sklearn.feature_extraction.text import CountVectorizer


class CountWordsTests(unittest.TestCase):

    def test_frequently_work(self):
        texts = []
        with open('/Users/len/kamill/tests/textures/sentences.txt', 'r', encoding='utf8') as input_file:
            for index, line in enumerate(input_file):
                line = re.sub('[^\w]', ' ', line)
                words = [word for word in line.split() if '효성' in word]
                new_str = ' '.join(words)
                texts.append(new_str)

        vect = CountVectorizer(ngram_range=(1, 1))
        matrix = vect.fit_transform(texts)
        print(len(vect.get_feature_names()))
        vect = CountVectorizer(ngram_range=(1, 1))
        matrix = vect.fit_transform(texts)
        print(len(vect.get_feature_names()))
        freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]
        # sort from largest to smallest

        for phrase, times in sorted(freqs, key=lambda x: -x[1])[:150]:
            print(phrase, times)
