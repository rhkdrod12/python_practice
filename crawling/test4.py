from selenium import webdriver
from bs4 import BeautifulSoup
from DB import DB

import  re
import  time

class crwaling:

    def __init__(self, URL, driver_path):
        # 쿠팡 URL
        self.URL = URL  # "https://www.coupang.com/"
        # 크롬 드라이버 경로(현재 작업폴더 경로)
        self.path = driver_path  # ".\\chromedriver"

    # 크롬드라이버를 사용하여 크롬 실행
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
    def get_data(self, *args):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data = soup.find_all(args[0], args[1])
        # data = soup.find_all('div',{'class':'baby-item'})
        return data

    # xpath쪽 텍스트 가져오기
    def get_title(self, xpath):
        text = self.driver.find_element_by_xpath(xpath).text
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
        URL = self.driver.current_url
        if "page" in URL:
            current_page = int(URL[-1]) + 1
            URL = URL[:-1] + str(current_page)
        else:
            URL = URL + "?page=1"
        self.driver.get(URL)

    # 현재 화면 URL 얻기
    def current_URL(self):
        return self.driver.current_url

    # css항목을 검색하여 잇으면 1을 반환
    def item_type(self, name):
        try:
            self.driver.find_element_by_css_selector(name)
            return 1
        except:
            return 0

    # 해당 화면에서 텍스트들을 하나라도 포함하고 잇으면 1를 내보냄
    def find_str(self, *args):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
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
        self.driver.close()

class coupang_category(crwaling):

    # 초기값
    def __init__(self):
        URL = DB.Coupang_category_URL
        Path = DB.Chromedrive_path
        super().__init__(URL, Path)

        self.item_MsMcdata = []
        self.item_MsScdata = []
        self.item_SsMcdata = []
        self.item_SsScdata = []

        self.count = 0
        self.sold_out_item_qty = 0

        self.chromeBeign()
        # sold in, sold out 구분
        # self.driver.find_elements_by_css_selector(DB.item_size)

    # 카테고리 목록 가져오기
    def category_dict_URL(self):
        time.sleep(0.5)
        if (self.current_URL() == DB.Coupang_category_URL):
            Category_data = self.get_data('div', {'class': 'baby-item'})
            self.Category_dic = self.get_URL_dic(Category_data)
            return self.Category_dic
        else:
            print("화면 확인")

    # 카테서리 목록에서 해당 카테고리로 이동
    def category_move(self, num = 14):
        URL = self.Category_dic[DB.Category_Keys[num]]
        self.move_url(URL)

    # 카테고리에서 아이템 목록 가져오기
    def category_items_list(self):
        self.item_120qty()
        time.sleep(0.5)
        items = self.get_data('li', {'class': 'baby-product renew-badge'})
        self.items_list = self.get_URL_list(items)
        return self.items_list

    # 상품 표시 갯수 변경
    def item_120qty(self):
        self.click(DB.Coupang_category_60qty)
        self.click(DB.Coupang_category_60qty)
        self.click(DB.Coupang_category_120qty)

    # 상품 형태 파악
    def item_type_check(self):
        self.itemType = 0
        # print("제조국확인:", self.info_table())
        if self.item_type(DB.item_multiple_size) and self.item_type(DB.item_multiple_color):
            print("분류: 멀티사이즈, 멀티색상")
            self.itemType = 1
        elif self.item_type(DB.item_multiple_size) and self.item_type(DB.item_sigle_color):
            print("분류: 멀티사이즈, 단일색상")
            self.itemType = 2
        elif self.item_type(DB.item_sigle_size) and self.item_type(DB.item_multiple_color):
            print("분류: 단일사이즈, 멀티색상")
            self.itemType = 3
        elif self.item_type(DB.item_sigle_color) and self.item_type(DB.item_sigle_size):
            print("분류: 단일, 단일색상")
            self.itemType = 4
        elif self.item_type(DB.item_multiple_image):
            self.itemType = 5

        return self.itemType    #

    # 상품 형태에 따른 작동부분
    def category_get_soldout(self, URL):
        URL = URL+"&isAddedCart="
        self.move_url(URL)
        # print(URL)
        time.sleep(0.5)

        self.count += 1
        print("검색 수 : ", self.count)

        maker = self.find_str("대한민국", "oem", "OEM")

        # print(self.find_str("대한민국"))
        # print(self.find_str("OEM"))
        # print(self.find_str("oem"))

        # maker = 0
        if not maker:
            check = self.item_type_check()
            if check == 1:
                # 멀티 사이즈, 멀티 색상
                print("1.진입")
                self.Coupang_MsMcItem_sold_data(URL)
            elif check == 2:
                # 멀티 사이즈, 단일 색상
                print("2.진입")
                self.Coupang_MsScItem_sold_data(URL)
            elif check == 3:
                # 단일 사이즈, 멀티 색상
                print("3.미구현")
            elif check == 4:
                # 단일 사이즈, 단일 색상
                print("4.미구현")
            elif check == 5:
                # 사이즈X, 멀티 이미지
                print("5.미구현")
            elif check == 6:

                print("6.미구현")
            else:
                print("URL:", URL)
                print("오류!!!!, 해당타입 없음")
        else:
            print("국내 또는 OEM생산")

    # 단일 사이즈, 다수 색상
    def Coupang_MsMcItem_sold_data(self, URL):
        item_title = self.get_title(DB.item_title_xpath)

        item_data = []
        item_sold_out = []
        item_sold_in = []
        item_color_text = ''
        item_sold_out_check = 0

        item_color = self.get_data('li', {'class': 'Image-Select__Item'})
        num = 1
        for color in item_color:
            class_name = color.i['class']
            self.driver.find_element_by_xpath("""// *[ @ id = "optionWrapper"] / div[2] / ul /li["""+str(num)+"]")\
                .click()
            num += 1
            item_color_text = self.get_text('i', {'class': 'select-option__text'})
            item_size = self.get_data('li', {'class': 'Dropdown-Select__Dropdown__Item'})

            for size in item_size:
                size_name = size.get('class')
                try:
                    # print(size_name)
                    if size_name[1] in "option-sold-out unavailable":
                        item_sold_out_check = 1
                        self.sold_out_item_qty = self.sold_out_item_qty + 1
                        item_sold_out.append(size.get_text().strip())

                    elif size_name[1] in "selected":
                        try:
                            if size_name[2] in "unavailable":
                                item_sold_out_check = 1
                                self.sold_out_item_qty = self.sold_out_item_qty + 1
                                item_sold_out.append(size.get_text().strip())
                        except:
                            None
                except:
                    None

            item_size_data = [item_title, item_color_text, item_sold_out, URL]
            item_sold_out = []
            item_color_text = ""
            item_data.append(item_size_data)

        # print(item_data)

        if item_sold_out_check:
            print(item_data)
            self.item_MsMcdata.append(item_data)

    # 다수 사이즈, 단일 색상
    def Coupang_MsScItem_sold_data(self, URL):
        item_title = self.get_title(DB.item_title_xpath)

        item_sold_out = []
        item_sold_in = []
        item_sold_out_check = 0

        item_color = self.get_text('i', {'class':'single-attribute__text'})
        item_size = self.get_data('li', {'class':'Dropdown-Select__Dropdown__Item'})

        for div in item_size:
            div_name = div.get('class')
            try:
                if div_name[1] in 'option-sold-out':
                    item_sold_out_check = 1
                    self.sold_out_item_qty = self.sold_out_item_qty + 1
                    item_sold_out.append(div.get_text().strip())
                else:
                    item_sold_in.append(div.get_text().strip())
            except:
                item_sold_in.append(div.get_text().strip())

        item_data = [item_title, item_color, item_sold_out, URL]

        # print(item_data)

        if item_sold_out_check:
            print(item_data)
            self.item_MsScdata.append(item_data)

        # print('item_data:', self.item_data)

if __name__ == '__main__':

    # a = coupang_category()
    # print(a.item_data)

    # Coupang = category_Coupang()
    # print(Coupang.category_dict_URL().keys())
    # Coupang.category_move()
    # print(Coupang.category_items_list())

    Coupang = coupang_category()
    print(Coupang.category_dict_URL().keys())
    Coupang.category_move()
    item_list = Coupang.category_items_list()

    print(len(item_list))
    for list in item_list:
        # print(list)
        time.sleep(0.2)
        Coupang.category_get_soldout(list[1])
