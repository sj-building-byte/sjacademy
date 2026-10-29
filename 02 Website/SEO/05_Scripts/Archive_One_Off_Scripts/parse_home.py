import urllib.request
import re

url = "https://www.sjacademy.pk/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    h1 = re.findall(r'<h1.*?>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    h2 = re.findall(r'<h2.*?>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
    
    print("TITLE:", title.group(1) if title else "None")
    print("H1s:", [re.sub(r'<[^>]+>', '', h).strip() for h in h1])
    print("H2s:", [re.sub(r'<[^>]+>', '', h).strip() for h in h2])
except Exception as e:
    print(e)
