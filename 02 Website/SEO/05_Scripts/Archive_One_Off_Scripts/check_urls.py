import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://www.sjacademy.pk/o-level-past-papers/",
    "https://www.sjacademy.pk/o-level-past-papers/physics-5054/",
    "https://www.sjacademy.pk/o-level-past-papers/mathematics-d-4024/",
    "https://www.sjacademy.pk/o-level-subjects-in-pakistan/"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            status = response.status
            match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
            title = match.group(1).strip() if match else "NO TITLE"
            print(f"[{status}] {url} -> Title: {title}")
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {url} -> Error")
    except Exception as e:
        print(f"[ERROR] {url} -> {str(e)}")
