"""HISTORICAL: already run on 2026-09-30 against the pre-reorganisation layout. Do not re-run."""
"""Reorganize the SJ Academy SEO workspace into numbered folders.

  python3 reorganize.py            preview only (default), nothing moves
  python3 reorganize.py --apply    perform the moves, write move_log.csv

Only moves files and folders (no deletes, no content changes), except for
rewriting hard-coded paths in the handful of active scripts listed in
PATH_FIXES. venv/ stays at the root because moving a virtualenv breaks it.
"""
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

D = "HTML_Tools_and_Drafts"
MOVES = [
    # 00 Start here
    ("SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md", "00_START_HERE/SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md"),

    # 01 Website pages (HTML that goes on sjacademy.pk)
    ("A_Level_Hubs", "01_Website_Pages/Past_Papers/A_Level"),
    ("O_Level_Hubs", "01_Website_Pages/Past_Papers/O_Level"),
    (f"{D}/past-paper-subject-template.html", "01_Website_Pages/Past_Papers/Template/past-paper-subject-template.html"),
    (f"{D}/top_10_tutor_academies_karachi.html", "01_Website_Pages/Blog_Posts/top_10_tutor_academies_karachi.html"),
    (f"{D}/o_level_ultimate_guide_pakistan.html", "01_Website_Pages/Blog_Posts/o_level_ultimate_guide_pakistan.html"),
    (f"{D}/fee_structure.html", "01_Website_Pages/Pages/fee_structure.html"),
    (f"{D}/homepage-preview.html", "01_Website_Pages/Pages/homepage-preview.html"),
    (f"{D}/a_level_math_tuition.html", "01_Website_Pages/Pages/a_level_math_tuition.html"),
    (f"{D}/private_candidate_registration_service.html", "01_Website_Pages/Pages/private_candidate_registration_service.html"),
    (f"{D}/resources_vault.html", "01_Website_Pages/Pages/resources_vault.html"),
    (f"{D}/resources_vault_elementor.html", "01_Website_Pages/Pages/resources_vault_elementor.html"),
    (f"{D}/newsletter-squeeze.html", "01_Website_Pages/Pages/newsletter-squeeze.html"),
    ("landing.html", "01_Website_Pages/Pages/a_level_business_9609_solved_papers_landing_v1.html"),
    ("sjacademy_landing.html", "01_Website_Pages/Pages/a_level_business_9609_solved_papers_landing_v2.html"),
    (f"{D}/terms_and_conditions.html", "01_Website_Pages/Pages/Policies/terms_and_conditions.html"),
    (f"{D}/refund_policy.html", "01_Website_Pages/Pages/Policies/refund_policy.html"),
    (f"{D}/ibcc-calculator.html", "01_Website_Pages/Tools/ibcc-calculator.html"),
    (f"{D}/career_finder_final.html", "01_Website_Pages/Tools/career_finder_final.html"),
    (f"{D}/scholarship_tool.html", "01_Website_Pages/Tools/scholarship_tool.html"),
    (f"{D}/sj_scholarship_tool_snippet.html", "01_Website_Pages/Tools/sj_scholarship_tool_snippet.html"),
    ("IBCC_Calculator", "01_Website_Pages/Tools/IBCC_Calculator_Widget"),
    ("New_Pages", "01_Website_Pages/New_Pages_Drafts"),

    # 02 Reports and audits, newest context first
    ("SEO_Fixes_2026_09_30", "02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit"),
    ("SEO_Comprehensive_Progress_Report.md", "02_Reports_and_Audits/2026-09-22_Progress_Report/SEO_Comprehensive_Progress_Report.md"),
    ("START_HERE_SJ_ACADEMY_SEO_HANDOFF.md", "02_Reports_and_Audits/2026-09-11_Handoff/START_HERE_SJ_ACADEMY_SEO_HANDOFF.md"),
    ("SEO_Deep_Dive_2026_09_11", "02_Reports_and_Audits/2026-09-11_Growth_Diagnosis"),
    ("IBCC_Audit_2026_09_11", "02_Reports_and_Audits/2026-09-11_IBCC_Calculator_Audit"),
    ("SEO_Audit_2026_09_10", "02_Reports_and_Audits/2026-09-10_Full_Site_Audit"),
    ("SEO_Docs/Archive_Past_Audits", "02_Reports_and_Audits/Older_Audits_Before_Sept_2026"),

    # 03 Plans, content drafts and metadata
    ("SEO_Docs/Yoast_Metadata_Changes_2026_09_30.csv", "03_Plans_and_Content/Metadata/Yoast_Metadata_Changes_2026_09_30.csv"),
    ("SEO_Docs/seo_domination_plan.md", "03_Plans_and_Content/Old_Plans_Outdated/seo_domination_plan.md"),
    ("SEO_Docs/SJ_Academy_Master_SEO_Progress_Report.md", "03_Plans_and_Content/Old_Plans_Outdated/SJ_Academy_Master_SEO_Progress_Report.md"),
    ("SEO_Docs/blog_a_level_subject_combinations_geo.md", "03_Plans_and_Content/Blog_Drafts/blog_a_level_subject_combinations_geo.md"),
    ("SEO_Docs/blog_ai_citation_guide_2026.md", "03_Plans_and_Content/Blog_Drafts/blog_ai_citation_guide_2026.md"),
    ("SEO_Docs/blog_best_academies_karachi.md", "03_Plans_and_Content/Blog_Drafts/blog_best_academies_karachi.md"),
    ("SEO_Docs/blog_caie_retake_2026.md", "03_Plans_and_Content/Blog_Drafts/blog_caie_retake_2026.md"),
    ("SEO_Docs/top_10_tutor_academies_karachi.md", "03_Plans_and_Content/Blog_Drafts/top_10_tutor_academies_karachi.md"),

    # 04 Data
    ("Data_Vault/Search console", "04_Data/Search_Console_and_GA4_Exports/2026-09_Export"),
    ("https___www.sjacademy.pk_-Performance-on-Search-2026-09-11.zip", "04_Data/Search_Console_and_GA4_Exports/GSC_Performance_2026-09-11.zip"),
    ("Data_Vault/Scholarship_Data", "04_Data/Scholarship_Data"),
    ("Data_Vault/caie_resources_database.csv", "04_Data/Resources_Database/caie_resources_database.csv"),
    ("Data_Vault/resources_with_images.json", "04_Data/Resources_Database/resources_with_images.json"),
    ("Data_Vault/SJ_Academy_SEO_Tracker.csv", "04_Data/SJ_Academy_SEO_Tracker.csv"),

    # 05 Scripts
    ("Python_Scripts/analyze_seo.py", "05_Scripts/Analysis/analyze_seo.py"),
    ("Python_Scripts/deep_analysis.py", "05_Scripts/Analysis/deep_analysis.py"),
    ("Python_Scripts/deep_ga4_analysis.py", "05_Scripts/Analysis/deep_ga4_analysis.py"),
    ("Python_Scripts/seo_analyzer.py", "05_Scripts/Analysis/seo_analyzer.py"),
    ("find_sources.py", "05_Scripts/Analysis/find_sources.py"),
    ("summarize_audit.py", "05_Scripts/Analysis/summarize_audit.py"),
    ("get_subject_queries.py", "05_Scripts/Analysis/get_subject_queries.py"),
    ("ocr.py", "05_Scripts/Analysis/ocr.py"),
    ("Python_Scripts/Archive_One_Off_Scripts", "05_Scripts/Archive_One_Off_Scripts"),

    # 99 Archive
    ("hub_html_backups", "99_Archive/Old_Hub_Backups_Aug_2026"),
]

# Folders emptied by the moves (removed only if empty apart from .DS_Store).
EMPTIED = ["HTML_Tools_and_Drafts", "SEO_Docs", "Data_Vault", "Python_Scripts"]

# Relative paths inside active scripts that must follow the move.
PATH_FIXES = {
    "05_Scripts/Analysis/find_sources.py": [
        ("'SEO_Audit_2026_09_10/evidence/", "'02_Reports_and_Audits/2026-09-10_Full_Site_Audit/evidence/")],
    "05_Scripts/Analysis/summarize_audit.py": [
        ("'SEO_Audit_2026_09_10/evidence/", "'02_Reports_and_Audits/2026-09-10_Full_Site_Audit/evidence/")],
    "05_Scripts/Analysis/get_subject_queries.py": [
        ("'Data_Vault/Search console/", "'04_Data/Search_Console_and_GA4_Exports/2026-09_Export/")],
}


def main(apply: bool) -> int:
    problems = []
    for src, dst in MOVES:
        if not (ROOT / src).exists():
            problems.append(f"missing source: {src}")
        if (ROOT / dst).exists():
            problems.append(f"destination exists: {dst}")
    if problems:
        print("\n".join(problems))
        return 1

    for src, dst in MOVES:
        print(f"{'MOVE' if apply else 'would move'}  {src}  ->  {dst}")
    if not apply:
        return 0

    log = []
    for src, dst in MOVES:
        target = ROOT / dst
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(ROOT / src), str(target))
        log.append((src, dst))

    for rel, fixes in PATH_FIXES.items():
        p = ROOT / rel
        text = p.read_text()
        for old, new in fixes:
            text = text.replace(old, new)
        p.write_text(text)

    for d in EMPTIED:
        p = ROOT / d
        leftovers = [f for f in p.rglob("*") if f.is_file() and f.name != ".DS_Store"]
        if leftovers:
            print(f"kept {d}/ (not empty): {[str(f.relative_to(ROOT)) for f in leftovers]}")
        else:
            shutil.rmtree(p)

    with open(ROOT / "00_START_HERE" / "move_log_2026-09-30.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["old_path", "new_path"])
        w.writerows(log)
    print(f"done: {len(log)} moves, log in 00_START_HERE/move_log_2026-09-30.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
