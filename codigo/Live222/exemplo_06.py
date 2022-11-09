# exemplo_06.py
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(base_url='https://selenium.dunossauro.live/')
    page.goto('aula_05_a.html')

    locator = page.locator('id=python')  # sugar
    print(locator.text_content())

    locator2 = page.locator('#python')  # CSS
    print(locator2.text_content())

    locator3 = page.locator('//*[@id="python"]')  # XPATH
    print(locator3.text_content())

    browser.close()
