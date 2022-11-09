from time import sleep
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        **p.devices['iPhone 6']
    )

    page = context.new_page()
    page.goto('http://ddg.gg')

    sleep(3)

    browser.close()
