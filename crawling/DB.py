class DB:
    # 크롬드라이버 경로
    Chromedrive_path = ".\\chromedriver"

    # 쿠팡 메인 URL
    Coupang_URL = "https://www.coupang.com"
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

    acc_ID = "rhkdrod12@naver.com"
    acc_PW = "zxc!7516155"

    Category_Keys = ['식품', '생활용품', '뷰티', '홈인테리어', '가전디지털', '주방용품', '출산/유아동', '반려동물용품', '완구/취미',
           '자동차용품', '문구/오피스', '스포츠/레저', '도서/음반/DVD', '헬스/건강식품', '여성패션', '남성패션',
           '여아패션 (3세 이상)', '남아패션 (3세 이상)', '베이비패션 (0~3세)']

    # item_setup = "div.optionWrapper"
    # item_sigle = "button.prod-option__selected.single"
    #
    # # item_sigle_color = "i.single-attribute__text"
    #
    #
    # item_multiple = "button.prod-option__selected.multiple"
    #
    # item_size = "ul.Dropdown-Select__Dropdown"
    #
    # item_image_select = "div.Image-Select__Container.prod-option__item"

    # 단일판매 여러개 판매일 경우에는    tag: class name: prod-option
    # Size값 형태인경우에는             tag: id name: otionWrapper

    #
    item_size_xpath = """//*[@id="optionWrapper"]/div[1]/ul"""
    # 상품명 위치 xpath  :상품명 가져올 떄 사용   get_title로
    item_title_xpath = """//*[@id="contents"]/div[1]/div/div[3]/div[3]/h2"""
    # 상품 사이즈 tag 및 속성명 :속성명을 가진 데이터를 찾을 때 사용함
    item_size_data_locate = ['li', {'class':'Dropdown-Select__Dropdown__Item'}]

    # item_sigle_color = "div.single-attribute__textLabel"
    # item_sigle_size = "div.single-attribute__textLabel"

    # -----상품 경우 수-----
    # 단일 사이즈, 단일 색상
    # 단일 사이즈, 다수 색상
    # 다수 사이즈, 다수 색상
    # 다수 사이즈, 단일 색상
    # 다수 이미지

    # 다수 사이즈인 경우
    item_multiple_size = "div.Dropdown-Select.prod-option__item"

    # 단일 색상
    item_sigle_color = "div.single-attribute__textLabel" #"색상"

    # 단일 사이즈
    item_sigle_size = "div.single-attribute__textLabel" #"사이즈"

    # 다수 색상
    item_multiple_color = "ul.Image-Select__Items"

    # 다수 이미지
    item_multiple_image = "ul.Image-Select__Items"

    sold_out_data = ["option-sold-out", "unavailable"]

    # 다른 제품
    item_deferent = "ul.prod-option__list"

    item_multi_image_css_selector = "li.Image-Select__Item"
    item_multi_size_css_selector = "li.Dropdown-Select__Dropdown__Item"