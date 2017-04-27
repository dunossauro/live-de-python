from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from time import sleep

binary = FirefoxBinary('/usr/lib/firefox/firefox')
ff = webdriver.Firefox(firefox_binary=binary)
ff.get('http://127.0.0.1:8080/')
# ff.get('http://google.com')
# ff.save_screenshot('teste.jpeg')
# ff.find_element_by_id('lst-ib').send_keys('Programação funcional')
# ff.find_element_by_id('_fZl').click()
print(ff.page_source)
