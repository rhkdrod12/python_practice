from selenium import webdriver
from bs4 import BeautifulSoup
from DB import DB

import  re
import  time


class itemType:

    def __init__(self):
        # URL = "https://www.coupang.com/vp/products/245316563?itemId=777690014&vendorItemId=4967114931&isAddedCart="
        # URL = "https://www.coupang.com/vp/products/1490682304?itemId=2559060098&vendorItemId=70551571053&sourceType=CATEGORY&categoryId=186664&isAddedCart="
        # URL = "https://www.coupang.com/vp/products/267662493?itemId=839322053&vendorItemId=5198164645&sourceType=CAMPAIGN&campaignId=82&categoryId=186664&isAddedCart="
        # URL = "https://www.coupang.com/vp/products/288451395?itemId=913593997&vendorItemId=5282130989&sourceType=CAMPAIGN&campaignId=82&categoryId=186664&isAddedCart="     #단일사이즈, 멀티칼라(이미지)
        URL = "https://www.coupang.com/vp/products/205655?itemId=390269&vendorItemId=3000296247&sourceType=CATEGORY&categoryId=276376&isAddedCart="                         #단일혼합
        global driver
        driver = webdriver.Chrome(DB.Chromedrive_path)
        driver.get(URL)

    # 기본 데이터 셋트
    def itemData(self):

        self.URL = driver.current_url
        self.soup = BeautifulSoup(driver.page_source, 'html.parser')

        self.SingleLength = 0
        self.DropboxLength = 0
        self.ColortextLength = 0
        self.ColorimageLength = 0

        # Size, Color 형태
        self.data = self.soup.find('div', {'id': 'optionWrapper'})
        if self.data:
            self.SingleData = self.data.find_all(class_='single-attribute__textLabel')
            self.DropboxData = self.data.find_all(class_='Dropdown-Select__Dropdown__Item')
            self.ColortextData = self.data.find_all(class_='Text-Select__Item')
            self.ColorimageData = self.data.find_all(class_='Image-Select__Item')

            self.SingleLength = len(self.SingleData)
            self.DropboxLength = len(self.DropboxData)
            self.ColortextLength = len(self.ColortextData)
            self.ColorimageLength = len(self.ColorimageData)

        self.data = self.soup.find('div',{'class': 'prod-option'})
        if self.data:
            self.prodDropbox = self.data.find_all(class_='prod-option__selected')
            if 'single' in self.prodDropbox[0].get('class'):
                print("Sd")
            elif 'multiple' in self.prodDropbox[0].get('class'):
                print("wer")



    # 상품 형태 파악
    def itemTypeCheck(self):

        self.itemData()

        if self.SingleLength == 2:
            print("분류: 단일 사이즈, 단일 색상")
            type = 1
        elif self.SingleLength == 1 and self.ColortextLength >= 1:
            print("분류: 단일 사이즈, 멀티 색상")
            type = 2
        elif self.SingleLength == 1 and self.ColorimageLength >= 1:
            print("분류: 단일 사이즈, 멀티 색상(이미지)")
            self.clickData = driver.find_elements_by_css_selector("li.Image-Select__Item")
            type = 3
        elif self.SingleLength == 1 and self.DropboxLength >= 1:
            print("분류: 멀티 사이즈, 단일 색상")
            type = 4
        elif self.DropboxLength >= 1 and self.ColortextLength >= 1:
            print("분류: 멀티 사이즈, 멀티 색상")
            self.clickData = driver.find_elements_by_css_selector("li.Text-Select__Item")
            type = 5
        elif self.DropboxLength >= 1 and self.ColorimageLength >= 1:
            print("분류: 멀티 사이즈, 멀티 색상(이미지)")
            self.clickData = driver.find_elements_by_css_selector("li.Image-Select__Item")
            type = 6
        else:
            print("분류: 미분류항목")
            type = 0

        return type

    def SsMciItem(self):
        item = []




    # 멀티사이즈, 멀티색상 처리
    def MsMcItem(self):
        item = []

        title = self.ItemTitle
        for color in self.ColorimageData():
            self.clickData[self.ColorimageData.index(color)].click()

    # 멀티사이즈, 단일색상 처리

    def MsScItem(self):

        item = []

        title = self.ItemTitle
        Size = self.GetMultiSize()
        Color = self.SingleData.i.get_text(strip=True)
        URL = self.CurrentURL

        if len(Size) > 0:
            item = [title, Color, Size, URL]

        return item

    def GetMultiSize(self):
        itemSize = []

        for Size in self.DropboxData:
            class_ = Size.get('class')
            if self.multicompare(class_, DB.sold_out_data):
                item = Size.get_text(strip=True)
                itemSize.append(item)

        return itemSize

    def multicompare(self, lists, args):
        check = 0
        for list in lists:
            if list in args:
                check = 1
        return check


if __name__ == '__main__':

    typecheck = itemType()

    print(typecheck.itemTypeCheck())
    print(typecheck.URL)

    # a.Check()

    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # data = soup.find('div', {'id': 'optionWrapper'})
    #
    # print(data)
    #
    # Size = ''
    # Color = ''
    #
    # dataFind = data.find_all( class_= 'single-attribute__textLabel')
    #
    #
    # for text in dataFind:
    #     if text.find_all(text=re.compile("사이즈+")):
    #         Size = text.i.get_text(strip=True)
    #         print(Size)
    #
    #     if text.find_all(text=re.compile("색상+")):
    #         Color = text.i.get_text(strip=True)
    #         print(Color)
    #
    #
    #
    #
    # print("Size:", Size, " Color:", Color)



