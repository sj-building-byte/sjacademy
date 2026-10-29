import csv

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"

new_resources = [
    # NEW SJ ACADEMY ASSET
    ["SJ Academy A-Level Maths", "YouTube Channel", "A Level", "Mathematics", "SJ Academy's dedicated content for mastering A Level Mathematics, taught by expert KGS faculty.", "https://youtube.com/@sjacademy", "Yes"],
    
    # NEW APPS & PRODUCTIVITY TOOLS
    ["Forest", "App / Tool", "O & A Level", "Productivity", "The best focus and Pomodoro app. Plant virtual trees while you study to stop yourself from checking your phone.", "https://www.forestapp.cc/", "No"],
    ["Yeolpumta (YPT)", "App / Tool", "O & A Level", "Productivity", "Massively popular study timer app. Join CAIE study groups and compete with peers on study hours.", "https://pallo.io/en", "No"],
    ["Quizlet", "App / Tool", "O & A Level", "Multiple", "Excellent alternative to Anki. Find thousands of pre-made O Level and A Level flashcards created by other students.", "https://quizlet.com/", "No"],
    ["Photomath", "App / Tool", "O & A Level", "Mathematics", "Scan any O Level or A Level Math equation with your phone camera to get step-by-step solutions.", "https://photomath.com/", "No"],
    ["GeoGebra", "App / Tool", "A Level", "Mathematics", "Advanced interactive geometry, algebra, and calculus app. Crucial for A Level Further Maths visualisations.", "https://www.geogebra.org/", "No"],
    ["Notion", "App / Tool", "O & A Level", "Productivity", "The ultimate all-in-one workspace. Great for tracking CAIE syllabus checklists, revision timetables, and notes.", "https://www.notion.so/", "No"],
    ["Adobe Scan", "App / Tool", "O & A Level", "Productivity", "Essential app for scanning handwritten past papers and converting them to high-quality PDFs for marking.", "https://acrobat.adobe.com/us/en/mobile/scanner-app.html", "No"],
    ["Knowt", "App / Tool", "O & A Level", "Multiple", "Free alternative to Quizlet Learn. Import Quizlet flashcards directly and study without paywalls.", "https://knowt.com/", "No"]
]

with open(filepath, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(new_resources)

print(f"Successfully appended {len(new_resources)} new resources to {filepath}")
