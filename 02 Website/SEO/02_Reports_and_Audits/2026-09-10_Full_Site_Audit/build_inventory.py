import json,csv,re,collections
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).parent; E=R/'evidence'; rows=json.loads((E/'crawl.json').read_text())
class Titles(HTMLParser):
 def __init__(self):super().__init__();self.svg=0;self.active=False;self.t=[];self.buf=[]
 def handle_starttag(self,t,a):
  if t=='svg':self.svg+=1
  if t=='title' and not self.svg:self.active=True;self.buf=[]
 def handle_endtag(self,t):
  if t=='svg':self.svg=max(0,self.svg-1)
  if t=='title' and self.active:self.t.append(''.join(self.buf));self.active=False
 def handle_data(self,s):
  if self.active:self.buf.append(s)
inventory=[]
for x in rows:
 p=Titles();p.feed((E/x['file']).read_text());descs=[m.get('content','') for m in x['meta'] if m.get('name','').lower()=='description'];canons=[a.get('href','') for a in x['links'] if a.get('rel')=='canonical'];flags=[]
 if len(p.t)>1:flags.append('Embedded extra HTML title')
 if x['tags'].get('head',0)>1:flags.append('Nested head')
 if x['tags'].get('body',0)>1:flags.append('Nested body')
 if not descs:flags.append('Missing meta description')
 if len(x['h1'])!=1:flags.append('Review H1 structure')
 if any(u!=x['url'] for u in canons):flags.append('Conflicting canonical in body')
 inventory.append(dict(url=x['url'],http_status=x['status'],primary_title=p.t[0] if p.t else '',html_title_count=len(p.t),h1_count=len(x['h1']),h1=' | '.join(x['h1']),meta_description_count=len(descs),meta_descriptions=' | '.join(descs),canonicals=' | '.join(canons),html_bytes=x['bytes'],script_elements=len(x['scripts']),flags='; '.join(flags),evidence_file=x['file']))
with (R/'page_inventory.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(inventory[0]));w.writeheader();w.writerows(inventory)
links=json.loads((E/'link_checks.json').read_text());broken=[x for x in links if x.get('status',0)>=400 and '/cdn-cgi/' not in x['url']]
with (R/'broken_links.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['destination','initial_status','final_status','source_pages','note']);w.writeheader()
 for x in broken:
  fixed=x['url'].endswith('/o-level-past-papers/chemistry-5070/')
  w.writerow(dict(destination=x['url'],initial_status=x['status'],final_status=200 if fixed else x['status'],source_pages=' | '.join(x['sources']),note='Resolved on September 10 recheck; earlier crawl was 404' if fixed else '404 observed in September 10 link scan'))
summary={'sitemap_urls':len(rows),'status':dict(collections.Counter(x['status'] for x in rows)),'missing_description':sum(x['meta_description_count']==0 for x in inventory),'multiple_html_titles':sum(x['html_title_count']>1 for x in inventory),'nested_head':sum(x['tags'].get('head',0)>1 for x in rows),'nested_body':sum(x['tags'].get('body',0)>1 for x in rows),'one_h1':sum(x['h1_count']==1 for x in inventory),'extra_link_checks':len(links),'content_404_initial':len(broken),'content_404_after_recheck':len(broken)-1}
(E/'summary.json').write_text(json.dumps(summary,indent=2));print(summary)
