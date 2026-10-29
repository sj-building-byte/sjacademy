# Folder Guide: SJ Academy SEO Workspace

Reorganised 30 September 2026. Nothing was deleted. Every move is listed in `move_log_2026-09-30.csv`.

## Start here

**`SJ_ACADEMY_SEO_MASTER_CONTEXT_2026_09_30.md`**: the complete, latest context (business, data, findings, changes, decisions, backlog). Upload this to Claude Chat or give it to any new session first.

## What's where

| Folder | What it holds | Go here when you want to... |
|---|---|---|
| `00_START_HERE/` | Master context file, this guide, move log | Get up to speed or brief someone |
| `01_Website_Pages/` | HTML that goes on sjacademy.pk (Elementor widgets and drafts) | Edit or paste a page |
| `02_Reports_and_Audits/` | Every audit and report, in dated folders | Check what was found, when, and the evidence |
| `03_Plans_and_Content/` | Blog plan + calendar, Instagram playbook + calendar, Yoast metadata sheet, blog drafts, old plans | Write content or update titles and descriptions |
| `04_Data/` | Search Console / GA4 exports, Instagram post export (`Instagram/`), scholarship data, resources database, SEO tracker | Look at raw numbers |
| `05_Scripts/` | Python analysis scripts | Re-run an analysis |
| `99_Archive/` | Old backups you won't normally need | Recover an old version |
| `venv/` | Python environment (leave at the root; moving it breaks it) | (nothing) |

### 01_Website_Pages in detail

| Subfolder | Files | Live URL |
|---|---|---|
| `Past_Papers/A_Level/` | 13 subject hubs + `main_a_level_directory.html` | /a-level-past-papers/[subject-code]/, /a-level-past-papers/ |
| `Past_Papers/O_Level/` | 12 subject hubs + `main_o_level_directory.html` | /o-level-past-papers/[subject-code]/, /o-level-past-papers/ |
| `Past_Papers/Template/` | Blank hub template | (none) |
| `Pages/` | `fee_structure.html` | /fee-structure/ |
| | `homepage-preview.html` | Draft only, not the live homepage |
| | `a_level_math_tuition.html` | A Level Maths tuition page draft |
| | `a_level_business_9609_solved_papers_landing_v1.html` / `_v2.html` | /a-level-business-9609-solved-past-papers-2025/ (v2 is newer, 25 Sep) |
| | `resources_vault.html`, `resources_vault_elementor.html` | Resources vault (/resources/ currently returns 404) |
| | `private_candidate_registration_service.html` | Draft (/private-candidate-registration/ currently returns 404) |
| | `newsletter-squeeze.html` | Newsletter signup page |
| | `Policies/terms_and_conditions.html`, `Policies/refund_policy.html` | Policy pages |
| `Blog_Posts/` | `top_10_tutor_academies_karachi.html` | /blog/the-best-tutor-academy-in-karachi/ (post ID 6716) |
| | `o_level_ultimate_guide_pakistan.html` | O Level guide draft |
| `Tools/` | `ibcc-calculator.html` | IBCC calculator (see the accuracy warning in the IBCC audit) |
| | `career_finder_final.html` | /a-level-subject-combinations-tool/ |
| | `scholarship_tool.html`, `sj_scholarship_tool_snippet.html` | Scholarship checker |
| | `IBCC_Calculator_Widget/` | Calculator engine, widget and official IBCC source PDFs |
| `New_Pages_Drafts/` | `o_a_level_class_equivalence_answer_block.html` | Goes at the top of /blog/o-levels-and-a-levels-in-pakistan/ (ready) |
| | `a_level_grade_thresholds.html` | Proposed /a-level-grade-thresholds/ (needs official Cambridge figures first) |

### 02_Reports_and_Audits (newest first)

| Folder | Main file |
|---|---|
| `2026-09-30_Instagram_Analysis/` | `Instagram_Analysis_2026-09-30.md` |
| `2026-09-30_Fixes_and_Reaudit/` | `CHANGE_SUMMARY.md` (+ `backup_originals/`, `staged/`, `scripts/`) |
| `2026-09-22_Progress_Report/` | `SEO_Comprehensive_Progress_Report.md` |
| `2026-09-11_Handoff/` | `START_HERE_SJ_ACADEMY_SEO_HANDOFF.md` (deep audit narrative) |
| `2026-09-11_Growth_Diagnosis/` | `SJ_Academy_SEO_Growth_Diagnosis.md` |
| `2026-09-11_IBCC_Calculator_Audit/` | `AUDIT.md` |
| `2026-09-10_Full_Site_Audit/` | `SJ_Academy_SEO_Director_Report.md`, `page_inventory.csv`, `broken_links.csv`, `evidence/`, PDF in `output/pdf/` |
| `Older_Audits_Before_Sept_2026/` | Earlier audits |

## Old paths in older documents

The 11 Sep and 22 Sep documents mention the old folder names. Quick translation:

| Old | New |
|---|---|
| `A_Level_Hubs/`, `O_Level_Hubs/` | `01_Website_Pages/Past_Papers/A_Level/`, `O_Level/` |
| `HTML_Tools_and_Drafts/` | Split across `01_Website_Pages/Pages/`, `Blog_Posts/`, `Tools/` |
| `New_Pages/` | `01_Website_Pages/New_Pages_Drafts/` |
| `IBCC_Calculator/` | `01_Website_Pages/Tools/IBCC_Calculator_Widget/` |
| `SEO_Audit_2026_09_10/` | `02_Reports_and_Audits/2026-09-10_Full_Site_Audit/` |
| `SEO_Deep_Dive_2026_09_11/` | `02_Reports_and_Audits/2026-09-11_Growth_Diagnosis/` |
| `IBCC_Audit_2026_09_11/` | `02_Reports_and_Audits/2026-09-11_IBCC_Calculator_Audit/` |
| `SEO_Fixes_2026_09_30/` | `02_Reports_and_Audits/2026-09-30_Fixes_and_Reaudit/` |
| `SEO_Docs/` | Split across `03_Plans_and_Content/` and `02_Reports_and_Audits/Older_Audits_Before_Sept_2026/` |
| `Data_Vault/` | `04_Data/` |
| `Python_Scripts/` and root `.py` files | `05_Scripts/` |
| `hub_html_backups/` | `99_Archive/Old_Hub_Backups_Aug_2026/` |
| `landing.html`, `sjacademy_landing.html` | `01_Website_Pages/Pages/a_level_business_9609_solved_papers_landing_v1.html`, `_v2.html` |

## Keeping it tidy

- New page drafts go in `01_Website_Pages/` (in the matching subfolder).
- Each new audit or fix round gets a dated folder in `02_Reports_and_Audits/` (`YYYY-MM-DD_Name`).
- New data exports go in `04_Data/` (Search Console/GA4 or Instagram subfolder) with the export date in the name.
- Update the master context file after each significant round of work.
