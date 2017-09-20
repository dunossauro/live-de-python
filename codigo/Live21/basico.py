from selenium import webdriver
from bs4 import BeautifulSoup as bs


class Page:
    def __init__(self, driver):
        self.driver = driver


ff = webdriver.Firefox()
ff.get('http://google.com')
html = ff.page_source
