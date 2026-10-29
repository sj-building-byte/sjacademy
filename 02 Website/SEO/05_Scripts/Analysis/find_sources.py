import json

with open('02_Reports_and_Audits/2026-09-10_Full_Site_Audit/evidence/link_checks.json', 'r') as f:
    checks = json.load(f)

target_url = "https://www.sjacademy.pk/o-level-past-papers/chemistry-5070/"
for c in checks:
    if c['url'] == target_url:
        print(f"Sources for {target_url}:")
        for source in c.get('sources', []):
            print(f"- {source}")
