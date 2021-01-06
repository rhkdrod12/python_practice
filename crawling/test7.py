from selenium import webdriver
from bs4 import BeautifulSoup
from DB import DB

import  re
import  time

class crwaling:
    # 크롬드라이버를 사용하여 크롬 실행
    def chromeBeign(self, URL, driver_path):
        # 쿠팡 URL
        self.URL = URL  # "https://www.coupang.com/"
        # 크롬 드라이버 경로(현재 작업폴더 경로)
        self.path = driver_path  # ".\\chromedriver"

        # 크롬 실행
        global driver
        driver = webdriver.Chrome(self.path)
        # URL로 이동
        driver.get(self.URL)
        return driver

    # url로 이동
    def move_url(self, url):
        driver.get(url)

    # xpath로 이동
    def move_xpath(self, xpath):
        data = driver.find_element_by_xpath(xpath)
        href = data.get_attribute("href")
        driver.get(href)

    # xpath로 value값 보내기
    def sendkey(self, xpath, value):
        data = driver.find_element_by_xpath(xpath)
        data.send_keys(value)

    # xpath로 클릭하기
    def click(self, xpath):
        driver.find_element_by_xpath(xpath).click()

    # 해당 테그안 내용을 전부 가져오기
    def get_data(self, *args):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        data = soup.find_all(args[0], args[1])
        # data = soup.find_all('div',{'class':'baby-item'})
        return data

    # xpath쪽 텍스트 가져오기
    def get_title(self, xpath):
        text = driver.find_element_by_xpath(xpath).text
        return text

    # 제목, search_data 내용을 dic으로 반납
    def get_URL_dic(self, data):
        items = {}
        for div in data:
            title = div.get_text().strip()
            link = div.a.get('href')
            link = DB.Coupang_URL + link
            items[title] = link
            # items.append([title, link])
        return items

    # 테그명과 클래스, 클래스명을 받아서 그 안의 텍스트를 반환
    def get_text(self, tag, class_):
        text = self.get_data(tag, class_)
        text = text[0].text
        return text

    # 제목, search_data 내용을 list으로 반납
    def get_URL_list(self, data):
        items = []
        for div in data:
            title = div.get_text().strip()
            link = div.a.get('href')
            link = DB.Coupang_URL + link
            items.append([title, link])
        return items

    # 다음 페이지로 이동(URL 형태로)
    def next_page(self):
        URL = driver.current_url
        if "page" in URL:
            current_page = int(URL[-1]) + 1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        driver.get(URL)

    # 현재 화면 URL 얻기
    def current_URL(self):
        return driver.current_url

    # css항목을 검색하여 잇으면 1을 반환
    def item_type(self, name):
        try:
            driver.find_element_by_css_selector(name)
            return 1
        except:
            return 0

    # 해당 화면에서 텍스트들을 하나라도 포함하고 잇으면 1를 내보냄
    def find_str(self, *args):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # 정규식을 사용하여 str 내용을 포함하는 태그를 가져옴
        for text in args:
            name = soup.find_all(text=re.compile(text+'+'))
            if len(name) > 0:
                return 1

        # print("name:", name)
        #
        # if len(name) > 0:
        #     return 1
        # else:
        #     return 0

    # 크롬 종료
    def close(self):
        driver.close()

