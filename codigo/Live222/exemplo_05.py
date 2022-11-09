from playwright.sync_api import sync_playwright
from time import sleep


def event_handler(request):
    print(request.url)
    response = request.response()
    print(response.status)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.on('request', event_handler)

    page.goto('http://ddg.gg')
    sleep(5)
    page.close()
