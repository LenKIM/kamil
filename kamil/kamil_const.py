input_args = "https://www.naver.com/"  # args 변경할 것

search_query = "효성계열사"
site_naver = 'https://www.naver.com/'
total_page_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.paging_area._page_navi > div > span.page_number > strong.total._total_page'
page_others_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > ul > li > div > div.item_tit > a'
page_only_one_selector = '#main_pack > div.sp_company_list.sc._au_company_search._company_list > div.api_subject_bx > div.content_area > ul > li > div > div.item_tit > a'
arrow_element_xpath = '//*[@id="main_pack"]/div[2]/div[2]/div[4]/div/a[2]'
chrome_driver_path = '/Users/len/Downloads/chromedriver'
wait_time = 3

const_subsidiary_companies = ['효성', '더클래스효성', '에이에스씨', '효성티앤에스', '진흥기업', '효성아이티엑스', '효성itx', '에프엠케이', 'FMK', '효성굿스프링스',
                         '효성캐피탈', '효성인포메이션시스템', '효성트랜스월드', '갤럭시아디바이스', '신화인터텍', '신성자동차', '효성토요타', '신동진',
                         '갤럭시아커뮤니케이션즈', '더프리미엄효성', '갤럭시아일렉트로닉스', '엔에이치테크', '갤럭시아에스엠', '엔에이치씨엠에스', '갤럭시아코퍼레이션',
                         '효성에프엠에스', '효성프리미어모터스', '아이티엑스마케팅', '평창풍력발전', '세빛섬', '공덕개발', '광주일보사', '공덕경우개발',
                         '트리니티에셋매니지먼트', '에이티엠플러스', '행복두드리미', '태안솔라팜', '에브리쇼', '동륭실업', '아승오토모티브그룹', '효성투자개발', '효성중공업']


ban_word = ['실효성','실효성을','실효성이','실효성에','유효성','유효성을','이효성','유효성과','유효성이','실효성은','유효성분을','전효성']
# 실효성, 유효성, 전효성, 이효성, 유효성분