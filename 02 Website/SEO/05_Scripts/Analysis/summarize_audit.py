import json

with open('02_Reports_and_Audits/2026-09-10_Full_Site_Audit/evidence/link_checks.json', 'r') as f:
    checks = json.load(f)

broken = []
for c in checks:
    status = c.get('status')
    if status and status >= 400:
        broken.append(c)

print(f"Total links checked: {len(checks)}")
print(f"Total broken links: {len(broken)}")
for b in broken[:10]:
    print(f"- {b['url']} (Status: {b.get('status')}) -> Found on {len(b.get('sources', []))} pages.")

with open('02_Reports_and_Audits/2026-09-10_Full_Site_Audit/evidence/crawl.json', 'r') as f:
    crawl = json.load(f)
print(f"\nTotal pages crawled: {len(crawl)}")
missing_h1 = [p['url'] for p in crawl if not p.get('h1') and 'error' not in p]
print(f"Pages missing H1 tag: {len(missing_h1)}")
for m in missing_h1[:5]:
    print(f"- {m}")

