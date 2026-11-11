#!/usr/bin/env python3
"""Build the seven new SJ Academy subject tuition pages as Elementor HTML widgets.

Pages: O Level English (1123), O Level Computer Science (2210), O Level Urdu (3248),
A Level General Paper (8021), A Level Sociology (9699), A Level Psychology (9990),
A Level Urdu (9686).

Every page is built on the shared stylesheet sj-brand.css 3.1.1 (already in the site's
Additional CSS) and follows the landing page copy guidelines v1.2. Output is plain ASCII.
Run:  python3 build-subject-pages.py   ->  writes one *-elementor-widget.html per page.
"""
import html
import json
import re
import urllib.parse

WA_NUM = "923362144454"
GOOGLE = "https://maps.app.goo.gl/QSrQVThJrZMzJgKF8"
SITE = "https://www.sjacademy.pk"
REGISTER = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
SHEET = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRNaIRWzVbWjAz6uXXzEngSykiYmSrY_jeeRCjLgMXf1aF8Zo39EqRCM7s8VuE4RWzf0edXe7UhTCf8"
         "/pub?single=true&output=tsv&gid=")
GID_O, GID_AS, GID_A2 = "674937139", "1456859397", "1559855613"
ADDRESS = "Plot 29C, Lane 5, Seher Commercial Area, DHA Phase 7"
WHERE_STD = "In class at DHA Phase 7, Karachi, or live online"
TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'
RING = ('<svg class="sjx-ring" viewBox="0 0 120 70" preserveAspectRatio="none" aria-hidden="true"><path d="M14 38C10 18 40 6 68 7c27 '
        '1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30" fill="none" stroke="#D63A2F" stroke-width="2.6" stroke-linecap="round" '
        'vector-effect="non-scaling-stroke"/></svg>')


def ent(s):
    """Write every non-ASCII character as an HTML entity so nothing can be garbled."""
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def wa(text):
    return "https://wa.me/%s?text=%s" % (WA_NUM, urllib.parse.quote(text, safe=""))


def demo_text(level, subject, ref):
    return ("Hi SJ Academy, I'd like to book a free demo class.\nLevel: %s\nSubject: %s\nSession: May/June 2027\n"
            "Mode (in class or online): \n(Ref: %s)\nMy name is " % (level, subject, ref))


def q_text(subject_words, ref):
    return "Hi SJ Academy, I have a question about %s classes.\n(Ref: %s)\nMy name is " % (subject_words, ref)


def ticks(items):
    return "\n".join('          <li>%s<span>%s</span></li>' % (TICK, i) for i in items)


# ---------------------------------------------------------------------------------------------
# Shared reviews (real Google reviews already used on live SJ Academy pages)
# ---------------------------------------------------------------------------------------------
REV_GENERAL = [
    ("SJ Academy just feels like a good place to learn. The teachers are approachable and always willing to help. "
     "They break things down in a way that actually makes sense, so you don't feel lost. It's easy to speak up or ask "
     "questions, and you can tell they actually want you to succeed.", "H", "Hamza", "Google review"),
    ("Honestly, this tuition academy has been a really great experience. The teachers are super helpful and explain things "
     "in a way that actually makes sense, even the topics that usually feel confusing. You can tell they genuinely care "
     "about how well their students do, which makes a big difference.", "A", "Arham", "Google review"),
    ("The teachers at SJ Academy explain difficult concepts in a simple, understandable way and create a supportive learning "
     "environment where students feel confident asking questions.", "A", "Ayaan", "Google review"),
]
REV_ONLINE = ("As a student studying online from abroad, I can say this academy has been amazing! &#8230; The classes are highly "
              "interactive and well organised! I never feel left out despite being behind a screen.", "GB", "Ghazifa Batool",
              "Online student")
REV_PARENT = ("My daughters had an amazing experience at SJ academy. &#8230; Sir Salman is a very dedicated teacher who goes out "
              "of his way to support and guide students.", "ZM", "Zahra Mohsin", "Parent &middot; Google review")


# ---------------------------------------------------------------------------------------------
# Page data
# ---------------------------------------------------------------------------------------------
PAGES = []

# ============================ O LEVEL ENGLISH 1123 ============================
PAGES.append(dict(
    file="o-level-english-tuition-elementor-widget.html",
    url="/o-level-english-tuition/",
    wrap="sj-p-o-level-english", fam="enrol", level="o",
    crumb="English (1123)",
    keywords="o level english tuition (primary); o level english tuition karachi; o level english 1123; online o level english classes; "
             "o level english teacher karachi; o level english summary writing; o level english directed writing",
    yoast_title="O Level English Tuition Karachi & Online (1123) | SJ Academy",
    yoast_meta="O Level English Language (1123) tuition with Miss Tayyaba Yaseen: summary, directed writing and composition, marked to "
               "the mark scheme. In class in Karachi or online.",
    refs="OLE-OL (demo), OLE-Q (question)",
    pill="O Level English tuition in Karachi & online",
    h1='You speak English all day. 1123 still finds <span class="sj-hl">the gaps.</span>',
    lead="O Level English Language (1123) with Miss Tayyaba Yaseen, for the May/June 2027 exams. Summary, directed writing and "
         "composition, practised until the method is automatic. In class at DHA Phase 7, Karachi, or live online.",
    hand="150 words. not 151.",
    levels={"ol": dict(label="O Level", title="O Level English Language (1123)", gid=GID_O, kw=r"\benglish",
                       papers="Paper 1 Reading and Paper 2 Writing, 2 hours each",
                       when="Mon, Tue, Wed &amp; Thu &middot; 7:00 - 8:00 PM; Fri &middot; 7:00 - 8:00 PM (online)",
                       lvl="O Level", subj="English Language (1123)", ref="OLE-OL")},
    teacher_short="Miss Tayyaba",
    teacher="Miss Tayyaba Yaseen",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level English",
    proof=[("3+ years", "Miss Tayyaba teaching English"), ("2 papers", "Reading and Writing, 50% each")],
    problem=dict(
        h2='Good English. <span class="sj-hl">Lost marks.</span>',
        intro="Most O Level English students are not short of vocabulary. The marks go on the rules of the paper: a summary that "
              "runs long, a letter that copies the text instead of using it, a composition that tells instead of shows. "
              "These are the four places they usually go.",
        pins=[("The summary ran long", "Paper 1 caps the summary at 150 words of continuous writing. Every word past the limit is "
               "a word the examiner did not need, and lifting whole sentences from Text B is not summarising."),
              ("The text was copied, not used", "Directed writing gives you a 400 to 450 word text. Ten of its 25 marks are for "
               "reading: developing and evaluating those ideas, not repeating them in the same order."),
              ("The composition told, not showed", "\u201cIt was a beautiful day\u201d gives the examiner nothing to picture. "
               "Section B rewards detail, structure and sentences chosen for effect."),
              ("The language question named a device", "Spotting a simile is the start. The marks in the use of language "
               "question are for explaining the effect the words create.")],
        outro="None of this means your child is weak at English. These are exam habits, and habits change with answers that are "
              "marked properly.",
        hand2="show me, don't tell me"),
    tryit=dict(type="lost", intro="Three short answers in the style of O Level English 1123. Each one loses marks on one line. "
                                   "Tap the line you think did it.",
               labels=["Summary", "Directed writing", "Composition"],
               sheets=[
                   dict(q_small="Paper 1 style &middot; summary", q="Using Text B, summarise the benefits of school gardens. Write no more than 150 words.",
                        lines=[("School gardens let students learn science outside the classroom.", "R", "A clear point from the text, in the student's own words."),
                               ("Growing food teaches patience and responsibility.", "R", "A second relevant point, written concisely.")],
                        lost="For example, in 2019 one school in Lahore grew 200 kilograms of tomatoes.",
                        note="no examples in a summary", stamp="-1",
                        why="The first two lines are points. The last is an example, and examples and statistics are detail, not "
                            "main points. It spends words the 150-word limit cannot spare and earns nothing. Full marks come from "
                            "more benefits, each in your own words, with the examples left in the text."),
                   dict(q_small="Paper 2 style &middot; directed writing", q="You have read an article about plans to close the school canteen. Write a letter to your principal giving your views. [25]",
                        lines=[("I am writing to share my concerns about the plan to close the canteen.", "W", "A clear opening with the right register for a principal."),
                               ("The article claims students waste money there, but most of us buy one meal a day.", "R", "It uses an idea from the text and develops it with a counter-point.")],
                        lost="The article also says the canteen is expensive and the food is unhealthy.",
                        note="you copied it. now evaluate it", stamp="R",
                        why="This line repeats two ideas from the article without doing anything with them. Reading marks in "
                            "directed writing are for developing and evaluating the text. Full marks: say whether the claim is fair "
                            "and what should change, for example healthier options instead of closing it."),
                   dict(q_small="Paper 2 style &middot; descriptive composition", q="Describe a busy market at the moment it opens. [25]",
                        lines=[("Shutters rattled upwards one after another, like a row of yawns.", "W", "A precise image that lets the reader hear the scene."),
                               ("The smell of frying pakoras reached me before the stalls did.", "W", "Detail through a different sense, placed for effect.")],
                        lost="It was a very nice and beautiful morning.",
                        note="nice how? show it", stamp="W",
                        why="Two strong sentences, then one that tells the reader what to feel instead of showing it. In a "
                            "descriptive composition, vague words like nice and beautiful hold the mark down. Full marks: replace it "
                            "with something the reader can see, hear or smell.")],
               legend="R = reading marks. W = writing marks. Sample questions written by SJ Academy in the style of O Level English "
                      "Language 1123; marks are illustrative."),
    teacher_section=dict(
        h2='Your O Level English teacher, <span class="sj-hl">in Karachi</span> or online',
        para="Miss Tayyaba Yaseen teaches O Level English Language (1123) at SJ Academy, in class at DHA Phase 7 and live online. "
             "She has more than 3 years of teaching experience and also teaches A Level Sociology and General Paper, so she knows "
             "where O Level writing habits help or hurt later on.",
        ticks=["Summary practice against the 150-word limit until cutting words is a habit, not a panic",
               "Directed writing in every format the paper uses: speech, email, report, letter and article",
               "Descriptive and narrative compositions written, marked and rewritten",
               "Past paper answers marked to the 1123 mark scheme, so you see which line lost the mark"],
        initials="TY", card_sub="O Level English Language (1123), in class and online",
        card_facts=["3+ years teaching", "Background in psychology", "Also teaches A Level Sociology and General Paper"],
        tile=("Moving on to A Level?", "AS Level General Paper (8021) is also taught by Miss Tayyaba, so the essay habits built here carry straight on.",
              "/a-level-general-paper-tuition/", "See General Paper")),
    syllabus=dict(
        h2='The O Level English syllabus (1123), <span class="sj-hl">paper by paper</span>',
        intro="O Level English Language has two compulsory papers of equal weight, both 2 hours long. There is no coursework and "
              "no speaking test, and dictionaries are not allowed in either paper.",
        papers=[("Paper 1", "Paper 1", "Reading", ("2h", "50", "50%"),
                 "Section A (25 marks) is comprehension and use of language on Text A, a narrative of about 900 words. Section B "
                 "(25 marks) is a summary of Text B in no more than 150 words, plus a short response on implicit meaning.",
                 "Answer in your own words, explain effects rather than naming devices, and practise summaries against the clock "
                 "and the word count."),
                ("Paper 2", "Paper 2", "Writing", ("2h", "50", "50%"),
                 "Section A (25 marks) is directed writing: a speech, email, report, letter or article of 250 to 350 words built "
                 "from one or two short texts. Section B (25 marks) is a composition of 350 to 450 words from four titles, two "
                 "descriptive and two narrative.",
                 "Use the texts rather than copy them, match the register to the reader, and plan the composition before writing.")],
        note="Based on the Cambridge O Level English Language 1123 syllabus for exams in 2027 and 2028."),
    parents_extra="If your child starts falling behind, Miss Tayyaba will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level English past papers", "1123 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/english-language-1123/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='See every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>, or <a class="sj-link" href="%s/online-o-a-level-classes/">online O and A Level classes</a>.' % (SITE, SITE),
    faqs=[("What is the fee for O Level English tuition?", "From Rs. 8,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the O Level English classes?", "The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches O Level English at SJ Academy?", "Miss Tayyaba Yaseen teaches O Level English Language (1123), in class and online. She has more than 3 years of teaching experience and also teaches A Level Sociology and General Paper."),
          ("Is there an O Level English tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, or outside Karachi, you can join live online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("Do you offer online O Level English classes?", "Yes. Online students join a live class with the same past paper practice, marking and tests as students in Karachi, from anywhere in Pakistan or abroad."),
          ("What is the word limit for the O Level English summary?", "The Paper 1 summary must be continuous writing of no more than 150 words. Writing in note form, or going over the limit, costs marks. Summaries are practised in class against the word count."),
          ("How many words should an O Level English composition be?", "About 350 to 450 words for the Section B composition, and about 250 to 350 words for the directed writing task in Section A of Paper 2."),
          ("How do I get an A* in O Level English?", "Read the question for its purpose and audience, use the texts instead of copying them, stay inside the summary limit, and show rather than tell in your compositions. In class you practise exactly that on past paper questions, marked to the 1123 mark scheme."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you where the class is and how to catch up."),
          ("Can we take a free demo class before registering?", "Yes. The first class is free, in class or online. Book it on WhatsApp."),
          ("Can private candidates join the O Level English class?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="Sit one English class before you pay for any",
    final_p="Book a free demo, in class or online. Worst case, your child leaves knowing why examples don't belong in a summary.",
    course_name="O Level English Language (1123) tuition in Karachi and online",
    course_desc="O Level English Language tuition for the Cambridge 1123 syllabus with Miss Tayyaba Yaseen: Paper 1 Reading (comprehension, use of language, summary) and Paper 2 Writing (directed writing and composition). In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))

# ============================ O LEVEL COMPUTER SCIENCE 2210 ============================
PAGES.append(dict(
    file="o-level-computer-science-tuition-elementor-widget.html",
    url="/o-level-computer-science-tuition/",
    wrap="sj-p-o-level-cs", fam="enrol", level="o",
    crumb="Computer Science (2210)",
    keywords="o level computer science tuition (primary); o level computer science tuition karachi; o level computer science 2210; "
             "igcse computer science tuition (0478); online o level computer science classes; o level computer science teacher karachi; "
             "2210 pseudocode",
    yoast_title="O Level Computer Science Tuition in Karachi & Online | 2210 & IGCSE",
    yoast_meta="O Level Computer Science (2210) and IGCSE (0478) tuition with Sir Riza Walji: theory, pseudocode and past papers, in "
               "class in Karachi or online.",
    refs="OLCS-OL (O Level demo), OLCS-IG (IGCSE demo), OLCS-Q (question)",
    pill="O Level Computer Science tuition in Karachi & online",
    h1='Your code works. Your answer still <span class="sj-hl">lost the mark.</span>',
    lead="O Level Computer Science (2210) and IGCSE Computer Science (0478) with Sir Riza Walji, who has 9+ years of teaching "
         "behind him. For the May/June 2027 exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="detect is not correct",
    levels={"ol": dict(label="O Level", title="O Level Computer Science (2210)", gid=GID_O, kw=r"\bcomput",
                       papers="Paper 1 Computer Systems and Paper 2 Algorithms, Programming and Logic, 1 hour 45 minutes each",
                       when="Tue &amp; Thu &middot; 5:00 - 6:00 PM; Fri &middot; 3:00 - 4:00 PM",
                       lvl="O Level", subj="Computer Science (2210)", ref="OLCS-OL"),
            "ig": dict(label="IGCSE", title="IGCSE Computer Science (0478)", gid=GID_O, kw=r"\bcomput",
                       papers="Paper 1 Computer Systems and Paper 2 Algorithms, Programming and Logic, 1 hour 45 minutes each",
                       when="Tue &amp; Thu &middot; 5:00 - 6:00 PM; Fri &middot; 3:00 - 4:00 PM",
                       lvl="IGCSE", subj="Computer Science (0478)", ref="OLCS-IG")},
    teacher_short="Sir Riza",
    teacher="Sir Riza Walji",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Computer Science",
    proof=[("9+ years", "Sir Riza's teaching experience"), ("4 schools", "taught at, including Beaconhouse and Bay View Academy")],
    problem=dict(
        h2='Knew the topic. Wrote <span class="sj-hl">the wrong word.</span>',
        intro="O Level Computer Science is marked on exact words. An answer that is nearly right in your head is often worth "
              "nothing on paper. These are the four places the marks usually go.",
        pins=[("Detect became correct", "A parity check detects an error. It does not fix it. Swapping one verb for another "
               "can turn a full-mark answer into a zero."),
              ("What, not why", "When a question says explain, it wants a reason. Describing what something does answers a "
               "different question."),
              ("The test data was wrong", "Normal, abnormal, extreme and boundary data each mean something precise. Extreme data "
               "is accepted at the edge of the range, not just a big number."),
              ("The pseudocode drifted", "Paper 2 is written on paper with no computer to catch mistakes, and it ends with a "
               "15-mark scenario question that rewards clear, complete logic.")],
        outro="None of this means you can't do Computer Science. It means the examiner never saw what you knew. That part is fixable.",
        hand2="which word? exactly that word"),
    tryit=dict(type="lost", intro="Three short answers in the style of O Level Computer Science 2210. Each one loses a mark on one "
                                   "line. Tap the line you think did it.",
               labels=["Paper 1", "Paper 2", "Explain"],
               sheets=[
                   dict(q_small="Paper 1 style &middot; data transmission", q="Describe how a parity check is used to find errors in data sent between two computers. [3]",
                        lines=[("The sender and receiver agree to use odd or even parity.", "K", "Correct: both sides must agree on the parity first."),
                               ("A parity bit is added so that each byte has the agreed number of 1s.", "K", "Correct: this is how the parity bit is set.")],
                        lost="If there is an error, the receiver uses the parity bit to correct it.",
                        note="it detects. it does not correct", stamp="2/3",
                        why="A parity check only tells the receiver that something is wrong. It cannot say which bit changed, so "
                            "it cannot correct it. Full marks: the receiver counts the 1s in each byte and, if the count does not "
                            "match the agreed parity, the data is flagged as an error and is sent again."),
                   dict(q_small="Paper 2 style &middot; testing", q="A program accepts whole numbers from 1 to 100. Give one example each of normal, abnormal and extreme test data. [3]",
                        lines=[("Normal: 50", "K", "Correct: a typical value inside the range."),
                               ("Abnormal: \"abc\"", "K", "Correct: data that should be rejected.")],
                        lost="Extreme: 1000",
                        note="1000 is abnormal. extreme is 1 or 100", stamp="2/3",
                        why="Extreme data is the largest or smallest value that should still be accepted, so here it is 1 or 100. "
                            "1000 is outside the range, which makes it abnormal data. Every term in this topic has a precise meaning, "
                            "and the mark scheme holds you to it."),
                   dict(q_small="Paper 1 style &middot; hardware", q="Explain why a solid state drive (SSD) is often used in a laptop instead of a hard disk drive. [2]",
                        lines=[("An SSD has no moving parts.", "K", "A correct feature of an SSD, which earns the first mark.")],
                        lost="So an SSD is better.",
                        note="better how? give the reason", stamp="1/2",
                        why="The first line is right, then the answer stops at better, which is not a reason. Explain means say "
                            "why it matters for a laptop. Full marks: with no moving parts it is less likely to be damaged if the "
                            "laptop is dropped or moved, and it uses less power, so the battery lasts longer.")],
               legend="K = a mark-earning point. Sample questions written by SJ Academy in the style of O Level Computer Science 2210; "
                      "marks are illustrative."),
    teacher_section=dict(
        h2='Your O Level Computer Science tutor: <span class="sj-hl">Sir Riza Walji</span>',
        para="Sir Riza Walji teaches O Level Computer Science (2210) and IGCSE Computer Science (0478) at SJ Academy, in class at "
             "DHA Phase 7 and live online. He has 9+ years of teaching experience and has taught at Beaconhouse, Bay View Academy, "
             "Links School and Jaffar Public School. He also teaches A Level Computer Science (9618), so students who carry on "
             "keep the same teacher.",
        ticks=["Theory taught with the exact keywords the mark scheme looks for, so answers say detect, not correct",
               "Pseudocode written to the Cambridge style, with trace tables and dry runs practised by hand",
               "The 15-mark Paper 2 scenario question practised until planning it is automatic",
               "Past paper answers marked to the 2210 mark scheme, so you see which line lost the mark"],
        photo=("https://www.sjacademy.pk/wp-content/uploads/2025/11/Sir-Riza-768x454.webp", 768, 454),
        initials="RW", card_sub="O Level Computer Science (2210) and IGCSE (0478), in class and online",
        card_facts=["9+ years teaching", "Taught at Beaconhouse and Bay View Academy", "Also teaches A Level Computer Science"],
        tile=("Carrying on to A Level?", "A Level Computer Science (9618) is also taught by Sir Riza, so the habits built here carry straight on.",
              "/a-level-computer-science-tuition/", "See A Level Computer Science")),
    syllabus=dict(
        h2='The O Level Computer Science syllabus (2210), <span class="sj-hl">paper by paper</span>',
        intro="O Level Computer Science has two compulsory papers of equal weight. IGCSE Computer Science (0478) uses the same "
              "papers, which is why O Level and IGCSE students sit in the same class. Calculators are not allowed in either paper.",
        papers=[("Paper 1", "Paper 1", "Computer Systems", ("1h 45m", "75", "50%"),
                 "Short-answer and structured questions on topics 1 to 6: data representation, data transmission, hardware, "
                 "software, the internet and its uses, and automated and emerging technologies.",
                 "Learn definitions word for word, convert binary, denary and hexadecimal by hand, and practise explain questions "
                 "that give reasons."),
                ("Paper 2", "Paper 2", "Algorithms, Programming and Logic", ("1h 45m", "75", "50%"),
                 "Short-answer and structured questions on topics 7 to 10: algorithm design and problem-solving, programming, "
                 "databases and Boolean logic, ending with a 15-mark scenario question.",
                 "Write pseudocode by hand, trace algorithms with trace tables, build logic circuits and truth tables, and plan the "
                 "scenario question before writing.")],
        note="Based on the Cambridge O Level Computer Science 2210 syllabus for exams in 2026, 2027 and 2028."),
    parents_extra="If your child starts falling behind, Sir Riza will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Computer Science past papers", "2210 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/computer-science-2210/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Maths as well? See <a class="sj-link" href="%s/o-level-math-tuition/">O Level Maths tuition</a>, or every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % (SITE, SITE),
    faqs=[("What is the fee for O Level Computer Science tuition?", "From Rs. 8,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the O Level Computer Science classes?", "The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches O Level Computer Science at SJ Academy?", "Sir Riza Walji teaches O Level Computer Science (2210) and IGCSE Computer Science (0478). He has 9+ years of teaching experience and has taught at Beaconhouse, Bay View Academy, Links School and Jaffar Public School. He also teaches A Level Computer Science (9618)."),
          ("Is there an O Level Computer Science tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, or outside Karachi, you can join live online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("Do you offer online O Level Computer Science classes?", "Yes. Online students join the same live class as students in Karachi, with the same teacher, tests and marking."),
          ("Do you teach IGCSE Computer Science (0478) too?", "Yes. IGCSE Computer Science (0478) uses the same two papers as O Level 2210, so O Level and IGCSE students sit in the same class. Tell us your syllabus code when you book the demo."),
          ("Can I use a calculator in O Level Computer Science?", "No. Calculators are not allowed in either 2210 paper, so binary, denary and hexadecimal conversions are practised by hand in class."),
          ("Which programming language is used in O Level Computer Science?", "Paper 2 answers are written mainly in pseudocode, and the syllabus expects practical programming experience behind them. Ask on WhatsApp which language the class uses for practice."),
          ("How do I get an A* in O Level Computer Science?", "Learn the keywords exactly, give reasons when a question says explain, know your test data terms, and write pseudocode that a reader can follow line by line. In class you practise past paper questions marked to the 2210 mark scheme until those habits are automatic."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you where the class is and how to catch up."),
          ("Can we take a free demo class before registering?", "Yes. The first class is free, in class or online. Book it on WhatsApp."),
          ("Can private candidates join the O Level Computer Science class?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="One free class. Then decide.",
    final_p="Sit one Computer Science class with Sir Riza before you pay for any. Worst case, you leave knowing why parity detects but never corrects.",
    course_name="O Level Computer Science (2210) and IGCSE Computer Science (0478) tuition in Karachi and online",
    course_desc="O Level Computer Science tuition for the Cambridge 2210 syllabus, with IGCSE 0478 students in the same class, taught by Sir Riza Walji: Paper 1 Computer Systems and Paper 2 Algorithms, Programming and Logic. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level and Cambridge IGCSE",
))

# ============================ O LEVEL URDU 3248 ============================
PAGES.append(dict(
    file="o-level-urdu-tuition-elementor-widget.html",
    url="/o-level-urdu-tuition/",
    wrap="sj-p-o-level-urdu", fam="enrol", level="o",
    crumb="Urdu (3248)",
    keywords="o level urdu tuition (primary); o level urdu tuition karachi; o level urdu 3248; o level urdu second language; "
             "online o level urdu classes; o level urdu translation; o level urdu teacher",
    yoast_title="O Level Urdu Tuition in Karachi & Online (3248) | SJ Academy",
    yoast_meta="O Level Second Language Urdu (3248) tuition with Miss Asmat Zafar: summary, writing and translation practice, in class in "
               "Karachi or online.",
    refs="OLU-OL (demo), OLU-Q (question)",
    pill="O Level Urdu tuition in Karachi & online",
    h1='You speak Urdu every day. The paper marks it <span class="sj-hl">differently.</span>',
    lead="O Level Second Language Urdu (3248) with Miss Asmat Zafar, former Head of Urdu at Education Bay. For the May/June 2027 "
         "exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="translate the meaning, not the words",
    levels={"ol": dict(label="O Level", title="O Level Second Language Urdu (3248)", gid=GID_O, kw=r"\burdu",
                       papers="Paper 1 Reading and Writing (1 hour 45 minutes) and Paper 2 Grammar, Writing and Translation (1 hour 30 minutes)",
                       when="Mon, Tue, Wed &amp; Thu &middot; 6:00 - 7:00 PM; Fri &middot; 4:30 - 5:30 PM (online); Sun &middot; 12:30 - 1:30 PM (online)",
                       lvl="O Level", subj="Urdu (3248)", ref="OLU-OL")},
    teacher_short="Miss Asmat",
    teacher="Miss Asmat Zafar",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Urdu",
    proof=[("Former Head", "of Urdu at Education Bay"), ("Senior Author", "worked with the University of Cambridge")],
    problem=dict(
        h2='Fluent Urdu. <span class="sj-hl">Average marks.</span>',
        intro="Speaking Urdu at home helps, but 3248 is a written exam with strict tasks and word limits. Students who speak it "
              "fluently still lose marks in these four places.",
        pins=[("The summary ran over 100 words", "Paper 1 asks for a paragraph-length summary of no more than 100 words, in your "
               "own words as far as possible. Long or copied summaries lose marks."),
              ("The register was wrong", "An email to a friend and a report for a newspaper are not written the same way. Purpose, "
               "format and audience are part of the mark."),
              ("The translation kept English word order", "Paper 2 ends with a 150-word passage from English into Urdu, worth 15 "
               "marks. Word-for-word translation reads like English written in Urdu script."),
              ("Grammar slipped under pressure", "Sentence transformation and the grammar cloze test verb forms, agreement and "
               "post-positions, and small slips add up quickly.")],
        outro="None of this means your child's Urdu is weak. These are exam skills, and they improve with writing that is marked "
              "properly.",
        hand2="who is reading this? write for them"),
    tryit=dict(type="map", intro="Every 3248 mark sits in one of nine exercises. Tap an exercise to see where students usually "
                                  "lose marks in it.",
               maps=[("Paper 1 &middot; Reading and Writing &middot; 50 marks", [
                         ("Exercise 1", "Short-answer questions", 8, "Single words or phrases from a short text such as an advert or leaflet. Read the question carefully and give only what it asks for."),
                         ("Exercise 2", "Multiple matching", 9, "Match sentences to short paragraphs. Look for meaning, not a repeated word, because the matching word is often a trap."),
                         ("Exercise 3", "Note-making", 9, "Brief notes under given headings from a longer text. Notes should be short and specific, not copied sentences."),
                         ("Exercise 4", "Summary, up to 100 words", 10, "A paragraph about the Exercise 3 text, in your own words as far as possible. Stay under 100 words."),
                         ("Exercise 5", "Writing, about 150 words", 14, "A short functional piece such as an email. The purpose, format and audience are given, and all three are marked.")]),
                     ("Paper 2 &middot; Grammar, Writing and Translation &middot; 50 marks", [
                         ("Exercise 1", "Sentence transformation", 5, "Rewrite five sentences using a prompt without changing the meaning. One wrong verb form can cost the mark."),
                         ("Exercise 2", "Multiple-choice cloze", 10, "Fill gaps from options: verb forms, agreement, comparatives, post-positions and vocabulary in context."),
                         ("Exercise 3", "Extended writing, about 200 words", 20, "The biggest single task. Organise ideas in paragraphs with linking words, and use the right register."),
                         ("Exercise 4", "Translation, English to Urdu", 15, "About 150 words from English into Urdu. Translate the meaning in natural Urdu word order, not word by word.")])],
               legend="Mark totals from the Cambridge O Level Second Language Urdu 3248 syllabus for exams in 2027 to 2029. Dictionaries are not allowed in either paper."),
    teacher_section=dict(
        h2='Your O Level Urdu teacher, <span class="sj-hl">in Karachi</span> or online',
        para="Miss Asmat Zafar teaches O Level Urdu and A Level Urdu (9686) at SJ Academy, in class at DHA Phase 7 and live online. "
             "She is a former Head of Urdu at Education Bay, has worked as a Senior Author with the University of Cambridge, and "
             "has taught at St. Michael's Convent.",
        ticks=["Summaries practised against the 100-word limit, in students' own words",
               "Emails, articles, reports and reviews written for a given purpose and reader, then marked",
               "English-to-Urdu translation practised as meaning, not word-for-word",
               "Grammar drilled through the sentence transformation and cloze formats the paper uses"],
        initials="AZ", card_sub="O Level Urdu (3248) and A Level Urdu (9686), in class and online",
        card_facts=["Former Head of Urdu at Education Bay", "Has worked as a Senior Author with the University of Cambridge", "Has taught at St. Michael's Convent"],
        tile=("Carrying on to A Level?", "A Level Urdu (9686) is also taught by Miss Asmat, with the set texts, essay and reading and writing papers.",
              "/a-level-urdu-tuition/", "See A Level Urdu")),
    syllabus=dict(
        h2='The O Level Urdu syllabus (3248), <span class="sj-hl">paper by paper</span>',
        intro="O Level Second Language Urdu has two compulsory papers of equal weight. All questions and answers are in Urdu, "
              "except the translation, which is set in English and answered in Urdu.",
        papers=[("Paper 1", "Paper 1", "Reading and Writing", ("1h 45m", "50", "50%"),
                 "Five exercises: short answers, multiple matching, note-making, a summary of no more than 100 words, and a "
                 "functional writing task of about 150 words.",
                 "Read for meaning, keep notes short, write summaries in your own words, and match register to the reader."),
                ("Paper 2", "Paper 2", "Grammar, Writing and Translation", ("1h 30m", "50", "50%"),
                 "Four exercises: sentence transformation, a multiple-choice cloze passage, extended writing of about 200 words, "
                 "and a translation of about 150 words from English into Urdu.",
                 "Practise verb forms and agreement, plan the 200-word piece in paragraphs, and translate meaning, not words.")],
        note="Based on the Cambridge O Level Second Language Urdu 3248 syllabus for exams in 2027, 2028 and 2029."),
    parents_extra="If your child starts falling behind, Miss Asmat will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Urdu past papers", "3248 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/urdu-second-language-3248/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Islamiat and Pakistan Studies too? See every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % SITE,
    faqs=[("What is the fee for O Level Urdu tuition?", "From Rs. 8,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the O Level Urdu classes?", "There are in-class and online batches. The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches O Level Urdu at SJ Academy?", "Miss Asmat Zafar teaches O Level Urdu and A Level Urdu. She is a former Head of Urdu at Education Bay, has worked as a Senior Author with the University of Cambridge, and has taught at St. Michael's Convent."),
          ("Is there an O Level Urdu tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, or outside Karachi, you can join an online batch. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("Do you offer online O Level Urdu classes?", "Yes. There are dedicated online Urdu batches, with the same marking and tests as the in-class batch."),
          ("Which O Level Urdu do you teach, 3247 or 3248?", "We teach O Level Second Language Urdu (3248), the Urdu taken by most O Level students in Pakistan. If you are entered for First Language Urdu (3247), ask us on WhatsApp before you book."),
          ("What is the word limit for the O Level Urdu summary?", "The Paper 1 summary is a paragraph of no more than 100 words, written in your own words as far as possible."),
          ("Are dictionaries allowed in O Level Urdu?", "No. Dictionaries are not allowed in either 3248 paper, which is why vocabulary and grammar are built up through practice in class."),
          ("How do I get an A* in O Level Urdu?", "Stay inside the word limits, match your writing to the purpose and reader, keep grammar accurate under time pressure, and translate meaning in natural Urdu. In class you practise each exercise on past papers, marked against the mark scheme."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you how to catch up."),
          ("Can we take a free demo class before registering?", "Yes. The first class is free, in class or online. Book it on WhatsApp."),
          ("Can private candidates join the O Level Urdu class?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="Sit one Urdu class before you pay for any",
    final_p="Book a free demo, in class or online. Worst case, your child leaves knowing why word-for-word translation never sounds like Urdu.",
    course_name="O Level Second Language Urdu (3248) tuition in Karachi and online",
    course_desc="O Level Urdu tuition for the Cambridge 3248 Second Language Urdu syllabus with Miss Asmat Zafar: Paper 1 Reading and Writing and Paper 2 Grammar, Writing and Translation. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))

# ============================ A LEVEL GENERAL PAPER 8021 ============================
PAGES.append(dict(
    file="a-level-general-paper-tuition-elementor-widget.html",
    url="/a-level-general-paper-tuition/",
    wrap="sj-p-a-level-gp", fam="enrol", level="a",
    crumb="General Paper (8021)",
    keywords="a level general paper tuition (primary); general paper a level; english general paper 8021; general paper tuition karachi; "
             "as level general paper; general paper essay; online general paper classes",
    yoast_title="A Level General Paper Tuition in Karachi & Online (8021) | SJ Academy",
    yoast_meta="AS Level English General Paper (8021) tuition with Miss Tayyaba Yaseen: essay planning and comprehension, marked to the "
               "mark scheme. In class in Karachi or online.",
    refs="ALGP-AS (demo), ALGP-Q (question)",
    pill="A Level General Paper tuition in Karachi & online",
    h1='Opinions are free. General Paper marks <span class="sj-hl">are not.</span>',
    lead="AS Level English General Paper (8021) with Miss Tayyaba Yaseen, for the May/June 2027 exams. Essays that argue, "
         "comprehension in your own words, in class at DHA Phase 7, Karachi, or live online.",
    hand="since the dawn of time? no.",
    levels={"as": dict(label="AS Level", title="AS Level English General Paper (8021)", gid=GID_AS, kw=r"\benglish",
                       papers="Paper 1 Essay (1 hour 15 minutes) and Paper 2 Comprehension (1 hour 45 minutes)",
                       when="Mon &amp; Wed &middot; 6:00 - 7:00 PM",
                       lvl="AS", subj="English General Paper (8021)", ref="ALGP-AS")},
    teacher_short="Miss Tayyaba",
    teacher="Miss Tayyaba Yaseen",
    batch="AS Level only, May/June 2027. Running now, still open.",
    fee="From Rs. 10,500 a month",
    q_words="A Level General Paper",
    proof=[("3+ years", "Miss Tayyaba teaching"), ("AS Level", "General Paper is a one-year subject")],
    problem=dict(
        h2='Strong views. <span class="sj-hl">Weak marks.</span>',
        intro="General Paper looks like the easy subject because there is nothing to memorise. That is exactly why students lose "
              "marks in it. These are the four places they usually go.",
        pins=[("The opening said nothing", "Paper 1 is one essay of about 600 to 700 words. An opening paragraph about human "
               "history is words the essay cannot spare."),
              ("The example was vague", "\u201cMany people say\u201d is not evidence. Specific, relevant examples, ideally from "
               "your own country, are what make an argument land."),
              ("The essay never answered the question", "Ten titles, one choice. Writing about the topic instead of the exact "
               "question asked is the most common way to lose a whole band."),
              ("The comprehension was copied", "Paper 2 has two sections of 25 marks. When a question asks for your own words, "
               "lifting the passage's phrasing earns nothing.")],
        outro="None of this means you can't write. It means the examiner needs an argument, not an opinion. That part is fixable.",
        hand2="which example? name it"),
    tryit=dict(type="lost", intro="Three short answers in the style of General Paper 8021. Each one loses marks on one line. Tap "
                                   "the line you think did it.",
               labels=["Opening", "Evidence", "Own words"],
               sheets=[
                   dict(q_small="Paper 1 style &middot; essay opening", q="\u2018Social media does more harm than good.\u2019 How far do you agree?",
                        lines=[("Social media now shapes how young people get news, make friends and see themselves.", "A", "A focused opening that names the areas the essay will weigh."),
                               ("This essay argues that the harm depends less on the platforms than on how they are used.", "A", "A clear line of argument that answers how far.")],
                        lost="Since the dawn of time, humans have always found ways to communicate.",
                        note="get to the question", stamp="-",
                        why="The first two lines are a strong opening. This one is a generic opener that could start any essay on "
                            "communication. It uses words a 600 to 700 word essay cannot spare and earns nothing. Cut it and start "
                            "with the question."),
                   dict(q_small="Paper 1 style &middot; using evidence", q="\u2018Governments should spend more on public transport than on roads.\u2019 Discuss.",
                        lines=[("Public transport moves more people for each rupee spent than private cars do.", "A", "A clear argument that answers the question."),
                               ("Karachi's Green Line bus gave many commuters a cheaper, faster alternative to driving.", "E", "A specific, local example used as evidence.")],
                        lost="Many people say public transport is good for everyone.",
                        note="which people? say what happened", stamp="E",
                        why="After a specific example, this line falls back on a vague claim with no evidence behind it. General "
                            "Paper rewards examples that are specific and relevant. Full marks: name a real case, or explain the "
                            "effect on the people who use it."),
                   dict(q_small="Paper 2 style &middot; comprehension", q="Using your own words, explain why the writer believes cities should plant more trees. [3]",
                        lines=[("Trees cool the streets, so people suffer less in the summer heat.", "C", "The writer's idea, expressed in the student's own words."),
                               ("They also clean the air, which helps people breathe more easily.", "C", "A second idea, paraphrased rather than copied.")],
                        lost="Trees act as \u201cnature's free air conditioners\u201d in crowded neighbourhoods.",
                        note="that's the writer's phrase", stamp="2/3",
                        why="The question says using your own words, and this line lifts the writer's phrase straight from the "
                            "passage. Copied wording does not show understanding. Full marks: say it plainly, for example that the "
                            "shade lowers temperatures where many people live close together.")],
               legend="A = argument. E = evidence. C = a comprehension point. Sample questions written by SJ Academy in the style of "
                      "AS Level English General Paper 8021; marks are illustrative."),
    teacher_section=dict(
        h2='Your General Paper teacher, <span class="sj-hl">in Karachi</span> or online',
        para="Miss Tayyaba Yaseen teaches AS Level English General Paper (8021) at SJ Academy, in class at DHA Phase 7 and live "
             "online. She has more than 3 years of teaching experience and also teaches A Level Sociology, so students learn to "
             "back an argument with evidence the way both subjects reward.",
        ticks=["Essay plans for every type of title, so you choose your question in minutes, not half an hour",
               "A bank of specific, local examples built across the course, ready for any topic",
               "Comprehension practised in your own words, with every answer marked",
               "Timed essays marked to the 8021 mark scheme, so you see which paragraph lost the band"],
        initials="TY", card_sub="AS Level English General Paper (8021), in class and online",
        card_facts=["3+ years teaching", "Background in psychology", "Also teaches A Level Sociology and O Level English"],
        tile=("Taking Sociology too?", "A Level Sociology (9699) is also taught by Miss Tayyaba, and the essay skills carry across both.",
              "/a-level-sociology-tuition/", "See A Level Sociology")),
    syllabus=dict(
        h2='The General Paper syllabus (8021), <span class="sj-hl">paper by paper</span>',
        intro="English General Paper is an AS Level only qualification: there is no A2 year. Students take both papers in the same "
              "exam series, and each is worth half of the AS Level.",
        papers=[("Paper 1", "Paper 1", "Essay", ("1h 15m", "30", "50%"),
                 "One essay from a choice of ten questions on contemporary issues, with a recommended length of about 600 to 700 "
                 "words.",
                 "Choose the question you can argue, not the topic you like. Plan before writing, and back every point with a "
                 "specific example."),
                ("Paper 2", "Paper 2", "Comprehension", ("1h 45m", "50", "50%"),
                 "Compulsory questions on reading material, in two sections of 25 marks each.",
                 "Read the question for exactly what it asks, use your own words when told to, and keep answers concise.")],
        note="Based on the Cambridge International AS Level English General Paper 8021 syllabus for exams in 2025, 2026 and 2027."),
    parents_extra="If your child starts falling behind, Miss Tayyaba will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("Past paper and mark scheme viewer", "Open a General Paper paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("Subject combinations tool", "See which subjects to pair for the degree you want. Free.", "/a-level-subject-combinations-tool/", "Open the tool"),
               ("University admission criteria", "Check what LUMS, IBA, NUST and others ask for. Free.", "/university-admission-criteria-tool/", "Check the criteria")],
    more_links='See every subject on the <a class="sj-link" href="%s/a-level-tuition-center-karachi/">A Level tuition page</a>, or <a class="sj-link" href="%s/online-o-a-level-classes/">online O and A Level classes</a>.' % (SITE, SITE),
    faqs=[("What is the fee for A Level General Paper tuition?", "From Rs. 10,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the General Paper classes?", "The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches General Paper at SJ Academy?", "Miss Tayyaba Yaseen teaches AS Level English General Paper (8021). She has more than 3 years of teaching experience and also teaches A Level Sociology and O Level English."),
          ("Is General Paper an AS Level or an A Level?", "General Paper (8021) is an AS Level only qualification. There is no A2 year, so it is usually taken alongside your other AS subjects."),
          ("How long should a General Paper essay be?", "Cambridge recommends about 600 to 700 words for the Paper 1 essay, written in 1 hour 15 minutes, so planning time matters."),
          ("Is there a General Paper tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, or outside Karachi, you can join live online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("Do you offer online General Paper classes?", "Yes. Online students join the same live class, with the same essay marking."),
          ("How do I get a good grade in General Paper?", "Answer the exact question, argue a clear line, back every point with a specific example, and use your own words in comprehension. In class you write timed essays and comprehension answers that are marked against the mark scheme."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you how to catch up."),
          ("Can I take a free demo class before I register?", "Yes. The first class is free, in class or online. Book it on WhatsApp."),
          ("Can private candidates take General Paper?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="One free class. Then decide.",
    final_p="Sit one General Paper class with Miss Tayyaba before you pay for any. Worst case, you leave never starting an essay with the dawn of time again.",
    course_name="AS Level English General Paper (8021) tuition in Karachi and online",
    course_desc="AS Level English General Paper tuition for the Cambridge 8021 syllabus with Miss Tayyaba Yaseen: Paper 1 Essay and Paper 2 Comprehension. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge International AS Level",
))

# ============================ A LEVEL SOCIOLOGY 9699 ============================
PAGES.append(dict(
    file="a-level-sociology-tuition-elementor-widget.html",
    url="/a-level-sociology-tuition/",
    wrap="sj-p-a-level-sociology", fam="enrol", level="a",
    crumb="Sociology (9699)",
    keywords="a level sociology tuition (primary); a level sociology tuition karachi; a level sociology 9699; a level sociology online classes; "
             "as level sociology; a2 sociology; a level sociology teacher",
    yoast_title="A Level Sociology Tuition in Karachi & Online (9699) | SJ Academy",
    yoast_meta="A Level Sociology (9699) tuition with Miss Tayyaba Yaseen, AS and A2: evidence, evaluation and essays marked to the mark "
               "scheme. Online and in Karachi.",
    refs="ALSOC-AS, ALSOC-A2 (demo), ALSOC-Q (question)",
    pill="A Level Sociology tuition in Karachi & online",
    h1='Sociology is not common sense. The examiner wants <span class="sj-hl">evidence.</span>',
    lead="A Level Sociology (9699) with Miss Tayyaba Yaseen, AS and A2 classes for May/June 2027. Live online, with an in-class "
         "batch at DHA Phase 7, Karachi.",
    hand="your house is not a study",
    levels={"as": dict(label="AS Level", title="AS Level Sociology (9699)", gid=GID_AS, kw=r"\bsocio",
                       papers="Paper 1 (socialisation, identity and methods of research) and Paper 2 (the family)",
                       when="See the class timetable", lvl="AS", subj="Sociology (9699)", ref="ALSOC-AS"),
            "a2": dict(label="A2 Level", title="A2 Level Sociology (9699)", gid=GID_A2, kw=r"\bsocio",
                       papers="Paper 3 (education) and Paper 4 (globalisation, media and religion)",
                       when="Tue, Thu &amp; Fri &middot; 8:00 - 9:00 PM (online)", lvl="A2", subj="Sociology (9699)", ref="ALSOC-A2")},
    teacher_short="Miss Tayyaba",
    teacher="Miss Tayyaba Yaseen",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 10,500 a month",
    q_words="A Level Sociology",
    proof=[("3+ years", "Miss Tayyaba teaching"), ("Psychology", "background behind her Sociology teaching")],
    problem=dict(
        h2='Interesting answer. <span class="sj-hl">No marks.</span>',
        intro="Sociology feels familiar because it is about families, schools and the media, things everyone has an opinion on. "
              "That familiarity is where the marks go. These are the four usual places.",
        pins=[("Opinion instead of evidence", "Your own family is not sociological evidence. Answers need concepts, studies, "
               "trends and theories."),
              ("Strength without the reason", "\u201cQuestionnaires are easy\u201d is not evaluation. The mark is for linking it to "
               "reliability, validity or representativeness."),
              ("Two sides, no judgement", "Every essay is marked on analysis and evaluation. Ending with \u201cboth views have "
               "good points\u201d leaves the top band empty."),
              ("The 26-mark essay ran out of time", "Papers 1 and 2 each end with a 26-mark essay, nearly half the paper. Students "
               "who spend too long on short answers rush the part that matters most.")],
        outro="None of this means your child is bad at Sociology. These are writing habits, and they change with essays that are "
              "marked properly.",
        hand2="which study? which trend?"),
    tryit=dict(type="lost", intro="Three short answers in the style of A Level Sociology 9699. Each one loses marks on one line. "
                                   "Tap the line you think did it.",
               labels=["Methods", "Argue against", "Evaluate"],
               sheets=[
                   dict(q_small="Paper 1 style &middot; methods of research", q="Evaluate the use of questionnaires in sociological research.",
                        lines=[("Questionnaires can reach large samples cheaply, so results may be more representative.", "AO3", "A strength, linked to representativeness."),
                               ("Pre-set answers can force people into choices that do not match their views, lowering validity.", "AO3", "A limitation, linked to validity.")],
                        lost="Questionnaires are also easy to do.",
                        note="easy how? link it to reliability", stamp="-",
                        why="The first two lines evaluate. This one makes a claim without saying why it matters. Full marks: "
                            "standardised questions can be repeated by another researcher in the same way, which makes the findings "
                            "more reliable."),
                   dict(q_small="Paper 2 style &middot; argue against a view", q="\u2018The nuclear family is still the dominant family form.\u2019 Using sociological material, give arguments against this view.",
                        lines=[("Rising divorce has increased the number of lone-parent households.", "AO2", "A trend used as evidence against the view."),
                               ("Remarriage creates reconstituted families, which differ from the traditional nuclear form.", "AO2", "A second family form, used as evidence.")],
                        lost="In my family, we live with my grandparents, so the nuclear family is not dominant.",
                        note="your house is not a study", stamp="-",
                        why="Personal experience is not sociological material. Extended families are a valid point, but they need "
                            "evidence behind them. Full marks: use trends, studies or a postmodernist view of family diversity "
                            "instead of one household."),
                   dict(q_small="Paper 2 style &middot; essay conclusion", q="Evaluate the view that the family mainly benefits capitalism. [26]",
                        lines=[("Marxists argue the family reproduces labour and encourages consumption, which benefits capitalism.", "AO1", "The view explained with its theory."),
                               ("Functionalists reply that the family meets the needs of its members and of society as a whole.", "AO3", "An opposing view, used to evaluate.")],
                        lost="In conclusion, both views have good points.",
                        note="decide. how far?", stamp="-",
                        why="Two views are explained, then the essay refuses to judge between them. The top band needs a reasoned "
                            "conclusion. Full marks: say which view is more convincing and why, for example that the Marxist view "
                            "explains the family's economic role but ignores the benefits feminists and functionalists point to.")],
               legend="AO1 = knowledge. AO2 = interpretation and application. AO3 = analysis and evaluation. Sample questions written by "
                      "SJ Academy in the style of A Level Sociology 9699; marks are illustrative."),
    teacher_section=dict(
        h2='Your A Level Sociology tutor: <span class="sj-hl">Miss Tayyaba</span> Yaseen',
        para="Miss Tayyaba Yaseen teaches AS and A2 Sociology (9699) at SJ Academy, live online and in class at DHA Phase 7. She "
             "has more than 3 years of teaching experience and a background in psychology, which shows in how she teaches "
             "research methods and evidence.",
        ticks=["A bank of studies, theories and trends built topic by topic, so every answer has evidence ready",
               "Evaluation practised as a habit: every strength and limitation linked to reliability, validity or representativeness",
               "The 26-mark and 35-mark essays planned and timed until the structure is automatic",
               "Answers marked to the 9699 mark scheme, so you see which line lost the mark"],
        initials="TY", card_sub="AS and A2 Sociology (9699), online and in class",
        card_facts=["3+ years teaching", "Background in psychology", "Also teaches General Paper and O Level English"],
        tile=("Taking Psychology too?", "A Level Psychology (9990) shares the research methods thinking, and it is taught at SJ Academy as well.",
              "/a-level-psychology-tuition/", "See A Level Psychology")),
    syllabus=dict(
        h2='The A Level Sociology syllabus (9699), <span class="sj-hl">paper by paper</span>',
        intro="AS students sit Papers 1 and 2. The full A Level adds Papers 3 and 4. Every paper is written, with no coursework, "
              "and every paper rewards knowledge, application and evaluation together.",
        papers=[("Paper 1", "Paper 1 &middot; AS Level", "Socialisation, Identity and Methods of Research", ("1h 30m", "60", "25%"),
                 "Section A has three compulsory questions. Section B is one 26-mark essay from a choice of two. It is 50% of a "
                 "standalone AS.",
                 "Learn the methods with their strengths and limitations, and practise arguing against a view using sociological "
                 "material."),
                ("Paper 2", "Paper 2 &middot; AS Level", "The Family", ("1h 30m", "60", "25%"),
                 "The same structure as Paper 1: three compulsory questions, then one 26-mark essay from a choice of two. It is 50% "
                 "of a standalone AS.",
                 "Know the functionalist, Marxist, feminist, New Right and postmodernist views, and the trends behind family "
                 "diversity."),
                ("Paper 3", "Paper 3 &middot; A2 Level", "Education", ("1h 15m", "50", "21%"),
                 "Four compulsory questions worth increasing marks, ending with a 26-mark essay.",
                 "Theories of education, social mobility and the curriculum, and how class, ethnicity and gender affect attainment."),
                ("Paper 4", "Paper 4 &middot; A2 Level", "Globalisation, Media and Religion", ("1h 45m", "70", "29%"),
                 "Two essays of 35 marks each, chosen from two different sections: globalisation, media and religion.",
                 "Pick two sections early and build deep evidence for both. Each essay must weigh contrasting views.")],
        note="Based on the Cambridge International AS &amp; A Level Sociology 9699 syllabus for exams in 2024 to 2026 (version 3). Check the 2027 syllabus for any update."),
    parents_extra="If your child starts falling behind, Miss Tayyaba will tell you. You can ask for an update at any time",
    reviews=[REV_GENERAL[0], REV_ONLINE, REV_GENERAL[2]],
    review_h2='&ldquo;I never feel left out despite being <span class="sj-hl">behind a screen</span>&rdquo;',
    resources=[("A Level Sociology past papers", "9699 question papers and mark schemes, by year and paper. Free.", "/a-level-past-papers/sociology-9699/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("A Level grade calculator", "See the A2 marks you need for the grade you want. Free.", "/a-level-grade-strategy-tool/", "Open the calculator"),
               ("Subject combinations tool", "See which subjects to pair with Sociology for your degree. Free.", "/a-level-subject-combinations-tool/", "Open the tool")],
    more_links='See every subject on the <a class="sj-link" href="%s/a-level-tuition-center-karachi/">A Level tuition page</a>, or <a class="sj-link" href="%s/online-o-a-level-classes/">online O and A Level classes</a>.' % (SITE, SITE),
    faqs=[("What is the fee for A Level Sociology tuition?", "From Rs. 10,500 a month per subject for AS or A2, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the A Level Sociology classes?", "There are AS and A2 batches, most of them live online. The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches A Level Sociology at SJ Academy?", "Miss Tayyaba Yaseen teaches AS and A2 Sociology (9699). She has more than 3 years of teaching experience and a background in psychology."),
          ("Do you offer online A Level Sociology classes?", "Yes. Most Sociology batches are live online, so you can join from anywhere in Pakistan or abroad, with the same marking and tests."),
          ("Is there an A Level Sociology tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("Do I need to have studied Sociology at O Level?", "No. Cambridge does not expect students starting AS Sociology to have studied it before."),
          ("What is the difference between AS and A2 Sociology?", "AS Level is Paper 1 (socialisation, identity and methods of research) and Paper 2 (the family). A2 adds Paper 3 (education) and Paper 4, where you write two essays from globalisation, media and religion."),
          ("How do I get an A* in A Level Sociology?", "Back every point with sociological evidence, link every strength and limitation to a concept like validity or reliability, and end every essay with a reasoned judgement. In class you practise exactly that, with answers marked to the 9699 mark scheme."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you how to catch up."),
          ("Can I take a free demo class before I register?", "Yes. The first class is free. Send us your level, AS or A2, on WhatsApp and we will book you in."),
          ("Can private candidates take A Level Sociology?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="One free class. Then decide.",
    final_p="Sit one Sociology class with Miss Tayyaba before you pay for any. Worst case, you leave knowing why your khala's opinion is not a study.",
    course_name="A Level Sociology (9699) tuition online and in Karachi",
    course_desc="AS and A2 Level Sociology tuition for the Cambridge 9699 syllabus with Miss Tayyaba Yaseen: Paper 1 socialisation, identity and methods of research, Paper 2 the family, Paper 3 education and Paper 4 globalisation, media and religion. Live online and in class at DHA Phase 7, Karachi.",
    edu_level="Cambridge International AS and A Level",
))

# ============================ A LEVEL PSYCHOLOGY 9990 ============================
PAGES.append(dict(
    file="a-level-psychology-tuition-elementor-widget.html",
    url="/a-level-psychology-tuition/",
    wrap="sj-p-a-level-psychology", fam="enrol", level="a",
    crumb="Psychology (9990)",
    keywords="a level psychology tuition (primary); a level psychology tuition karachi; a level psychology 9990; a level psychology online classes; "
             "as level psychology; a2 psychology; a level psychology core studies",
    yoast_title="A Level Psychology Tuition in Karachi & Online (9990) | SJ Academy",
    yoast_meta="A Level Psychology (9990) tuition with Miss Muzna Zaidi, AS and A2: core studies, research methods and evaluation, marked "
               "to the mark scheme.",
    refs="ALPSY-AS, ALPSY-A2 (demo), ALPSY-Q (question)",
    pill="A Level Psychology tuition in Karachi & online",
    h1='Remembering Bandura is easy. Evaluating him is <span class="sj-hl">the marks.</span>',
    lead="A Level Psychology (9990) with Miss Muzna Zaidi, AS and A2 classes for May/June 2027, with a focus on the analytical "
         "writing the papers reward. In class at DHA Phase 7, Karachi, or live online.",
    hand="reliable is not generalisable",
    levels={"as": dict(label="AS Level", title="AS Level Psychology (9990)", gid=GID_AS, kw=r"\bpsych",
                       papers="Paper 1 (approaches, issues and debates) and Paper 2 (research methods)",
                       when="Wed &amp; Fri &middot; 9:00 - 10:00 PM", lvl="AS", subj="Psychology (9990)", ref="ALPSY-AS"),
            "a2": dict(label="A2 Level", title="A2 Level Psychology (9990)", gid=GID_A2, kw=r"\bpsych",
                       papers="Paper 3 and Paper 4 (specialist options)",
                       when="Tue &amp; Thu &middot; 9:00 - 10:00 PM", lvl="A2", subj="Psychology (9990)", ref="ALPSY-A2")},
    teacher_short="Miss Muzna",
    teacher="Miss Muzna Zaidi",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 10,500 a month",
    q_words="A Level Psychology",
    proof=[("AS and A2", "both levels of 9990 taught"), ("4 papers", "all written, no coursework")],
    problem=dict(
        h2='Knew the study. Lost the <span class="sj-hl">evaluation.</span>',
        intro="A Level Psychology students usually know the core studies well. The marks go on what happens next. These are the "
              "four places they usually go.",
        pins=[("Reliability became generalisability", "The papers mark these terms precisely. Saying a study is unreliable "
               "when you mean its sample was narrow costs the mark."),
              ("The finding was too vague", "\u201cChildren copied the adult\u201d describes the idea, not the finding. Results "
               "need detail: which children, which behaviour, compared with whom."),
              ("\u201cMake it fair\u201d", "Research methods questions want the actual control: the same instructions, the same "
               "room, the same timing. Fair is not a method."),
              ("The study wasn't applied", "Many questions give you a scenario. Answers that describe the study without using it "
               "for the scenario stay in the lower marks.")],
        outro="None of this means your child is bad at Psychology. It is precision, and precision improves with answers that are "
              "marked properly.",
        hand2="which control? say it exactly"),
    tryit=dict(type="lost", intro="Three short answers in the style of A Level Psychology 9990. Each one loses a mark on one line. "
                                   "Tap the line you think did it.",
               labels=["Finding", "Evaluate", "Methods"],
               sheets=[
                   dict(q_small="Paper 1 style &middot; core study", q="Describe one finding from the Bandura et al. study of aggression. [2]",
                        lines=[("Children who watched an aggressive model showed more imitative physical aggression.", "K", "A specific finding, with the behaviour named.")],
                        lost="So the children copied the adult.",
                        note="compared with whom?", stamp="1/2",
                        why="The first line is a good start. The second just restates it vaguely instead of completing the "
                            "finding. Full marks need the comparison: more imitative aggression than children in the non-aggressive "
                            "or control groups, with boys showing more imitative physical aggression than girls."),
                   dict(q_small="Paper 1 style &middot; evaluation", q="Evaluate the Andrade study on doodling in terms of generalisability. [3]",
                        lines=[("Participants came from one research panel in Cambridge, UK.", "E", "A relevant feature of the sample."),
                               ("They had just taken part in another study, so may have been more tired than most people.", "E", "A second feature, explained.")],
                        lost="So the study is unreliable.",
                        note="that's generalisability, not reliability", stamp="2/3",
                        why="The evidence is about who the participants were, which is generalisability. The conclusion then "
                            "names reliability, which is about consistency. Full marks: so the findings may not generalise to people "
                            "who are not tired, or to people outside that panel."),
                   dict(q_small="Paper 2 style &middot; research methods", q="Suggest one way a researcher could standardise the procedure of a memory experiment. [2]",
                        lines=[("Every participant could be tested in the same quiet room.", "M", "A specific control, which earns a mark.")],
                        lost="This would make the experiment fair.",
                        note="fair how? say what it controls", stamp="1/2",
                        why="Fair is not a reason the mark scheme rewards. The second mark is for explaining what the control "
                            "does. Full marks: so that noise cannot affect some participants' recall more than others, which would "
                            "be an extraneous variable.")],
               legend="K = knowledge. E = evaluation point. M = methods point. Sample questions written by SJ Academy in the style of A "
                      "Level Psychology 9990; marks are illustrative."),
    teacher_section=dict(
        h2='Your A Level Psychology tutor: <span class="sj-hl">Miss Muzna Zaidi</span>',
        para="Miss Muzna Zaidi teaches AS and A2 Psychology (9990) at SJ Academy. She teaches the Cambridge A Level Psychology "
             "syllabus with a focus on analytical writing: taking each core study from description to evaluation to application, "
             "the way the papers mark it.",
        ticks=["Core studies learned with their findings in detail, ready for describe and outline questions",
               "Evaluation practised with the exact terms: reliability, validity, generalisability, ethics and more",
               "Research methods taught through planning questions, so controls and variables come out precise",
               "Answers marked to the 9990 mark scheme, so you see which line lost the mark"],
        initials="MZ", card_sub="AS and A2 Psychology (9990)",
        card_facts=["Teaches the full Cambridge 9990 syllabus", "Focus on analytical writing", "AS and A2 batches"],
        tile=("Taking Sociology too?", "A Level Sociology (9699) shares the research methods thinking, and it is taught at SJ Academy as well.",
              "/a-level-sociology-tuition/", "See A Level Sociology")),
    syllabus=dict(
        h2='The A Level Psychology syllabus (9990), <span class="sj-hl">paper by paper</span>',
        intro="AS students sit Papers 1 and 2, built around the core studies and research methods. The full A Level adds Papers 3 "
              "and 4 on two specialist options chosen from clinical, consumer, health and organisational psychology.",
        papers=[("Paper 1", "Paper 1 &middot; AS Level", "Approaches, Issues and Debates", ("1h 30m", "60", "25%"),
                 "Short-answer questions on the core studies, then extended response and essay questions. It is 50% of a "
                 "standalone AS.",
                 "Know each core study's aim, procedure and findings in detail, and evaluate it with the right terms."),
                ("Paper 2", "Paper 2 &middot; AS Level", "Research Methods", ("1h 30m", "60", "25%"),
                 "Short-answer and scenario-based questions on research methods, plus a planning question. It is 50% of a "
                 "standalone AS.",
                 "Practise designing studies: variables, controls, sampling, ethics and data, all applied to a scenario."),
                ("Paper 3", "Paper 3 &middot; A2 Level", "Specialist Options: Approaches, Issues and Debates", ("1h 30m", "60", "25%"),
                 "Questions on the two specialist options you study.",
                 "Learn each option's topics, theories and studies, and evaluate them with issues and debates."),
                ("Paper 4", "Paper 4 &middot; A2 Level", "Specialist Options: Application and Research Methods", ("1h 30m", "60", "25%"),
                 "Application and research methods questions on your two specialist options, including a planning question.",
                 "Apply the options to new scenarios and plan research that would test them.")],
        note="Based on the Cambridge International AS &amp; A Level Psychology 9990 syllabus. Check the 2027 syllabus for any update."),
    parents_extra="If your child starts falling behind, Miss Muzna will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("A Level Psychology past papers", "9990 question papers and mark schemes, by year and paper. Free.", "/a-level-past-papers/psychology-9990/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("A Level grade calculator", "See the A2 marks you need for the grade you want. Free.", "/a-level-grade-strategy-tool/", "Open the calculator"),
               ("University admission criteria", "Check what LUMS, IBA, AKU and others ask for. Free.", "/university-admission-criteria-tool/", "Check the criteria")],
    more_links='Taking Biology with Psychology? See <a class="sj-link" href="%s/a-level-biology-tuition/">A Level Biology tuition</a>, or every subject on the <a class="sj-link" href="%s/a-level-tuition-center-karachi/">A Level tuition page</a>.' % (SITE, SITE),
    faqs=[("What is the fee for A Level Psychology tuition?", "From Rs. 10,500 a month per subject for AS or A2, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the A Level Psychology classes?", "AS and A2 Psychology run in the evening, Pakistan time. The current days and times are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches A Level Psychology at SJ Academy?", "Miss Muzna Zaidi teaches AS and A2 Psychology (9990), with a focus on analytical writing."),
          ("Do you offer online A Level Psychology classes?", "Yes. Online students join the live class, with the same marking and tests."),
          ("Is there an A Level Psychology tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, you can join live online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("What is the difference between AS and A2 Psychology?", "AS Level is Paper 1 (approaches, issues and debates, built on the core studies) and Paper 2 (research methods). A2 adds Papers 3 and 4 on two specialist options from clinical, consumer, health and organisational psychology."),
          ("Which specialist options do you teach for A2 Psychology?", "Students study two of the four options. Ask us on WhatsApp which two the current A2 batch is taking."),
          ("Does A Level Psychology have coursework?", "No. All four 9990 papers are written exams."),
          ("How do I get an A* in A Level Psychology?", "Know the core studies in detail, use evaluation terms exactly, give specific controls in methods answers, and apply studies to the scenario in front of you. In class, answers are marked to the 9990 mark scheme until that precision is automatic."),
          ("Can I still join the May/June 2027 batch?", "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you how to catch up."),
          ("Can I take a free demo class before I register?", "Yes. The first class is free. Send us your level, AS or A2, on WhatsApp and we will book you in."),
          ("Can private candidates take A Level Psychology?", "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="One free class. Then decide.",
    final_p="Sit one Psychology class with Miss Muzna before you pay for any. Worst case, you leave never mixing up reliable and generalisable again.",
    course_name="A Level Psychology (9990) tuition in Karachi and online",
    course_desc="AS and A2 Level Psychology tuition for the Cambridge 9990 syllabus with Miss Muzna Zaidi: Paper 1 approaches, issues and debates, Paper 2 research methods, and Papers 3 and 4 on the specialist options. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge International AS and A Level",
))

# ============================ A LEVEL URDU 9686 ============================
PAGES.append(dict(
    file="a-level-urdu-tuition-elementor-widget.html",
    url="/a-level-urdu-tuition/",
    wrap="sj-p-a-level-urdu", fam="enrol", level="a",
    crumb="Urdu (9686)",
    keywords="a level urdu tuition (primary); a level urdu 9686; a level urdu tuition karachi; a level urdu online classes; "
             "a level urdu set texts; a level urdu essay; a level urdu teacher",
    yoast_title="A Level Urdu Tuition in Karachi & Online (9686) | SJ Academy",
    yoast_meta="A Level Urdu (9686) tuition with Miss Asmat Zafar: reading and writing, essay and set texts, marked to the mark scheme. In "
               "class in Karachi or online.",
    refs="ALU-A (demo), ALU-Q (question)",
    pill="A Level Urdu tuition in Karachi & online",
    h1='Great Urdu can still <span class="sj-hl">hit a ceiling.</span>',
    lead="A Level Urdu (9686) with Miss Asmat Zafar, former Head of Urdu at Education Bay, for the May/June 2027 exams. Reading "
         "and writing, the essay and the set texts, in class at DHA Phase 7, Karachi, or live online.",
    hand="601 words? capped.",
    levels={"a": dict(label="A Level", title="A Level Urdu (9686)", gid="", kw="",
                      papers="Paper 2 Reading and Writing, Paper 3 Essay and Paper 4 Texts, all in one series",
                      when="Ask us on WhatsApp for the current timings", lvl="A Level", subj="Urdu (9686)", ref="ALU-A")},
    teacher_short="Miss Asmat",
    teacher="Miss Asmat Zafar",
    batch="A Level, all three papers in May/June 2027. Admissions open.",
    fee="From Rs. 10,500 a month",
    q_words="A Level Urdu",
    proof=[("Former Head", "of Urdu at Education Bay"), ("Senior Author", "worked with the University of Cambridge")],
    problem=dict(
        h2='Fluent Urdu. <span class="sj-hl">Capped marks.</span>',
        intro="A Level Urdu students are usually strong in the language. The marks go on the rules of each paper, and a few of "
              "them are strict. These are the four places they usually go.",
        pins=[("The texts answer ran past 600 words", "Cambridge advises 500 to 600 words for each Paper 4 answer. Write more "
               "and that answer cannot be placed above the 16 to 17 band out of 25."),
              ("The essay was all content", "Paper 3 gives 24 of its 40 marks for the quality of the language and 16 for content. "
               "Ideas alone cannot carry it."),
              ("The answer retold the story", "Paper 4 rewards understanding of how a text works and what the author is saying, "
               "not a summary of the plot."),
              ("The response forgot the opinion", "The last Paper 2 task draws on both passages and adds your own view. Leaving "
               "out the personal response leaves marks on the table.")],
        outro="None of this means your child's Urdu is weak. These are exam rules, and they are easy to learn once someone marks "
              "against them.",
        hand2="less story, more meaning"),
    tryit=dict(type="map", intro="A Level Urdu is three papers sat together. Tap a task to see where students usually lose marks in it.",
               maps=[("Paper 2 &middot; Reading and Writing &middot; 70 marks", [
                         ("Passage 1", "Vocabulary and grammar tests", 10, "Two 5-mark tests on the first passage. Small grammar slips cost marks quickly."),
                         ("Passage 1", "Comprehension questions", 20, "15 marks for content and 5 for the quality of your Urdu. Answer exactly what is asked."),
                         ("Passage 2", "Comprehension questions", 20, "Again 15 for content and 5 for language. Do not copy the passage when you can say it yourself."),
                         ("Both passages", "Response of about 140 words", 20, "10 marks for information from both passages, 5 for your own opinion and 5 for language.")]),
                     ("Paper 3 &middot; Essay &middot; 40 marks", [
                         ("One essay", "250 to 400 words from five topics", 40, "24 marks for the quality of the language and 16 for content. The set topics change every year.")]),
                     ("Paper 4 &middot; Texts &middot; 75 marks", [
                         ("Three answers", "One per text, 25 marks each", 75, "500 to 600 words each. Go over 600 and the answer cannot score above the 16 to 17 band.")])],
               legend="Mark totals from the Cambridge International A Level Urdu 9686 syllabus. Dictionaries are not allowed in any paper. "
                      "Unannotated set texts may be taken into the Paper 4 exam."),
    teacher_section=dict(
        h2='Your A Level Urdu teacher: <span class="sj-hl">Miss Asmat Zafar</span>',
        para="Miss Asmat Zafar teaches A Level Urdu (9686) and O Level Urdu at SJ Academy. She is a former Head of Urdu at "
             "Education Bay, has worked as a Senior Author with the University of Cambridge, and has taught at St. Michael's "
             "Convent.",
        ticks=["Set texts taught for meaning and the author's message, not just the plot",
               "Paper 4 answers written to 500 to 600 words, so no answer caps itself",
               "Essays on the year's set topics, marked for language as well as content",
               "Reading and writing practice on both passages, with the opinion task built in"],
        initials="AZ", card_sub="A Level Urdu (9686) and O Level Urdu, in class and online",
        card_facts=["Former Head of Urdu at Education Bay", "Has worked as a Senior Author with the University of Cambridge", "Has taught at St. Michael's Convent"],
        tile=("Younger sibling at O Level?", "O Level Urdu (3248) is also taught by Miss Asmat, with in-class and online batches.",
              "/o-level-urdu-tuition/", "See O Level Urdu")),
    syllabus=dict(
        h2='The A Level Urdu syllabus (9686), <span class="sj-hl">paper by paper</span>',
        intro="A Level Urdu (9686) is for centres in Pakistan and is taken as a full A Level: all three papers in the same exam "
              "series, with no staged AS year. All questions and answers are in Urdu.",
        papers=[("Paper 2", "Paper 2", "Reading and Writing", ("1h 45m", "70", "c39%"),
                 "Two related passages, together no more than 750 words, with vocabulary, grammar and comprehension questions, then "
                 "a response of about 140 words drawing on both passages and your own opinion.",
                 "Answer precisely, keep your Urdu accurate, and plan the final response so both passages and your view are in it."),
                ("Paper 3", "Paper 3", "Essay", ("1h 30m", "40", "c22%"),
                 "One essay of 250 to 400 words from five questions, one on each of the year's set topics.",
                 "Prepare all five topics, and write in varied, accurate Urdu, because language carries 24 of the 40 marks."),
                ("Paper 4", "Paper 4", "Texts", ("2h 30m", "75", "39%"),
                 "Three answers, each on a different set text, with at least one from each section of the list. Each answer is "
                 "worth 25 marks.",
                 "Know the texts in detail, stay within 500 to 600 words, and write about meaning and the author's intention.")],
        note="Based on the Cambridge International A Level Urdu 9686 syllabus for centres in Pakistan. The set texts and essay topics for 2027 are listed in the 2027 syllabus."),
    thresholds=("161", "That is the weighted mark out of 180 an A* needed in A Level Urdu (9686) in June 2026. An A needed 147. With "
                "language marks in every paper, the gap between those grades is usually accuracy, not knowledge."),
    parents_extra="If your child starts falling behind, Miss Asmat will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("A Level Urdu past papers", "9686 question papers and mark schemes, by year and paper. Free.", "/a-level-past-papers/urdu-9686/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("A Level grade thresholds", "How raw marks turn into an A*, A or B. Free.", "/blog/a-level-thresholds-guide/", "Read the guide"),
               ("University admission criteria", "Check what LUMS, IBA, NUST and others ask for. Free.", "/university-admission-criteria-tool/", "Check the criteria")],
    more_links='See every subject on the <a class="sj-link" href="%s/a-level-tuition-center-karachi/">A Level tuition page</a>, or <a class="sj-link" href="%s/online-o-a-level-classes/">online O and A Level classes</a>.' % (SITE, SITE),
    faqs=[("What is the fee for A Level Urdu tuition?", "From Rs. 10,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE),
          ("When are the A Level Urdu classes?", "Message us on WhatsApp for the current A Level Urdu timings, or check the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE),
          ("Who teaches A Level Urdu at SJ Academy?", "Miss Asmat Zafar teaches A Level Urdu (9686). She is a former Head of Urdu at Education Bay, has worked as a Senior Author with the University of Cambridge, and has taught at St. Michael's Convent."),
          ("Is A Level Urdu taken as AS and A2?", "No. A Level Urdu (9686) is sat as a full A Level, with all three papers in the same exam series. Cambridge offers AS Level Urdu Language as a separate syllabus (8686)."),
          ("What is the word limit for A Level Urdu Paper 4?", "Cambridge advises 500 to 600 words for each Paper 4 answer. An answer longer than 600 words cannot be placed higher than the 16 to 17 band out of 25."),
          ("Can I take the set texts into the A Level Urdu exam?", "Yes, for Paper 4, as long as they are unannotated: not written in or marked in any way."),
          ("Is there an A Level Urdu tutor near me in Karachi?", "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, ask about joining online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE)),
          ("How do I get an A* in A Level Urdu?", "Write accurate, varied Urdu, because language is marked in every paper; keep Paper 4 answers within 500 to 600 words; write about meaning, not plot; and prepare all five essay topics. In June 2026 an A* needed 161 out of 180 weighted marks."),
          ("Can I still join the May/June 2027 batch?", "Yes, admissions are open. Message us on WhatsApp and we will tell you where the class is in the set texts and how to catch up."),
          ("Can I take a free demo class before I register?", "Yes. The first class is free. Book it on WhatsApp."),
          ("Can private candidates take A Level Urdu?", "Yes. 9686 is available to private candidates. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)],
    final_h2="One free class. Then decide.",
    final_p="Sit one A Level Urdu class with Miss Asmat before you pay for any. Worst case, you leave knowing exactly where 600 words ends.",
    course_name="A Level Urdu (9686) tuition in Karachi and online",
    course_desc="A Level Urdu tuition for the Cambridge 9686 syllabus (for centres in Pakistan) with Miss Asmat Zafar: Paper 2 Reading and Writing, Paper 3 Essay and Paper 4 Texts. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge International A Level",
))


# ---------------------------------------------------------------------------------------------
# SEO pass 2 (9 Nov 2026): titles, metas, at-a-glance facts, extra FAQs, photo, schema offers
# ---------------------------------------------------------------------------------------------
PHOTO = ("https://www.sjacademy.pk/wp-content/uploads/2026/10/IMG_6923_Original-1-1.webp", 768, 473)
SEO = {
 "o-level-english": dict(
   title="O Level English Tuition Karachi & Online (1123) | SJ Academy",
   meta="O Level English (1123) tuition in Karachi & online with Miss Tayyaba Yaseen. Summary, directed writing and composition, marked properly. Free demo class.",
   subject="O Level English Language (1123)", papers="Paper 1 Reading and Paper 2 Writing, 2 hours each, 50% each",
   mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
   faqs=[("Who is the best O Level English teacher in Karachi?", "The best teacher for your child is the one whose method fixes their mistakes. At SJ Academy, Miss Tayyaba Yaseen marks every summary, letter and composition against the 1123 mark scheme, and your child can sit one class free to judge for themselves."),
         ("Is O Level English 1123 the same as IGCSE First Language English?", "No. IGCSE First Language English (0500) is a different syllabus with different papers, and Cambridge does not allow it to be taken in the same exam series as O Level English 1123. This class prepares students for 1123.")]),
 "o-level-cs": dict(
   title="O Level Computer Science Tuition in Karachi & Online | 2210",
   meta="O Level Computer Science (2210) & IGCSE (0478) tuition with Sir Riza Walji, 9+ years teaching. Theory, pseudocode, past papers. Karachi & online. Free demo.",
   subject="O Level Computer Science (2210) and IGCSE Computer Science (0478)", papers="Paper 1 Computer Systems and Paper 2 Algorithms, Programming and Logic, 1 hour 45 minutes each",
   mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
   faqs=[("Who is the best O Level Computer Science teacher in Karachi?", "Pick the teacher whose method fits how the papers are marked. Sir Riza Walji has 9+ years of teaching, has taught at Beaconhouse and Bay View Academy, and marks every answer to the 2210 mark scheme. The first class is free, so you can judge for yourself."),
         ("Which topics are in O Level Computer Science Paper 1 and Paper 2?", "Paper 1 covers data representation, data transmission, hardware, software, the internet and its uses, and automated and emerging technologies. Paper 2 covers algorithm design and problem-solving, programming, databases and Boolean logic, and ends with a 15-mark scenario question.")]),
 "o-level-urdu": dict(
   title="O Level Urdu Tuition in Karachi & Online (3248) | SJ Academy",
   meta="O Level Urdu (3248) tuition with Miss Asmat Zafar, former Head of Urdu at Education Bay. Summary, writing and translation. Karachi & online. Free demo.",
   subject="O Level Second Language Urdu (3248)", papers="Paper 1 Reading and Writing (1 hour 45 minutes) and Paper 2 Grammar, Writing and Translation (1 hour 30 minutes), 50% each",
   mode="In class at DHA Phase 7, Karachi, or in an online batch", price="8500",
   faqs=[("Who is the best O Level Urdu teacher in Karachi?", "Choose the teacher who knows how the paper is marked. Miss Asmat Zafar is a former Head of Urdu at Education Bay and has worked as a Senior Author with the University of Cambridge. Your child can sit one class free before you decide."),
         ("How long is the O Level Urdu translation?", "Paper 2 ends with a translation of about 150 words from English into Urdu, worth 15 of the paper's 50 marks. It rewards meaning in natural Urdu, not word-for-word translation.")]),
 "a-level-gp": dict(
   title="A Level General Paper Tuition in Karachi & Online | 8021",
   meta="A Level General Paper (8021) tuition with Miss Tayyaba Yaseen. Essay planning, evidence and comprehension, marked to the mark scheme. Free demo class.",
   subject="AS Level English General Paper (8021)", papers="Paper 1 Essay (1 hour 15 minutes) and Paper 2 Comprehension (1 hour 45 minutes), 50% each",
   mode="In class at DHA Phase 7, Karachi, or live online", price="10500",
   faqs=[("Who is the best General Paper teacher in Karachi?", "The one who marks your essays the way Cambridge does. Miss Tayyaba Yaseen marks every General Paper essay and comprehension answer against the 8021 mark scheme, and you can sit one class free before deciding."),
         ("What is the difference between General Paper and A Level English Literature?", "General Paper (8021) is an AS Level skills subject: one essay on a contemporary issue and a comprehension paper. A Level Literature in English (9695) is a separate subject built on set poems, plays and novels. This class prepares students for General Paper.")]),
 "a-level-sociology": dict(
   title="A Level Sociology Tuition in Karachi & Online | 9699",
   meta="A Level Sociology (9699) tuition with Miss Tayyaba Yaseen, AS and A2. Evidence, evaluation and essays marked to the mark scheme. Live online and in Karachi.",
   subject="A Level Sociology (9699), AS and A2", papers="AS: Papers 1 and 2. A2: Papers 3 and 4. All written, no coursework",
   mode="Live online, with an in-class batch at DHA Phase 7, Karachi", price="10500",
   faqs=[("Who is the best A Level Sociology teacher in Karachi?", "The one who teaches evaluation, not just content. Miss Tayyaba Yaseen marks every answer to the 9699 mark scheme and has a background in psychology that shows in how she teaches research methods. The first class is free."),
         ("Is A Level Sociology hard?", "The content is approachable, because it is about families, schools and the media. The difficulty is the writing: backing every point with evidence, evaluating it with the right concepts, and finishing 26-mark and 35-mark essays in time. That is what the class practises.")]),
 "a-level-psychology": dict(
   title="A Level Psychology Tuition in Karachi & Online | 9990",
   meta="A Level Psychology (9990) tuition with Miss Muzna Zaidi, AS and A2. Core studies, research methods and evaluation, marked properly. Free demo class.",
   subject="A Level Psychology (9990), AS and A2", papers="AS: Papers 1 and 2. A2: Papers 3 and 4 on two specialist options. All written, no coursework",
   mode="In class at DHA Phase 7, Karachi, or live online", price="10500",
   faqs=[("Who is the best A Level Psychology teacher in Karachi?", "The one who turns knowing a study into evaluating it. Miss Muzna Zaidi teaches 9990 with a focus on analytical writing, and answers are marked to the mark scheme. You can sit one class free before you decide."),
         ("What are the core studies in A Level Psychology?", "AS Level Psychology (9990) is built around a set of core studies across several approaches, including studies such as Bandura et al. on aggression and Andrade on doodling. Check the syllabus for your exam year for the full list.")]),
 "a-level-urdu": dict(
   title="A Level Urdu Tuition in Karachi & Online (9686) | SJ Academy",
   meta="A Level Urdu (9686) tuition with Miss Asmat Zafar, former Head of Urdu at Education Bay. Reading, writing, essay and set texts. Karachi & online. Free demo.",
   subject="A Level Urdu (9686)", papers="Paper 2 Reading and Writing, Paper 3 Essay and Paper 4 Texts, all in one series",
   mode="In class at DHA Phase 7, Karachi, or online", price="10500",
   faqs=[("Who is the best A Level Urdu teacher in Karachi?", "Look for someone who knows how Cambridge marks Urdu. Miss Asmat Zafar is a former Head of Urdu at Education Bay and has worked as a Senior Author with the University of Cambridge. The first class is free."),
         ("What are the A Level Urdu set texts?", "Cambridge publishes the Paper 4 set texts, and the five Paper 3 essay topics, in the syllabus for each exam year, and the essay topics change every year. Ask us on WhatsApp which texts the May/June 2027 class is studying.")]),
}


def seo(p):
    return SEO[p["wrap"].replace("sj-p-", "")]


def sec_glance(p):
    g = seo(p)
    rows = [("Exam board", "Cambridge International (CAIE)"), ("Subject", g["subject"]), ("Papers", g["papers"]),
            ("Exam series", "May/June 2027"), ("Teacher", p["teacher"]), ("Where", g["mode"]),
            ("Fee", "%s per subject, plus a one-time admission fee of Rs. 3,500" % p["fee"]), ("Free demo", "Yes, the first class is free")]
    trs = "\n".join('          <tr><th scope="row">%s</th><td>%s</td></tr>' % (a, b) for a, b in rows)
    summary = ("SJ Academy teaches %s tuition in Karachi and online. Classes are taught by %s, %s, for the May/June 2027 exams. "
               "Every answer is marked against the Cambridge mark scheme, fees start at %s per subject, and the first class is a free demo."
               % (g["subject"], p["teacher"], g["mode"][0].lower() + g["mode"][1:], p["fee"].replace("From ", "")))
    return """      <div class="sjx-glance">
        <h3 class="sj-h3">{subj} tuition at a glance</h3>
        <p class="sjx-top">{summary}</p>
        <div class="sj-table-wrap sjx-top"><table class="sj-table sjx-gt">
          <caption class="sj-vh">{subj} tuition at SJ Academy: key facts</caption>
          <tbody>
{trs}
          </tbody>
        </table></div>
      </div>
""".format(subj=g["subject"], summary=summary, trs=trs)


# ---------------------------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------------------------
def first_level(p):
    return list(p["levels"].values())[0]


def demo_href(p, lv=None):
    lv = lv or first_level(p)
    return wa(demo_text(lv["lvl"], lv["subj"], lv["ref"]))


def q_href(p):
    ref = list(p["levels"].values())[0]["ref"].split("-")[0] + "-Q"
    return wa(q_text(p["q_words"], ref))


def btn_demo(p, loc, cls="sj-btn sj-btn-primary", label="Book a free demo on WhatsApp", extra=""):
    return ('<a class="%s%s" href="%s" target="_blank" rel="noopener" data-sjx-demo data-loc="%s">%s</a>'
            % (cls, extra, esc(demo_href(p)), loc, label))


def sec_hero(p):
    lvl = first_level(p)
    crumb_parent = ("%s/o-level-tuition-center-karachi/" % SITE, "O Level tuition") if p["level"] == "o" else \
                   ("%s/a-level-tuition-center-karachi/" % SITE, "A Level tuition")
    choices = ""
    if len(p["levels"]) > 1:
        opts = []
        for i, (k, v) in enumerate(p["levels"].items()):
            opts.append('          <label class="sj-choice"><input type="radio" name="sjx-level" value="%s"%s><span>%s</span></label>'
                        % (k, " checked" if i == 0 else "", v["label"]))
        choices = ('        <div class="sj-choices" role="group" aria-label="Level">\n%s\n        </div>\n' % "\n".join(opts))
    proof = "\n".join('        <span><b>%s</b>%s</span>' % (b, s) for b, s in p["proof"])
    return """  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="{site}/">Home</a></li><li><a href="{cp}">{cl}</a></li><li aria-current="page">{crumb}</li></ol></nav>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>{pill}</span></span>{h1}</h1>
        <p class="sj-lead sj-measure">{lead}</p>
        <span class="sj-hand sj-tilt-l">{hand}</span>
        {phone}
      </div>
      <div class="sj-offset sj-stack" id="sjx-card">
{choices}        <h2 class="sj-h3" id="sjx-title">{title}</h2>
        <ul class="sjx-rows">
          <li><span>Teacher</span><span>{teacher}</span></li>
          <li><span>Classes</span><span id="sjx-when">{when}</span></li>
          <li><span>Where</span><span id="sjx-where">{where}</span></li>
          <li><span>Papers</span><span id="sjx-papers">{papers}</span></li>
          <li><span>Batch</span><span>{batch}</span></li>
          <li><span>Fee</span><span>{fee} &middot; <a class="sj-link" href="{site}/fee-structure/">See full fees</a></span></li>
        </ul>
        <div class="sjx-acts">
          {demo}
        </div>
        <p class="sj-small sj-muted">One class free, then decide. Already sure? <a class="sj-link" href="{reg}" data-loc="hero">Register for a class</a></p>
        <p class="sj-small sj-muted">Timings are in Pakistan time. <a class="sj-link" href="{site}/classes-schedule/">See the timetable</a> &middot; Updated <time datetime="2026-11">November 2026</time></p>
      </div>
    </div>
    <div class="sj-wrap sjx-gap">
      <div class="sj-proof">
{proof}
        <a href="{google}" target="_blank" rel="noopener"><b>5.0 on Google</b>SJ Academy, from 226 reviews</a>
      </div>
    </div>
  </section>
""".format(site=SITE, cp=crumb_parent[0], cl=crumb_parent[1], crumb=p["crumb"], pill=esc(p["pill"]).replace("&amp;", "&amp;"),
           h1=p["h1"], lead=p["lead"], hand=p["hand"],
           phone=btn_demo(p, "hero_top", extra=" sjx-phone-cta"), choices=choices, title=lvl["title"], teacher=p["teacher"],
           when=lvl["when"], where=WHERE_STD, papers=lvl["papers"], batch=p["batch"], fee=p["fee"],
           demo=btn_demo(p, "hero"), reg=REGISTER, proof=proof, google=GOOGLE)


def sec_problem(p):
    pr = p["problem"]
    pins = "\n".join('        <div class="sj-pinned"><span class="sj-pin" aria-hidden="true"></span><b>%s</b><p>%s</p></div>' % (t, x)
                     for t, x in pr["pins"])
    return """  <!-- 2. THE PROBLEM -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">The problem</div>
        <h2 class="sj-h2">{h2}</h2>
        <p class="sjx-top">{intro}</p>
      </div>
      <div class="sj-grid sj-grid-4 sjx-pins">
{pins}
      </div>
      <div class="sj-measure sj-stack">
        <p>{outro}</p>
        <span class="sj-hand sj-tilt-r">{hand2}</span>
      </div>
    </div>
  </section>
""".format(h2=pr["h2"], intro=pr["intro"], pins=pins, outro=pr["outro"], hand2=pr["hand2"])


def sec_try_lost(p):
    t = p["tryit"]
    radios = "\n".join('          <label class="sj-choice"><input type="radio" name="sjx-r" value="%d"%s><span>%s</span></label>'
                       % (i + 1, " checked" if i == 0 else "", lab) for i, lab in enumerate(t["labels"]))
    sheets, whys = [], []
    for i, s in enumerate(t["sheets"]):
        r = i + 1
        lines = "\n".join('              <button type="button" class="sjx-line" data-why="%s">%s<span class="sj-mark">%s</span></button>'
                          % (esc(why), txt, mk) for txt, mk, why in s["lines"])
        lost = ('              <button type="button" class="sjx-line" data-lost><span class="sjx-c">%s%s</span></button>' % (s["lost"], RING))
        sheets.append("""          <div class="sj-paper sjx-sheet" data-r="{r}">
            <div class="sj-paper-q"><small>{qs}</small>{q}</div>
            <div class="sj-paper-a">
{lines}
{lost}
            </div>
            <div class="sj-paper-note sjx-note" data-key><span>{note}</span><span class="sj-stamp">{stamp}</span></div>
          </div>""".format(r=r, qs=s["q_small"], q=s["q"], lines=lines, lost=lost, note=s["note"], stamp=s["stamp"]))
        whys.append('          <div class="sjx-why" data-r="%d" data-key><b>The last line</b><p>%s</p></div>' % (r, s["why"]))
    return """  <!-- 3. TRY IT: FIND THE LOST MARK -->
  <section class="sj-section sj-bg-brown">
    <div class="sj-wrap sjx-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">Try it</div>
        <h2 class="sj-h2">Find the line that <span class="sj-hl">lost the mark</span></h2>
        <p class="sj-measure">{intro} This is how every answer is marked in class.</p>
        <div class="sj-choices" id="sjx-rounds" role="group" aria-label="Question" hidden>
{radios}
        </div>
        <span class="sj-hand sj-tilt-l" id="sjx-hint" hidden>tap the line you suspect</span>
      </div>
      <div class="sj-stack">
        <div class="sjx-sheets">
{sheets}
        </div>
        <div class="sjx-panel" aria-live="polite">
          <p id="sjx-status" hidden><b>Pick a line on the answer above</b></p>
          <p id="sjx-miss" hidden></p>
{whys}
          <p class="sj-small sjx-legend">{legend}</p>
        </div>
      </div>
    </div>
  </section>
""".format(intro=t["intro"], radios=radios, sheets="\n".join(sheets), whys="\n".join(whys), legend=t["legend"])


def sec_try_map(p):
    t = p["tryit"]
    blocks = []
    for title, rows in t["maps"]:
        mx = max(m for _, _, m, _ in rows) if rows else 1
        top = max(75, mx)
        items = []
        for a, b, m, tip in rows:
            w = max(8, round(100 * m / top))
            items.append("""          <details class="sjx-ex">
            <summary><span class="sjx-bar" style="width:{w}%"></span><span class="sjx-ex-t"><b>{a}</b> {b}</span><span class="sjx-ex-m">{m} marks</span></summary>
            <p>{tip}</p>
          </details>""".format(w=w, a=a, b=b, m=m, tip=tip))
        blocks.append('        <div class="sjx-map"><h3 class="sj-h4">%s</h3>\n%s\n        </div>' % (title, "\n".join(items)))
    return """  <!-- 3. TRY IT: WHERE THE MARKS ARE -->
  <section class="sj-section sj-bg-brown">
    <div class="sj-wrap sjx-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">Where the marks are</div>
        <h2 class="sj-h2">Every mark, exercise by <span class="sj-hl">exercise</span></h2>
        <p class="sj-measure">{intro}</p>
        <span class="sj-hand sj-tilt-l">tap a row</span>
      </div>
      <div class="sjx-panel sj-stack">
{blocks}
        <p class="sj-small sjx-legend">{legend}</p>
      </div>
    </div>
  </section>
""".format(intro=t["intro"], blocks="\n".join(blocks), legend=t["legend"])


def sec_teacher(p):
    t = p["teacher_section"]
    if t.get("photo"):
        src, w, h = t["photo"]
        img = ('<img src="%s" alt="%s, %s teacher at SJ Academy, Karachi" width="%d" height="%d" loading="lazy" decoding="async">'
               % (src, p["teacher"], p["crumb"].split(" (")[0], w, h))
    else:
        img = '<span class="sjx-av" aria-hidden="true">%s</span>' % t["initials"]
    facts = "".join("<li>%s</li>" % f for f in t["card_facts"])
    tile = t["tile"]
    return """  <!-- 4. TEACHER AND METHOD -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sjx-two sjx-two-t">
      <div class="sj-stack">
        <div class="sj-eyebrow">Your teacher</div>
        <h2 class="sj-h2">{h2}</h2>
        <p class="sj-measure">{para}</p>
        <ul class="sj-ticks">
{ticks}
        </ul>
        <p>{demo}</p>
      </div>
      <div class="sj-stack">
        <div class="sj-card sjx-teacher">
          {img}
          <div><b>{name}</b><span>{sub}</span></div>
          <ul>{facts}</ul>
        </div>
        <a class="sj-tile" href="{site}{turl}"><b>{tt}</b><p>{tp}</p><span class="sj-link sj-link-go">{tl}</span></a>
{photo}      </div>
    </div>
  </section>
""".format(h2=t["h2"], para=t["para"], ticks=ticks(t["ticks"]),
           demo=btn_demo(p, "teacher", cls="sj-link sj-link-go", label="Book a free demo class"),
           photo=("" if t.get("photo") else '        <figure class="sj-polaroid sjx-class"><span class="sj-tape" aria-hidden="true"></span><img src="%s" alt="A class in progress at SJ Academy, DHA Phase 7, Karachi" width="%d" height="%d" loading="lazy" decoding="async"><figcaption class="sj-hand">a real SJ Academy class, not stock</figcaption></figure>\n' % PHOTO), img=img, name=p["teacher"], sub=t["card_sub"], facts=facts, site=SITE, turl=tile[2], tt=tile[0], tp=tile[1], tl=tile[3])


def sec_syllabus(p):
    s = p["syllabus"]
    tabs, panels = [], []
    for i, (tab, small, title, (dur, marks, wt), what, prep) in enumerate(s["papers"]):
        n = i + 1
        sel = "true" if i == 0 else "false"
        tabs.append('          <button role="tab" id="sjx-t%d" aria-controls="sjx-p%d" aria-selected="%s"%s>%s</button>'
                    % (n, n, sel, "" if i == 0 else ' tabindex="-1"', tab))
        of = "of the A Level" if p["level"] == "a" and "AS Level" not in p["batch"] else ("of the AS Level" if "AS Level" in p["batch"] else "of the O Level")
        panels.append("""        <div class="sj-tabpanel sjx-tp" role="tabpanel" id="sjx-p{n}" aria-labelledby="sjx-t{n}"{hid}>
          <div><h3 class="sj-h3"><small>{small}</small>{title}</h3><ul class="sjx-facts"><li><b>{dur}</b>duration</li><li><b>{marks}</b>marks</li><li><b>{wt}</b>{of}</li></ul></div>
          <div class="sj-stack"><p><b>What it asks.</b> {what}</p><p><b>How to prepare.</b> {prep}</p></div>
        </div>""".format(n=n, hid="" if i == 0 else " hidden", small=small, title=title, dur=dur, marks=marks, wt=wt, of=of,
                         what=what, prep=prep))
    ths = ""
    if p.get("thresholds"):
        big, txt = p["thresholds"]
        ths = """      <div class="sj-card sjx-ths">
        <b class="sjx-big">{big}</b>
        <div class="sj-stack"><p>{txt}</p></div>
      </div>
""".format(big=big, txt=txt)
    return """  <!-- 5. SYLLABUS AND PAPERS -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">The syllabus</div>
        <h2 class="sj-h2">{h2}</h2>
        <p class="sjx-top">{intro}</p>
      </div>
{glance}      <div>
        <div class="sj-tabs" role="tablist" aria-label="Paper">
{tabs}
        </div>
{panels}
      </div>
{ths}      <p class="sj-small sj-muted">{note} SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge.</p>
    </div>
  </section>
""".format(h2=s["h2"], intro=s["intro"], tabs="\n".join(tabs), panels="\n".join(panels), ths=ths, note=s["note"], glance=sec_glance(p))


def kwname(p):
    short = p["crumb"].split(" (")[0]
    return ("O Level " if p["level"] == "o" else "A Level ") + short


def sec_year_parents(p):
    fee_line = p["fee"].replace("From ", "From ") + " per subject, with 10% off when you pay 3 months upfront"
    return """  <!-- 6. HOW THE YEAR RUNS + PARENTS -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sjx-two sjx-two-b">
      <div class="sj-stack">
        <div class="sj-eyebrow">How {kw} tuition runs</div>
        <h2 class="sj-h2">Learn it. Practise it. <span class="sj-hl">Get it marked.</span></h2>
        <ol class="sj-steps">
          <li><b>Learn it</b><span>The syllabus is taught topic by topic, with the exam skill for each one built in from the start.</span></li>
          <li><b>Practise it</b><span>Past paper questions with every topic, in the format Cambridge uses.</span></li>
          <li><b>Get it marked</b><span>Answers marked against the mark scheme, so students see which line lost the mark, not just the total.</span></li>
          <li><b>Test it</b><span>Tests through the year, so gaps show up while there is time to fix them.</span></li>
          <li><b>Rehearse it</b><span>Timed past papers in the final months, so the real exam feels like a rerun.</span></li>
          <li><b>In class or online</b><span>Online students join a live class, with the same marking and tests.</span></li>
        </ol>
      </div>
      <div class="sj-card sj-stack sjx-parents">
        <div class="sj-eyebrow">For parents</div>
        <h3 class="sj-h3">No surprises on results day</h3>
        <p>The goal of {kw} tuition is not just to cover the syllabus. It is to change how your child writes an answer, and to let you see that it is changing.</p>
        <ul class="sj-ticks">
{ticks}
        </ul>
        <p class="sj-row">{demo} <a class="sj-link" href="{site}/fee-structure/">See full fees</a></p>
      </div>
    </div>
  </section>
""".format(ticks=ticks([fee_line,
                        "Classes are kept small, and every test your child sits is marked, so nobody hides at the back",
                        p["parents_extra"],
                        "Your child can sit one class free before you pay anything"]),
           demo=btn_demo(p, "parents", cls="sj-link sj-link-go", label="Book a free demo class"), site=SITE, kw=kwname(p))


def sec_reviews(p):
    cards = []
    for txt, av, name, sub in p["reviews"]:
        cards.append('        <div class="sj-card sj-review"><p class="sj-review-text">"%s"</p><div class="sj-review-by"><span class="sj-avatar" aria-hidden="true">%s</span><span><b>%s</b><br>%s</span></div></div>'
                     % (txt, av, name, sub))
    return """  <!-- 7. REVIEWS -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">SJ Academy students</div>
        <h2 class="sj-h2">{h2}</h2>
      </div>
      <div class="sj-grid sj-grid-3">
{cards}
      </div>
      <p>SJ Academy is rated 5.0 on Google from 226 reviews. <a class="sj-link sj-link-go" href="{g}" target="_blank" rel="noopener" data-loc="reviews">Read them on Google</a></p>
    </div>
  </section>
""".format(h2=p["review_h2"], cards="\n".join(cards), g=GOOGLE)


def sec_resources(p):
    tiles = "\n".join('        <a class="sj-tile" href="%s%s"><b>%s</b><p>%s</p><span class="sj-link sj-link-go">%s</span></a>'
                      % (SITE, u, t, d, l) for t, d, u, l in p["resources"])
    return """  <!-- 8. FREE RESOURCES -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">Not ready yet?</div>
        <h2 class="sj-h2">Start with the <span class="sj-hl">free resources</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
{tiles}
      </div>
      <p class="sj-small sj-muted">{more}</p>
    </div>
  </section>
""".format(tiles=tiles, more=p["more_links"])


def sec_faq(p):
    items = []
    for i, (q, a) in enumerate(p["faqs"]):
        items.append('        <details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>'
                     % (" open" if i == 0 else "", q, a))
    short = p["crumb"].split(" (")[0]
    lvl = "O Level" if p["level"] == "o" else "A Level"
    if short == "General Paper":
        lvl = ""
    return """  <!-- 9. FAQ -->
  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about {name} <span class="sj-hl">tuition</span></h2>
      </div>
      <div class="sj-faq">
{items}
      </div>
    </div>
  </section>
""".format(name=(lvl + " " + short).strip(), items="\n".join(items))


def sec_final(p):
    return """  <!-- 10. FINAL -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjx-final">
      <h2 class="sj-h2">{h2}</h2>
      <p class="sj-measure">{pp}</p>
      <p class="sj-small">{kw} tuition at SJ Academy, DHA Phase 7, Karachi, and live online.</p>
      <div class="sj-row">{demo}</div>
      <p>or <a class="sj-link" href="{reg}" data-loc="final_band">register for a class</a></p>
    </div>
  </section>

  <!-- phone bottom bar -->
  <div class="sj-bar">
    {bar}
    <a class="sj-btn sj-btn-wa" href="{q}" target="_blank" rel="noopener" data-loc="bottom_bar">WhatsApp us</a>
  </div>
""".format(h2=p["final_h2"], pp=p["final_p"], demo=btn_demo(p, "final_band"), reg=REGISTER,
           bar=btn_demo(p, "bottom_bar", label="Book a free demo"), q=esc(q_href(p)), kw=kwname(p))


def page_css(w):
    s = "#sj.%s" % w
    rules = """
{s} .sjx-top{{margin-top:var(--sj-s3)}}
{s} .sjx-gap{{margin-top:var(--sj-s6)}}
{s} .sjx-rows{{border-top:1.5px solid var(--sj-ink)}}
{s} .sjx-rows li{{display:grid;grid-template-columns:84px minmax(0,1fr);gap:10px;padding:11px 0;border-bottom:1px solid var(--sj-line);color:var(--sj-ink)}}
{s} .sjx-rows li>span:first-child,{s} .sjx-tp h3 small{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--sj-muted);display:block;padding:3px 0}}
{s} .sjx-acts{{display:grid;gap:var(--sj-s3)}}
{s} .sjx-two{{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}}
{s} .sjx-pins .sj-pinned{{text-align:left;padding:24px 18px 18px}}
{s} .sjx-pins .sj-pinned p{{margin-top:6px;font-size:15px;line-height:1.5}}
{s} .sjx-sheets{{display:grid;justify-items:center}}
{s} .sjx-sheet{{width:100%}}
{s} .sjx-sheet .sj-paper-a{{background:none;padding-top:6px;padding-bottom:6px}}
{s} .sjx-line{{position:relative;display:block;width:100%;min-height:46px;padding:8px 10px;margin-left:-10px;border-bottom:1px solid #D8E2EE;border-radius:4px;color:var(--sj-exam-ink);line-height:1.5;text-align:left}}
{s} .sjx-line .sj-mark{{float:right;margin-left:8px}}
{s} .sjx-line.is-miss{{color:#8A93A6}}
{s} .sjx-c{{position:relative;display:inline-block}}
{s} .sjx-ring{{position:absolute;left:-12%;top:-10px;width:124%;height:calc(100% + 20px);pointer-events:none;display:none}}
{s} .sjx-line.is-found .sjx-ring{{display:block}}
{s} .sjx-note{{display:flex;align-items:center;justify-content:space-between;gap:var(--sj-s3)}}
{s} .sjx-panel{{background:#fff;color:var(--sj-text);border-radius:var(--sj-r-lg);padding:var(--sj-s5) var(--sj-s4)}}
{s} .sjx-panel b{{font-weight:500;color:var(--sj-ink)}}
{s} .sjx-why+.sjx-why{{margin-top:var(--sj-s4)}}
{s} .sjx-why p{{margin-top:4px}}
{s} .sjx-legend{{margin-top:var(--sj-s4);padding-top:var(--sj-s3);border-top:1px solid var(--sj-line);color:var(--sj-muted)}}
{s} .sjx-map+.sjx-map{{margin-top:var(--sj-s5)}}
{s} .sjx-map h3{{margin-bottom:var(--sj-s3);color:var(--sj-ink)}}
{s} .sjx-ex{{border-bottom:1px solid var(--sj-line)}}
{s} .sjx-ex summary{{position:relative;display:flex;align-items:center;gap:10px;min-height:48px;padding:10px 4px;cursor:pointer;list-style:none}}
{s} .sjx-ex summary::-webkit-details-marker{{display:none}}
{s} .sjx-bar{{position:absolute;left:0;bottom:4px;height:5px;background:var(--sj-yellow);border-radius:3px;z-index:0}}
{s} .sjx-ex-t,{s} .sjx-ex-m{{position:relative;z-index:1}}
{s} .sjx-ex-t{{flex:1;color:var(--sj-ink)}}
{s} .sjx-ex-m{{font-size:14px;color:var(--sj-muted);white-space:nowrap}}
{s} .sjx-ex[open] .sjx-bar{{background:var(--sj-orange)}}
{s} .sjx-ex p{{padding:4px 6px 14px;font-size:15px;line-height:1.5}}
{s} .sjx-facts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 10px;border-top:1.5px solid var(--sj-ink);border-bottom:1px solid var(--sj-line);margin:var(--sj-s3) 0 var(--sj-s4)}}
{s} .sjx-facts li{{padding:10px 0;font-size:14px;color:var(--sj-muted);line-height:1.35}}
{s} .sjx-facts b{{display:block;font-size:20px;font-weight:400;color:var(--sj-ink)}}
{s} .sjx-teacher{{display:grid;gap:var(--sj-s3)}}
{s} .sjx-teacher img{{width:100%;height:auto;max-height:260px;object-fit:cover;object-position:50% 25%;border-radius:var(--sj-r-md)}}
{s} .sjx-teacher b{{display:block;color:var(--sj-ink);font-weight:500}}
{s} .sjx-teacher span{{color:var(--sj-muted);font-size:15px}}
{s} .sjx-teacher ul{{display:grid;gap:6px;padding-top:var(--sj-s3);border-top:1px solid var(--sj-line)}}
{s} .sjx-teacher li{{font-size:15px;color:var(--sj-text)}}
{s} .sjx-av{{display:grid;place-items:center;width:84px;height:84px;border-radius:50%;background:var(--sj-yellow);color:var(--sj-ink)!important;font-size:28px!important;font-weight:600}}
{s} .sjx-ths{{display:grid;gap:var(--sj-s3) var(--sj-s6);align-items:center;background:var(--sj-yellow-light);border-color:var(--sj-yellow)}}
{s} .sjx-big{{font-size:clamp(56px,calc(40px + 4vw),96px);font-weight:600;line-height:1;letter-spacing:-.04em;color:var(--sj-ink)}}
{s} .sjx-parents{{background:var(--sj-yellow-light);border-color:transparent;align-self:start}}
{s} .sj-table td b{{font-weight:500}}
{s} .sjx-glance{{max-width:860px}}
{s} .sjx-gt th{{width:32%;background:var(--sj-canvas);text-transform:none;letter-spacing:0;font-size:15px;color:var(--sj-ink);white-space:normal;vertical-align:top;border-bottom:1px solid var(--sj-line)}}
{s} .sjx-gt td{{border-top:0;border-bottom:1px solid var(--sj-line)}}
{s} .sjx-gt tr:last-child th,{s} .sjx-gt tr:last-child td{{border-bottom:0}}
{s} .sjx-class{{max-width:380px;margin:var(--sj-s5) auto 8px}}
{s} .sjx-class img{{aspect-ratio:auto}}
{s} .sjx-final{{text-align:center;display:grid;justify-items:center}}
{s} .sjx-final .sj-row{{justify-content:center}}
{s} .sjx-phone-cta{{display:none}}
@media (max-width:899px){{.joinchat,#back-to-top{{display:none!important}}{s} .sjx-phone-cta{{display:flex;width:fit-content}}}}
@media (min-width:600px){{{s} .sjx-panel{{padding:var(--sj-s5)}}{s} .sjx-ths{{grid-template-columns:auto minmax(0,1fr);padding:var(--sj-s6)}}}}
@media (min-width:900px){{{s} .sjx-two{{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--sj-s7);align-items:start}}{s} .sjx-two-t{{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr)}}{s} .sjx-two-b{{grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr)}}{s} .sjx-tp:not([hidden]){{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 var(--sj-s7);align-items:start}}}}
""".format(s=s)
    return "<style>\n/* Page-only layout. Every rule is scoped to this page. */" + rules + "</style>\n"


PAGE_JS = r"""<script>
/* Page script: level switch, find-the-lost-mark answers, live class timings from the timetable sheet. */
(function(){
  var root=document.getElementById('sj'); if(!root||!root.classList.contains('__WRAP__')) return;
  var $=function(id){return document.getElementById(id)};
  var each=function(list,fn){Array.prototype.forEach.call(list,fn)};
  var SHEET='__SHEET__',WA='https://wa.me/__WANUM__?text=';
  var CFG=__CFG__;
  var level=CFG.first;

  /* hero card */
  function card(){
    var l=CFG.levels[level];
    $('sjx-title').textContent=l.title;$('sjx-papers').textContent=l.papers;
    $('sjx-when').innerHTML=l.when;$('sjx-where').textContent=l.where||CFG.where;
    var href=WA+encodeURIComponent("Hi SJ Academy, I'd like to book a free demo class.\nLevel: "+l.lvl+"\nSubject: "+l.subj+"\nSession: May/June 2027\nMode (in class or online): \n(Ref: "+l.ref+")\nMy name is ");
    each(root.querySelectorAll('[data-sjx-demo]'),function(a){a.setAttribute('href',href)});
  }
  each(root.querySelectorAll('input[name="sjx-level"]'),function(i){
    i.addEventListener('change',function(){if(i.checked){level=i.value;card()}});
    if(i.checked){level=i.value}
  });
  card();

  /* find the lost mark */
  var rounds=$('sjx-rounds');
  if(rounds){
    var round='1',status=$('sjx-status'),miss=$('sjx-miss');
    var show=function(r){
      round=r;
      each(root.querySelectorAll('.sjx-sheet,.sjx-why'),function(d){d.hidden=d.getAttribute('data-r')!==r});
      var sheet=root.querySelector('.sjx-sheet[data-r="'+r+'"]'),done=!!sheet.querySelector('.is-found');
      each(sheet.querySelectorAll('[data-key]'),function(k){k.hidden=!done});
      root.querySelector('.sjx-why[data-r="'+r+'"]').hidden=!done;
      status.hidden=done;miss.hidden=true;
    };
    each(root.querySelectorAll('.sjx-line'),function(b){
      b.addEventListener('click',function(){
        var sheet=b.closest('.sjx-sheet');
        if(b.hasAttribute('data-lost')){
          b.classList.add('is-found');
          each(sheet.querySelectorAll('.sjx-line'),function(x){x.classList.remove('is-miss')});
          show(round);
        }else if(!sheet.querySelector('.is-found')){
          b.classList.add('is-miss');
          miss.innerHTML='<b>Not this one.</b> This line is safe. '+b.getAttribute('data-why')+' Try another line.';
          miss.hidden=false;status.hidden=true;
        }
      });
    });
    rounds.hidden=false;$('sjx-hint').hidden=false;
    each(root.querySelectorAll('input[name="sjx-r"]'),function(i){
      i.addEventListener('change',function(){if(i.checked){show(i.value)}});
    });
    show('1');
  }

  /* class timings from the timetable sheet (shares its cache with the homepage and timetable page) */
  function parseTsv(text){
    var rows=[],row=[],f='',q=false;
    for(var i=0;i<text.length;i++){var c=text[i],n=text[i+1];
      if(c==='"'&&q&&n==='"'){f+='"';i++;continue}
      if(c==='"'){q=!q;continue}
      if(c==='\t'&&!q){row.push(f);f='';continue}
      if((c==='\n'||c==='\r')&&!q){if(c==='\r'&&n==='\n')i++;row.push(f);rows.push(row);row=[];f='';continue}
      f+=c}
    row.push(f);rows.push(row);
    rows=rows.filter(function(r){return r.some(function(v){return String(v||'').trim()!==''})});
    if(rows.length<2) return null;
    var days=rows[0].slice(1).map(function(d){return String(d||'').trim()});
    return {days:days,rows:rows.slice(1).map(function(r){return {time:String(r[0]||'').trim(),cells:r.slice(1,days.length+1)}}).filter(function(r){return r.time})};
  }
  function when(d,kw){
    var re=new RegExp(kw,'i'),G={},O=[];
    d.rows.forEach(function(r){r.cells.forEach(function(cell,di){
      var toks=String(cell||'').split(/[+()\[\]]/);
      toks.forEach(function(tok,ti){
        if(!re.test(tok)) return;
        var on=/online/i.test(tok)||String(toks[ti+1]||'').trim().toLowerCase()==='online';
        var t=r.time.replace(/\s*-\s*/g,' - ').replace(/(\d)\s*(AM|PM)/gi,'$1 $2').replace(/\s+/g,' ').trim(),k=(on?'on|':'ic|')+t;
        if(!G[k]){G[k]={days:[],first:di,on:on,t:t};O.push(k)}
        var day=String(d.days[di]||'').slice(0,3),g=G[k];
        if(day&&g.days.indexOf(day)<0){g.days.push(day);if(di<g.first)g.first=di}
      })})});
    if(!O.length) return null;
    O.sort(function(a,b){return G[a].first-G[b].first});
    var mixed=O.some(function(k){return !G[k].on}),all=!mixed;
    return {all:all,txt:O.map(function(k){var g=G[k],ds=g.days;
      return (ds.length>1?ds.slice(0,-1).join(', ')+' &amp; '+ds[ds.length-1]:ds[0])+' &middot; '+g.t+(g.on&&mixed?' (online)':'')}).join('; ')};
  }
  function load(key){
    var l=CFG.levels[key];if(!l.gid) return;
    var done=function(d){if(!d)return;var w=when(d,l.kw);if(w){l.when=w.txt;l.where=w.all?'Live online, from anywhere':CFG.where;if(key===level)card()}};
    try{var s=sessionStorage.getItem('sjh-tt-'+l.gid);if(s){var v=JSON.parse(s);if(v&&v._t&&Date.now()-v._t<600000){done(v);return}}}catch(e){}
    if(!window.fetch) return;
    fetch(SHEET+l.gid).then(function(r){if(!r.ok)throw 0;return r.text()}).then(function(t){
      var d=parseTsv(t);try{if(d){d._t=Date.now();sessionStorage.setItem('sjh-tt-'+l.gid,JSON.stringify(d))}}catch(e){}done(d);
    }).catch(function(){});
  }
  setTimeout(function(){Object.keys(CFG.levels).forEach(load)},1200);
})();
</script>
"""

STD_JS = r"""<script>
/* Standard page script, copied unchanged from 02 Website/Scripts/sj-page-script.js */
(function(){
  var root=document.getElementById('sj');
  if(!root){return;}
  var each=function(list,fn){Array.prototype.forEach.call(list,fn);};

  /* Tabs: role="tablist" > role="tab" aria-controls="panel-id" */
  each(root.querySelectorAll('[role="tablist"]'),function(list){
    var tabs=Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    var pick=function(tab,focus){
      tabs.forEach(function(t){
        var on=t===tab;
        t.setAttribute('aria-selected',on?'true':'false');
        t.tabIndex=on?0:-1;
        var panel=document.getElementById(t.getAttribute('aria-controls'));
        if(panel){panel.hidden=!on;}
      });
      if(focus){tab.focus();}
    };
    tabs.forEach(function(tab,i){
      tab.addEventListener('click',function(){pick(tab,false);});
      tab.addEventListener('keydown',function(e){
        var step=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
        if(!step){return;}
        e.preventDefault();
        pick(tabs[(i+step+tabs.length)%tabs.length],true);
      });
    });
  });

  /* Phone bottom bar: shows once the element marked data-sj-hero has scrolled away */
  var bar=root.querySelector('.sj-bar');
  var hero=root.querySelector('[data-sj-hero]');
  if(bar&&hero&&'IntersectionObserver' in window){
    root.classList.add('sj-has-bar');
    new IntersectionObserver(function(entries){
      bar.classList.toggle('is-on',!entries[0].isIntersecting);
    }).observe(hero);
  }

  /* Video: loads the player only after a tap */
  each(root.querySelectorAll('.sj-video[data-src]'),function(v){
    v.addEventListener('click',function(e){
      e.preventDefault();
      var f=document.createElement('iframe');
      f.src=v.getAttribute('data-src');
      f.title=v.getAttribute('data-title')||'Video';
      f.allow='autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen=true;
      f.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:0';
      v.innerHTML='';
      v.appendChild(f);
    });
  });

  /* Measurement: one event name per action, location read from data-loc */
  var send=function(name,loc){
    var g=window['gt'+'ag'];
    if(typeof g==='function'){g('event',name,{link_location:loc||'unknown',page_family:root.getAttribute('data-family')||''});}
  };
  root.addEventListener('click',function(e){
    var a=e.target.closest?e.target.closest('a,button'):null;
    if(!a){return;}
    var href=a.getAttribute('href')||'';
    var loc=a.getAttribute('data-loc');
    if(href.indexOf('wa.me')>-1){send('whatsapp_click',loc);}
    else if(href.indexOf('popup%3Aopen')>-1){send('register_open',loc);}
    else if(a.hasAttribute('download')){send('resource_download',loc);}
    else if(a.hasAttribute('data-event')){send(a.getAttribute('data-event'),loc);}
  });
})();
</script>
"""


def schema(p):
    url = SITE + p["url"]
    prov = {"@type": "EducationalOrganization", "name": "SJ Academy", "url": SITE + "/", "telephone": "+92-336-2144454",
            "address": {"@type": "PostalAddress", "streetAddress": ADDRESS, "addressLocality": "Karachi", "addressCountry": "PK"}}
    inst = {"@type": "Person", "name": p["teacher"].replace("Sir ", "").replace("Miss ", ""),
            "worksFor": {"@type": "EducationalOrganization", "name": "SJ Academy", "url": SITE + "/"}}
    g = seo(p)
    inst.update({"jobTitle": "%s teacher" % p["crumb"].split(" (")[0], "knowsAbout": [g["subject"]]})
    course = {"@context": "https://schema.org", "@type": "Course", "name": p["course_name"], "description": p["course_desc"],
              "url": url, "inLanguage": "en", "educationalLevel": p["edu_level"], "provider": prov,
              "image": [PHOTO[0]], "dateModified": "2026-11-09",
              "offers": {"@type": "Offer", "category": "Paid", "price": g["price"], "priceCurrency": "PKR",
                         "description": "Per subject, per month. One-time admission fee Rs. 3,500. First class free."},
              "hasCourseInstance": [
                  {"@type": "CourseInstance", "courseMode": "Onsite",
                   "location": {"@type": "Place", "name": "SJ Academy, DHA Phase 7, Karachi", "address": prov["address"]},
                   "instructor": inst},
                  {"@type": "CourseInstance", "courseMode": "Online", "instructor": inst}]}
    parent = ("O Level tuition", SITE + "/o-level-tuition-center-karachi/") if p["level"] == "o" else \
             ("A Level tuition", SITE + "/a-level-tuition-center-karachi/")
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": parent[0], "item": parent[1]},
        {"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for q, a in p["faqs"]]}
    out = ""
    for obj in (course, crumbs, faq):
        out += '<script type="application/ld+json">%s</script>\n' % json.dumps(obj, ensure_ascii=True)
    return out


def header(p):
    return """<!-- SJ Academy {crumb} tuition page, Elementor HTML widget. Version 1.0, November 2026.
     Written to the landing page copy guidelines v1.2. Built on the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS). Family: Enrol.
     NEW PAGE at {url} (Elementor Full Width, Hide Title: Yes). Paste this whole file into one HTML widget. Section: full width, zero padding, no entrance animation.
     Keywords (best-available, confirm in Semrush): {kw}.
     Yoast SEO title: {yt}
     Yoast meta description: {ym}
     Set the social title to match the SEO title.
     WhatsApp refs: {refs}. Add them to the site register.
     Built by build-subject-pages.py; edit the data there and rebuild rather than editing this file by hand.
     This file is plain ASCII on purpose: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>
""".format(crumb=p["crumb"], url=p["url"], kw=p["keywords"], yt=p["yoast_title"], ym=p["yoast_meta"], refs=p["refs"])


def build(p):
    g = seo(p)
    p = dict(p, yoast_title=g["title"], yoast_meta=g["meta"], faqs=p["faqs"][:-1] + g["faqs"] + p["faqs"][-1:])
    assert len(g["title"]) <= 60, g["title"]
    assert 120 <= len(g["meta"]) <= 156, (len(g["meta"]), g["meta"])
    tryit = sec_try_lost(p) if p["tryit"]["type"] == "lost" else sec_try_map(p)
    body = "".join([sec_hero(p), "\n", sec_problem(p), "\n", tryit, "\n", sec_teacher(p), "\n", sec_syllabus(p), "\n",
                    sec_year_parents(p), "\n", sec_reviews(p), "\n", sec_resources(p), "\n", sec_faq(p), "\n", sec_final(p)])
    cfg = {"first": list(p["levels"].keys())[0], "where": WHERE_STD, "levels": {}}
    for k, v in p["levels"].items():
        cfg["levels"][k] = {kk: v[kk] for kk in ("title", "papers", "when", "lvl", "subj", "ref", "gid", "kw")}
    js = (PAGE_JS.replace("__WRAP__", p["wrap"]).replace("__SHEET__", SHEET).replace("__WANUM__", WA_NUM)
          .replace("__CFG__", json.dumps(cfg, ensure_ascii=True)))
    doc = (header(p) + '\n<div id="sj" class="%s" data-family="%s">\n\n' % (p["wrap"], p["fam"]) + body + "</div>\n\n"
           + page_css(p["wrap"]) + "\n" + js + "\n" + STD_JS + "\n" + schema(p))
    doc = re.sub(r"<!--.*?-->\n?", "", doc, flags=re.S)  # no HTML comments in page code (rule of 3 Nov 2026)
    return ent(doc)


if __name__ == "__main__":
    for p in PAGES:
        out = build(p)
        with open(p["file"], "w", encoding="ascii") as f:
            f.write(out)
        print("%-58s %6.1f KB" % (p["file"], len(out) / 1024))
