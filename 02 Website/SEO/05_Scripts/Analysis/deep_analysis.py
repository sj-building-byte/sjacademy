import csv

queries = []
with open('Search Console/Queries.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        queries.append({
            'query': row['Top queries'],
            'clicks': int(row['Clicks']),
            'imp': int(row['Impressions']),
            'ctr': float(row['CTR'].strip('%')),
            'pos': float(row['Position'])
        })

print("=== COMPETITOR BRAND SEARCHES ===")
competitors = ['beacon', 'city school', 'kgs', 'grammar school', 'lyceum', 'cedar', 'nixor', 'alpha', 'siddique', 'teachwink']
comp_queries = [q for q in queries if any(c in q['query'].lower() for c in competitors)]
comp_sorted = sorted(comp_queries, key=lambda x: x['imp'], reverse=True)[:10]
for q in comp_sorted:
    print(f"{q['query']} (Pos: {q['pos']}, Imp: {q['imp']}, Clicks: {q['clicks']})")

print("\n=== SUBJECT SPECIFIC QUERIES ===")
subjects = ['math', 'physics', 'chemistry', 'bio', 'econ', 'business', 'accounting', 'computer', 'urdu']
subj_queries = [q for q in queries if any(s in q['query'].lower() for s in subjects)]
subj_sorted = sorted(subj_queries, key=lambda x: x['imp'], reverse=True)[:10]
for q in subj_sorted:
    print(f"{q['query']} (Pos: {q['pos']}, Imp: {q['imp']}, Clicks: {q['clicks']})")

print("\n=== HIGH CTR / NICHE DOMINANCE (CTR > 15%, Imp > 50) ===")
high_ctr = sorted([q for q in queries if q['ctr'] > 15.0 and q['imp'] > 50 and 'sj academy' not in q['query'].lower()], key=lambda x: x['clicks'], reverse=True)[:10]
for q in high_ctr:
    print(f"{q['query']} (Pos: {q['pos']}, Imp: {q['imp']}, Clicks: {q['clicks']}, CTR: {q['ctr']}%)")

