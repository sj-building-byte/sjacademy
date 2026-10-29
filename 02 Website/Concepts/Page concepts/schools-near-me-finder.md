# 09 - Karachi "Schools Near Me" Directory & Finder

> **Type:** Local Directory / Programmatic SEO Geo-Tool / High-Converting Lead Magnet  
> **Brand / Project:** SJ Academy (`sjacademy.pk/schools-near-me/` or local landing page)  
> **Target Audience:** Parents and students in Karachi searching for local Cambridge, IB, Edexcel, Aga Khan, and Matric schools by neighborhood/area.

---

## 1. Overview & SEO Architecture

The **Schools Near Me Finder** is a geo-targeted directory tool for discovering and evaluating schools across Karachi neighborhoods (DHA, Clifton, Gulshan-e-Iqbal, PECHS, North Nazimabad, etc.).

### Strategic Capabilities:
1. **Live Google Sheets Directory Backend:** Streams real-time school records directly from a published Google Sheet CSV feed using PapaParse.
2. **Programmatic URL & Dynamic Metadata Sync:** As users select an area or board, the URL (`?area=DHA&board=Cambridge`) and Page Title/H1 update dynamically in real time for maximum SEO shareability and UX continuity:
   - *H1:* `Find Schools Near You in [DHA]`
   - *Title:* `Find Cambridge Schools Near You in DHA - SJ Academy`
3. **Google Maps Search API Integration:** Every school card generates a direct 1-click navigation link into Google Maps:
   ```
   https://www.google.com/maps/search/?api=1&query=[School+Name]+[Address]+Karachi
   ```
4. **In-Feed Native Conversion Card (Injected at Position 3 / Index 2):** Captures high-intent parent/student search traffic with an in-feed promo for SJ Academy's O/A Level tuition with faculty from IBA, LUMS, and KGS.
5. **Multi-Board Normalization:** Intelligently maps board variations across Cambridge (O/A Level), IB, Edexcel, Aga Khan Board, and Matric.

---

## 2. Design Tokens & Styling System

Scoped inside container `#sj-school-finder`.

| Token | Hex / Value | Purpose |
| :--- | :--- | :--- |
| `--sja-yellow` | `#FCE004` | H1 highlight, mode badge, school tags border, map button |
| `--sja-light-yellow` | `#FFF9CC` | School tag background, in-feed conversion card background |
| `--sja-brown` | `#453516` | Card top accent border, map button border, outline button font |
| `--sja-orange` | `#FE6100` | Primary action button, ad card header & CTA, focus ring |
| `--sja-whatsapp` | `#25D366` | WhatsApp brand accent |
| `--sja-black` | `#000000` | Headings, titles, high-contrast borders |
| `--sja-dark-grey` | `#222222` | Subtitles, ad card body copy |
| `--sja-grey` | `#555555` | Field labels, sector subtitle, school count |
| `--sja-light-bg` | `#FAFAFA` | Filter controls full-width background |
| `--sja-white` | `#FFFFFF` | Card surfaces, inputs, body contrast |

---

## 3. Component Hierarchy

```
#sj-school-finder (Data Source: Google Sheets CSV)
├── .wrap > .sja-header
│   ├── .sja-badge ("Schools Near Me" Finder)
│   ├── H1 ("Find Schools Near You in [Area]")
│   └── Subtitle
│
├── .sja-controls (Full-Width Background Band)
│   └── .wrap > .sja-controls-grid
│       ├── Area Select (<select id="sj-area"> populated dynamically from CSV)
│       ├── Board Select (<select id="sj-board"> Cambridge / IB / Edexcel / AKU / Matric)
│       ├── Sector Select (<select id="sj-sector"> Private / Government)
│       └── .sja-toolbar (Counter: "X schools found" + "Clear Filters" button)
│
└── .wrap
    ├── #sj-results (.sja-output > #sj-grid)
    │   ├── .sja-card (School Name, Sector, Badges, Phone, Address, Map Link, Review Link)
    │   └── .sja-card [Position 3 In-Feed Ad] ("Need A*s in Cambridge?" Demo Class CTA)
    │
    └── #sj-more-wrap ("Show More Results" Pagination Button)
```

---

## 4. In-Feed Conversion Card Copy (Position 3)

- **Headline:** *"Need A\*s in Cambridge?"*
- **Social Proof:** `⭐⭐⭐⭐⭐ 220+ 5-Star Google Reviews`
- **Body Copy:** *"Don't rely solely on school teachers to beat the CAIE curve. Get coached by Karachi's elite faculty from **IBA, LUMS, and KGS**."*
- **Badge:** `📍 Physical Campus (DHA) | 💻 Premium Live Online`
- **Button CTA:** `BOOK A FREE DEMO CLASS`  
  *(Target URL: `https://sjacademy.pk/o-a-level-classes/?utm_source=school_finder_tool&utm_medium=internal_ad_card&utm_campaign=oa_level_leads`)*

---

## 5. Complete Source Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SJ Academy - Schools Near Me Finder</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        /* ===== SJ ACADEMY BRANDING VARIABLES ===== */
        #sj-school-finder {
            --sja-yellow: #FCE004;
            --sja-brown: #453516;
            --sja-black: #000000;
            --sja-orange: #FE6100;
            --sja-white: #ffffff;
            --sja-whatsapp: #25D366;
            --sja-grey: #555;
            --sja-dark-grey: #222;
            --sja-light-bg: #fafafa;
            --sja-light-yellow: #FFF9CC;
            font-family: 'Poppins', sans-serif;
            color: var(--sja-black);
            line-height: 1.6;
            background-color: var(--sja-white);
            width: 100%;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
        }

        #sj-school-finder *, #sj-school-finder *::before, #sj-school-finder *::after {
            box-sizing: border-box;
        }

        #sj-school-finder .wrap {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* ===== HEADER ===== */
        #sj-school-finder .sja-header {
            background: #fff;
            padding: 40px 0 30px;
            text-align: center;
        }

        #sj-school-finder .sja-badge {
            display: inline-block;
            background-color: #fff;
            border: 2px solid var(--sja-black);
            border-radius: 50px;
            padding: 4px;
            margin-bottom: 20px;
            box-shadow: 3px 3px 0px rgba(0,0,0,0.15);
        }

        #sj-school-finder .sja-mode-pill {
            padding: 6px 16px;
            border-radius: 40px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            line-height: 1;
            background-color: var(--sja-yellow);
            color: var(--sja-black);
        }

        #sj-school-finder .sja-title {
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--sja-black);
            margin: 0 0 15px 0;
            line-height: 1.2;
        }

        #sj-school-finder .sja-subtitle {
            font-size: 1rem;
            color: var(--sja-dark-grey);
            margin: 0 auto 25px;
            max-width: 700px;
        }

        #sj-school-finder .sja-highlight {
            background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%);
            background-repeat: no-repeat;
            background-size: 100% 35%;
            background-position: 0 85%;
            display: inline;
            padding: 0 3px;
        }

        /* ===== CONTROLS SECTION ===== */
        #sj-school-finder .sja-controls {
            background: var(--sja-light-bg);
            padding: 40px 0;
            border-top: 1px solid #eee;
            border-bottom: 1px solid #eee;
            width: 100%;
        }

        #sj-school-finder .sja-controls-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }

        #sj-school-finder .sja-field label {
            display: block;
            font-weight: 700;
            font-size: 12px;
            color: var(--sja-black);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        #sj-school-finder .select {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e5e5e5;
            background: var(--sja-white);
            font-size: 16px; 
            font-weight: 500;
            color: var(--sja-black);
            border-radius: 8px;
            outline: none;
            transition: all 0.2s ease;
            appearance: none;
            -webkit-appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='%23000000' viewBox='0 0 16 16'%3E%3Cpath d='M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 15px center;
            background-size: 12px;
            font-family: 'Poppins', sans-serif;
        }

        #sj-school-finder .select:focus {
            border-color: var(--sja-orange);
            box-shadow: 0 0 0 4px rgba(254,97,0,0.1);
        }

        /* ===== TOOLBAR ===== */
        #sj-school-finder .sja-toolbar {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 10px;
        }

        #sj-school-finder .sja-count {
            font-size: 14px;
            font-weight: 600;
            color: var(--sja-grey);
            padding: 12px;
            background: #fff;
            border-radius: 8px;
            border: 1px solid #eee;
            text-align: center;
            width: 100%;
        }

        #sj-school-finder .sja-btn {
            width: 100%;
            padding: 14px 24px;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            border-radius: 8px;
            border: 2px solid transparent;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            display: inline-block;
            text-decoration: none;
        }

        #sj-school-finder .sja-btn-primary {
            background-color: var(--sja-orange);
            color: var(--sja-white);
            box-shadow: 0 4px 12px rgba(254,97,0,0.2);
        }

        #sj-school-finder .sja-btn-outline {
            background-color: var(--sja-white);
            color: var(--sja-brown);
            border-color: var(--sja-brown);
        }

        /* ===== OUTPUT SECTION ===== */
        #sj-school-finder .sja-output {
            padding: 40px 0;
            background: #fff;
        }

        #sj-school-finder .sja-output-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }

        /* ===== CARDS ===== */
        #sj-school-finder .sja-card {
            background: #fff;
            padding: 24px;
            border-top: 5px solid var(--sja-brown);
            box-shadow: 0 8px 20px rgba(0,0,0,0.06);
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            height: 100%;
            transition: transform 0.2s ease;
        }

        #sj-school-finder .sja-card:active {
            transform: scale(0.98);
        }

        #sj-school-finder .sja-card h3 {
            font-size: 1.3rem;
            margin: 0 0 6px 0;
            font-weight: 700;
        }

        #sj-school-finder .sector-line {
            font-size: 12px;
            font-weight: 700;
            color: var(--sja-grey);
            margin-bottom: 15px;
            text-transform: uppercase;
        }

        #sj-school-finder .sja-badges {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }

        #sj-school-finder .sja-tag {
            background: var(--sja-light-yellow);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid var(--sja-yellow);
        }

        #sj-school-finder .sja-kv {
            margin-bottom: 20px;
            flex-grow: 1;
        }

        #sj-school-finder .sja-kv .row {
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #f5f5f5;
        }

        #sj-school-finder .sja-kv .k {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            color: #888;
            margin-bottom: 4px;
        }

        #sj-school-finder .sja-kv .v {
            font-size: 14px;
            font-weight: 500;
            color: #333;
        }

        #sj-school-finder .sja-mapbtn {
            background: var(--sja-yellow);
            color: var(--sja-brown);
            text-align: center;
            padding: 12px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            border: 2px solid var(--sja-brown);
            margin-bottom: 15px;
        }

        #sj-school-finder .sja-meta {
            font-size: 12px;
            text-align: center;
            border-top: 1px solid #eee;
            padding-top: 15px;
        }

        #sj-school-finder .sja-meta a {
            color: var(--sja-orange);
            font-weight: 700;
            text-decoration: none;
        }

        @media(min-width: 768px) {
            #sj-school-finder .sja-header { padding: 60px 0 40px; }
            #sj-school-finder .sja-title { font-size: 3rem; }
            #sj-school-finder .sja-controls-grid { 
                grid-template-columns: repeat(3, 1fr); 
                align-items: end;
            }
            #sj-school-finder .sja-toolbar {
                grid-column: span 3;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
            #sj-school-finder .sja-count { width: auto; min-width: 200px; }
            #sj-school-finder .sja-btn { width: auto; }
            #sj-school-finder .sja-output-grid { grid-template-columns: repeat(2, 1fr); gap: 30px; }
        }

        @media(min-width: 1024px) {
            #sj-school-finder .sja-output-grid { grid-template-columns: repeat(3, 1fr); }
            #sj-school-finder .sja-title { font-size: 3.8rem; }
        }

        #sj-school-finder .sja-more-wrap {
            display: flex;
            justify-content: center;
            padding-bottom: 60px;
        }
        
        .loading-overlay {
            text-align: center;
            padding: 40px;
            color: var(--sja-grey);
            font-weight: 600;
        }
    </style>
</head>
<body>

<div id="sj-school-finder" data-csv="https://docs.google.com/spreadsheets/d/1JeL1ixggGTh60pFQAk8KgnKNTDLh1DZxBi66Tl_D2L8/export?format=csv&gid=0">
    
    <div class="wrap">
        <div class="sja-header">
            <div class="sja-badge">
                <div class="sja-mode-pill">
                    <span>"Schools Near Me" Finder</span>
                </div>
            </div>
            <h1 class="sja-title">Find Schools Near You in <span class="sja-highlight">Karachi</span></h1>
            <p class="sja-subtitle">Filter by area, board, or sector to find the nearest schools to you in seconds.</p>
        </div>
    </div>

    <div class="sja-controls">
        <div class="wrap">
            <div class="sja-controls-grid">
                <div class="sja-field">
                    <label for="sj-area">Select Area</label>
                    <select id="sj-area" class="select">
                        <option value="">All Areas</option>
                    </select>
                </div>
                <div class="sja-field">
                    <label for="sj-board">Select Board</label>
                    <select id="sj-board" class="select">
                        <option value="">All Boards</option>
                        <option>Cambridge</option>
                        <option>Cambridge (O Level)</option>
                        <option>Cambridge (A Level)</option>
                        <option>IB</option>
                        <option>Matric</option>
                        <option>Edexcel</option>
                        <option>Aga Khan Board</option>
                    </select>
                </div>
                <div class="sja-field">
                    <label for="sj-sector">Select Sector</label>
                    <select id="sj-sector" class="select">
                        <option value="">All Sectors</option>
                        <option>Private</option>
                        <option>Government</option>
                    </select>
                </div>

                <div class="sja-toolbar">
                    <div class="sja-count"><span id="sj-count">0</span> schools found</div>
                    <button id="sj-reset" class="sja-btn sja-btn-outline" type="button">Clear Filters</button>
                </div>
            </div>
        </div>
    </div>

    <div class="wrap">
        <div id="sj-results" class="sja-output">
            <div class="sja-output-grid" id="sj-grid">
                <div class="loading-overlay">Loading schools data...</div>
            </div>
        </div>
        
        <div class="sja-more-wrap" id="sj-more-wrap" style="display:none">
            <button id="sj-more" class="sja-btn sja-btn-outline" type="button">Show More Results</button>
        </div>
    </div>
</div>

<script src="https://unpkg.com/papaparse@5.4.1/papaparse.min.js" crossorigin></script>
<script>
(function(){
    const root = document.getElementById('sj-school-finder');
    const csvUrl = root.getAttribute('data-csv') || '';

    const els = {
        area:     document.getElementById('sj-area'),
        board:    document.getElementById('sj-board'),
        sector:   document.getElementById('sj-sector'),
        grid:     document.getElementById('sj-grid'),
        count:    document.getElementById('sj-count'),
        reset:    document.getElementById('sj-reset'),
        moreWrap: document.getElementById('sj-more-wrap'),
        moreBtn:  document.getElementById('sj-more'),
        h1Highlight: document.querySelector('.sja-highlight') 
    };

    let DATA = [];
    let expanded = false;
    const DEFAULT_LIMIT = 12;
    const FILTER_LIMIT  = 18;

    function esc(s){
        return String(s||'').replace(/[&<>"']/g, function(m){
            return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m];
        });
    }

    function normalizeBoard(s){
        if(!s) return '';
        var t = s.toLowerCase();
        if(t.includes('ib')) return 'IB';
        if(t.includes('edexcel')) return 'Edexcel';
        if(t.includes('aga khan')) return 'Aga Khan Board';
        if(t.includes('matric')) return 'Matric';
        if(t.includes('cambridge')){
            if(t.includes('o level')) return 'Cambridge (O Level)';
            if(t.includes('a level')) return 'Cambridge (A Level)';
            return 'Cambridge';
        }
        return s;
    }

    function mapsHref(name, addr){
        return 'https://www.google.com/maps/search/?api=1&query=' 
            + encodeURIComponent((name||'') + ' ' + (addr||' Karachi'));
    }

    function filtersApplied(){
        return !!(els.area.value || els.board.value || els.sector.value);
    }

    function currentLimit(){
        if(expanded) return Infinity;
        return filtersApplied() ? FILTER_LIMIT : DEFAULT_LIMIT;
    }

    function populateAreas(){
        var areas = [];
        DATA.forEach(function(r){
            var a = (r.Area || '').trim();
            if(a && areas.indexOf(a) === -1) areas.push(a);
        });
        areas.sort();
        
        els.area.innerHTML = '<option value="">All Areas</option>';
        areas.forEach(function(a){
            var opt = document.createElement('option');
            opt.value = a;
            opt.textContent = a;
            els.area.appendChild(opt);
        });
    }

    function syncFromUrl() {
        const params = new URLSearchParams(window.location.search);
        const areaParam = params.get('area');
        const boardParam = params.get('board');
        const sectorParam = params.get('sector');

        if(areaParam) els.area.value = areaParam;
        if(boardParam) els.board.value = boardParam;
        if(sectorParam) els.sector.value = sectorParam;
    }

    function updateUrlAndSEO() {
        const a = els.area.value;
        const b = els.board.value;
        const s = els.sector.value;

        const params = new URLSearchParams();
        if(a) params.set('area', a);
        if(b) params.set('board', b);
        if(s) params.set('sector', s);

        const newUrl = window.location.pathname + (params.toString() ? '?' + params.toString() : '');
        window.history.replaceState({}, '', newUrl);

        const locationText = a ? a : "Karachi";
        const boardText = b ? b + " " : "";
        
        if(els.h1Highlight) els.h1Highlight.textContent = locationText;
        document.title = `Find ${boardText}Schools Near You in ${locationText} - SJ Academy`;
    }

    function cardHtml(r){
        var board   = r['Board(s)'] || 'N/A';
        var sector  = r.Sector || 'Private';
        var area    = r.Area || '';
        var phone   = r.Phone || 'N/A';
        var address = r.Address || 'Contact school for address';
        var review  = (r['SJ Review'] || '').trim();
        var href    = mapsHref(r.School, address);

        return '<div class="sja-card">'
            + '<h3>'+esc(r.School||'')+'</h3>'
            + '<div class="sector-line">'+esc(sector)+'</div>'
            + '<div class="sja-badges">'
                + (area ? '<span class="sja-tag">'+esc(area)+'</span>' : '')
                + '<span class="sja-tag">'+esc(board)+'</span>'
            + '</div>'
            + '<div class="sja-kv">'
                + '<div class="row"><div class="k">Phone</div><div class="v">'+esc(phone)+'</div></div>'
                + '<div class="row"><div class="k">Address</div><div class="v">'+esc(address)+'</div></div>'
            + '</div>'
            + '<a class="sja-mapbtn" href="'+href+'" target="_blank" rel="noopener">View on Map</a>'
            + '<div class="sja-meta">'
                + (review 
                    ? '<a href="'+esc(review)+'" target="_blank" rel="noopener">Read SJ Academy Review</a>' 
                    : 'SJ Review Coming Soon')
            + '</div>'
        + '</div>';
    }

    function render(){
        var rows = DATA.slice();
        var a = els.area.value;
        var b = els.board.value;
        var s = els.sector.value;

        if(a) rows = rows.filter(r => r.Area === a);
        if(b) rows = rows.filter(r => {
            var nb = normalizeBoard(r['Board(s)']);
            return nb === b || (r['Board(s)']||'').includes(b);
        });
        if(s) rows = rows.filter(r => (r.Sector||'') === s);

        els.count.textContent = rows.length.toString();

        var limit = currentLimit();
        var visible = rows.slice(0, Math.min(rows.length, limit));

        if(visible.length === 0) {
            els.grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #666;">No schools found matching your criteria. Try adjusting the filters.</div>';
        } else {
            let cardsArray = visible.map(cardHtml);
            
            const adCardHtml = `
            <div class="sja-card" style="border-top: 5px solid var(--sja-orange); background-color: var(--sja-light-yellow); text-align: center; padding: 25px 20px;">
                <h3 style="color: var(--sja-orange); font-weight: 800; font-size: 1.5rem; margin-bottom: 5px;">Need A*s in Cambridge?</h3>
                
                <div style="font-size: 13px; font-weight: 800; color: var(--sja-brown); margin-bottom: 12px;">
                    <span style="font-size: 16px;">⭐⭐⭐⭐⭐</span> <br> 220+ 5-Star Google Reviews
                </div>

                <p style="font-size: 13px; font-weight: 500; margin-bottom: 15px; flex-grow: 1; color: var(--sja-dark-grey); line-height: 1.5;">
                    Don't rely solely on school teachers to beat the CAIE curve. Get coached by Karachi's elite faculty from <strong>IBA, LUMS, and KGS</strong>.
                </p>

                <div style="background: rgba(254,97,0,0.1); border: 1px dashed var(--sja-orange); padding: 8px; border-radius: 6px; font-size: 12px; font-weight: 700; color: var(--sja-orange); margin-bottom: 20px;">
                    📍 Physical Campus (DHA) <br> 💻 Premium Live Online
                </div>

                <a class="sja-mapbtn" href="https://sjacademy.pk/o-a-level-classes/?utm_source=school_finder_tool&utm_medium=internal_ad_card&utm_campaign=oa_level_leads" style="background-color: var(--sja-orange); color: white; border-color: var(--sja-orange); margin-bottom: 0; padding: 14px; font-size: 14px; width: 100%; display: block;">BOOK A FREE DEMO CLASS</a>
            </div>
            `;
            
            if (cardsArray.length >= 2) {
                cardsArray.splice(2, 0, adCardHtml);
            } else {
                cardsArray.push(adCardHtml);
            }
            
            els.grid.innerHTML = cardsArray.join('');
        }

        els.moreWrap.style.display = (visible.length < rows.length) ? 'flex' : 'none';
        updateUrlAndSEO();
    }

    function loadCsv(url){
        if(!window.Papa) return;
        Papa.parse(url, {
            download: true, header: true, skipEmptyLines: true,
            complete: function(res){
                DATA = res.data.map(row => ({
                    "Area":      row.Area      || row.area      || '',
                    "School":    row.School    || row.school    || '',
                    "Board(s)":  row["Board(s)"] || row.board     || '',
                    "Sector":    row.Sector    || row.sector    || '',
                    "Address":   row.Address   || row.address   || '',
                    "Phone":     (row.Phone || row.phone || 'N/A').toString().trim(),
                    "SJ Review": row["SJ Review"] || row.review   || ''
                }));
                populateAreas();
                syncFromUrl(); 
                render();
            },
            error: function(){ 
                els.grid.innerHTML = '<div style="color:red; text-align:center; width:100%;">Failed to load school data. Please refresh the page.</div>';
            }
        });
    }

    ['change','input'].forEach(ev => {
        els.area.addEventListener(ev, () => { expanded=false; render(); });
        els.board.addEventListener(ev, () => { expanded=false; render(); });
        els.sector.addEventListener(ev, () => { expanded=false; render(); });
    });

    els.moreBtn.addEventListener('click', () => { expanded=true; render(); });
    els.reset.addEventListener('click', () => {
        els.area.value=''; els.board.value=''; els.sector.value='';
        
        window.history.replaceState({}, '', window.location.pathname);
        if(els.h1Highlight) els.h1Highlight.textContent = "Karachi";
        document.title = "Find Schools Near You in Karachi - SJ Academy";
        
        expanded=false; 
        render();
    });

    if(csvUrl) loadCsv(csvUrl);
})();
</script>
</body>
</html>
```
