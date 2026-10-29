import urllib.request, urllib.error, xml.etree.ElementTree as ET, concurrent.futures, json, time, re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin,urlsplit
ROOT=Path(__file__).parent/'evidence'
class Parser(HTMLParser):
 def __init__(self):
  super().__init__(); self.tags={}; self.titles=[]; self.h1=[]; self.meta=[]; self.links=[]; self.images=[]; self.scripts=[]; self.schema=[]; self.active=None; self.buf=[]; self.text=[]; self.skip=0
 def handle_starttag(self,t,a):
  d=dict(a); self.tags[t]=self.tags.get(t,0)+1
  if t in ['title','h1']: self.active=t; self.buf=[]
  if t=='meta': self.meta.append(d)
  if t=='link': self.links.append(d)
  if t=='a': self.links.append(d)
  if t=='img': self.images.append(d)
  if t=='script':
   self.scripts.append(d); self.skip+=1
   if d.get('type')=='application/ld+json': self.active='schema';self.buf=[]
  if t=='style': self.skip+=1
 def handle_data(self,d):
  if self.active:self.buf.append(d)
  if not self.skip:self.text.append(d)
 def handle_endtag(self,t):
  if (t in ['title','h1'] and self.active==t) or (t=='script' and self.active=='schema'):
   v=' '.join(self.buf).strip()
   if self.active=='title':self.titles.append(v)
   elif self.active=='h1':self.h1.append(v)
   else:self.schema.append(v)
   self.active=None
  if t in ['script','style']: self.skip=max(0,self.skip-1)
def fetch(pair):
 i,u=pair; start=time.time()
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (compatible; SJAcademySiteAudit/1.0)'})
  with urllib.request.urlopen(req,timeout=35) as r: raw=r.read(); final=r.url;status=r.status;headers=dict(r.headers)
  html=raw.decode('utf-8',errors='replace'); (ROOT/f'page_{i:03}.html').write_text(html)
  p=Parser();p.feed(html)
  return dict(url=u,final=final,status=status,seconds=round(time.time()-start,2),bytes=len(raw),file=f'page_{i:03}.html',titles=p.titles,h1=p.h1,tags=p.tags,meta=p.meta,links=p.links,images=p.images,scripts=p.scripts,schema=p.schema,text=' '.join(' '.join(p.text).split()),headers=headers)
 except Exception as e:return dict(url=u,error=str(e))
urls=[]
for f in ['page-sitemap.xml','post-sitemap.xml']:
 tree=ET.parse(ROOT/f); urls += [x.text for x in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
urls=list(dict.fromkeys(urls));print('Sitemap URLs:',len(urls),flush=True)
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(fetch,enumerate(urls)):
  results.append(r)
  if len(results)%20==0:print('Fetched',len(results),flush=True)
(ROOT/'crawl.json').write_text(json.dumps(results,indent=2));print('Done',len(results),'errors',sum('error' in r for r in results),flush=True)
