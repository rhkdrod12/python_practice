from selenium import webdriver
from bs4 import BeautifulSoup
from DB import DB
import  time


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
        return self.driver

    # url로 이동
    def move_url(self, url):
        self.driver.get(url)

    # xpath로 이동
    def move_xpath(self, xpath):
        data = self.driver.find_element_by_xpath(xpath)
        href = data.get_attribute("href")
        self.driver.get(href)

    # xpath로 value값 보내기
    def sendkey(self, xpath, value):
        data = self.driver.find_element_by_xpath(xpath)
        data.send_keys(value)

    # xpath로 클릭하기
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    # 해당 테그안 내용을 전부 가져오기
    def get_data(self, tag, tag_name):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data = soup.find_all(tag, tag_name)
        # data = soup.find_all('div',{'class':'baby-item'})
        return data

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
        URL = self.driver.current_url
        if "page" in URL:
            current_page = int(URL[-1]) + 1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        self.driver.get(URL)

    # 현재 URL 얻기
    def current_URL(self):
        return self.driver.current_url

class category_Coupang(crwaling):

    def __init__(self):
        super().__init__(DB.Coupang_category_URL,DB.Chromedrive_path)
        self.Coupang = crwaling(DB.Coupang_category_URL,DB.Chromedrive_path)
        self.Coupang.chromeBeign()

    def category_dict_URL(self):
        time.sleep(0.5)
        if (self.Coupang.current_URL() == DB.Coupang_category_URL):
            Category_data = self.Coupang.get_data('div', {'class': 'baby-item'})
            self.Category_dic = self.Coupang.get_URL_dic(Category_data)
            return self.Category_dic
        else:
            print("화면 확인")

    def category_move(self, num = 14):
        URL = self.Category_dic[DB.Category_Keys[num]]
        self.Coupang.move_url(URL)

    def category_items_list(self):
        time.sleep(0.5)
        items = self.Coupang.get_data('li', {'class': 'baby-product renew-badge'})
        self.items_list = self.Coupang.get_URL_list(items)
        return self.items_list




if __name__ == '__main__':

    Coupang = category_Coupang()
    print(Coupang.category_dict_URL().keys())
    Coupang.category_move()
    item_list = Coupang.category_items_list()

    for list in item_list:
        print(list)
        Coupang.category_get_soldout(list[1])

