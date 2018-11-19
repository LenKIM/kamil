input_args = "https://www.naver.com/"  # args 변경할 것

search_query = "효성계열사"
site_naver = 'https://www.naver.com/'
total_page_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.paging_area._page_navi > div > span.page_number > strong.total._total_page'
page_others_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > ul > li > div > div.item_tit > a'
page_only_one_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a'
arrow_element_xpath = '//*[@id="main_pack"]/div[2]/div[2]/div[4]/div/a[2]'
chrome_driver_path = '/Users/len/Downloads/chromedriver'
wait_time = 3