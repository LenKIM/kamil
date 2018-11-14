import re

from bs4 import BeautifulSoup
from selenium import webdriver


class Main:

    def naver_crawler(self):

        chromedriver = '/Users/len/Downloads/chromedriver'
        query = '효성계열사'

        driver, html = self.get_page_source_by_query(chromedriver, query)
        soup = BeautifulSoup(html, 'html.parser')
        page_number = soup.select(
            '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.paging_area._page_navi > div > span.page_number > strong.total._total_page'
        )
        page_number = int(re.sub(r'\D', "", page_number[0].text))  # \d get Page totalNumber
        index = 1
        list_of_company = []

        while index < page_number:
            company_selector = soup.select(
                '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a'
            )
            for html_single in company_selector:
                a = BeautifulSoup(html_single.string, 'html.parser')
                list_of_company.append()
            driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[4]/div/a[2]').click()
            index = index + 1

        print(list_of_company)

    def get_page_source_by_query(self, chromedriver, query):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        driver = webdriver.Chrome(chromedriver)
        driver.implicitly_wait(3)  # to give some air
        driver.get('https://www.naver.com/')
        driver.find_element_by_id('query').send_keys(query)
        driver.find_element_by_xpath('//*[@id="search_btn"]').click()
        html = driver.page_source
        return driver, html

a =  Main()
a.naver_crawler()