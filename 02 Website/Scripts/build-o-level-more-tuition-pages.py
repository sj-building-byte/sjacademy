#!/usr/bin/env python3
"""Build five more O Level subject tuition pages as Elementor HTML widgets.

Pages: O Level Economics (2281), Accounting (7707), Chemistry (5070), Islamiyat (2058), Pakistan Studies (2059).

This script reuses the page engine in build-subject-pages.py (same folder), so the pages share the
design, the page script and the schema. Only the page data lives here.

Run:  python3 build-o-level-more-tuition-pages.py [output folder]
Default output folder: ../Pages/O Level tuition
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("bsp", os.path.join(HERE, "build-subject-pages.py"))
bsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsp)

SITE, ADDRESS, GOOGLE, REV_GENERAL = bsp.SITE, bsp.ADDRESS, bsp.GOOGLE, bsp.REV_GENERAL
GID_O = bsp.GID_O
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "Pages", "O Level tuition")

PAGES = []
SEO = {}

FEE_FAQ = lambda subj: ("What is the fee for %s tuition?" % subj,
                        "From Rs. 8,500 a month per subject, plus a one-time admission fee of Rs. 3,500. You get 10%% off when you pay 3 months upfront. Full figures and a fee calculator are on the <a class=\"sj-link\" href=\"%s/fee-structure/\">fee structure page</a>." % SITE)
WHEN_FAQ = lambda subj: ("When are the %s classes?" % subj,
                         "The current days and times, in Pakistan time, are in the class card at the top of this page and on the <a class=\"sj-link\" href=\"%s/classes-schedule/\">timetable page</a>." % SITE)
NEAR_FAQ = lambda subj: ("Is there an %s tutor near me in Karachi?" % subj,
                         "Yes. SJ Academy is at %s, Karachi, close to Clifton and the rest of DHA. If you live further away, or outside Karachi, you can join live online. <a class=\"sj-link\" href=\"%s\" target=\"_blank\" rel=\"noopener\">Get directions</a>." % (ADDRESS, GOOGLE))
ONLINE_FAQ = lambda subj: ("Do you offer online %s classes?" % subj,
                           "Yes. Online students join the same live class as students in Karachi, with the same teacher, tests and marking.")
JOIN_FAQ = ("Can I still join the May/June 2027 batch?",
            "Yes. The batch is in session and admissions are open. Message us on WhatsApp and we will tell you where the class is and how to catch up.")
DEMO_FAQ = ("Can we take a free demo class before registering?", "Yes. The first class is free, in class or online. Book it on WhatsApp.")
PRIV_FAQ = lambda subj: ("Can private candidates join the %s class?" % subj,
                         "Yes. Private candidates join the same batch as school students. Not sure how to register with Cambridge? See our guide to <a class=\"sj-link\" href=\"%s/caie-private-candidate-registration/\">CAIE private candidate registration</a>." % SITE)

PARTS = "&middot;"

# ============================ O LEVEL ECONOMICS 2281 ============================
PAGES.append(dict(
    file="o-level-economics-tuition-elementor-widget.html",
    url="/o-level-economics-tuition/",
    wrap="sj-p-o-level-economics", fam="enrol", level="o",
    crumb="Economics (2281)",
    keywords="o level economics tuition (primary); o level economics tuition karachi; o level economics 2281; online o level economics classes; "
             "o level economics teacher karachi; o level economics classes; supporting: o level economics syllabus, o level economics notes, economics o level past papers",
    yoast_title="", yoast_meta="",
    refs="OLECO-OL (demo), OLECO-Q (question)",
    pill="O Level Economics tuition in Karachi & online",
    h1='You know the topic. The answer needs <span class="sj-hl">the because.</span>',
    lead="O Level Economics (2281) with Sir Aaliyan, who has 7+ years of coaching O and A Level students. For the May/June 2027 "
         "exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="explain means add the because",
    levels={"ol": dict(label="O Level", title="O Level Economics (2281)", gid=GID_O, kw=r"\becon",
                       papers="Paper 1 Multiple Choice (1 hour) and Paper 2 Structured Questions (2 hours)",
                       when="Tue, Thu &amp; Fri &middot; 6:00 - 7:00 PM",
                       lvl="O Level", subj="Economics (2281)", ref="OLECO-OL")},
    teacher_short="Sir Aaliyan",
    teacher="Sir Aaliyan",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Economics",
    proof=[("7+ years", "Sir Aaliyan's coaching of O and A Level students"), ("Free demo", "one class before you pay")],
    problem=dict(
        h2='Knew the chapter. <span class="sj-hl">Missed the chain.</span>',
        intro="O Level Economics rewards the full line of reasoning, not just the right topic. Paper 2 is 70% of the grade, and "
              "these are the four places the marks usually go.",
        pins=[("The definition was close", "Definitions are marked on key words. Demand is not what people want. It is what they are "
               "willing and able to buy at a given price, and one missing word can cost the mark."),
              ("The curve moved the wrong way", "A change in price moves you along a curve. A change in anything else shifts the "
               "whole curve. Mixing the two up turns a good explanation into a wrong one."),
              ("The chain stopped halfway", "Explain means add the because. A statement such as costs rise earns the first mark, and "
               "the answer needs what happens next to earn the rest."),
              ("Section B ran out of time", "Paper 2 has one compulsory 20-mark question and three more chosen from four, all in "
               "2 hours. A first answer that runs long leaves too little for the last.")],
        outro="None of this means Economics is too hard. It means the examiner never saw the full chain. That part is fixable.",
        hand2="so what happens next?"),
    tryit=dict(type="lost", intro="Three short answers in the style of O Level Economics 2281. Each one loses a mark on one "
                                   "line. Tap the line you think did it.",
               labels=["Demand", "Definition", "Subsidy"],
               sheets=[
                   dict(q_small="Paper 2 style &middot; demand", q="Explain what happens to the demand for a normal good when consumers' incomes rise. [3]",
                        lines=[("Demand for a normal good increases when incomes rise.", "K", "Correct: for a normal good, more income means more demand."),
                               ("More is demanded at every price, so the demand curve shifts to the right.", "K", "Correct: this describes a shift of the whole curve.")],
                        lost="So the quantity demanded rises, which is a movement along the demand curve.",
                        note="income shifts the curve. price moves along it", stamp="2/3",
                        why="A movement along the demand curve happens only when the good's own price changes. A rise in income changes "
                            "demand at every price, so the whole curve shifts. The first two lines already said so, and the last line "
                            "contradicted them."),
                   dict(q_small="Paper 2 style &middot; definitions", q="Define opportunity cost. [2]",
                        lines=[("Opportunity cost is what you give up when you make a choice.", "K", "This earns a mark: it names the idea of giving something up.")],
                        lost="It is the money that you spend on the choice.",
                        note="money spent is not the next best choice", stamp="1/2",
                        why="Opportunity cost is not the amount spent. Full marks need the next best alternative that is given up when "
                            "a choice is made. The first line had the idea, and the second line replaced it with money spent."),
                   dict(q_small="Paper 2 style &middot; supply", q="Explain one effect of a government subsidy on a firm's costs and output. [3]",
                        lines=[("A subsidy is a payment from the government to a producer.", "K", "Correct: this defines the subsidy."),
                               ("It lowers the firm's costs of production.", "K", "Correct: the subsidy covers part of the cost.")],
                        lost="So the firm will produce less.",
                        note="lower costs mean more output, not less", stamp="2/3",
                        why="Lower costs make production more profitable, so supply increases and output rises. The chain was right "
                            "until the last line, where the direction flipped.")],
               legend="K = a mark-earning point. Sample questions written by SJ Academy in the style of O Level Economics 2281; "
                      "marks are illustrative."),
    teacher_section=dict(
        h2='Your O Level Economics teacher: <span class="sj-hl">Sir Aaliyan</span>',
        para="Sir Aaliyan teaches O Level Economics (2281) and O Level Business Studies at SJ Academy, in class at DHA Phase 7 and "
             "live online. He has 7+ years of experience coaching O and A Level students, so the Business and Economics ideas "
             "that overlap are taught side by side.",
        ticks=["Definitions learned word for word, because the mark scheme looks for the key words",
               "Demand and supply diagrams drawn, labelled and explained, with shifts and movements kept apart",
               "Every explain answer practised as a chain: point, because, so what",
               "Section B timed from the first week, so choosing three of four questions becomes a habit"],
        photo=dict(src="https://www.sjacademy.pk/wp-content/uploads/2026/06/Alyaan-768x960.jpeg", w=768, h=960, alt="Sir Aaliyan, O Level Business and Economics teacher at SJ Academy, Karachi", avatar=(112, "width:183.9%;left:-41.9%;top:-56.2%")),
        initials="SA", card_sub="O Level Economics (2281) and O Level Business Studies, in class and online",
        card_facts=["7+ years coaching O and A Level students", "Teaches Business and Economics", "Teaches in class and online"],
        tile=("Carrying on to A Level?", "A Level Economics (9708) is taught at SJ Academy too, so O Level students can carry on in the same place.",
              "/a-level-economics-tuition/", "See A Level Economics")),
    syllabus=dict(
        h2='The O Level Economics syllabus (2281), <span class="sj-hl">paper by paper</span>',
        intro="O Level Economics has two compulsory papers: a multiple-choice paper worth 30% and a structured paper worth 70%. "
              "Calculators are allowed in both papers. The syllabus has six sections, from the basic economic problem to "
              "international trade and globalisation.",
        papers=[("Paper 1", "Paper 1", "Multiple Choice", ("1h", "40", "30%"),
                 "Forty compulsory multiple-choice questions across all six syllabus sections.",
                 "Learn the definitions exactly, practise reading graphs quickly, and use topical past paper questions to find the "
                 "sections that need work."),
                ("Paper 2", "Paper 2", "Structured Questions", ("2h", "80", "70%"),
                 "Section A is one compulsory 20-mark question with parts (a) to (f). Section B is three questions chosen from four, "
                 "each worth 20 marks with parts (a) to (d).",
                 "Practise each answer as a chain of reasoning, draw diagrams that are labelled, and time the paper so the last "
                 "question gets its full 20 minutes.")],
        note="Based on the Cambridge O Level Economics 2281 syllabus for exams in 2027, 2028 and 2029."),
    parents_extra="If your child starts falling behind, Sir Aaliyan will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Economics past papers", "2281 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/economics-2281/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Business Studies as well? See every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>, or the <a class="sj-link" href="%s/o-level-business-tuition/">O Level Business tuition page</a>.' % (SITE, SITE),
    faqs=[FEE_FAQ("O Level Economics"), WHEN_FAQ("O Level Economics"),
          ("Who teaches O Level Economics at SJ Academy?", "Sir Aaliyan teaches O Level Economics (2281) and O Level Business Studies. He has 7+ years of experience coaching O and A Level students."),
          NEAR_FAQ("O Level Economics"), ONLINE_FAQ("O Level Economics"),
          ("Can I use a calculator in O Level Economics?", "Yes. Calculators are allowed in both 2281 papers, so practise the calculations you are likely to meet, such as percentage change and elasticity, with the calculator you will use in the exam."),
          ("How do I get an A* in O Level Economics?", "Learn the definitions word for word, keep shifts and movements apart on a diagram, finish every explain answer with what happens next, and time Paper 2 so the last question gets its full share. In class you practise past paper questions marked to the 2281 mark scheme."),
          JOIN_FAQ, DEMO_FAQ, PRIV_FAQ("O Level Economics")],
    final_h2="One free class. Then decide.",
    final_p="Sit one Economics class with Sir Aaliyan before you pay for any. Worst case, you leave knowing why a rise in income shifts the curve and a rise in price does not.",
    course_name="O Level Economics (2281) tuition in Karachi and online",
    course_desc="O Level Economics tuition for the Cambridge 2281 syllabus, taught by Sir Aaliyan: Paper 1 Multiple Choice and Paper 2 Structured Questions. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))
SEO["o-level-economics"] = dict(
    title="O Level Economics Tuition in Karachi & Online | 2281",
    meta="O Level Economics (2281) tuition in Karachi & online with Sir Aaliyan, 7+ years coaching. Definitions, diagrams and Paper 2 practice. Free demo class.",
    subject="O Level Economics (2281)", papers="Paper 1 Multiple Choice (1 hour) and Paper 2 Structured Questions (2 hours)",
    mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
    faqs=[("Who is the best O Level Economics teacher in Karachi?", "The best teacher is the one whose method fixes your mistakes. Sir Aaliyan marks every definition, diagram and explain answer against the 2281 mark scheme, and the first class is free, so you can judge for yourself."),
          ("Is O Level Economics 2281 the same as IGCSE Economics?", "No. They are separate Cambridge syllabuses with their own papers. This class prepares students for O Level Economics 2281. Tell us which syllabus you are entered for when you book the demo.")])

# ============================ O LEVEL ACCOUNTING 7707 ============================
PAGES.append(dict(
    file="o-level-accounting-tuition-elementor-widget.html",
    url="/o-level-accounting-tuition/",
    wrap="sj-p-o-level-accounting", fam="enrol", level="o",
    crumb="Accounting (7707)",
    keywords="o level accounting tuition (primary); o level accounts tuition karachi; o level accounting 7707; online o level accounting classes; "
             "o level accounting teacher karachi; supporting: o level accounting syllabus, o level accounting notes, accounts o level past papers, accounting o level threshold",
    yoast_title="", yoast_meta="",
    refs="OLACC-OL (demo), OLACC-Q (question)",
    pill="O Level Accounting tuition in Karachi & online",
    h1='Right figures. Wrong side of <span class="sj-hl">the ledger.</span>',
    lead="O Level Accounting (7707), also called Accounts, with Sir Shaibaz Ali and Sir Saifullah. For the May/June 2027 "
         "exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="debit the receiver, credit the giver",
    levels={"ol": dict(label="O Level", title="O Level Accounting (7707)", gid=GID_O, kw=r"\baccount",
                       papers="Paper 1 Multiple Choice (1 hour 30 minutes) and Paper 2 Structured Written Paper (1 hour 45 minutes)",
                       when="Tue &amp; Thu &middot; 4:00 - 5:00 PM",
                       lvl="O Level", subj="Accounting (7707)", ref="OLACC-OL")},
    teacher_short="Sir Shaibaz",
    teacher="Sir Shaibaz Ali and Sir Saifullah",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Accounting",
    proof=[("Since 2011", "Sir Shaibaz Ali has been teaching, CAT (ACCA)"), ("CAIE-certified", "Accounting teacher, Sir Saifullah")],
    problem=dict(
        h2='Balanced in your head. <span class="sj-hl">Not on the page.</span>',
        intro="O Level Accounting is marked on method, layout and the right side of the ledger. Paper 2 is 70% of the grade, and "
              "these are the four places the marks usually go.",
        pins=[("Debit and credit swapped", "Money paid out of the bank is a credit in the business's own books. The bank statement "
               "shows the opposite, which is where the confusion starts."),
              ("Depreciation was treated as saving", "Depreciation is a charge that spreads the cost of an asset over its useful life. "
               "It does not put cash aside to buy a new one."),
              ("The working was missing", "Paper 2 is five structured questions of 20 marks each. A correct figure with no working "
               "earns less than a slightly wrong figure with clear method."),
              ("The layout lost marks", "Statements, ledgers and journals have set formats with headings, dates and labels. A "
               "right total in the wrong layout still loses marks.")],
        outro="None of this means Accounting is not your subject. It means the method was not on the page. That part is fixable.",
        hand2="show the working, always"),
    tryit=dict(type="lost", intro="Three short answers in the style of O Level Accounting 7707. Each one loses a mark on one "
                                   "line. Tap the line you think did it.",
               labels=["Debit or credit", "Depreciation", "Gross profit"],
               sheets=[
                   dict(q_small="Paper 2 style &middot; double entry", q="A business buys office equipment for Rs. 50,000 and pays by cheque. State which account is debited and which account is credited. [2]",
                        lines=[("The office equipment account is debited.", "K", "Correct: the business receives an asset, so the asset account is debited.")],
                        lost="The bank account is debited, because money has gone out.",
                        note="money out of the bank is a credit", stamp="1/2",
                        why="Paying by cheque reduces the bank balance in the business's own books, so the bank account is credited. "
                            "The bank's statement shows it the other way round, and that is where the mix-up begins. Full marks: debit "
                            "office equipment, credit bank."),
                   dict(q_small="Paper 2 style &middot; depreciation", q="Explain why a business charges depreciation on its delivery van. [2]",
                        lines=[("A van loses value over its useful life through wear and use.", "K", "Correct: this is why the charge is needed.")],
                        lost="Depreciation is the money that the business saves to buy a new van.",
                        note="a charge, not savings", stamp="1/2",
                        why="Depreciation is an accounting charge that spreads the cost of the van over the years it is used. It "
                            "does not set cash aside. The first line explained the reason, and the second line described something "
                            "else."),
                   dict(q_small="Paper 2 style &middot; income statement", q="Revenue is Rs. 90,000, opening inventory is Rs. 10,000, purchases are Rs. 60,000 and closing inventory is Rs. 15,000. Calculate gross profit. [3]",
                        lines=[("Cost of sales = opening inventory + purchases - closing inventory", "K", "Correct: this is the right formula."),
                               ("Cost of sales = 10,000 + 60,000 - 15,000 = 55,000", "K", "Correct: the cost of sales is Rs. 55,000.")],
                        lost="Gross profit = 90,000 - 15,000 = 75,000",
                        note="gross profit = revenue - cost of sales", stamp="2/3",
                        why="Gross profit is revenue minus cost of sales: 90,000 - 55,000 = 35,000. The answer found the cost of sales "
                            "and then did not use it, subtracting the closing inventory instead.")],
               legend="K = a mark-earning point. Sample questions written by SJ Academy in the style of O Level Accounting 7707; "
                      "marks are illustrative."),
    teacher_section=dict(
        h2='Your O Level Accounting teachers: <span class="sj-hl">Sir Shaibaz Ali and Sir Saifullah</span>',
        para="O Level Accounting (7707) at SJ Academy is taught by Sir Shaibaz Ali and Sir Saifullah, in class at DHA Phase 7 "
             "and live online. Sir Shaibaz Ali is CAT (ACCA) qualified and has been teaching since 2011, at BSS PECHS, LGS DHA, "
             "The Froebel's School and Karachi High School. Sir Saifullah is a CAIE-certified Accounting teacher with 5+ years "
             "of teaching at The City School, The Next School, Falconhouse and The Academy. Ask us on WhatsApp which of them takes "
             "your batch.",
        ticks=["Double entry taught from the first week, so debit and credit stop being a guess",
               "Ledgers, trial balances and final accounts practised in the formats Cambridge uses",
               "Working shown on every calculation, because method earns marks",
               "Past paper answers marked to the 7707 mark scheme, so you see which line lost the mark"],
        photo=dict(src="https://www.sjacademy.pk/wp-content/uploads/2026/07/Saifullah-Accounts-768x829.jpeg", w=768, h=829, alt="Sir Saifullah, O Level Accounting teacher at SJ Academy, Karachi"),
        card_name="Sir Saifullah",
        initials="SA", card_sub="O Level Accounting (7707) and A Level Accounting (9706), in class and online",
        card_facts=["Sir Shaibaz Ali: CAT (ACCA), teaching since 2011", "Sir Saifullah: CAIE-certified Accounting teacher, 5+ years", "Both also teach A Level Accounting"],
        tile=("Carrying on to A Level?", "A Level Accounting (9706) is also taught by Sir Shaibaz Ali and Sir Saifullah, so the habits built here carry straight on.",
              "/a-level-accounting-tuition/", "See A Level Accounting")),
    syllabus=dict(
        h2='The O Level Accounting syllabus (7707), <span class="sj-hl">paper by paper</span>',
        intro="O Level Accounting has two compulsory papers: a multiple-choice paper worth 30% and a structured written paper worth "
              "70%. Calculators are allowed in both. The syllabus has seven sections, from the fundamentals of accounting to "
              "accounting concepts and modern practice.",
        papers=[("Paper 1", "Paper 1", "Multiple Choice", ("1h 30m", "40", "30%"),
                 "Forty compulsory multiple-choice questions across the syllabus, many of them short calculations.",
                 "Practise quick journal and ledger entries, learn the accounting terms exactly, and use past paper questions to "
                 "build speed."),
                ("Paper 2", "Paper 2", "Structured Written Paper", ("1h 45m", "100", "70%"),
                 "Five compulsory structured questions of 20 marks each, covering ledgers, financial statements, analysis and "
                 "interpretation, and concepts.",
                 "Show every step of the working, learn the formats of each statement, and time the paper at about 20 minutes a "
                 "question.")],
        note="Based on the Cambridge O Level Accounting 7707 syllabus for exams in 2027, 2028 and 2029."),
    parents_extra="If your child starts falling behind, the teacher will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Accounting past papers", "7707 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/accounting-7707/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("O Level grade thresholds", "See where the grade boundaries have sat in past series. Free.", "/o-level-grade-thresholds/", "See grade thresholds"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Business Studies and Economics as well? See every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % SITE,
    faqs=[FEE_FAQ("O Level Accounting"), WHEN_FAQ("O Level Accounting"),
          ("Who teaches O Level Accounting at SJ Academy?", "Sir Shaibaz Ali and Sir Saifullah teach O Level Accounting (7707). Sir Shaibaz Ali is CAT (ACCA) and has been teaching since 2011. Sir Saifullah is a CAIE-certified Accounting teacher with 5+ years of teaching. Message us on WhatsApp to find out which of them takes your batch."),
          NEAR_FAQ("O Level Accounting"), ONLINE_FAQ("O Level Accounting"),
          ("Can I use a calculator in O Level Accounting?", "Yes. Calculators are allowed in both 7707 papers. Showing your working still matters, because Paper 2 awards marks for method."),
          ("How do I get an A* in O Level Accounting?", "Get double entry right, show the working for every figure, learn the format of each statement, and time Paper 2 at about 20 minutes a question. In class you practise past paper questions marked to the 7707 mark scheme."),
          JOIN_FAQ, DEMO_FAQ, PRIV_FAQ("O Level Accounting")],
    final_h2="One free class. Then decide.",
    final_p="Sit one Accounting class before you pay for any. Worst case, you leave knowing which side of the ledger the bank account sits on.",
    course_name="O Level Accounting (7707) tuition in Karachi and online",
    course_desc="O Level Accounting tuition for the Cambridge 7707 syllabus, taught by Sir Shaibaz Ali and Sir Saifullah: Paper 1 Multiple Choice and Paper 2 Structured Written Paper. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))
SEO["o-level-accounting"] = dict(
    title="O Level Accounting Tuition in Karachi & Online | 7707",
    meta="O Level Accounting (7707), also called Accounts, tuition in Karachi & online with Sir Shaibaz Ali and Sir Saifullah. Ledgers, final accounts. Free demo.",
    subject="O Level Accounting (7707)", papers="Paper 1 Multiple Choice (1 hour 30 minutes) and Paper 2 Structured Written Paper (1 hour 45 minutes)",
    mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
    faqs=[("Who is the best O Level Accounting teacher in Karachi?", "Look for a teacher who shows you how the marks are awarded. Sir Shaibaz Ali is CAT (ACCA) and has taught since 2011, and Sir Saifullah is CAIE-certified. Both mark answers against the 7707 mark scheme, and the first class is free."),
          ("Is O Level Accounts the same as O Level Accounting?", "Yes. Schools and students often say Accounts, but the Cambridge subject is O Level Accounting, syllabus code 7707. This class prepares students for 7707.")])

# ============================ O LEVEL CHEMISTRY 5070 ============================
PAGES.append(dict(
    file="o-level-chemistry-tuition-elementor-widget.html",
    url="/o-level-chemistry-tuition/",
    wrap="sj-p-o-level-chemistry", fam="enrol", level="o",
    crumb="Chemistry (5070)",
    keywords="o level chemistry tuition (primary); o level chemistry tuition karachi; o level chemistry 5070; o level chemistry tutor; online o level chemistry classes; "
             "supporting: chemistry o level syllabus, o level chemistry notes, o level chemistry past papers, o level chemistry topical past papers",
    yoast_title="", yoast_meta="",
    refs="OLCHEM-OL (demo), OLCHEM-Q (question)",
    pill="O Level Chemistry tuition in Karachi & online",
    h1='You learned the reaction. The mark wanted <span class="sj-hl">the reason.</span>',
    lead="O Level Chemistry (5070) with Sir Abdullah Zaman and Sir Basharat. For the May/June 2027 exams, in class at DHA "
         "Phase 7, Karachi, or live online.",
    hand="name the particles",
    levels={"ol": dict(label="O Level", title="O Level Chemistry (5070)", gid=GID_O, kw=r"\bchem",
                       papers="Paper 1 Multiple Choice (1 hour), Paper 2 Theory (1 hour 45 minutes) and one practical paper, Paper 3 or Paper 4",
                       when="Mon, Wed &amp; Fri &middot; 8:00 - 9:00 PM (online); Tue &middot; 8:00 - 9:00 PM; Fri &amp; Sat &middot; 5:00 - 6:00 PM",
                       lvl="O Level", subj="Chemistry (5070)", ref="OLCHEM-OL")},
    teacher_short="Sir Abdullah",
    teacher="Sir Abdullah Zaman and Sir Basharat",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Chemistry",
    proof=[("5+ years", "Sir Abdullah's O and A Level Chemistry teaching"), ("In class or online", "same marking, same tests")],
    problem=dict(
        h2='Knew the reaction. <span class="sj-hl">Lost the explanation.</span>',
        intro="O Level Chemistry is marked on precise words: the right particle, the right test and the right result. Papers 1 and 2 "
              "together are 80% of the grade, and these are the four places the marks usually go.",
        pins=[("Faster stopped at faster", "A higher temperature does not just make a reaction faster. The marks are for particles moving "
               "faster, colliding more often, and more collisions having enough energy."),
              ("The test had no result", "Gas tests and ion tests are marked as a pair: the test and the exact result. It changes "
               "colour is not a result."),
              ("Electrons or ions?", "Metals conduct with moving electrons. Ionic compounds conduct with moving ions, when molten or "
               "dissolved. Mixing the two up is a common lost mark."),
              ("The working was missing", "Mole calculations are marked step by step, so working that is shown can earn marks even when "
               "the final answer slips.")],
        outro="None of this means Chemistry is not for you. It means the examiner never saw the reason. That part is fixable.",
        hand2="what exactly did the particles do?"),
    tryit=dict(type="lost", intro="Three short answers in the style of O Level Chemistry 5070. Each one loses a mark on one "
                                   "line. Tap the line you think did it.",
               labels=["Rate", "Gas test", "Conduction"],
               sheets=[
                   dict(q_small="Paper 2 style &middot; rates of reaction", q="Explain, in terms of particles, why increasing the temperature increases the rate of a reaction. [3]",
                        lines=[("The particles gain energy and move faster.", "K", "Correct: more kinetic energy means faster-moving particles."),
                               ("They collide more often.", "K", "Correct: more frequent collisions is a mark point.")],
                        lost="The collisions are also more energetic because the activation energy is lowered.",
                        note="a catalyst lowers it. heat does not", stamp="2/3",
                        why="Temperature does not change the activation energy. It increases the number of particles that have at least "
                            "that much energy, so a greater proportion of collisions are successful. Lowering the activation energy is "
                            "what a catalyst does."),
                   dict(q_small="Paper 2 style &middot; chemical tests", q="Describe how you would test for ammonia gas. State the positive result. [2]",
                        lines=[("Hold damp red litmus paper in the gas.", "K", "Correct: this is the test for ammonia.")],
                        lost="The litmus paper turns red.",
                        note="ammonia is alkaline, so it turns blue", stamp="1/2",
                        why="Ammonia is an alkaline gas, so damp red litmus paper turns blue. A result that is already the starting "
                            "colour cannot be a positive result, and the result is the second mark."),
                   dict(q_small="Paper 2 style &middot; bonding", q="Explain why molten sodium chloride conducts electricity but solid sodium chloride does not. [3]",
                        lines=[("In solid sodium chloride the ions are held in fixed positions in a lattice.", "K", "Correct: the ions cannot move."),
                               ("When molten, the ions are free to move.", "K", "Correct: movement is the key idea.")],
                        lost="The electrons are free to move and carry the charge.",
                        note="ions carry the charge here, not electrons", stamp="2/3",
                        why="Ionic compounds conduct when their ions are free to move, so the ions carry the charge. Free electrons "
                            "carry charge in metals. The first two lines had the right idea, and the last line swapped the charge "
                            "carrier.")],
               legend="K = a mark-earning point. Sample questions written by SJ Academy in the style of O Level Chemistry 5070; "
                      "marks are illustrative."),
    teacher_section=dict(
        h2='Your O Level Chemistry teachers: <span class="sj-hl">Sir Abdullah Zaman and Sir Basharat</span>',
        para="O Level Chemistry (5070) at SJ Academy is taught by Sir Abdullah Zaman and Sir Basharat, in class at DHA Phase 7 "
             "and live online. Sir Abdullah Zaman has 5+ years of teaching O and A Level Chemistry, at Lions Schooling System, "
             "Progressive Public School and Iqra University. Sir Basharat teaches O Level classes at the DHA Phase 7 campus. "
             "Ask us on WhatsApp which of them takes your batch.",
        ticks=["Every explanation taught in particle terms, so answers name what the particles do",
               "Gas tests, ion tests and results learned as pairs",
               "Mole calculations practised step by step, with the working shown",
               "Past paper answers marked to the 5070 mark scheme, so you see which line lost the mark"],
        photo=dict(src="https://www.sjacademy.pk/wp-content/uploads/2025/12/Zaman-chemistry-768x569.jpeg", w=768, h=569, alt="Sir Abdullah Zaman, O Level Chemistry teacher at SJ Academy, Karachi"),
        card_name="Sir Abdullah Zaman",
        initials="AZ", card_sub="O Level Chemistry (5070) and A Level Chemistry (9701), in class and online",
        card_facts=["Sir Abdullah Zaman: 5+ years teaching O and A Level Chemistry", "Has taught at Lions Schooling System, Progressive Public School and Iqra University", "Sir Basharat teaches O Level classes at the DHA Phase 7 campus"],
        tile=("Carrying on to A Level?", "A Level Chemistry (9701) is also taught by Sir Abdullah Zaman, with lab practicals in SJ Academy's lab.",
              "/a-level-chemistry-tuition/", "See A Level Chemistry")),
    syllabus=dict(
        h2='The O Level Chemistry syllabus (5070), <span class="sj-hl">paper by paper</span>',
        intro="O Level Chemistry has two written papers and one practical paper. Paper 1 is worth 30%, Paper 2 is worth 50%, and "
              "students take either Paper 3 or Paper 4 for the last 20%. Calculators are allowed. The syllabus has twelve topics, from "
              "states of matter to experimental techniques and chemical analysis.",
        papers=[("Paper 1", "Paper 1", "Multiple Choice", ("1h", "40", "30%"),
                 "Forty four-option multiple-choice questions across the whole syllabus.",
                 "Learn the facts and tests precisely, and use topical past paper questions to find weak topics early."),
                ("Paper 2", "Paper 2", "Theory", ("1h 45m", "80", "50%"),
                 "Short-answer and structured questions on all twelve topics, including organic chemistry, calculations and "
                 "explanations.",
                 "Explain in particle terms, practise mole calculations with the working shown, and learn every test with its result."),
                ("Paper 3 or 4", "Paper 3 or Paper 4", "Practical test, or alternative to practical", ("1h 30m or 1h", "40", "20%"),
                 "Paper 3 is a practical test done in a laboratory. Paper 4 tests the same skills on paper, with no laboratory work. "
                 "Students take one of the two.",
                 "Practise reading apparatus, tables and graphs, and learn the experimental techniques and tests in topic 12. Ask "
                 "your school which paper you are entered for.")],
        note="Based on the Cambridge O Level Chemistry 5070 syllabus for exams in 2026, 2027 and 2028."),
    parents_extra="If your child starts falling behind, the teacher will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Chemistry past papers", "5070 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/chemistry-5070/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("How to use a mark scheme", "The method for marking your own paper properly. Free.", "/blog/how-to-use-mark-scheme/", "Read the guide"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Physics and Maths as well? See <a class="sj-link" href="%s/o-level-physics-tuition/">O Level Physics tuition</a> and <a class="sj-link" href="%s/o-level-math-tuition/">O Level Maths tuition</a>, or every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % (SITE, SITE, SITE),
    faqs=[FEE_FAQ("O Level Chemistry"), WHEN_FAQ("O Level Chemistry"),
          ("Who teaches O Level Chemistry at SJ Academy?", "Sir Abdullah Zaman and Sir Basharat teach O Level Chemistry (5070). Sir Abdullah has 5+ years of teaching O and A Level Chemistry, and Sir Basharat teaches O Level classes at the DHA Phase 7 campus. Message us on WhatsApp to find out which of them takes your batch."),
          NEAR_FAQ("O Level Chemistry"), ONLINE_FAQ("O Level Chemistry"),
          ("Can I use a calculator in O Level Chemistry?", "Yes. The 5070 syllabus allows calculators in all parts of the examination, so bring the one you practise with."),
          ("Do you run O Level Chemistry practical classes?", "No. SJ Academy runs lab practical classes for A Level Physics, Chemistry and Biology only. O Level students take either Paper 3, a practical test, or Paper 4, a written alternative to practical, and the class covers the experimental techniques and chemical analysis in the syllabus. Ask your school which paper you are entered for."),
          ("How do I get an A* in O Level Chemistry?", "Explain in particle terms, learn every test with its exact result, show the working in calculations, and practise past paper questions marked against the 5070 mark scheme. That is how every answer is marked in class."),
          JOIN_FAQ, DEMO_FAQ, PRIV_FAQ("O Level Chemistry")],
    final_h2="One free class. Then decide.",
    final_p="Sit one Chemistry class before you pay for any. Worst case, you leave knowing why heat speeds up a reaction and a catalyst does something different.",
    course_name="O Level Chemistry (5070) tuition in Karachi and online",
    course_desc="O Level Chemistry tuition for the Cambridge 5070 syllabus, taught by Sir Abdullah Zaman and Sir Basharat: Paper 1 Multiple Choice, Paper 2 Theory, and the practical paper options. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))
SEO["o-level-chemistry"] = dict(
    title="O Level Chemistry Tuition in Karachi & Online | 5070",
    meta="O Level Chemistry (5070) tuition in Karachi & online with Sir Abdullah Zaman and Sir Basharat. Theory, calculations, gas and ion tests. Free demo class.",
    subject="O Level Chemistry (5070)", papers="Paper 1 Multiple Choice (1 hour), Paper 2 Theory (1 hour 45 minutes) and one practical paper, Paper 3 or Paper 4",
    mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
    faqs=[("Who is the best O Level Chemistry teacher in Karachi?", "The best teacher is the one whose method fixes your mistakes. Sir Abdullah Zaman and Sir Basharat mark every explanation against the 5070 mark scheme, and the first class is free, so you can judge for yourself."),
          ("What is the O Level Chemistry syllabus?", "The Cambridge O Level Chemistry 5070 syllabus has twelve topics: states of matter; atoms, elements and compounds; stoichiometry; electrochemistry; chemical energetics; chemical reactions; acids, bases and salts; the Periodic Table; metals; chemistry of the environment; organic chemistry; and experimental techniques and chemical analysis.")])

# ============================ O LEVEL ISLAMIYAT 2058 ============================
PAGES.append(dict(
    file="o-level-islamiat-tuition-elementor-widget.html",
    url="/o-level-islamiat-tuition/",
    wrap="sj-p-o-level-islamiyat", fam="enrol", level="o",
    crumb="Islamiyat (2058)",
    keywords="o level islamiat tuition (primary); o level islamiyat tuition karachi; o level islamiyat 2058; online o level islamiat classes; o level islamiat teacher karachi; "
             "supporting: o level islamiat notes, o level islamiyat syllabus, o level islamiat past papers, islamiyat o level threshold",
    yoast_title="", yoast_meta="",
    refs="OLISL-OL (demo), OLISL-Q (question)",
    pill="O Level Islamiyat tuition in Karachi & online",
    h1='You know the history. The question asked for <span class="sj-hl">something narrower.</span>',
    lead="O Level Islamiyat (2058), also written Islamiat, with Sir Kashaan Ali, who has been teaching since 2003. For the "
         "May/June 2027 exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="answer the question, not the topic",
    levels={"ol": dict(label="O Level", title="O Level Islamiyat (2058)", gid=GID_O, kw=r"\bislam",
                       papers="Paper 1 and Paper 2, 1 hour 30 minutes each",
                       when="Mon, Tue, Wed &amp; Thu &middot; 5:00 - 6:00 PM",
                       lvl="O Level", subj="Islamiyat (2058)", ref="OLISL-OL")},
    teacher_short="Sir Kashaan",
    teacher="Sir Kashaan Ali",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Islamiyat",
    proof=[("Since 2003", "Sir Kashaan's teaching"), ("5 schools", "taught at, including Beaconhouse DHA and The City School")],
    problem=dict(
        h2='Knew the topic. <span class="sj-hl">Answered a different question.</span>',
        intro="O Level Islamiyat is marked on how directly an answer meets the question. Both papers carry equal weight, and "
              "these are the four places the marks usually go.",
        pins=[("A retelling, not an answer", "The 14-mark questions need essay-length answers, marked in levels. A general retelling of "
               "the topic sits low. A direct answer with specific detail sits higher."),
              ("The passage was repeated, not explained", "Question 1 in each paper sets passages from the prescribed lists. The answer "
               "has to explain them, not repeat them."),
              ("Names and events went missing", "Specific people, events and examples are what lift an answer. The Caliph did many "
               "good things is not a fact."),
              ("Four answers, ninety minutes", "Each paper asks for four answers in 1 hour 30 minutes. The 8-mark question should "
               "not get 14-mark time.")],
        outro="None of this means the content is the problem. It means the answer did not match the question. That part is fixable.",
        hand2="read the question twice"),
    tryit=dict(type="map", intro="Every 2058 mark sits in one of four answers per paper. Tap a question to see where students "
                                  "usually lose marks in it.",
               maps=[("Paper 1 &middot; 1 hour 30 minutes &middot; 50 marks", [
                         ("Question 1", "Major themes of the Qur'an: two passages", 8, "Two passages chosen from the three set. Explain what each passage teaches instead of repeating it, and keep the answer short for the marks."),
                         ("Question 2", "The history and importance of the Qur'an", 14, "An essay-length answer, usually in more than one part. Plan it, and include specific details about how the Qur'an was revealed, compiled and used."),
                         ("Two more questions", "From the life of the Prophet and the first Islamic community", 28, "You choose two more answers of 14 marks each. Pick the questions where you can give names, events and reasons, not just the topics you like.")]),
                     ("Paper 2 &middot; 1 hour 30 minutes &middot; 50 marks", [
                         ("Question 1", "Major teachings in the Hadiths: two passages", 8, "Two passages chosen from the four set. Explain the teaching in each passage and what it means for how a Muslim should live."),
                         ("Question 2", "The history and importance of the Hadiths", 14, "An essay-length answer, usually in more than one part. Include how the Hadiths were collected and why they matter."),
                         ("Two more questions", "From the Rightly Guided Caliphs, the Articles of Faith and the Pillars of Islam", 28, "You choose two more answers of 14 marks each. Use events, policies and examples as evidence, and answer the exact question that is set.")])],
               legend="Mark totals from the Cambridge O Level Islamiyat 2058 syllabus for exams in 2026 and 2027. In each paper you answer Question 1, Question 2 and two others."),
    teacher_section=dict(
        h2='Your O Level Islamiyat teacher: <span class="sj-hl">Sir Kashaan Ali</span>',
        para="Sir Kashaan Ali teaches O Level Islamiyat (2058) and O Level Pakistan Studies (2059) at SJ Academy, in class at "
             "DHA Phase 7 and live online. He has been teaching since 2003, at Beaconhouse DHA, The City School, Bahria Foundation, "
             "LINKS and The Indus Academy.",
        ticks=["Every essay question practised against the levels used in the mark scheme",
               "Passages from the prescribed lists explained, not just memorised",
               "Names, events and examples built into answers as evidence",
               "Timed answers from the start, so four answers in ninety minutes feels normal"],
        photo=dict(src="https://www.sjacademy.pk/wp-content/uploads/2025/12/IMG_6390.jpg", w=768, h=536, alt="Sir Kashaan Ali, Islamiyat and Pakistan Studies teacher at SJ Academy, Karachi"),
        initials="KA", card_sub="O Level Islamiyat (2058) and Pakistan Studies (2059), in class and online",
        card_facts=["Teaching since 2003", "Has taught at Beaconhouse DHA, The City School and LINKS", "Also teaches O Level Pakistan Studies"],
        tile=("Taking Pakistan Studies too?", "O Level Pakistan Studies (2059) is also taught by Sir Kashaan, so both compulsory subjects sit with one teacher.",
              "/o-level-pakistan-studies-tuition/", "See Pakistan Studies")),
    syllabus=dict(
        h2='The O Level Islamiyat syllabus (2058), <span class="sj-hl">paper by paper</span>',
        intro="O Level Islamiyat has two compulsory papers of equal weight, and both must be taken to receive a grade. Each paper "
              "has five questions, and you answer Question 1, Question 2 and two others.",
        papers=[("Paper 1", "Paper 1", "The Qur'an and the Prophet", ("1h 30m", "50", "50%"),
                 "Major themes of the Qur'an, the history and importance of the Qur'an, the life and importance of the Prophet "
                 "Muhammad (pbuh), and the first Islamic community.",
                 "Learn the key events in order, practise explaining the set passages, and write essay answers that meet the "
                 "exact question."),
                ("Paper 2", "Paper 2", "The Hadiths, the Caliphs and the faith", ("1h 30m", "50", "50%"),
                 "Major teachings in the Hadiths, the history and importance of the Hadiths, the Rightly Guided Caliphs, and the "
                 "Articles of Faith and the Pillars of Islam.",
                 "Learn the Hadith passages and their lessons, know the main events and policies of each Caliph, and practise "
                 "timed essay answers.")],
        note="Based on the Cambridge O Level Islamiyat 2058 syllabus for exams in 2026 and 2027."),
    parents_extra="If your child starts falling behind, Sir Kashaan will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Islamiyat past papers", "2058 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/islamiyat-2058/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("O Level grade thresholds", "See where the grade boundaries have sat in past series. Free.", "/o-level-grade-thresholds/", "See grade thresholds"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Urdu and Pakistan Studies too? See <a class="sj-link" href="%s/o-level-pakistan-studies-tuition/">O Level Pakistan Studies tuition</a>, or every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % (SITE, SITE),
    faqs=[FEE_FAQ("O Level Islamiyat"), WHEN_FAQ("O Level Islamiyat"),
          ("Who teaches O Level Islamiyat at SJ Academy?", "Sir Kashaan Ali teaches O Level Islamiyat (2058) and O Level Pakistan Studies (2059). He has been teaching since 2003, at Beaconhouse DHA, The City School, Bahria Foundation, LINKS and The Indus Academy."),
          NEAR_FAQ("O Level Islamiyat"), ONLINE_FAQ("O Level Islamiyat"),
          ("Is Islamiyat compulsory in O Level?", "IBCC lists Islamiyat and Pakistan Studies among the compulsory subjects for Pakistani students who want an O Level equivalence certificate. Check the current IBCC requirements for your case, and use our <a class=\"sj-link\" href=\"%s/ibcc-equivalence-calculator/\">IBCC equivalence calculator</a> once you have your grades." % SITE),
          ("How do I get an A* in O Level Islamiyat?", "Answer the exact question, use names, events and examples as evidence, explain the set passages instead of repeating them, and time all four answers in each paper. In class you practise past paper questions marked against the 2058 mark scheme."),
          JOIN_FAQ, DEMO_FAQ, PRIV_FAQ("O Level Islamiyat")],
    final_h2="Sit one Islamiyat class before you pay for any",
    final_p="Book a free demo, in class or online. Worst case, your child leaves knowing how to turn what they know into an answer that matches the question.",
    course_name="O Level Islamiyat (2058) tuition in Karachi and online",
    course_desc="O Level Islamiyat tuition for the Cambridge 2058 syllabus, taught by Sir Kashaan Ali: Paper 1 on the Qur'an and the Prophet, and Paper 2 on the Hadiths, the Caliphs and the faith. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))
SEO["o-level-islamiyat"] = dict(
    title="O Level Islamiyat Tuition in Karachi & Online | 2058",
    meta="O Level Islamiyat (Islamiat) 2058 tuition in Karachi & online with Sir Kashaan Ali, teaching since 2003. Qur'an, Hadith, history, essays. Free demo class.",
    subject="O Level Islamiyat (2058)", papers="Paper 1 and Paper 2, 1 hour 30 minutes each",
    mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
    faqs=[("Who is the best O Level Islamiyat teacher in Karachi?", "Look for a teacher who knows how the papers are marked. Sir Kashaan Ali has been teaching since 2003 and marks every essay answer against the 2058 mark scheme. The first class is free, so you can judge for yourself."),
          ("Islamiat or Islamiyat: which spelling is right?", "Cambridge spells it Islamiyat, and many students and schools write Islamiat. They are the same subject, syllabus code 2058, and the same class at SJ Academy.")])

# ============================ O LEVEL PAKISTAN STUDIES 2059 ============================
PAGES.append(dict(
    file="o-level-pakistan-studies-tuition-elementor-widget.html",
    url="/o-level-pakistan-studies-tuition/",
    wrap="sj-p-o-level-pakistan-studies", fam="enrol", level="o",
    crumb="Pakistan Studies (2059)",
    keywords="o level pakistan studies tuition (primary); o level pak studies tuition karachi; o level pakistan studies 2059; online o level pakistan studies classes; "
             "supporting: o level pakistan studies notes, o level pakistan studies syllabus, o level pakistan studies past papers, pakistan studies o level threshold",
    yoast_title="", yoast_meta="",
    refs="OLPS-OL (demo), OLPS-Q (question)",
    pill="O Level Pakistan Studies tuition in Karachi & online",
    h1='You know Pakistan. The paper wants <span class="sj-hl">evidence and evaluation.</span>',
    lead="O Level Pakistan Studies (2059), also called Pak Studies, with Sir Kashaan Ali, who has been teaching since 2003. For "
         "the May/June 2027 exams, in class at DHA Phase 7, Karachi, or live online.",
    hand="use the source",
    levels={"ol": dict(label="O Level", title="O Level Pakistan Studies (2059)", gid=GID_O, kw=r"\bpak",
                       papers="Paper 1 History and Culture and Paper 2 Environment, 1 hour 30 minutes each",
                       when="Mon, Tue, Wed &amp; Thu &middot; 4:00 - 5:00 PM",
                       lvl="O Level", subj="Pakistan Studies (2059)", ref="OLPS-OL")},
    teacher_short="Sir Kashaan",
    teacher="Sir Kashaan Ali",
    batch="May/June 2027. Running now, still open.",
    fee="From Rs. 8,500 a month",
    q_words="O Level Pakistan Studies",
    proof=[("Since 2003", "Sir Kashaan's teaching"), ("5 schools", "taught at, including Beaconhouse DHA and The City School")],
    problem=dict(
        h2='Knew the facts. <span class="sj-hl">Missed the analysis.</span>',
        intro="O Level Pakistan Studies is marked on how you use knowledge, not how much of it you can write. Both papers carry "
              "equal weight, and these are the four places the marks usually go.",
        pins=[("The source was ignored", "Paper 1 Section A starts with source-based parts. An answer that does not use the source "
               "misses what the question is asking."),
              ("The 14-mark part was a description", "Each Section B question ends with a 14-mark part that asks for analysis or "
               "evaluation, answered as an essay. Describing events fills the page but not the mark scheme."),
              ("Paper 2 answers had no places or figures", "Paper 2 asks you to interpret resources, then analyse and evaluate. "
               "Environment answers need named places and figures, not general statements."),
              ("Three questions, ninety minutes", "Paper 2 asks for three questions from five, about 30 minutes each. A first answer "
               "that runs long costs marks on the last.")],
        outro="None of this means you do not know Pakistan Studies. It means the examiner never saw the evidence. That part is fixable.",
        hand2="where is your evidence?"),
    tryit=dict(type="map", intro="Every 2059 mark sits in one of a few questions per paper. Tap a question to see where "
                                  "students usually lose marks in it.",
               maps=[("Paper 1 &middot; History and Culture &middot; 1 hour 30 minutes &middot; 75 marks", [
                         ("Section A", "One compulsory question, four parts on one theme", 25, "Parts (a) and (b) are source-based, so use the source in your answer. Parts (c) and (d) ask for more explanation and judgement."),
                         ("Section B", "Two questions chosen from four", 50, "Each question is 25 marks in three parts: knowledge for 4 marks, understanding for 7 marks, and analysis and evaluation for 14 marks, answered in essay form. Most of the marks are in the last part.")]),
                     ("Paper 2 &middot; Environment of Pakistan &middot; 1 hour 30 minutes &middot; 75 marks", [
                         ("Question 1 of 3", "Your first choice, four parts (a) to (d)", 25, "Choose the questions where you can give named places and figures. Read the resources carefully before you write."),
                         ("Question 2 of 3", "Your second choice, four parts (a) to (d)", 25, "Keep to about 30 minutes. The recommended time per question is the same for all three."),
                         ("Question 3 of 3", "Your third choice, four parts (a) to (d)", 25, "Leave enough time for this one. The analysis and evaluation parts carry the most marks in each question.")])],
               legend="Mark totals from the Cambridge O Level Pakistan Studies 2059 syllabus. All answers must be in English."),
    teacher_section=dict(
        h2='Your O Level Pakistan Studies teacher: <span class="sj-hl">Sir Kashaan Ali</span>',
        para="Sir Kashaan Ali teaches O Level Pakistan Studies (2059) and O Level Islamiyat (2058) at SJ Academy, in class at "
             "DHA Phase 7 and live online. He has been teaching since 2003, at Beaconhouse DHA, The City School, Bahria Foundation, "
             "LINKS and The Indus Academy.",
        ticks=["Source questions practised until using the source is automatic",
               "The 14-mark analysis and evaluation part practised as a planned essay",
               "Paper 2 answers built on named places, data and resources",
               "Past paper answers marked to the 2059 mark scheme, so you see which line lost the mark"],
        photo=dict(src="https://www.sjacademy.pk/wp-content/uploads/2025/12/IMG_6390.jpg", w=768, h=536, alt="Sir Kashaan Ali, Islamiyat and Pakistan Studies teacher at SJ Academy, Karachi"),
        initials="KA", card_sub="O Level Pakistan Studies (2059) and Islamiyat (2058), in class and online",
        card_facts=["Teaching since 2003", "Has taught at Beaconhouse DHA, The City School and LINKS", "Also teaches O Level Islamiyat"],
        tile=("Taking Islamiyat too?", "O Level Islamiyat (2058) is also taught by Sir Kashaan, so both compulsory subjects sit with one teacher.",
              "/o-level-islamiat-tuition/", "See Islamiyat")),
    syllabus=dict(
        h2='The O Level Pakistan Studies syllabus (2059), <span class="sj-hl">paper by paper</span>',
        intro="O Level Pakistan Studies has two compulsory papers of equal weight. All answers must be written in English, and "
              "the recommended time is about 30 minutes per question.",
        papers=[("Paper 1", "Paper 1", "History and Culture of Pakistan", ("1h 30m", "75", "50%"),
                 "Section A is one compulsory 25-mark question in four parts, with the first two parts source-based. Section B is "
                 "two questions chosen from four, each worth 25 marks.",
                 "Use the source in Section A, and plan the 14-mark analysis and evaluation part of each Section B question "
                 "before writing."),
                ("Paper 2", "Paper 2", "Environment of Pakistan", ("1h 30m", "75", "50%"),
                 "Three questions chosen from five, each worth 25 marks, in four parts (a) to (d). The paper tests interpreting "
                 "resources, analysis and evaluation.",
                 "Learn named places and figures, read the resources before answering, and keep each question to about 30 "
                 "minutes.")],
        note="Based on the Cambridge O Level Pakistan Studies 2059 syllabus."),
    parents_extra="If your child starts falling behind, Sir Kashaan will tell you. You can ask for an update at any time",
    reviews=REV_GENERAL,
    review_h2='&ldquo;They break things down in a way that actually <span class="sj-hl">makes sense</span>&rdquo;',
    resources=[("O Level Pakistan Studies past papers", "2059 question papers and mark schemes, by year and paper. Free.", "/o-level-past-papers/pakistan-studies-2059/", "Open past papers"),
               ("Past paper and mark scheme viewer", "Open a paper and its mark scheme side by side. Free.", "/past-paper-viewer/", "Open the viewer"),
               ("O Level grade thresholds", "See where the grade boundaries have sat in past series. Free.", "/o-level-grade-thresholds/", "See grade thresholds"),
               ("IBCC equivalence calculator", "Turn O Level grades into IBCC marks in a minute. Free.", "/ibcc-equivalence-calculator/", "Open the calculator")],
    more_links='Taking Islamiyat and Urdu too? See <a class="sj-link" href="%s/o-level-islamiat-tuition/">O Level Islamiyat tuition</a>, or every subject on the <a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level tuition page</a>.' % (SITE, SITE),
    faqs=[FEE_FAQ("O Level Pakistan Studies"), WHEN_FAQ("O Level Pakistan Studies"),
          ("Who teaches O Level Pakistan Studies at SJ Academy?", "Sir Kashaan Ali teaches O Level Pakistan Studies (2059) and O Level Islamiyat (2058). He has been teaching since 2003, at Beaconhouse DHA, The City School, Bahria Foundation, LINKS and The Indus Academy."),
          NEAR_FAQ("O Level Pakistan Studies"), ONLINE_FAQ("O Level Pakistan Studies"),
          ("Is Pakistan Studies compulsory in O Level?", "IBCC lists Pakistan Studies and Islamiyat among the compulsory subjects for Pakistani students who want an O Level equivalence certificate. Check the current IBCC requirements for your case, and use our <a class=\"sj-link\" href=\"%s/ibcc-equivalence-calculator/\">IBCC equivalence calculator</a> once you have your grades." % SITE),
          ("How do I get an A* in O Level Pakistan Studies?", "Use the source in Section A, plan the 14-mark analysis and evaluation parts, back every Paper 2 answer with named places and figures, and keep to about 30 minutes a question. In class you practise past paper questions marked against the 2059 mark scheme."),
          JOIN_FAQ, DEMO_FAQ, PRIV_FAQ("O Level Pakistan Studies")],
    final_h2="Sit one Pakistan Studies class before you pay for any",
    final_p="Book a free demo, in class or online. Worst case, your child leaves knowing why the source is part of the answer.",
    course_name="O Level Pakistan Studies (2059) tuition in Karachi and online",
    course_desc="O Level Pakistan Studies tuition for the Cambridge 2059 syllabus, taught by Sir Kashaan Ali: Paper 1 History and Culture of Pakistan and Paper 2 Environment of Pakistan. In class at DHA Phase 7, Karachi, and live online.",
    edu_level="Cambridge O Level",
))
SEO["o-level-pakistan-studies"] = dict(
    title="O Level Pakistan Studies Tuition in Karachi & Online | 2059",
    meta="O Level Pakistan Studies (2059), or Pak Studies, tuition in Karachi & online with Sir Kashaan Ali, teaching since 2003. Sources, essays. Free demo class.",
    subject="O Level Pakistan Studies (2059)", papers="Paper 1 History and Culture and Paper 2 Environment, 1 hour 30 minutes each",
    mode="In class at DHA Phase 7, Karachi, or live online", price="8500",
    faqs=[("Who is the best O Level Pakistan Studies teacher in Karachi?", "Look for a teacher who knows how the papers are marked. Sir Kashaan Ali has been teaching since 2003 and marks every answer against the 2059 mark scheme. The first class is free, so you can judge for yourself."),
          ("Is O Level Pak Studies the same as Pakistan Studies?", "Yes. Pak Studies is the short name for O Level Pakistan Studies, syllabus code 2059. This class prepares students for 2059.")])


def fix_schema(doc, names):
    """Replace the single instructor in the Course schema with one Person per teacher."""
    if len(names) < 2:
        return doc

    def sub(m):
        obj = json.loads(m.group(1))
        if obj.get("@type") == "Course":
            for inst in obj["hasCourseInstance"]:
                one = inst["instructor"]
                inst["instructor"] = [dict(one, name=n) for n in names]
        return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=True)
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', sub, doc, flags=re.S)


SCHEMA_NAMES = {
    "sj-p-o-level-accounting": ["Shaibaz Ali", "Saifullah"],
    "sj-p-o-level-chemistry": ["Abdullah Zaman", "Basharat"],
}

if __name__ == "__main__":
    bsp.SEO.update(SEO)
    os.makedirs(OUT, exist_ok=True)
    for p in PAGES:
        out = bsp.build(p)
        out = fix_schema(out, SCHEMA_NAMES.get(p["wrap"], []))
        out = out.replace('"dateModified": "2026-11-09"', '"dateModified": "2026-11-11"')
        path = os.path.join(OUT, p["file"])
        with open(path, "w", encoding="ascii") as f:
            f.write(out)
        g = SEO[p["wrap"].replace("sj-p-", "")]
        print("%-52s %6.1f KB   title %d / meta %d" % (p["file"], len(out) / 1024, len(g["title"]), len(g["meta"])))
