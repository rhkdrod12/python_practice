from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


from bs4 import BeautifulSoup

import time
import requests

URL ="https://newtoki59.com/webtoon/90492?toon=%EC%99%84%EA%B2%B0%EC%9B%B9%ED%88%B0"

path = ".\\chromedriver"

driver = webdriver.Chrome(path)
actionChains = ActionChains(driver)
driver.get(URL)

time.sleep(1)




time.sleep(1)
driver.find_element_by_xpath("//*[@id='sticky-wrapper']/header/nav/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='mb_id']").send_keys("rhkdrod12")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='mb_password']").send_keys("rhkdwls")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='miso_sidelogin']/div[1]/div[1]/button").click()
textbox = "//*[@id='wr_content']"

for i in range(1,100):
    # # driver.find_element_by_xpath(textbox).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(textbox).send_keys("ㅅ")
    driver.find_element_by_xpath("//*[@id='btn_submit']").click()
    time.sleep(30)
    try:
        res = driver.find_elements_by_xpath("""//*[@id="content_wrapper"]/div[2]/div/div[4]/div[6]/a""")
        html = res[0].get_attribute('href')
        print(html)
        driver.get(html)
    except:
        print("실패")
        res = driver.find_elements_by_xpath("""//*[@id="content_wrapper"]/div[2]/div/div[4]/div[6]/a""")
        html = res[0].get_attribute('href')
        print(html)
        driver.get(html)

# driver.close()



