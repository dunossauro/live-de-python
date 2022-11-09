from playwright.sync_api import (
    Browser, BrowserContext, Page, Playwright, sync_playwright
)


def event_handler(request_event):
    response = request_event.response()
    print(response.status, ' - ', request_event.url)


with sync_playwright() as p:
    browser: Browser = p.chromium.launch(headless=False)

    page: Page = browser.new_page()

    page.on('request', event_handler)

    page.goto('http://ddg.gg')

    browser.close()
