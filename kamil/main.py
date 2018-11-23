import re

from kamil.helpers.file_helpers import get_frequent_counted_companies_from_file, get_total_text_from_files
from kamil.helpers.stop_word_helpers import get_stopwords_from_file
from kamil.kamil_const import const_subsidiary_companies

stopwords = get_stopwords_from_file()
removed_special_texts, origin_texts = get_total_text_from_files()

passed_sentences = open('valid_sentences.txt', 'w', encoding='utf8')
not_passed_sentences = open('valid_not_sentences.txt', 'w', encoding='utf8')
not_yet_passed_sentences = open('unsure_sentences.txt', 'w', encoding='utf8')

must_words = []
must_not_words = ["실효성", "유효성", "전효성", "이효성", "유효성분", "원효성지", "발효성분"]
must_not_words = '|'.join(must_not_words)
must_not_only_words_pattern = '(' + must_not_words + ')'

stop_words_pattern = '|'.join(stopwords)
must_not_words_pattern = '(' + must_not_words + ')(' + stop_words_pattern + ')'
frequency_company = get_frequent_counted_companies_from_file()
ordered_companies = sorted(const_subsidiary_companies, key=lambda a: len(a), reverse=True)

for company in ordered_companies:
    subsidiary_company_with_stop_words_pattern = '^' + company + f'({stop_words_pattern})?$'
    subsidiary_company_with_stop_words_pattern = re.compile(subsidiary_company_with_stop_words_pattern)

    for key, value in frequency_company:
        if re.match(subsidiary_company_with_stop_words_pattern, key) is not None:
            must_words.append(key)

must_words_text = '|'.join(must_words)
must_only_words_pattern = '(' + must_words_text + ')'
must_words_text_pattern = '(' + must_words_text + ')+(' + stop_words_pattern + ')'

# 전처리를 위한 패턴 생성 완료
for index, text in enumerate(removed_special_texts):
    if re.search(must_not_words_pattern, text):
        result = str(origin_texts[index]).strip() + '0' + '\n'
        not_passed_sentences.write(result)
    elif re.search(must_not_only_words_pattern, text):
        result = str(origin_texts[index]).strip() + '0' + '\n'
        not_passed_sentences.write(result)
    elif re.search(must_words_text_pattern, text):
        result = str(origin_texts[index]).strip() + '1' + '\n'
        passed_sentences.write(result)
    elif re.search(must_only_words_pattern, text):
        result = str(origin_texts[index]).strip() + '1' + '\n'
        passed_sentences.write(result)
    else:
        not_yet_passed_sentences.write(origin_texts[index])

passed_sentences.close()
not_passed_sentences.close()
not_yet_passed_sentences.close()
# 라벨 0
# 라벨 1

# Not yet


# 각 종목들.
