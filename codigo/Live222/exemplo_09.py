# exemplo_09.py
from playwright.sync_api import sync_playwright

url = 'https://selenium.dunossauro.live/todo_list.html'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    page.locator('#todo-name').fill('Fazer Live 222')
    page.locator('#todo-desc').fill('Live sobre playwright')
    page.locator('#todo-next').click()
    page.locator('#todo-submit').click()

    page.screenshot(path='result.png', full_page=True)

    page.close()
