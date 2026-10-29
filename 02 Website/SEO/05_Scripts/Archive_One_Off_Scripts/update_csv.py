import csv

input_file = '/Users/sunyyanjunaid/Documents/WEbsite SEO/SJ_Academy_SEO_Tracker.csv'
output_file = '/Users/sunyyanjunaid/Documents/WEbsite SEO/SJ_Academy_SEO_Tracker_fixed.csv'

with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    headers = next(reader)
    writer.writerow(headers)
    
    for row in reader:
        url = row[3]
        if '/a-level-' in url and '-past-papers/' in url and not '/a-level-past-papers/' in url:
            # Convert /a-level-accounts-past-papers/ to /a-level-past-papers/accounts-9706/ (approx)
            # Actually I'll just hard replace them based on standard names
            pass # I'll do this in python more explicitly below
