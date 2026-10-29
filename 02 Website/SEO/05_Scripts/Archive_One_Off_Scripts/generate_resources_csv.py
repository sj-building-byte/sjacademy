import csv

headers = ["Resource Name", "Type", "Level", "Subject", "Description", "Link", "Is_SJ_Academy_Resource"]

resources = [
    # SJ ACADEMY ASSETS (The Core Funnel)
    ["SJ Academy O-Level Past Papers", "Past Papers", "O Level", "All Subjects", "Ad-free, instantly downloadable topical and yearly past papers for Cambridge O Levels.", "https://sjacademy.com/o-level-past-papers/", "Yes"],
    ["SJ Academy A-Level Past Papers", "Past Papers", "A Level", "All Subjects", "Comprehensive directory of A Level past papers covering 20+ subjects.", "https://sjacademy.com/a-level-past-papers/", "Yes"],
    ["SJ Academy IBCC Equivalence Calculator", "Tool / App", "O & A Level", "General", "Instantly calculate your Pakistani IBCC equivalence marks from CAIE O and A Level grades.", "https://sjacademy.com/ibcc-equivalence-calculator/", "Yes"],
    ["SJ Academy Scholarship Test", "Tool / App", "O & A Level", "General", "Take the interactive scholarship test to see your eligibility for up to 100% off tuition fees.", "https://sjacademy.com/scholarship-test/", "Yes"],
    ["CAIE Private Candidate Registration", "Service", "O & A Level", "General", "Seamless, hassle-free registration service for private O and A level candidates in Pakistan.", "https://sjacademy.com/caie-private-candidate-registration/", "Yes"],
    ["SJ Academy Official YouTube", "YouTube Channel", "O & A Level", "General", "Expert tutorials, exam hacks, and walkthroughs by KGS faculty and top CAIE instructors.", "https://youtube.com/@sjacademy", "Yes"],
    ["SJ Academy Official Instagram", "Community", "O & A Level", "General", "Daily CAIE updates, quick tips, and student community announcements.", "https://instagram.com/sjacademy", "Yes"],

    # MATHEMATICS
    ["Zainematics", "YouTube Channel", "O & A Level", "Mathematics", "Legendary channel for CAIE O & A Level Maths. Brilliant Urdu/Hindi explanations for South Asian students.", "https://www.youtube.com/@Zainematics", "No"],
    ["TLMaths", "YouTube Channel", "A Level", "Mathematics", "Over 3000 videos covering the entire A Level Maths and Further Maths syllabus in bite-sized pieces.", "https://www.youtube.com/@TLMaths", "No"],
    ["Intuitive", "YouTube Channel", "O & A Level", "Mathematics", "Focuses heavily on past paper exam hacks and worksheet walkthroughs. Incredible for exam prep.", "https://www.youtube.com/@Intuitive_education", "No"],
    ["Bicen Maths", "YouTube Channel", "A Level", "Mathematics", "High-quality, full-length A Level Maths whiteboard lessons. Great for learning from scratch.", "https://www.youtube.com/@BicenMaths", "No"],
    ["The Ginger Mathematician", "YouTube Channel", "O Level", "Mathematics", "Specializes in IGCSE and O Level Mathematics walkthroughs, predictions, and tips.", "https://www.youtube.com/@TheGingerMathematician", "No"],

    # PHYSICS
    ["Physics Online", "YouTube Channel", "A Level", "Physics", "Run by Lewis Matheson. Excellent visual experiments and theory breakdowns for A Level Physics.", "https://www.youtube.com/@PhysicsOnline", "No"],
    ["ETphysics", "YouTube Channel", "A Level", "Physics", "In-depth CAIE specific paper 1, 2, and 4 walkthroughs. Perfect for understanding the Cambridge mark scheme.", "https://www.youtube.com/@ETphysics", "No"],
    ["Science Shorts", "YouTube Channel", "A Level", "Physics", "Rapid-fire syllabus recaps and summary videos. Ideal for night-before revision.", "https://www.youtube.com/@ScienceShorts", "No"],
    ["Prosperity Academy", "YouTube Channel", "O Level", "Physics", "Excellent O Level and IGCSE Physics topical revision videos.", "https://www.youtube.com/@ProsperityAcademy", "No"],

    # CHEMISTRY
    ["Chemguide", "Website / Notes", "A Level", "Chemistry", "The absolute gold standard for A Level Physical, Inorganic, and Organic Chemistry explanations.", "https://www.chemguide.co.uk/", "No"],
    ["Allery Chemistry", "YouTube Channel", "A Level", "Chemistry", "Clear, well-structured module breakdowns and revision tutorials for A Level Chemistry.", "https://www.youtube.com/@AlleryChemistry", "No"],
    ["Bilawal Khan", "YouTube Channel", "O & A Level", "Chemistry", "Cambridge specific Chemistry lessons, extremely popular among students in the Middle East and Pakistan.", "https://www.youtube.com/@BilawalKhan", "No"],
    ["FreeScienceLessons", "YouTube Channel", "O Level", "Chemistry", "Straight to the point, no-nonsense foundational science concepts for O Levels/IGCSE.", "https://www.youtube.com/@Freesciencelessons", "No"],

    # BIOLOGY
    ["Behlogy", "YouTube Channel", "A Level", "Biology", "In-depth CAIE A Level Biology syllabus walkthroughs. Very highly rated by A* students.", "https://www.youtube.com/@Behlogy", "No"],
    ["Amoeba Sisters", "YouTube Channel", "O & A Level", "Biology", "Fun, animated videos that make complex cellular and molecular biology concepts easy to grasp.", "https://www.youtube.com/@AmoebaSisters", "No"],
    ["Cognito", "YouTube Channel", "O Level", "Biology", "Visual animations and concise explanations for O Level / IGCSE Sciences.", "https://www.youtube.com/@Cognitoedu", "No"],
    ["DSR Biology", "YouTube Channel", "O & A Level", "Biology", "O and A Level topical mastery, specific to the CAIE syllabus.", "https://www.youtube.com/@dsrbiology", "No"],

    # COMPUTER SCIENCE
    ["Papersdock", "YouTube Channel", "O & A Level", "Computer Science", "The best channel for CAIE CS (2210/9618). Covers pseudocode, Python, and theory.", "https://www.youtube.com/@papersdock", "No"],
    ["Craig'n'Dave", "YouTube Channel", "A Level", "Computer Science", "Structured CS curriculum videos covering everything from theory of computation to hardware.", "https://www.youtube.com/@craigndave", "No"],

    # ECON, BUSINESS & ACCOUNTING
    ["EconplusDal", "YouTube Channel", "A Level", "Economics", "The ultimate resource for A Level Economics. Master evaluation techniques and complex diagrams.", "https://www.youtube.com/@EconplusDal", "No"],
    ["Jacob Clifford", "YouTube Channel", "O & A Level", "Economics", "Fast-paced, engaging Micro and Macro economics basics.", "https://www.youtube.com/@JacobClifford", "No"],
    ["tutor2u", "Website / Notes", "A Level", "Business Studies", "Comprehensive revision notes, quizzes, and videos for A Level Business and Economics.", "https://www.tutor2u.net/", "No"],
    ["Accounting Lecture", "YouTube Channel", "O & A Level", "Accounting", "Covers CAIE O and A Level double-entry bookkeeping, ratios, and final accounts.", "https://www.youtube.com/@AccountingLecture", "No"],

    # PAK STUDIES & ISLAMIYAT
    ["Sir Iftikhar Ul Haq", "YouTube Channel", "O Level", "Islamiyat", "Extremely popular for O Level Islamiyat (2058). Teaches past paper answering structures.", "https://www.youtube.com/@siriftikharulhaq", "No"],
    ["Agha Zoo", "YouTube Channel", "O Level", "Pakistan Studies", "Engaging and comprehensive coverage of CAIE Pakistan Studies (2059) History and Geography.", "https://www.youtube.com/@aghazoo", "No"],

    # NOTES & REVISION PORTALS
    ["ZNotes", "Website / Notes", "O & A Level", "Multiple", "Community-driven, high-yield condensed revision sheets for almost every CAIE subject.", "https://znotes.org/", "No"],
    ["Save My Exams", "Website / Notes", "O & A Level", "Multiple", "Premium revision notes, topic questions, and model answers (Freemium).", "https://www.savemyexams.com/", "No"],
    ["Physics & Maths Tutor (PMT)", "Website / Notes", "O & A Level", "Multiple", "Unrivaled collection of topical past paper questions and mark schemes for STEM subjects.", "https://www.physicsandmathstutor.com/", "No"],
    ["GCE Guide", "Website / Notes", "O & A Level", "Multiple", "The classic repository for CAIE syllabus PDFs, learner guides, and examiner reports.", "https://gceguide.com/", "No"],
    ["MegaLecture", "Website / Notes", "O & A Level", "Multiple", "Free live classes recordings and comprehensive topical notes by experienced teachers.", "https://megalecture.com/", "No"],

    # PAST PAPERS & QUESTION BANKS
    ["PapaCambridge", "Past Papers", "O & A Level", "Multiple", "One of the oldest and largest repositories of CAIE past papers and marking schemes.", "https://papacambridge.com/", "No"],
    ["BestExamHelp", "Past Papers", "O & A Level", "Multiple", "Clean interface for finding yearly past papers without overwhelming ads.", "https://bestexamhelp.com/", "No"],
    ["Exam-Mate", "Past Papers", "O & A Level", "Multiple", "Excellent topical question generator for O Level, IGCSE, and A Levels.", "https://www.exam-mate.com/", "No"],
    ["Rove Papers", "App / Tool", "O & A Level", "Multiple", "Mobile app and website for accessing past papers, topical MCQs, and custom paper generation.", "https://rovepapers.com/", "No"],

    # TOOLS & UTILITIES
    ["Anki", "App / Tool", "O & A Level", "Multiple", "Spaced repetition flashcards software. Essential for memorizing Biology and Chemistry definitions.", "https://apps.ankiweb.net/", "No"],
    ["Desmos", "App / Tool", "O & A Level", "Mathematics", "Beautiful, interactive online graphing calculator for algebra and calculus.", "https://www.desmos.com/calculator", "No"],
    ["PhET Interactive Simulations", "App / Tool", "O & A Level", "Sciences", "Virtual Physics, Chemistry, and Math lab simulations by the University of Colorado.", "https://phet.colorado.edu/", "No"],

    # COMMUNITIES
    ["r/alevel (Reddit)", "Community", "A Level", "Multiple", "The largest A Level student community on the internet. Great for paper discussions and advice.", "https://www.reddit.com/r/alevel/", "No"],
    ["r/igcse (Reddit)", "Community", "O Level", "Multiple", "Massive community for O Level and IGCSE students worldwide.", "https://www.reddit.com/r/igcse/", "No"]
]

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"

with open(filepath, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(resources)

print(f"Successfully generated {filepath}")
