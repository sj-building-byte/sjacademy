import csv

queries = []
with open('Search Console/Queries.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['Impressions'] = int(row['Impressions'])
        row['Clicks'] = int(row['Clicks'])
        row['CTR'] = float(row['CTR'].strip('%'))
        row['Position'] = float(row['Position'])
        queries.append(row)

print("=== STRIKING DISTANCE KEYWORDS (Positions 11-25, High Impressions) ===")
striking = sorted([q for q in queries if 11 <= q['Position'] <= 25], key=lambda x: x['Impressions'], reverse=True)[:10]
for q in striking:
    print(f"{q['Top queries']} (Pos: {q['Position']}, Imp: {q['Impressions']}, Clicks: {q['Clicks']})")

print("\n=== HIGH IMPRESSION, LOW CTR KEYWORDS (Page 1, CTR < 3%) ===")
low_ctr = sorted([q for q in queries if q['Position'] <= 10 and q['CTR'] < 3.0 and q['Impressions'] > 500], key=lambda x: x['Impressions'], reverse=True)[:10]
for q in low_ctr:
    print(f"{q['Top queries']} (Pos: {q['Position']}, Imp: {q['Impressions']}, CTR: {q['CTR']}%, Clicks: {q['Clicks']})")

print("\n=== AI / GEO OPPORTUNITIES (Questions/Comparisons) ===")
geo_keywords = ['how', 'what', 'where', 'why', 'vs', 'difference', 'fee', 'cost', 'best']
geo_queries = sorted([q for q in queries if any(k in q['Top queries'].lower() for k in geo_keywords)], key=lambda x: x['Impressions'], reverse=True)[:10]
for q in geo_queries:
    print(f"{q['Top queries']} (Pos: {q['Position']}, Imp: {q['Impressions']})")

ga4 = []
with open('Search Console/GA4 Metrics.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[8:]
    reader = csv.DictReader(lines)
    for row in reader:
        try:
            row['Views'] = int(row['Views'])
            row['Average engagement time per active user'] = float(row['Average engagement time per active user'])
            ga4.append(row)
        except:
            pass

print("\n=== LOW ENGAGEMENT PAGES (Potential Content Issues) ===")
low_eng = sorted([p for p in ga4 if p['Average engagement time per active user'] < 30 and p['Views'] > 200], key=lambda x: x['Views'], reverse=True)[:5]
for p in low_eng:
    print(f"{p['Page path and screen class']} (Views: {p['Views']}, Avg Time: {round(p['Average engagement time per active user'], 1)} sec)")

print("\n=== HIGH ENGAGEMENT PAGES ===")
high_eng = sorted([p for p in ga4 if p['Views'] > 200], key=lambda x: x['Average engagement time per active user'], reverse=True)[:5]
for p in high_eng:
    print(f"{p['Page path and screen class']} (Views: {p['Views']}, Avg Time: {round(p['Average engagement time per active user'], 1)} sec)")
