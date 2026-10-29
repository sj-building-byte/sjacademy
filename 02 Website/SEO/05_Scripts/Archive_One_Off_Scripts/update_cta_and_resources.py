import csv
import json
import hashlib
from urllib.parse import urlparse
import re

filepath_csv = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"
html_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"
elementor_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault_elementor.html"

# 1. New Reddit-Recommended Resources
reddit_resources = [
    ["Anki", "App / Tool", "O & A Level", "Productivity", "The absolute gold standard for memorization. A free spaced-repetition flashcard app heavily recommended on r/6thForm for biology and chemistry.", "https://apps.ankiweb.net/", "No"],
    ["Notion", "App / Tool", "O & A Level", "Productivity", "The ultimate digital workspace. Thousands of students use it to build revision wikis, track past paper scores, and organize notes.", "https://www.notion.so/", "No"],
    ["Chemguide", "Website / Notes", "A Level", "Sciences", "The absolute bible for A Level Chemistry. It explains complex concepts better than most textbooks. A must-use resource.", "https://www.chemguide.co.uk/", "No"],
    ["Isaac Physics", "Website / Notes", "A Level", "Sciences", "Mastery-level physics and maths problem-solving. Recommended for students aiming for A*s or applying to top UK universities.", "https://isaacphysics.org/", "No"],
    ["Flora", "App / Tool", "O & A Level", "Productivity", "The best free alternative to Forest. Block distracting apps and websites on your phone while growing virtual trees with friends.", "https://flora.appfinca.com/", "No"],
    ["Knowunity", "App / Tool", "O & A Level", "Multiple", "A massive, rapidly growing student community app where thousands of students share their personal A* study notes for free.", "https://knowunity.com/", "No"],
    ["ExamSolutions", "Website / Notes", "A Level", "Mathematics", "Legendary maths tutorials. Provides step-by-step video solutions for almost every A Level Maths topic and past paper question.", "https://www.examsolutions.net/", "No"],
    ["Madasmaths", "Website / Notes", "A Level", "Mathematics", "Famous on Reddit for having incredibly challenging A Level Maths papers. If you can solve these, the actual exam will feel easy.", "https://www.madasmaths.com/", "No"],
    ["GCE Guide", "Past Papers", "O & A Level", "Multiple", "Widely considered the fastest and most reliable repository for downloading CAIE past papers, mark schemes, and examiner reports.", "https://gceguide.com/", "No"],
    ["Obsidian", "App / Tool", "A Level", "Productivity", "A highly advanced, free note-taking app that links your notes together like a brain. Perfect for essay-heavy subjects like History or Law.", "https://obsidian.md/", "No"],
    ["Cold Turkey", "App / Tool", "O & A Level", "Productivity", "The strictest website blocker on the internet. Once you lock your computer for a study session, it is impossible to bypass.", "https://getcoldturkey.com/", "No"],
    ["Ali Abdaal", "YouTube Channel", "O & A Level", "Productivity", "Former Cambridge medical student. His videos on Active Recall and Spaced Repetition completely transformed how modern students study.", "https://www.youtube.com/@aliabdaal", "No"]
]

# Append to CSV
with open(filepath_csv, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(reddit_resources)

# Read all back to update HTML
resources = []
with open(filepath_csv, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        resources.append(row)

# Re-generate image URLs and votes
for idx, row in enumerate(resources):
    row["id"] = f"res_{idx}"
    hash_val = int(hashlib.md5(row["Resource Name"].encode()).hexdigest(), 16)
    row["votes"] = 40 + (hash_val % 410)
    if row["Is_SJ_Academy_Resource"] == "Yes":
        row["votes"] = 350 + (hash_val % 100)
        
    link = row["Link"]
    name = row["Resource Name"]
    img_url = ""
    domain = urlparse(link).netloc.replace('www.', '')
    
    if 'youtube.com' in domain:
        if '@' in link:
            handle = link.split('@')[-1].split('/')[0]
            img_url = f"https://unavatar.io/youtube/{handle}"
        else:
            img_url = f"https://unavatar.io/youtube/{name.replace(' ', '')}"
    elif 'instagram.com' in domain:
        handle = link.rstrip('/').split('/')[-1]
        img_url = f"https://unavatar.io/instagram/{handle}"
    elif 'reddit.com' in domain:
        subreddit = link.rstrip('/').split('/')[-1]
        img_url = f"https://unavatar.io/reddit/{subreddit}"
    elif 'sjacademy.pk' in domain:
        img_url = "https://sjacademy.pk/wp-content/uploads/2023/10/SJ-Academy-Logo-1.png"
    else:
        img_url = f"https://logo.clearbit.com/{domain}"
    row["Image_URL"] = img_url

resources_json = json.dumps(resources)
new_js_payload = f" {resources_json};\n  "

def update_html_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace JSON Payload
    start_marker = "const rawData ="
    end_marker = "const grid = document.getElementById"
    if start_marker in html and end_marker in html:
        start_idx = html.find(start_marker) + len(start_marker)
        end_idx = html.find(end_marker)
        html = html[:start_idx] + new_js_payload + html[end_idx:]
        
    # 2. Replace CTA Link
    old_link = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
    new_link = "https://www.sjacademy.pk/o-a-level-classes/"
    html = html.replace(old_link, new_link)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_html_file(html_filepath)
update_html_file(elementor_filepath)

print(f"Successfully added 12 Reddit resources and updated the CTA link. Total resources: {len(resources)}.")
