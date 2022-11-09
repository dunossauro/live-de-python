# exemplo_08.py
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(base_url='https://selenium.dunossauro.live/')
    page.goto('aula_05_a.html')

    l_h2 = page.locator('div#python > h2')
    l_p = page.locator('div#python > p')

    print(
        l_h2.text_content(),
        l_p.text_content()
    )

    browser.close()
