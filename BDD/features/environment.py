from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox/firefox')

def before_feature(context, feature):
    context.ff = webdriver.Firefox(firefox_binary=binary)


def after_feature(context, feature):
    context.ff.quit()
