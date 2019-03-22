# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup


# setup Driver|Chrome
driver = webdriver.Chrome('F:\\00.Nas\99.Coding\\00.MachineLearningStudy\\02.Crawling\\00.Module\chromedriver_win32\\chromedriver')
driver.implicitly_wait(3)

# Login
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('syncchrh')
driver.find_element_by_name('pw').send_keys('rmfls0811')
driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/input'
    ).click()

# Naver Pay
driver.get('https://order.pay.naver.com/home') ## Naver 페이 들어가기
html = driver.page_source ## 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())


# find_element_by_name('HTML_name')
# find_element_by_id('HTML_id')
# find_element_by_xpath('/html/body/some/xpath')
# find_element_by_css_selector('#css > div.selector')
# find_element_by_class_name('some_class_name')
# find_element_by_tag_name('h1'