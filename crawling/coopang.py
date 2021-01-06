from selenium import webdriver
from bs4 import BeautifulSoup
from DB import DB
import  time


# class DB:
#     Coupang_URL = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang." \
#                                "com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252Fnp%25" \
#                        "2Fcampaigns%252F82"
#     # 크롬드라이버 경로
#     Chromedrive_path = ".\\chromedriver"
#     # self.Login_xpath = """//*[@id="login"]/a"""
#     # 아이디 xpath
#     Id_locate_xpath = """//*[@id="login-email-input"]"""
#     # 패스워드 xpath
#     Passward_locate_xpath = """//*[@id="login-password-input"]"""
#     # 로그인 클릭 xpath
#     Login_botton_xpath = "/html/body/div[1]/div/div/form/div[5]/button"
#
#     category_xpath = """//*[@id="searchOptionForm"]/div/div/div[1]/div[3]"""
#


class crwaling:
    # 초기화
    def __init__(self, URL, driver_path):
        # 쿠팡 URL
        self.URL = URL #"https://www.coupang.com/"
        # 크롬 드라이버 경로(현재 작업폴더 경로)
        self.path = driver_path    #".\\chromedriver"

    # 초기화면 실행
    def chromeBeign(self):
        # 크롬 실행
        self.driver = webdriver.Chrome(self.path)
        # URL로 이동
        self.driver.get(self.URL)

    # url로 이동
    def move_url(self, url):
        self.driver.get(url)

    # xpath로 이동
    def move_xpath(self, xpath):
        data=self.driver.find_element_by_xpath(xpath)
        href = data.get_attribute("href")
        self.driver.get(href)

    # xpath로 value값 보내기
    def sendkey(self, xpath, value):
        data=self.driver.find_element_by_xpath(xpath)
        data.send_keys(value)

    # xpath로 클릭하기
    def click(self, xpath):
        a = self.driver.find_element_by_xpath(xpath)
        print(a)
        a.click()

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
            link = DB.Coupang_URL+link
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
            current_page = int(URL[-1])+1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        self.driver.get(URL)

    def current_URL(self):
        return self.driver.current_url

    # def item_state(self):
    #

class chrome(DB):
    def __init__(self):
        super().__init__()
        self.Coupang = crwaling(self.Coupang_URL, self.Chromedrive_path)
        self.Coupang.chromeBeign()

    def login(self):
        time.sleep(0.5)
        self.Coupang.move_url(self.Coupang_Login_URL)
        time.sleep(0.5)
        self.Coupang.sendkey(self.Id_locate_xpath, self.acc_ID)
        self.Coupang.sendkey(self.Passward_locate_xpath, self.acc_PW)
        time.sleep(0.5)
        self.Coupang.click(self.Login_botton_xpath)




class category(chrome):
    def __init__(self):
        super().__init__()

    def category(self):
        time.sleep(0.5)
        self.Coupang.move_url(self.Coupang_category_URL)
        time.sleep(0.5)

    def category_dic(self):
        time.sleep(0.5)
        if(self.Coupang.current_URL() == self.Coupang_category_URL):
            Category = self.Coupang.get_data('div', {'class':'baby-item'})
            Category_dic = self.Coupang.get_URL_dic(Category)
            return Category_dic

    def category_move(self, URL):
        self.Coupang.move_url(URL)
        time.sleep(0.5)


    def category_item(self):
        items = self.Coupang.get_data('li', {'class': 'baby-product renew-badge'})
        items_list = self.Coupang.get_URL_list(items, 'href')

if __name__ == '__main__':

    Coupang = chrome()
    # Coupang.login()
    Coupang.login()

    # a = Coupang.category_dic()
    #
    # print(a)
    #
    # b = '여성패션'
    #
    # print(a[b])



