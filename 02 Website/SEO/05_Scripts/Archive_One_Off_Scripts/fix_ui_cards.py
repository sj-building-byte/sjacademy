import csv
import json

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"
html_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"

resources = []
with open(filepath, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        resources.append(row)

# Re-run image logic just to ensure it's baked into JSON
from urllib.parse import urlparse
for row in resources:
    link = row["Link"]
    name = row["Resource Name"]
    img_url = ""
    domain = urlparse(link).netloc.replace('www.', '')
    if 'youtube.com' in domain:
        if '@' in link:
            handle = link.split('@')[-1].split('/')[0]
            img_url = f"https://unavatar.io/youtube/{handle}"
        else:
            img_url = f"https://unavatar.io/youtube/{name.replace(' ', '')}"
    elif 'instagram.com' in domain:
        handle = link.rstrip('/').split('/')[-1]
        img_url = f"https://unavatar.io/instagram/{handle}"
    elif 'reddit.com' in domain:
        subreddit = link.rstrip('/').split('/')[-1]
        img_url = f"https://unavatar.io/reddit/{subreddit}"
    elif 'sjacademy.pk' in domain:
        img_url = "https://sjacademy.pk/wp-content/uploads/2023/10/SJ-Academy-Logo-1.png"
    else:
        img_url = f"https://logo.clearbit.com/{domain}"
    row["Image_URL"] = img_url

resources_json = json.dumps(resources)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>O & A Level Resources Vault | SJ Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <style>
    #sja-widget-root {
      --sja-yellow: #FCE004;
      --sja-light-yellow: #FFF9CC;
      --sja-brown: #453516;
      --sja-orange: #FE6100;
      --sja-orange-hover: #E55800;
      --sja-black: #000000;
      --sja-dark-grey: #222222;
      --sja-grey: #4B5563; /* Softer readable grey for text */
      --sja-light-bg: #FAFAFA;
      --sja-white: #FFFFFF;
      --sja-border-light: #E5E5E5;
      --sja-whatsapp: #25D366;
      --sja-transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      
      font-family: 'Poppins', sans-serif;
      color: var(--sja-black);
      line-height: 1.6;
      background: var(--sja-white);
      width: 100%;
      box-sizing: border-box;
    }

    #sja-widget-root *, #sja-widget-root *::before, #sja-widget-root *::after {
      box-sizing: border-box;
    }

    .container { max-width: 1250px; margin: 0 auto; padding: 0 20px; }

    /* Header */
    .sja-header { text-align: center; padding: 60px 0 40px; }
    .sja-badge { display: inline-block; background: #fff; border: 2px solid #000; border-radius: 50px; padding: 5px; margin-bottom: 25px; box-shadow: 4px 4px 0 rgba(0,0,0,0.15); }
    .sja-mode-pill { padding: 8px 20px; border-radius: 40px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; background: var(--sja-yellow); color: #000; }
    .sja-title { font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 800; margin-bottom: 20px; line-height: 1.2; color: var(--sja-black); }
    .sja-highlight { background: linear-gradient(120deg, var(--sja-yellow) 0%, var(--sja-yellow) 100%) no-repeat 0 85% / 100% 35%; display: inline; padding: 0 3px; color: var(--sja-black); }
    .sja-subtitle { font-size: 1.1rem; color: var(--sja-dark-grey); max-width: 700px; margin: 0 auto 30px; }

    /* Controls & Search */
    .sja-controls { background: var(--sja-light-bg); padding: 40px 0; border-top: 1px solid var(--sja-border-light); border-bottom: 1px solid var(--sja-border-light); }
    
    .sja-search-wrapper { margin-bottom: 30px; position: relative; }
    .sja-search-input { 
        width: 100%; padding: 18px 24px; font-family: 'Poppins', sans-serif; font-size: 16px;
        border: 2px solid var(--sja-brown); border-radius: 12px; box-shadow: 4px 4px 0 rgba(0,0,0,0.08);
        transition: var(--sja-transition); outline: none;
    }
    .sja-search-input:focus { border-color: var(--sja-orange); box-shadow: 4px 4px 0 rgba(254,97,0,0.2); }
    
    .sja-filter-group { margin-bottom: 25px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .sja-filter-label { font-weight: 700; font-size: 14px; margin-right: 15px; color: var(--sja-dark-grey); text-transform: uppercase; letter-spacing: 0.5px; }
    
    /* Option Pills */
    .sja-opt {
      font-family: 'Poppins', sans-serif; font-size: 13px; font-weight: 700; padding: 8px 18px;
      border-radius: 40px; border: 1.5px solid var(--sja-brown); background: var(--sja-white);
      color: var(--sja-black); cursor: pointer; box-shadow: 3px 3px 0 rgba(0,0,0,0.08);
      transition: all 0.2s ease;
    }
    .sja-opt:hover { background: var(--sja-light-yellow); }
    .sja-opt.selected { background: var(--sja-yellow); border-color: var(--sja-brown); box-shadow: 3px 3px 0 rgba(0,0,0,0.15); }

    /* Modern UI Cards Grid */
    .sja-grid { display: grid; grid-template-columns: 1fr; gap: 24px; padding: 50px 0; }
    @media(min-width: 768px) { .sja-grid { grid-template-columns: repeat(2, 1fr); } }
    @media(min-width: 1024px) { .sja-grid { grid-template-columns: repeat(3, 1fr); } }

    .sja-card {
      background: var(--sja-white);
      padding: 26px; 
      border-top: 6px solid var(--sja-brown);
      border-radius: 16px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.03);
      transition: var(--sja-transition);
      display: flex; 
      flex-direction: column; 
      gap: 16px;
      height: 100%;
      border-bottom: 1px solid rgba(0,0,0,0.04);
      border-left: 1px solid rgba(0,0,0,0.04);
      border-right: 1px solid rgba(0,0,0,0.04);
    }
    
    .sja-card:hover { 
      transform: translateY(-5px); 
      box-shadow: 0 15px 35px rgba(0,0,0,0.1); 
      border-top-color: var(--sja-orange); 
    }
    
    .sja-highlight-card {
      border-top-color: var(--sja-yellow); 
      background: linear-gradient(145deg, #FFFDF5 0%, #FFFFFF 100%);
    }
    .sja-highlight-card:hover { border-top-color: var(--sja-orange); }

    /* New "App Icon" / "Avatar" Header Layout */
    .sja-card-header {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .sja-card-logo {
      width: 60px;
      height: 60px;
      border-radius: 14px;
      object-fit: contain;
      background: #FFFFFF;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      border: 1px solid rgba(0,0,0,0.04);
      padding: 8px; /* Creates natural padding for logos */
      flex-shrink: 0;
    }
    
    .sja-highlight-card .sja-card-logo {
      box-shadow: 0 4px 15px rgba(252, 224, 4, 0.4);
      border-color: var(--sja-yellow);
    }

    .sja-card-title-group {
      display: flex;
      flex-direction: column;
      gap: 5px;
      overflow: hidden;
    }

    .sja-card h3 { 
      font-size: 1.15rem; 
      font-weight: 800; 
      margin: 0; 
      line-height: 1.25; 
      color: var(--sja-black); 
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    
    /* Subtle Pill Tags */
    .sja-card-meta { display: flex; gap: 6px; flex-wrap: wrap; }
    .sja-meta-tag { 
      font-size: 10px; 
      font-weight: 700; 
      text-transform: uppercase; 
      background: #F3F4F6; 
      padding: 4px 8px; 
      border-radius: 6px; 
      color: #52525B;
      letter-spacing: 0.3px;
    }
    .sja-highlight-card .sja-meta-tag { background: var(--sja-light-yellow); color: var(--sja-brown); }
    
    .sja-card p { 
      font-size: 13.5px; 
      color: var(--sja-grey); 
      margin: 0; 
      line-height: 1.6; 
      flex-grow: 1; 
    }

    .sja-card-footer {
      margin-top: auto;
      padding-top: 10px;
    }

    /* Buttons */
    .sja-btn {
      font-family: 'Poppins', sans-serif; font-size: 13px; font-weight: 700; text-transform: uppercase;
      letter-spacing: 0.5px; padding: 12px 24px; border-radius: 8px; display: inline-flex;
      align-items: center; justify-content: center; gap: 8px; cursor: pointer; text-decoration: none;
      border: 2px solid transparent; transition: var(--sja-transition); width: 100%; text-align: center;
    }
    .sja-btn-primary { background: var(--sja-orange); color: var(--sja-white); border-color: var(--sja-orange); box-shadow: 0 4px 10px rgba(254,97,0,0.3); }
    .sja-btn-primary:hover { background: var(--sja-orange-hover); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(254, 97, 0, 0.4); color: var(--sja-white); }
    
    .sja-btn-outline { background: var(--sja-white); color: var(--sja-brown); border-color: #D1D5DB; }
    .sja-btn-outline:hover { background: var(--sja-brown); border-color: var(--sja-brown); color: var(--sja-white); }

    /* Special Conversion Ad Card */
    .sja-ad-card {
      background: var(--sja-brown);
      border-top-color: var(--sja-orange);
      color: #fff;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 15px;
    }
    .sja-ad-card:hover {
      box-shadow: 0 15px 35px rgba(254,97,0,0.25);
    }
    .sja-ad-card h3 {
      color: var(--sja-yellow);
      font-size: 1.4rem;
      white-space: normal;
    }
    .sja-ad-card p {
      color: rgba(255, 255, 255, 0.85);
      font-size: 14px;
    }

    /* Empty state */
    .sja-empty-state { grid-column: 1 / -1; text-align: center; padding: 40px; font-weight: 700; color: var(--sja-grey); }
  </style>
</head>
<body>

<div id="sja-widget-root">
  <div class="container">
    <div class="sja-header">
      <div class="sja-badge">
        <div class="sja-mode-pill">⚡ ULTIMATE CAIE DIRECTORY</div>
      </div>
      <h1 class="sja-title">O & A Level <span class="sja-highlight">Resources Vault</span></h1>
      <p class="sja-subtitle">The largest curated database of free YouTube channels, topical notes, past papers, and productivity apps for Cambridge students globally.</p>
    </div>
  </div>

  <div class="sja-controls">
    <div class="container">
      
      <div class="sja-search-wrapper">
        <input type="text" id="sja-search" class="sja-search-input" placeholder="Search for a subject, channel, or resource (e.g. 'Physics', 'Zainematics')...">
      </div>

      <div class="sja-filter-group" id="filter-level">
        <span class="sja-filter-label">Level:</span>
        <button class="sja-opt selected" data-val="All">All Levels</button>
        <button class="sja-opt" data-val="O Level">O Level / IGCSE</button>
        <button class="sja-opt" data-val="A Level">A Level</button>
      </div>

      <div class="sja-filter-group" id="filter-type">
        <span class="sja-filter-label">Resource Type:</span>
        <button class="sja-opt selected" data-val="All">All Types</button>
        <button class="sja-opt" data-val="YouTube Channel">YouTube Channels</button>
        <button class="sja-opt" data-val="Website / Notes">Notes & Websites</button>
        <button class="sja-opt" data-val="Past Papers">Past Papers</button>
        <button class="sja-opt" data-val="App / Tool">Apps & Tools</button>
      </div>

    </div>
  </div>

  <div class="container">
    <div class="sja-grid" id="sja-results-grid">
      <!-- Cards rendered via JS -->
    </div>
  </div>
</div>

<script>
(function(){
  const rawData = DATA_PLACEHOLDER;
  const grid = document.getElementById('sja-results-grid');
  const searchInput = document.getElementById('sja-search');
  
  let currentFilters = {
      level: 'All',
      type: 'All',
      query: ''
  };

  // Modern Conversion Ad Card Content
  const adHTML = `
    <h3 style="color:var(--sja-orange);font-weight:900;font-size:1.6rem;line-height:1.2; margin:0;">Stuck on past papers?</h3>
    <p style="margin-bottom:8px;line-height:1.6;flex-grow:1; color:rgba(255,255,255,0.9);">
      Don't lose marks on tricky questions. Master the exact CAIE marking scheme with Karachi's elite faculty from <strong>IBA, LUMS, and KGS</strong>. Join hundreds of SJ Academy students who secured straight A*s.
    </p>
    <div class="sja-card-footer" style="padding-top:0;">
      <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-btn sja-btn-primary" style="box-shadow:none;">Join a Free Demo Class</a>
    </div>
  `;

  function renderGrid() {
      grid.innerHTML = '';
      
      const filtered = rawData.filter(item => {
          const matchQuery = item["Resource Name"].toLowerCase().includes(currentFilters.query) || 
                             item["Subject"].toLowerCase().includes(currentFilters.query) ||
                             item["Description"].toLowerCase().includes(currentFilters.query);
                             
          const levelData = item["Level"];
          let matchLevel = true;
          if(currentFilters.level !== 'All') {
              if(currentFilters.level === 'O Level' && !levelData.includes('O Level')) matchLevel = false;
              if(currentFilters.level === 'A Level' && !levelData.includes('A Level')) matchLevel = false;
          }
          
          let matchType = (currentFilters.type === 'All' || item["Type"].includes(currentFilters.type));
          
          return matchQuery && matchLevel && matchType;
      });

      if(filtered.length === 0) {
          grid.innerHTML = `<div class="sja-empty-state">No resources found matching your criteria. Try adjusting your filters.</div>`;
          return;
      }

      let renderedCount = 0;
      filtered.forEach((item, index) => {
          
          if(renderedCount === 3) {
              const adCard = document.createElement('div');
              adCard.className = 'sja-card sja-ad-card';
              adCard.innerHTML = adHTML;
              grid.appendChild(adCard);
              renderedCount++;
          }

          const isSJ = item["Is_SJ_Academy_Resource"] === "Yes";
          const cardClass = isSJ ? 'sja-card sja-highlight-card' : 'sja-card';
          const btnClass = isSJ ? 'sja-btn sja-btn-primary' : 'sja-btn sja-btn-outline';
          const btnText = isSJ ? 'Access Tool' : 'Visit Resource';
          
          const imgUrl = item["Image_URL"];
          const domain = item["Link"].replace('https://','').replace('http://','').split('/')[0];
          const fallbackImg = `https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://${domain}&size=256`;

          const card = document.createElement('div');
          card.className = cardClass;
          
          // New Modern "App Icon" UI Layout
          card.innerHTML = `
              <div class="sja-card-header">
                  <img src="${imgUrl}" onerror="this.onerror=null; this.src='${fallbackImg}';" class="sja-card-logo" alt="${item["Resource Name"]} Logo" loading="lazy">
                  <div class="sja-card-title-group">
                      <h3>${item["Resource Name"]}</h3>
                      <div class="sja-card-meta">
                          <span class="sja-meta-tag">${item["Level"]}</span>
                          <span class="sja-meta-tag">${item["Subject"]}</span>
                          <span class="sja-meta-tag">${item["Type"]}</span>
                      </div>
                  </div>
              </div>
              <p>${item["Description"]}</p>
              <div class="sja-card-footer">
                  <a href="${item["Link"]}" target="_blank" class="${btnClass}">${btnText}</a>
              </div>
          `;
          grid.appendChild(card);
          renderedCount++;
      });
  }

  searchInput.addEventListener('input', (e) => {
      currentFilters.query = e.target.value.toLowerCase();
      renderGrid();
  });

  function setupFilter(groupId, filterKey) {
      const group = document.getElementById(groupId);
      const buttons = group.querySelectorAll('.sja-opt');
      buttons.forEach(btn => {
          btn.addEventListener('click', () => {
              buttons.forEach(b => b.classList.remove('selected'));
              btn.classList.add('selected');
              currentFilters[filterKey] = btn.getAttribute('data-val');
              renderGrid();
          });
      });
  }

  setupFilter('filter-level', 'level');
  setupFilter('filter-type', 'type');

  renderGrid();
})();
</script>

</body>
</html>
""".replace("DATA_PLACEHOLDER", resources_json)

with open(html_filepath, mode='w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully redesigned UI to use App Icon layout.")
