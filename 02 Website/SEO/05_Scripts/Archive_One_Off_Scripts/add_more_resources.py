import csv
import json
import hashlib
from urllib.parse import urlparse

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"
html_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"

new_resources = [
    ["Alt Academy", "Website / Notes", "O & A Level", "Multiple", "High-quality CAIE video lessons, topical worksheets, and revision crash courses.", "https://altacademy.org/", "No"],
    ["Seneca Learning", "App / Tool", "O & A Level", "Multiple", "Incredibly popular, interactive, and gamified free revision courses for IGCSE and A Level subjects.", "https://senecalearning.com/", "No"],
    ["Englicious", "Website / Notes", "O & A Level", "English", "Excellent grammar, vocabulary, and linguistic resources perfect for CAIE English Language (1123 & 9093).", "https://englicious.org/", "No"],
    ["The Sociology Guy", "Website / Notes", "A Level", "Sociology", "Detailed notes, exam techniques, and essay structures specifically for A Level Sociology (9699).", "https://thesociologyguy.com/", "No"],
    ["Dr. Frost Maths", "Website / Notes", "O & A Level", "Mathematics", "A massive, free database of maths resources, PPTs, and interactive questions for all levels.", "https://www.drfrostmaths.com/", "No"],
    ["Study Mind", "Website / Notes", "O & A Level", "Sciences", "Topical past paper questions, video tutorials, and revision notes for Bio, Chem, and Physics.", "https://studymind.co.uk/", "No"],
    ["Revisely", "Website / Notes", "O & A Level", "Multiple", "Free past papers, video tutorials, and revision notes covering a wide range of CAIE subjects.", "https://www.revisely.com/", "No"],
    ["BBC Bitesize", "Website / Notes", "O Level", "Multiple", "Although tailored to GCSE, the content flawlessly overlaps with Cambridge O Level and IGCSE syllabuses.", "https://www.bbc.co.uk/bitesize", "No"],
    ["IGCSE English Pro", "YouTube Channel", "O Level", "English", "Dedicated channel for scoring A* in O Level / IGCSE English. Covers directed writing, narratives, and comprehension.", "https://www.youtube.com/@igcseenglishpro", "No"],
    ["tutor2u Psychology", "YouTube Channel", "A Level", "Psychology", "The ultimate destination for A Level Psychology (9990) revision, core studies, and evaluation tips.", "https://www.youtube.com/@tutor2uPsychology", "No"],
    ["Asif Farooq", "YouTube Channel", "O Level", "Urdu", "Excellent Urdu First & Second Language (3248) lectures, syllabus breakdowns, and paper attempting techniques.", "https://www.youtube.com/@asiffarooqurdu", "No"],
    ["ExamQA", "YouTube Channel", "O & A Level", "Sciences", "High-yield summary videos and past paper walkthroughs for A Level and IGCSE sciences and maths.", "https://www.youtube.com/@examqa", "No"],
    ["The Cambridge Geek", "Website / Notes", "A Level", "Computer Science", "Niche but incredible site with specific A Level Computer Science (9618) notes and programming solutions.", "https://www.thecambridgegeek.com/", "No"],
    ["Markscheme.com", "Past Papers", "O & A Level", "Multiple", "Clean and simple interface to find past papers and mark schemes quickly when PapaCambridge is down.", "https://markscheme.com/", "No"],
    ["Revision World", "Past Papers", "O & A Level", "Multiple", "Another reliable backup source for fetching recent CAIE past papers and marking guidelines.", "https://revisionworld.com/", "No"],
    ["My Study Life", "App / Tool", "O & A Level", "Productivity", "The ultimate digital student planner. Track classes, homework, and CAIE exam schedules across all your devices.", "https://mystudylife.com/", "No"],
    ["Pomofocus", "App / Tool", "O & A Level", "Productivity", "A simple, customizable Pomodoro timer in your browser that works flawlessly for timing past paper practice.", "https://pomofocus.io/", "No"],
    ["A Level Law Notes (TSR)", "Community", "A Level", "Law", "The Student Room's dedicated section for A Level Law (9084). Features peer-reviewed essays and case summaries.", "https://www.thestudentroom.co.uk/revision/law/", "No"],
    ["SnapRevise", "App / Tool", "A Level", "Sciences", "Bite-sized, high-quality video courses and smart quizzes tailored for A Level exams.", "https://snaprevise.co.uk/", "No"]
]

# Append to CSV
with open(filepath, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(new_resources)

# Read all back to update HTML
resources = []
with open(filepath, mode='r', encoding='utf-8') as f:
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

# Update HTML file
with open(html_filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the old rawData payload with the new expanded one
start_marker = "const rawData ="
end_marker = "const grid = document.getElementById"
start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

new_js_payload = f" {resources_json};\n  "
html = html[:start_idx] + new_js_payload + html[end_idx:]

with open(html_filepath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Successfully added 19 new resources. Total resources: {len(resources)}.")
