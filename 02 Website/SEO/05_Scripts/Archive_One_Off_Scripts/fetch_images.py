import csv
import json
import urllib.request
from urllib.parse import urlparse
import concurrent.futures
import re
import ssl

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"

resources = []
with open(filepath, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        resources.append(row)

# Ignore SSL errors for scraping
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_image_url(row):
    link = row['Link']
    domain = urlparse(link).netloc.replace('www.', '')
    
    # Try fetching og:image for actual thumbnails/avatars
    try:
        req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=8, context=ctx).read().decode('utf-8', errors='ignore')
        
        # Look for og:image
        match = re.search(r'<meta\s+(?:property|name)="og:image"\s+content="([^"]+)"', html, re.IGNORECASE)
        if match:
            return match.group(1)
            
        # Look for twitter:image
        match = re.search(r'<meta\s+(?:property|name)="twitter:image"\s+content="([^"]+)"', html, re.IGNORECASE)
        if match:
            return match.group(1)
            
    except Exception as e:
        pass
        
    # Fallback for standard websites: Clearbit Logo API
    if 'youtube.com' not in domain and 'instagram.com' not in domain and 'reddit.com' not in domain:
        return f"https://logo.clearbit.com/{domain}"
        
    # Final generic fallback
    return ""

print("Fetching actual images from resources... This will take ~10 seconds.")

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    results = list(executor.map(get_image_url, resources))

for i, row in enumerate(resources):
    # Set the Image URL, fallback to empty if none found
    row['Image_URL'] = results[i]
    
with open('/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_with_images.json', 'w', encoding='utf-8') as f:
    json.dump(resources, f)

print("Images fetched successfully.")
