import json,urllib.request,urllib.error,concurrent.futures
from pathlib import Path
R=Path(__file__).parent/'evidence'; sources=json.loads((R/'extra_links.json').read_text())
urls=[u for u in sources if not any(s in u for s in ['/wp-json/','/feed/','/xmlrpc.php','/wp-login.php'])]
def check(u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:
   data=r.read(); return {'url':u,'status':r.status,'final':r.url,'sources':sources[u],'bytes':len(data)}
 except urllib.error.HTTPError as e:return {'url':u,'status':e.code,'sources':sources[u]}
 except Exception as e:return {'url':u,'error':str(e),'sources':sources[u]}
print('Checking',len(urls),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:result=list(ex.map(check,urls))
(R/'link_checks.json').write_text(json.dumps(result,indent=2));print('Done',len(result),flush=True)
for r in result:
 if r.get('status',0)>=400 or 'error' in r:print(r['url'],r.get('status',r.get('error')),flush=True)
