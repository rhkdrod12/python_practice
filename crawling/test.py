from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests


class DB:
    # 크롬드라이버 경로
    Chromedrive_path = ".\\chromedriver"

    # 쿠팡 메인 URL
    Coupang_URL = "https://www.coupang.com/"
    # 쿠팡 카테코리 URL
    Coupang_category_URL = "https://www.coupang.com/np/campaigns/82"
    # 쿠팡 로그인 URL
    Coupang_Login_URL = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang." \
                        "com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252Fnp%25" \
                        "2Fcampaigns%252F82"

    # 항목 60개
    Coupang_category_60qty = """//*[@id="searchSortingList"]/ul/li[1]"""
    # 항목 120개
    Coupang_category_120qty = """//*[@id="searchSortingList"]/ul/li[2]"""

    # 로그인 이동 xpath
    Login_xpath = """//*[@id="login"]/a"""
    # 아이디 xpath
    Id_locate_xpath = """//*[@id="login-email-input"]"""
    # 패스워드 xpath
    Passward_locate_xpath = """//*[@id="login-password-input"]"""
    # 로그인 클릭 xpath
    Login_botton_xpath = "/html/body/div[1]/div/div/form/div[5]/button"
    # 카테고리 xpath
    category_xpath = """//*[@id="searchOptionForm"]/div/div/div[1]/div[3]"""


class crwaling:
    def __init__(self, URL, driver_path):
        # 쿠팡 URL
        self.URL = URL  # "https://www.coupang.com/"
        # 크롬 드라이버 경로(현재 작업폴더 경로)
        self.path = driver_path  # ".\\chromedriver"

    def chromeBeign(self):
        # 크롬 실행
        self.driver = webdriver.Chrome(self.path)
        # URL로 이동
        self.driver.get(self.URL)

    def move_xpath(self, xpath):
        data = self.driver.find_element_by_xpath(xpath)
        href = data.get_attribute("href")
        self.driver.get(href)

    def move_url(self, url):
        self.driver.get(url)

    def get_data(self, clas, clas_name):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data = soup.find_all(clas, clas_name)
        # data = soup.find_all('div',{'class':'baby-item'})
        return data

    def data_list(self, data, search_data):
        items = []
        for div in data:
            title = div.get_text().strip()
            link = div.a.get(search_data)
            link = DB.Coupang_URL+link
            items.append([title, link])
        return items

    def sendkey(self, xpath, value):
        data = self.driver.find_element_by_xpath(xpath)
        data.send_keys(value)

    def click(self, xpath):
        data = self.driver.find_element_by_xpath(xpath).click()

    def next_page(self):
        URL = self.driver.current_url
        if "page" in URL:
            current_page = int(URL[-1])+1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        self.driver.get(URL)



if __name__ == '__main__':

    # Coupang = crwaling(DB.Coupang_Login_URL, DB.Chromedrive_path)
    # Coupang.chromeBeign()
    # time.sleep(1)
    # Coupang.sendkey(DB.Id_locate_xpath, "rhkdrod12@naver.com")
    # Coupang.sendkey(DB.Passward_locate_xpath, "zxc!7516155")
    # Coupang.click(DB.Login_botton_xpath)
    # time.sleep(1)
    #
    # print("로그인 완료")
    # time.sleep(1)

    Coupang = crwaling(DB.Coupang_category_URL, DB.Chromedrive_path)
    Coupang.chromeBeign()
    time.sleep(1)

    Category = Coupang.get_data('div', {'class':'baby-item'})
    Category_list = Coupang.data_list(Category,'href')

    print(Category_list)

    Coupang.move_url(Category_list[1][1])
    time.sleep(1)

    # 60항목 -> 120항목으로 변경
    # Coupang.click(DB.Coupang_category_60qty)
    # Coupang.click(DB.Coupang_category_60qty)
    # time.sleep(1)
    # Coupang.click(DB.Coupang_category_120qty)
    # time.sleep(1)

    Coupang.next_page()
    time.sleep(1)
    Coupang.next_page()

    # 현재화면 아이템 URL가져오기
        items = Coupang.get_data('li', {'class':'baby-product renew-badge'})
        items_list = Coupang.data_list(items,'href')

    items_URL = []
    for list in items_list:
        items_URL.append(list[1])

    print(items_URL)
    Coupang.move_url(items_URL[0])
    item_state = Coupang.get_data('div', {'class':'prod-option__item'})
    print(item_state[0])
    a = item_state[0].div.div.button.get('class')

    if 'single' == a[1]:
        print("진입완료")

        





