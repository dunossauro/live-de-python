import re
from playwright.sync_api import expect, sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        base_url='https://selenium.dunossauro.live/'
    )

    page.goto('todo_list.html')

    page.locator('#todo-name').fill('Fazer Live #222')
    page.locator('#todo-desc').fill('Live de PW')
    page.locator('#todo-submit').click()
    page.locator('button.do').click()
    page.locator('button.do').click()

    # page.screenshot(path='result.png', full_page=True)

    card = page.locator('.terminal-card')

    title = card.locator('header')
    desc = card.locator('.description')

    # expect(title).to_have_text('Fazer Live #222')
    # expect(desc).to_have_text('Live de PW')

    expect(title).to_have_text(re.compile('.*Live.*'))

    expect(page).to_have_title('Todo list')

    request = p.request.new_context()

    response = request.get('https://duckduckgo.com')

    expect(response).to_be_ok()

    browser.close()
