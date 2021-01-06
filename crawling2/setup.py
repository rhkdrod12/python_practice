from selenium import webdriver
from DB import *

class begin:
    def chrome(self):
        driver = webdriver.Chrome(Chromedrive_path)
        return driver

