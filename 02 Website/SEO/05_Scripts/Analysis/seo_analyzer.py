import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def analyze_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title'
        desc = soup.find('meta', attrs={'name': 'description'})
        desc = desc['content'] if desc else 'No description'
        h1s = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        
        # Word count & keyword mentions
        text = soup.get_text(separator=' ').lower()
        word_count = len(text.split())
        kw_mentions = text.count('o level') + text.count('o levels')
        coaching_mentions = text.count('coaching')
        karachi_mentions = text.count('karachi')
        
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Meta Desc: {desc}")
        print(f"H1s: {h1s}")
        print(f"Word Count: ~{word_count}")
        print(f"Mentions - 'O Level': {kw_mentions}, 'Coaching': {coaching_mentions}, 'Karachi': {karachi_mentions}\n")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

analyze_url('https://teachwink.com/')
analyze_url('https://www.sjacademy.pk/')
analyze_url('https://www.sjacademy.pk/o-level-tuition-center-karachi/')
