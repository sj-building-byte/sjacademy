from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.instagram.com/sjacademypk/', wait_until='networkidle')
    time.sleep(5)
    
    page.screenshot(path="ig_screenshot.png")
    with open("ig_page.html", "w") as f:
        f.write(page.content())
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
