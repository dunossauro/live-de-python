# exemplo_07.py
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(base_url='https://selenium.dunossauro.live/')
    page.goto('aula_05_a.html')

    locator = page.locator('div')

    result = locator.nth(0).text_content()

    print(result)

    browser.close()
