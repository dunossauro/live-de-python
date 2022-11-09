# exemplo_10.py
import re
from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto('https://selenium.dunossauro.live/')

    expect(page).to_have_title('Curso de selenium com Python')
    expect(page).to_have_title(re.compile(r'Curso.*Python'))

    expect(page).to_have_url(re.compile(r'.*dunossauro.live'))

    page.close()
