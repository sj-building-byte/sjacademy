from playwright.sync_api import sync_playwright
import json
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.instagram.com/sjacademypk/', wait_until='domcontentloaded')
    
    # Wait for the page to load initial data
    time.sleep(5)
    
    # Instagram usually stores shared data in window._sharedData or similar variables
    # Or in script tags. We can just evaluate a script to get all images and links.
    
    # Let's extract visible posts (links and images)
    posts = page.evaluate("""() => {
        const postElements = Array.from(document.querySelectorAll('a[href^="/p/"]'));
        return postElements.map(el => {
            const img = el.querySelector('img');
            return {
                href: el.href,
                img_src: img ? img.src : null,
                img_alt: img ? img.alt : null
            };
        });
    }""")
    
    # Extract profile metadata
    profile = page.evaluate("""() => {
        const metaTags = document.querySelectorAll('meta');
        let description = '';
        metaTags.forEach(tag => {
            if (tag.name === 'description' || tag.property === 'og:description') {
                description = tag.content;
            }
        });
        
        const h1 = document.querySelector('h1');
        const h1Text = h1 ? h1.innerText : '';
        
        return {
            description,
            h1: h1Text
        };
    }""")
    
    data = {
        "profile": profile,
        "posts": posts
    }
    
    with open('playwright_data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Scraped {len(posts)} posts.")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
