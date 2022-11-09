# exemplo_11.py
from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    req = p.request.new_context()

    response = req.get('http://ddg.gg')

    expect(response).to_be_ok()
