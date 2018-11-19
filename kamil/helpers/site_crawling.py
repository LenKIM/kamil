# -*- coding: utf-8 -*-
# ! /usr/bin/env python3

"""
네이버 검색페이지에서 효성 계열사라고 검색한 뒤, 계열사에 대한 정보 크롤링하는 프로그램.
"""
import re
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver

from kamil.kamil_const import *


def set_webdriver_options():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")


def until_total_page(index, page_number):
    return index < page_number


class SiteCrawling:
    html_parser = 'html.parser'

    def __init__(self) -> None:
        super().__init__()

    def start_crawling(self) -> List:
        set_webdriver_options()

        driver = webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(wait_time)
        driver.get(site_naver)

        if input_args is site_naver:
            driver.find_element_by_id('query').send_keys(search_query)
            driver.find_element_by_xpath('//*[@id="search_btn"]').click()

        soup = BeautifulSoup(driver.page_source, self.html_parser)

        total_page = soup.select(total_page_selector)
        total_page = int(re.sub(r'\D', "", total_page[0].text))

        company_selector = soup.select(page_only_one_selector)

        list_of_company = []
        for html_single in company_selector:
            self.append_soup_text(html_single, list_of_company, self.html_parser)

        current_page = 0
        while until_total_page(current_page, total_page):
            current_page = current_page + 1

            driver.find_element_by_xpath(arrow_element_xpath).click()
            driver.implicitly_wait(wait_time)

            soup = driver.page_source
            soup = BeautifulSoup(soup, self.html_parser)
            company_selector = soup.select(page_others_selector)

            for html_single in company_selector:
                self.append_soup_text(html_single, list_of_company, self.html_parser)
        return list_of_company

    @staticmethod
    def append_soup_text(html_single, list_of_company, html_parser):
        soup = BeautifulSoup(html_single.string, html_parser)
        list_of_company.append(soup.text)


if __name__ == '__main__':
    SiteCrawling().start_crawling()
