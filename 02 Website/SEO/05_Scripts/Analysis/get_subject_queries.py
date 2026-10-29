import csv

queries = []
with open('04_Data/Search_Console_and_GA4_Exports/2026-09_Export/Queries.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = row['Top queries'].lower()
        if 'subject' in query or 'combination' in query or 'a level' in query or 'o level' in query:
            queries.append({
                'query': query,
                'imp': int(row['Impressions']),
                'clicks': int(row['Clicks']),
                'pos': float(row['Position'])
            })

# Filter specifically for subject-related queries
subject_queries = [q for q in queries if 'subject' in q['query'] or 'combination' in q['query']]
subject_sorted = sorted(subject_queries, key=lambda x: x['imp'], reverse=True)[:15]

print("=== ACTUAL GOOGLE DATA (Search Console) ===")
for q in subject_sorted:
    print(f"Query: '{q['query']}' | Impressions: {q['imp']} | Clicks: {q['clicks']} | Pos: {q['pos']}")
