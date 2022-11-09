from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('http://ddg.gg')
    sleep(1)
    page.goto('http://google.com')
    sleep(1)
    page.go_back()
    sleep(1)
    page.go_forward()
