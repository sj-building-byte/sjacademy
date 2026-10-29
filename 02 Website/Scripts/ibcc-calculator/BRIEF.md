# IBCC Equivalence Calculator v2.0: accuracy check

Page: /ibcc-equivalence-calculator/. Widget: `02 Website/Pages/ibcc-calculator-elementor-widget.html`. Rebuild with `python3 build.py`.

## Accuracy check (20 October 2026)
- A* values: `ref_check.py` reads IBCC's own A* PDFs (text in `sources/`, 2021 to 2026, O and A Level) and compares 120 values with `engine.js`. All match.
- Second solve: a separate Python version of the rules, written from the sources, gives the same marks as the engine on 5,000 random students (every route, group, year mix, letter and 9 to 1 grades). 0 differences.
- Worked examples reproduced exactly: IBCC O Level 844/900 and 846/900, IBCC A Level 1030/1100 and 1031/1100, Cambridge brochure 629/800 (708/900), plus the 11 Sep audit fixtures.
- Edge cases (`node edge.test.js`, 17 tests): blank or failed grades never give a result, duplicates rejected, 2006-2020 A* = 90, forecasts for 2027 and 2028, Humanities stays on the old rule, mixed Pakistan/abroad counts Urdu, Islamiyat and Pak Studies.
- UI (`test.py`, Playwright): three full flows at 320, 375 and 1280 px, no sideways scroll, no script errors, state restored after reload.

## Decisions (Sunyyan, 20 Oct 2026)
- O Level (SSC) shown out of 900. IBCC's April 2026 example labels 1100 but its numbers are worked on 900.
- 2027 and 2028 use 2026 A* values, labelled forecast. Swap in the real table when IBCC publishes it (edit ASTAR in engine.js, add the PDF text to sources/, rerun ref_check.py).
- IGCSE 9 to 1 and 2006 to 2020 sessions supported. Pre-2006 not supported.

## Rules that are our reading of IBCC (flagged in the tool)
- February 2026 rule applies when the latest O Level session is 2026 or later, science groups only.
- Marks under the February 2026 rule are scaled to 1100 like IBCC's overseas example (no official example yet).
- Grade 9 uses the subject A* value.
