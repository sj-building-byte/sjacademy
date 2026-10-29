import csv

def read_ga4_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            if len(row) > 4 and row[1].isdigit():
                data.append(row)
        return data

traffic = read_ga4_csv('Search Console/Traffic_acquisition_Session_source_medium (1).csv')
print("=== TRAFFIC ACQUISITION ===")
for row in traffic[:10]:
    print(f"Source: {row[0]} | Sessions: {row[1]} | Eng Rate: {round(float(row[3])*100,1)}% | Avg Time: {round(float(row[4]),1)}s")

landing = read_ga4_csv('Search Console/Landing_page_Landing_page.csv')
print("\n=== WORST PERFORMING LANDING PAGES ===")
worst = sorted([r for r in landing if int(r[1]) > 500], key=lambda x: float(x[4]))
for row in worst[:7]:
    print(f"Page: {row[0]} | Sessions: {row[1]} | Avg Time: {round(float(row[4]),1)}s")

print("\n=== BEST PERFORMING LANDING PAGES ===")
best = sorted([r for r in landing if int(r[1]) > 500], key=lambda x: float(x[4]), reverse=True)
for row in best[:5]:
    print(f"Page: {row[0]} | Sessions: {row[1]} | Avg Time: {round(float(row[4]),1)}s")
