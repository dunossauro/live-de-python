# exemplo_11.py
from playwright.sync_api import expect, sync_playwright

url = 'https://selenium.dunossauro.live/todo_list.html'


def create_task(page):
    page.locator('#todo-name').fill('Fazer Live 222')
    page.locator('#todo-desc').fill('Live sobre playwright')
    page.locator('#todo-next').click()
    page.locator('#todo-submit').click()


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    create_task(page)

    expect_header = expect(page.locator('.terminal-card > header'))
    expect_header.to_have_text('Fazer Live 222')
    expect_header.to_have_class('name')

    browser.close()
