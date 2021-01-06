import time

from setup import begin
from bs4 import BeautifulSoup
from DB import *


class itemAciton:
    # 크롬드라이버 정보 얻기
    def __init__(self):
        global driver
        driver = begin().chrome()

    # 상품 120개로 변경하기
    def item_120qty(self):
        driver.find_element_by_xpath(Coupang_category_60qty).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(Coupang_category_60qty).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(Coupang_category_120qty).click()

    # 상품리스트 얻기(키워드와 URL 얻기)
    def GetitemList(self):
        items = {}
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        data = soup.find_all('li', {'class':'baby-product renew-badge'})

        if soup.find_all(class_='no-list-item'):
            print("페이지 없음")
            return 0

        for div in data:
            title = div.get_text(strip=True)#.strip()
            link = div.a.get('href')
            link = Coupang_URL + link
            items[title] = link

        return items

    # 다음 페이지로 이동(URL 형태로)
    def next_page(self):
        URL = driver.current_url
        current_page = -1
        if "page" in URL:
            current_page = int(URL[-1]) + 1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        driver.get(URL)
        return current_page

    # url로 이동
    def move_url(self, URL):
        driver.get(URL)

class getData:
    def __init__(self):
        self.soup = BeautifulSoup(driver.page_source, 'html.parser')

    def Find(self, tag, value):
        self.soup = BeautifulSoup(driver.page_source, 'html.parser')
        if tag == 'class_':
            data = self.soup.find_all(class_=value)
        elif tag == 'id':
            data = self.soup.find_all(id=value)
        return data

    def Title(self):
        title = self.Find('class_', 'prod-buy-header__title')
        title = title[0].get_text(strip=True)
        return title



    def Group(self):
        lists = self.Find('class_', "breadcrumb-link")
        Group = []
        print(lists)
        if lists:

            for listc in list(lists):
                print(listc)
                a = listc.find('title')
                print(a)
                Group.append(listc.get_text(strip=True))
        else:
            print("위치: Group, 반환된 값 없음")
        return Group

class itemCoupang:
    def __init__(self):
        self.itemAction = itemAciton()
        self.getData = getData()
