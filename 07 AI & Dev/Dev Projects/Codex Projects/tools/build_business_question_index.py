#!/usr/bin/env python3
import csv
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import pdfplumber
except ImportError:
    print("pdfplumber is required. Use the bundled Codex Python runtime.", file=sys.stderr)
    raise


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "business-9609"
PDF_DIR = ROOT / "tmp" / "business-9609-pdfs"

BASE = "https://f006.backblazeb2.com/file/Past-papers-storage/A+Level/Business+(9609)"

SESSIONS = [
    ("February/March", "February March", "m"),
    ("May/June", "May June", "s"),
    ("October/November", "October November", "w"),
]

PAPER_NUMBERS = {
    "1": "Paper 1",
    "2": "Paper 2",
    "3": "Paper 3",
    "4": "Paper 4",
}

VARIANTS = ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]
MARCH_VARIANTS = ["12", "22", "32", "42"]

TOPIC_RULES = [
    ("Business and its environment", [
        "corporate social responsibility", "csr", "stakeholder", "externality", "business objective",
        "private sector", "public sector", "mission statement", "ethic", "enterprise", "entrepreneur",
        "limited liability", "partnership", "co-operative", "cooperative", "franchise", "franchising",
        "public limited company", "private limited company", "triple bottom line", "added value"
    ]),
    ("People in organisations", [
        "delegation", "motivation", "leadership", "manager", "employee", "workforce", "training",
        "recruitment", "human resource", "hrm", "labour", "organisational structure", "span of control",
        "communication", "teamwork", "dismissal", "redundancy", "job enrichment", "job rotation",
        "job description", "person specification", "curriculum vitae", "résumé", "resume", "salary",
        "contract of employment", "performance-related pay", "piece rate", "morale", "welfare",
        "emotional intelligence", "corporate culture"
    ]),
    ("Marketing", [
        "marketing", "market research", "market segment", "segmentation", "price", "pricing", "promotion",
        "product life cycle", "brand", "distribution", "place", "advertising", "sales", "customer",
        "consumer", "demand", "market share", "target market", "elasticity",
        "national market", "sampling", "primary research", "product differentiation", "usp",
        "unique selling point", "boston matrix", "product portfolio", "niche market"
    ]),
    ("Operations management", [
        "operations", "production", "capacity", "inventory", "stock", "quality", "lean", "kaizen",
        "just in time", "jit", "location", "factory", "supplier", "outsourcing", "time series",
        "moving average", "forecasting", "productivity", "efficiency", "labour intensive", "capital intensive",
        "computer aided manufacture", "computer aided design", "cam", "cad", "transformation process",
        "economies of scale", "mass customisation", "mass customization", "job production", "batch produced",
        "batch production", "network diagram", "critical path", "earliest start time", "est"
    ]),
    ("Finance and accounting", [
        "cash flow", "profit", "revenue", "cost", "break-even", "budget", "finance", "accounting",
        "balance sheet", "income statement", "ratio", "liquidity", "gearing", "payback", "arr",
        "accounting rate of return", "investment appraisal", "npv", "net present value", "capital",
        "shareholder", "dividend", "opportunity cost", "published accounts", "overdraft", "debt factoring",
        "bankruptcy", "liquidation", "margin of safety", "investor return"
    ]),
    ("Business strategy", [
        "strategy", "strategic", "decision-making", "decision making", "swot", "pest", "pestle",
        "ansoff", "porter", "growth", "takeover", "merger", "joint venture", "globalisation",
        "international", "competitive advantage", "contingency plan", "corporate planning", "business plan",
        "change management", "change culture", "research and development", "r&d", "grow internally",
        "organically", "intrapreneur"
    ]),
    ("External influences", [
        "exchange rate", "currency", "inflation", "interest rate", "government", "legal", "law",
        "economic", "environmental", "social", "technological", "tax", "tariff", "quota",
        "trade", "global", "country", "recession"
    ]),
]

COMMAND_WORDS = [
    "Analyse", "Analyze", "Evaluate", "Explain", "Calculate", "Discuss", "Assess", "Recommend",
    "Define", "State", "Identify", "Outline", "Justify", "Advise", "Comment"
]


def url_for(folder_name, year, code, kind, variant):
    folder = urllib.parse.quote_plus(f"{folder_name} {year}")
    filename = f"9609_{code}{str(year)[2:]}_{kind}_{variant}.pdf"
    return f"{BASE}/{folder}/{filename}"


def url_exists(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "SJAcademyIndexer/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return 200 <= resp.status < 400
    except Exception:
        req = urllib.request.Request(url, headers={"User-Agent": "SJAcademyIndexer/1.0", "Range": "bytes=0-0"})
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                return 200 <= resp.status < 400
        except Exception:
            return False


def download(url, path):
    if path.exists() and path.stat().st_size > 1000:
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "SJAcademyIndexer/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 1000:
            return False
        path.write_bytes(data)
        return True
    except Exception as exc:
        print(f"download failed: {url} ({exc})", file=sys.stderr)
        return False


def extract_text(pdf_path):
    parts = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            parts.append(text)
    return "\n".join(parts)


def clean_question_text(text):
    text = re.sub(r"\(cid:\d+\)", " ", text)
    text = re.sub(r"\b(?:SIHT|NI|ETIRW|TON|OD)\b", " ", text)
    text = text.replace("Write the question number here:", " ")
    text = re.sub(r"\.{5,}.*", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+\[(\d+)\]$", r" [\1]", text)
    return text


def strip_noise(text):
    lines = []
    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        if "(cid:" in raw:
            continue
        if raw.startswith("*"):
            continue
        if raw in {"BLANK PAGE", "Answer all questions.", "Answer all questions"}:
            continue
        if raw.startswith("© UCLES") or raw.startswith("© Cambridge"):
            continue
        if "DO NOT WRITE IN THIS MARGIN" in raw or "NIGRAM" in raw or "SIHT NI" in raw:
            continue
        if re.search(r"^9609/\d+/.+/\d+$", raw):
            continue
        if re.search(r"^\d+$", raw):
            continue
        if raw.startswith("Permission to reproduce"):
            continue
        lines.append(raw)
    return "\n".join(lines)


def extract_questions(text):
    text = strip_noise(text)
    if "Paper 2 Data Response" in text:
        paper2_questions = extract_subpart_questions(text)
        if paper2_questions:
            return paper2_questions

    candidates = []
    pattern = re.compile(
        r"(?m)^(?P<num>\d{1,2}(?:\s*\([a-z]\))?)\s+(?P<body>(?:(?!^\d{1,2}(?:\s*\([a-z]\))?\s+[A-Z]).)+?\[\s*(?P<marks>\d{1,2})\s*\])",
        re.S,
    )
    for match in pattern.finditer(text):
        num = re.sub(r"\s+", "", match.group("num"))
        if num == "0":
            continue
        body = clean_question_text(match.group("body"))
        marks = int(match.group("marks"))
        if len(body) < 12:
            continue
        if body.upper().startswith(("INSTRUCTIONS", "INFORMATION")):
            continue
        candidates.append({"questionNumber": num, "question": body, "marks": marks})

    if candidates:
        return candidates

    # Fallback for papers where extraction places each question on one line.
    for line in text.splitlines():
        m = re.match(r"^(\d{1,2}(?:\s*\([a-z]\))?)\s+(.+?)\s*\[(\d{1,2})\]$", line.strip())
        if m:
            num = re.sub(r"\s+", "", m.group(1))
            if num == "0":
                continue
            candidates.append({
                "questionNumber": num,
                "question": clean_question_text(m.group(2)),
                "marks": int(m.group(3)),
            })
    return candidates


def extract_subpart_questions(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    candidates = []
    current_case = ""
    current_num = ""
    current_parts = []

    def is_command_start(value):
        low = value.lower()
        return any(low.startswith(word.lower()) for word in COMMAND_WORDS)

    def flush():
        nonlocal current_num, current_parts
        if not current_num or not current_parts:
            current_num = ""
            current_parts = []
            return
        raw = " ".join(current_parts)
        m = re.search(r"\[(\d{1,2})\]\s*$", raw)
        if not m:
            current_num = ""
            current_parts = []
            return
        question = clean_question_text(raw)
        if len(question) >= 12:
            candidates.append({
                "questionNumber": current_num,
                "question": question,
                "marks": int(m.group(1)),
            })
        current_num = ""
        current_parts = []

    for line in lines:
        main = re.match(r"^(\d{1,2})\s+(.+)$", line)
        if main:
            rest = main.group(2).strip()
            if not is_command_start(rest) and not re.match(r"^\([a-z]\)", rest):
                flush()
                current_case = main.group(1)
                continue

        start = re.match(r"^\(([a-d])\)\s*(?:\((i{1,3}|iv|v)\))?\s*(.*)$", line, re.I)
        if start and current_case:
            flush()
            letter = start.group(1).lower()
            roman = start.group(2)
            current_num = f"{current_case}({letter})" + (f"({roman.lower()})" if roman else "")
            current_parts = [start.group(3).strip()]
            continue

        roman_start = re.match(r"^\((i{1,3}|iv|v)\)\s*(.*)$", line, re.I)
        if roman_start and current_case and current_num:
            current_letter = re.search(r"\(([a-d])\)", current_num)
            if current_letter:
                flush()
                current_num = f"{current_case}({current_letter.group(1)})({roman_start.group(1).lower()})"
                current_parts = [roman_start.group(2).strip()]
                continue

        if current_parts:
            current_parts.append(line)

    flush()
    # Avoid treating Paper 1/Paper 3 papers as subpart papers just because of table labels.
    return candidates if len(candidates) >= 4 else []


def classify_topic(question):
    q = question.lower()
    best_topic = "Uncategorised"
    best_score = 0
    for topic, keywords in TOPIC_RULES:
        score = sum(1 for keyword in keywords if keyword in q)
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


def command_word(question):
    q = question.strip().lower()
    for word in COMMAND_WORDS:
        if q.startswith(word.lower()):
            return "Analyse" if word == "Analyze" else word
    return ""


def build_manifest():
    candidates = []
    for year in range(2020, 2026):
        for session_label, folder_name, code in SESSIONS:
            variants = MARCH_VARIANTS if code == "m" else VARIANTS
            for variant in variants:
                paper_num = variant[0]
                qp_url = url_for(folder_name, year, code, "qp", variant)
                candidates.append({
                    "year": str(year),
                    "session": session_label,
                    "sessionCode": f"{code}{str(year)[2:]}",
                    "paper": PAPER_NUMBERS.get(paper_num, f"Paper {paper_num}"),
                    "variant": variant,
                    "qpUrl": qp_url,
                    "msUrl": url_for(folder_name, year, code, "ms", variant),
                    "insertUrl": url_for(folder_name, year, code, "in", variant),
                })

    rows = []
    with ThreadPoolExecutor(max_workers=24) as executor:
        future_to_row = {executor.submit(url_exists, row["qpUrl"]): row for row in candidates}
        for future in as_completed(future_to_row):
            row = future_to_row[future]
            if future.result():
                rows.append(row)
                print(f"found {row['year']} {row['session']} {row['variant']}", flush=True)

    with ThreadPoolExecutor(max_workers=24) as executor:
        checks = {}
        for row in rows:
            checks[executor.submit(url_exists, row["msUrl"])] = (row, "msUrl")
            checks[executor.submit(url_exists, row["insertUrl"])] = (row, "insertUrl")
        for future in as_completed(checks):
            row, key = checks[future]
            if not future.result():
                row[key] = ""

    rows.sort(key=lambda item: (item["year"], item["session"], item["variant"]))
    return rows


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def build_index(manifest):
    questions = []
    for row in manifest:
        local_name = f"9609_{row['sessionCode']}_qp_{row['variant']}.pdf"
        pdf_path = PDF_DIR / local_name
        if not download(row["qpUrl"], pdf_path):
            continue
        try:
            extracted = extract_questions(extract_text(pdf_path))
        except Exception as exc:
            print(f"extract failed: {local_name} ({exc})", file=sys.stderr)
            continue
        for q in extracted:
            topic = classify_topic(q["question"])
            qid = f"9609_{row['sessionCode']}_{row['variant']}_q{q['questionNumber'].lower().replace('(', '').replace(')', '')}"
            questions.append({
                "id": qid,
                "year": row["year"],
                "session": row["session"],
                "paper": row["paper"],
                "variant": row["variant"],
                "questionNumber": q["questionNumber"],
                "marks": q["marks"],
                "topic": topic,
                "commandWord": command_word(q["question"]),
                "question": q["question"],
                "insertUrl": row["insertUrl"],
            })
        print(f"indexed {len(extracted):>2} questions from {local_name}")
    return questions


def inject_questions_into_html(html_path, questions):
    html_text = html_path.read_text(encoding="utf-8")
    payload = json.dumps(questions, ensure_ascii=False, indent=8)
    payload = "\n".join("      " + line if line else line for line in payload.splitlines())
    new_text = re.sub(
        r"      var questions = \[[\s\S]*?\n      \];",
        "      var questions = " + payload.strip() + ";",
        html_text,
        count=1,
    )
    if new_text == html_text:
        raise RuntimeError("Could not replace questions array in HTML")
    html_path.write_text(new_text, encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    manifest_path = OUT_DIR / "business-9609-pdf-list.csv"
    if "--use-existing-manifest" in sys.argv and manifest_path.exists():
        with manifest_path.open(newline="", encoding="utf-8") as f:
            manifest = list(csv.DictReader(f))
    else:
        manifest = build_manifest()
        write_csv(
            manifest_path,
            manifest,
            ["year", "session", "sessionCode", "paper", "variant", "qpUrl", "msUrl", "insertUrl"],
        )
    questions = build_index(manifest)
    questions.sort(key=lambda item: (item["year"], item["session"], item["paper"], item["variant"], item["questionNumber"]))

    (OUT_DIR / "business-9609-question-index.json").write_text(
        json.dumps(questions, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_csv(
        OUT_DIR / "business-9609-question-index.csv",
        questions,
        ["id", "year", "session", "paper", "variant", "questionNumber", "marks", "topic", "commandWord", "question", "insertUrl"],
    )
    inject_questions_into_html(ROOT / "a-level-business-topic-finder-elementor.html", questions)
    print(f"manifest files: {len(manifest)}")
    print(f"indexed questions: {len(questions)}")


if __name__ == "__main__":
    main()
