import re
import unittest

from bs4 import BeautifulSoup
from selenium import webdriver


class crawl_tests(unittest.TestCase):

    def test_main(self):
        options = webdriver.ChromeOptions()

        options.headless = True
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        driver = webdriver.Chrome('/Users/len/Downloads/chromedriver')
        driver.implicitly_wait(3)

        driver.get('https://www.naver.com/')
        driver.find_element_by_id('query').send_keys('효성계열사')
        driver.find_element_by_xpath('//*[@id="search_btn"]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        page_number = soup.select(
            '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.paging_area._page_navi > div > span.page_number > strong.total._total_page'
        )
        page_number = re.sub(r'\D', "", page_number[0].text)  # \d
        page_number = int(page_number)
        index = 0
        list_of_company = []

        company_selector = soup.select(
            '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a'
        )
        # main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a
        # main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > ul > li > div > div.item_tit > a
        for html_single in company_selector:
            a = BeautifulSoup(html_single.string, 'html.parser')
            list_of_company.append(a.text)

        while index < page_number:
            driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[4]/div/a[2]').click()
            driver.implicitly_wait(3)
            index = index + 1
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            company_selector = soup.select(
                '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > ul > li > div > div.item_tit > a'
            )
            for html_single in company_selector:
                a = BeautifulSoup(html_single.string, 'html.parser')
                list_of_company.append(a.text)
        re.match('r[^(a|b|c)].+', "aaaa")
        print(list_of_company)
        self.assertEqual([], [])
