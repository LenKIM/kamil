# -*- coding: utf-8 -*-
"""
네이버 검색페이지에서 효성 계열사라고 검색한 뒤, 계열사에 대한 정보 크롤링하는 프로그램.
"""
import re
import unittest

from bs4 import BeautifulSoup
from selenium import webdriver


def setoptions():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


class NaverCrawling(unittest.TestCase):

    def test_main(self):
        setoptions()

        naver = 'https://www.naver.com/'
        total_page_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.paging_area._page_navi > div > span.page_number > strong.total._total_page'
        page_others_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > ul > li > div > div.item_tit > a'
        page_only_one_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a'
        input = "https://www.naver.com/"  # args 변경할 것
        chromedriver_path = '/Users/len/Downloads/chromedriver'
        wait_time = 3

        driver = webdriver.Chrome(chromedriver_path)
        driver.implicitly_wait(wait_time)
        driver.get(naver)

        if input is naver:
            driver.find_element_by_id('query').send_keys('효성계열사')
            driver.find_element_by_xpath('//*[@id="search_btn"]').click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        page_number = soup.select(total_page_selector)
        page_number = int(re.sub(r'\D', "", page_number[0].text))

        company_selector = soup.select(page_only_one_selector)

        list_of_company = []
        for html_single in company_selector:
            self.append_soup_text(html_single, list_of_company)
        index = 0
        while index < page_number:
            index = index + 1
            driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[4]/div/a[2]').click()
            driver.implicitly_wait(wait_time)

            soup = driver.page_source
            soup = BeautifulSoup(soup, 'html.parser')
            company_selector = soup.select(page_others_selector)

            for html_single in company_selector:
                self.append_soup_text(html_single, list_of_company)

        print(list_of_company)
        self.assertEqual([], [])

    @staticmethod
    def append_soup_text(html_single, list_of_company):
        soup = BeautifulSoup(html_single.string, 'html.parser')
        list_of_company.append(soup.text)
