from pathlib import Path
p=Path(__file__).parent
s=(p/'original.html').read_text()
css='''
/* Limited accessibility and mobile patch. Calculation engine still awaits replacement. */
#sj-ibcc-widget, #sj-ibcc-widget * { box-sizing: border-box; }
#sj-ibcc-widget { --orange-dark: #a83c00; --border-color: #767676; }
#sj-ibcc-widget[data-theme="dark"] { --orange-dark: #ffab75; --select-bg: #111822; --border-color: #8493a7; }
#sj-ibcc-widget .header-controls { grid-template-columns: minmax(0,1fr) auto !important; gap: 12px; }
#sj-ibcc-widget .header-spacer { display: none !important; }
#sj-ibcc-widget .mode-badge-wrap { margin-bottom: 0 !important; }
#sj-ibcc-widget .theme-switch-wrapper { flex-wrap: wrap; justify-content: flex-end; }
#sj-ibcc-widget .theme-switch { width: 44px !important; height: 44px !important; }
#sj-ibcc-widget .slider { top: 12px !important; bottom: 12px !important; }
#sj-ibcc-widget .theme-switch input:checked + .slider:before { transform: translateX(24px) !important; }
#sj-ibcc-widget .type-toggle input { display: block !important; position: absolute; width: 1px; height: 1px; opacity: 0; }
#sj-ibcc-widget :is(select,a,input):focus-visible { outline: 3px solid var(--text-main) !important; outline-offset: 3px !important; }
#sj-ibcc-widget .type-toggle input:focus-visible + label,
#sj-ibcc-widget .theme-switch input:focus-visible + .slider { outline: 3px solid var(--text-main); outline-offset: 3px; }
#sj-ibcc-widget .subject-row { gap: 12px; }
#sj-ibcc-widget .subject-row label { font-size: 14px !important; text-transform: none !important; letter-spacing: 0 !important; flex: 1; }
#sj-ibcc-widget select { font-size: 16px !important; min-height: 44px; flex-shrink: 0; }
#sj-ibcc-widget .grade-section p.helper, #sj-ibcc-widget .disclaimer { font-size: 14px !important; line-height: 1.6 !important; }
#sj-ibcc-widget .btn-cta { color: #000 !important; }
#sj-ibcc-widget .review-warning { border: 2px solid var(--border-heavy); border-radius: 8px; padding: 16px; margin-bottom: 20px; font-size: 14px; }
#sj-ibcc-widget .review-warning a { color: inherit; text-decoration: underline; }
#sj-ibcc-widget .results-panel { display: none !important; }
@media(max-width: 480px) {
 #sj-ibcc-widget { padding: 20px 12px; }
 #sj-ibcc-widget .header-controls { grid-template-columns: 1fr !important; }
 #sj-ibcc-widget .theme-switch-wrapper { justify-self: center !important; }
 #sj-ibcc-widget .subject-row { flex-direction: column !important; align-items: stretch !important; }
 #sj-ibcc-widget select { width: 100% !important; }
 #sj-ibcc-widget .calc-wrapper { padding: 16px !important; }
}
@media(prefers-reduced-motion: reduce) { #sj-ibcc-widget * { transition: none !important; } }
'''
s=s.replace('</style>',css+'\n</style>')
s=s.replace('<div class="calc-wrapper">','''<div class="review-warning"><strong>UI review preview. Not for publication.</strong><br>Results are disabled while the calculation rules are rebuilt and verified. <a href="https://ibcc.edu.pk/conversion-for-equivalence/">View official IBCC conversion data</a>.</div>
    <div class="calc-wrapper">''')
s=s.replace('Enter your O and A-Level grades to calculate your estimated IBCC equivalence based on official post-2021 guidelines.','Estimate your O Level or A Level equivalence. Final equivalence is issued by IBCC.')
s=s.replace('id="theme-checkbox" onchange','id="theme-checkbox" aria-label="Dark mode" onchange')
s=s.replace('Worried about a low equivalence?','Planning your next exam attempt?')
s=s.replace("Don't let a bad grade ruin your university merit formula. Master the exact CAIE marking scheme with Karachi's elite faculty. Join hundreds of SJ Academy students who secured straight A*s last year.", 'Get exam-focused O and A Level support at SJ Academy, with physical classes in DHA Phase 7, Karachi, and live online classes.')
s=s.replace('function createDropdown() {','function createDropdown(id) {')
s=s.replace('<select class="grade-select"', '<select id="${id}" class="grade-select"')
s=s.replace('div.innerHTML = `<label>${label}</label>${createDropdown()}`;', 'const id = `${container.id}-${container.children.length}`;\n            div.innerHTML = `<label for="${id}">${label}</label>${createDropdown(id)}`;')
# Preserve grades through route/level toggles, including temporarily hidden fields.
s=s.replace('function buildInterface() {','const savedGrades = new Map();\n        function buildInterface() {\n            document.querySelectorAll("#sj-ibcc-widget .subject-row").forEach(row => savedGrades.set(row.querySelector("label").textContent, row.querySelector("select").value));')
s=s.replace('            calculateEquivalence();\n        }','            document.querySelectorAll("#sj-ibcc-widget .subject-row").forEach(row => {\n                row.querySelector("select").value = savedGrades.get(row.querySelector("label").textContent) || "None";\n            });\n            calculateEquivalence();\n        }',1)
s=s.replace('// UPDATED IBCC MATH (Post-2021 Rule: A* = 100)', '// LEGACY ENGINE: incorrect and retained only for comparison; results disabled in this UI preview.')
s=s.replace('${grade} (${value})', '${grade}')
(p/'ui-review-preview.html').write_text(s)
(p/'mobile-accessibility-patch.css').write_text(css)
