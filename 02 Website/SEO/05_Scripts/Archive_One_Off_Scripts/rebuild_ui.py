import csv
import json
import hashlib
from urllib.parse import urlparse

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/caie_resources_database.csv"
html_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"

resources = []
with open(filepath, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        resources.append(row)

# Process images and generate stable mock votes
for idx, row in enumerate(resources):
    row["id"] = f"res_{idx}"
    
    # Stable random votes between 40 and 450
    hash_val = int(hashlib.md5(row["Resource Name"].encode()).hexdigest(), 16)
    row["votes"] = 40 + (hash_val % 410)
    
    # High votes for SJ Academy assets
    if row["Is_SJ_Academy_Resource"] == "Yes":
        row["votes"] = 350 + (hash_val % 100)

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
    /* Gradient Background and Core Variables */
    body {
        margin: 0;
        padding: 0;
        background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 50%, #FFFDF5 100%);
        background-attachment: fixed;
    }

    #sja-widget-root {
      --sja-yellow: #FCE004;
      --sja-light-yellow: #FFF9CC;
      --sja-brown: #453516;
      --sja-orange: #FE6100;
      --sja-orange-hover: #E55800;
      --sja-black: #111827;
      --sja-dark-grey: #374151;
      --sja-grey: #6B7280;
      --sja-light-bg: #FFFFFF;
      --sja-border-light: #E5E7EB;
      --sja-transition: all 0.25s ease;
      
      font-family: 'Poppins', sans-serif;
      font-weight: 400; /* Font weight 400 as requested */
      color: var(--sja-dark-grey);
      line-height: 1.6;
      width: 100%;
      box-sizing: border-box;
    }

    #sja-widget-root *, #sja-widget-root *::before, #sja-widget-root *::after {
      box-sizing: border-box;
    }

    .container { max-width: 1350px; margin: 0 auto; padding: 0 20px; }

    /* Header */
    .sja-header { text-align: center; padding: 70px 0 50px; }
    .sja-header h1 { font-size: clamp(2rem, 4vw, 3.2rem); font-weight: 600; margin: 0 0 15px 0; line-height: 1.2; color: var(--sja-black); }
    .sja-header p { font-size: 1.1rem; color: var(--sja-grey); max-width: 700px; margin: 0 auto; font-weight: 400; }
    
    /* Layout: Sidebar + Main Content */
    .sja-layout {
        display: grid;
        grid-template-columns: 260px 1fr;
        gap: 40px;
        align-items: start;
        padding-bottom: 80px;
    }

    /* Mobile Filter Toggle */
    .sja-mobile-filter-btn {
        display: none;
        width: 100%; padding: 14px; background: var(--sja-white); border: 1px solid var(--sja-border-light);
        border-radius: 12px; font-weight: 600; text-align: center; cursor: pointer; margin-bottom: 20px;
        color: var(--sja-black); box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }

    /* Sidebar Filters */
    .sja-sidebar {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.8);
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        position: sticky;
        top: 20px;
    }
    .sja-sidebar h3 { font-size: 1.2rem; font-weight: 600; margin: 0 0 20px 0; color: var(--sja-black); }
    
    .filter-group { margin-bottom: 25px; }
    .filter-group h4 { font-size: 0.9rem; font-weight: 600; color: var(--sja-grey); text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 12px 0; }
    
    .filter-checkbox {
        display: flex; align-items: center; gap: 10px; margin-bottom: 10px; cursor: pointer; font-size: 0.95rem; font-weight: 400;
    }
    .filter-checkbox input {
        width: 18px; height: 18px; border-radius: 4px; border: 1px solid var(--sja-border-light);
        accent-color: var(--sja-orange); cursor: pointer;
    }

    /* Search Bar */
    .sja-main-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; gap: 20px; }
    .sja-search-wrapper { flex-grow: 1; position: relative; }
    .sja-search-input { 
        width: 100%; padding: 16px 20px 16px 45px; font-family: 'Poppins', sans-serif; font-size: 15px; font-weight: 400;
        border: 1px solid var(--sja-border-light); border-radius: 12px; background: #fff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02); transition: var(--sja-transition); outline: none;
    }
    .sja-search-input:focus { border-color: var(--sja-orange); box-shadow: 0 4px 15px rgba(254,97,0,0.1); }
    .sja-search-icon { position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: #9CA3AF; width: 18px; height: 18px; }
    
    .sja-result-count { font-size: 14px; color: var(--sja-grey); font-weight: 500; white-space: nowrap; }

    /* StartupStash Style Grid */
    .sja-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; }

    /* The Card UI */
    .sja-card {
      background: var(--sja-white);
      padding: 24px; 
      border: 1px solid rgba(0,0,0,0.04);
      border-radius: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      transition: var(--sja-transition);
      display: flex; 
      flex-direction: column; 
      gap: 16px;
      height: 100%;
      position: relative;
    }
    .sja-card:hover { 
      transform: translateY(-4px); 
      box-shadow: 0 12px 24px rgba(0,0,0,0.06); 
      border-color: rgba(0,0,0,0.08);
    }
    
    /* Top Header: Logo + Title + Upvote */
    .sja-card-header {
      display: flex;
      align-items: flex-start;
      gap: 14px;
    }

    .sja-card-logo {
      width: 56px;
      height: 56px;
      border-radius: 12px;
      object-fit: contain;
      background: #FFFFFF;
      border: 1px solid var(--sja-border-light);
      padding: 6px; 
      flex-shrink: 0;
    }

    .sja-card-title-group {
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      padding-top: 4px;
    }

    .sja-card h3 { 
      font-size: 1.1rem; 
      font-weight: 600; /* refined weight */
      margin: 0 0 2px 0; 
      line-height: 1.25; 
      color: var(--sja-black); 
    }
    
    .sja-card-subtitle {
        font-size: 12px;
        color: var(--sja-grey);
        font-weight: 400;
    }
    .sja-card-subtitle strong { color: var(--sja-orange); font-weight: 500; }

    /* Voting Widget */
    .sja-upvote {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 1px solid var(--sja-border-light);
        border-radius: 8px;
        padding: 6px 10px;
        cursor: pointer;
        transition: all 0.2s;
        background: #fff;
    }
    .sja-upvote:hover { border-color: var(--sja-orange); background: #FFF7ED; }
    .sja-upvote.voted { border-color: var(--sja-orange); background: var(--sja-orange); color: #fff; }
    .sja-upvote svg { width: 16px; height: 16px; fill: currentColor; margin-bottom: 2px; }
    .sja-upvote.voted svg { fill: #fff; }
    .sja-upvote span { font-size: 12px; font-weight: 600; }
    
    /* Badges / Pills */
    .sja-card-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
    .sja-meta-tag { 
      font-size: 11px; 
      font-weight: 500; 
      background: #F3F4F6; 
      padding: 4px 10px; 
      border-radius: 20px; 
      color: #4B5563;
    }
    .sja-meta-tag.green { background: #ECFDF5; color: #059669; border: 1px solid #A7F3D0; }
    
    /* Description */
    .sja-card p { 
      font-size: 13.5px; 
      color: var(--sja-dark-grey); 
      margin: 0; 
      line-height: 1.6; 
      font-weight: 400;
      flex-grow: 1; 
    }

    /* Footer Tags */
    .sja-card-footer {
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid var(--sja-border-light);
    }
    .sja-tags { display: flex; gap: 6px; flex-wrap: wrap; }
    .sja-hashtag { font-size: 11px; color: var(--sja-grey); background: #F9FAFB; padding: 3px 8px; border-radius: 4px; }
    
    .sja-visit-link {
        font-size: 13px; font-weight: 500; color: var(--sja-orange); text-decoration: none;
        display: flex; align-items: center; gap: 4px; transition: 0.2s;
    }
    .sja-visit-link:hover { color: var(--sja-orange-hover); text-decoration: underline; }

    /* Ad Card */
    .sja-ad-card {
        background: linear-gradient(135deg, var(--sja-orange) 0%, #D95300 100%);
        color: #fff;
        justify-content: center;
        text-align: center;
        border: none;
    }
    .sja-ad-card h3 { color: #fff; font-size: 1.4rem; font-weight: 600; }
    .sja-ad-card p { color: rgba(255,255,255,0.9); }
    .sja-ad-btn {
        background: #fff; color: var(--sja-orange); font-weight: 600; padding: 12px 24px;
        border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Mobile Adjustments */
    @media (max-width: 991px) {
        .sja-layout { grid-template-columns: 1fr; gap: 20px; }
        .sja-sidebar { display: none; margin-bottom: 20px; }
        .sja-sidebar.open { display: block; }
        .sja-mobile-filter-btn { display: block; }
        .sja-main-header { flex-direction: column; align-items: flex-start; }
    }
  </style>
</head>
<body>

<div id="sja-widget-root">
  <div class="container">
    <div class="sja-header">
      <h1>O & A Level Resources</h1>
      <p>Check out the best curated tools, YouTube channels, and Past Papers for CAIE students. We gathered the top free and premium resources from around the web!</p>
    </div>

    <div class="sja-layout">
        <!-- Sidebar Filters -->
        <aside>
            <button class="sja-mobile-filter-btn" id="sja-toggle-filters">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 8px;"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
                Filter Resources
            </button>
            <div class="sja-sidebar" id="sja-sidebar">
                <h3>Filter By:</h3>
                
                <div class="filter-group" id="filter-level">
                    <h4>Category (Level)</h4>
                    <label class="filter-checkbox"><input type="checkbox" value="O Level" class="sja-chk-level"> O Level / IGCSE</label>
                    <label class="filter-checkbox"><input type="checkbox" value="A Level" class="sja-chk-level"> A Level</label>
                </div>

                <div class="filter-group" id="filter-type">
                    <h4>Resource Type</h4>
                    <label class="filter-checkbox"><input type="checkbox" value="YouTube Channel" class="sja-chk-type"> YouTube Channels</label>
                    <label class="filter-checkbox"><input type="checkbox" value="Website / Notes" class="sja-chk-type"> Notes & Websites</label>
                    <label class="filter-checkbox"><input type="checkbox" value="Past Papers" class="sja-chk-type"> Past Papers</label>
                    <label class="filter-checkbox"><input type="checkbox" value="App / Tool" class="sja-chk-type"> Apps & Tools</label>
                </div>
            </div>
        </aside>

        <!-- Main Content -->
        <main>
            <div class="sja-main-header">
                <div class="sja-search-wrapper">
                    <svg class="sja-search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    <input type="text" id="sja-search" class="sja-search-input" placeholder="Search by name, subject, or description...">
                </div>
                <div class="sja-result-count" id="sja-count">0 Tools Found</div>
            </div>

            <div class="sja-grid" id="sja-results-grid">
                <!-- Cards rendered via JS -->
            </div>
        </main>
    </div>
  </div>
</div>

<script>
(function(){
  const rawData = DATA_PLACEHOLDER;
  const grid = document.getElementById('sja-results-grid');
  const searchInput = document.getElementById('sja-search');
  const countDisplay = document.getElementById('sja-count');
  
  // Mobile Filter Toggle
  document.getElementById('sja-toggle-filters').addEventListener('click', function() {
      document.getElementById('sja-sidebar').classList.toggle('open');
  });

  // Upvote Logic
  window.toggleVote = function(id, baseVotes, btn) {
      const storageKey = 'voted_' + id;
      const countEl = btn.querySelector('.vote-count');
      if (!localStorage.getItem(storageKey)) {
          localStorage.setItem(storageKey, 'true');
          btn.classList.add('voted');
          countEl.innerText = parseInt(baseVotes) + 1;
      } else {
          localStorage.removeItem(storageKey);
          btn.classList.remove('voted');
          countEl.innerText = baseVotes;
      }
  };

  const adHTML = `
    <h3 style="margin-bottom: 10px;">Stuck on past papers?</h3>
    <p style="margin-bottom: 20px; line-height: 1.6; color: #fff;">
      Master the exact CAIE marking scheme with Karachi's elite faculty from IBA, LUMS, and KGS. Join hundreds of SJ Academy students who secured straight A*s.
    </p>
    <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-ad-btn">Join Free Demo Class</a>
  `;

  function renderGrid() {
      grid.innerHTML = '';
      
      const query = searchInput.value.toLowerCase();
      const levelCheckboxes = Array.from(document.querySelectorAll('.sja-chk-level:checked')).map(cb => cb.value);
      const typeCheckboxes = Array.from(document.querySelectorAll('.sja-chk-type:checked')).map(cb => cb.value);

      const filtered = rawData.filter(item => {
          const matchQuery = item["Resource Name"].toLowerCase().includes(query) || 
                             item["Subject"].toLowerCase().includes(query) ||
                             item["Description"].toLowerCase().includes(query);
                             
          let matchLevel = levelCheckboxes.length === 0;
          if (!matchLevel) {
              levelCheckboxes.forEach(val => {
                  if (item["Level"].includes(val)) matchLevel = true;
              });
          }
          
          let matchType = typeCheckboxes.length === 0 || typeCheckboxes.includes(item["Type"]);
          
          return matchQuery && matchLevel && matchType;
      });

      countDisplay.innerText = `${filtered.length} Tools Found`;

      if(filtered.length === 0) {
          grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 50px; color: #6B7280;">No resources found. Try clearing your filters.</div>`;
          return;
      }

      let renderedCount = 0;
      filtered.forEach((item) => {
          
          // Ad Injection
          if(renderedCount === 2) {
              const adCard = document.createElement('div');
              adCard.className = 'sja-card sja-ad-card';
              adCard.innerHTML = adHTML;
              grid.appendChild(adCard);
              renderedCount++;
          }

          const isSJ = item["Is_SJ_Academy_Resource"] === "Yes";
          const imgUrl = item["Image_URL"];
          const domain = item["Link"].replace('https://','').replace('http://','').split('/')[0];
          const fallbackImg = `https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://${domain}&size=256`;
          
          // Format subject display
          let subjectDisp = item["Subject"] === "Multiple" ? "General Studies" : item["Subject"];

          // Vote State initialization
          const voted = localStorage.getItem('voted_' + item.id) ? 'voted' : '';
          const currentVotes = voted ? item.votes + 1 : item.votes;

          const card = document.createElement('div');
          card.className = 'sja-card';
          
          card.innerHTML = `
              <div class="sja-card-header">
                  <img src="${imgUrl}" onerror="this.onerror=null; this.src='${fallbackImg}';" class="sja-card-logo" alt="${item["Resource Name"]} Logo" loading="lazy">
                  <div class="sja-card-title-group">
                      <h3>${item["Resource Name"]}</h3>
                      <div class="sja-card-subtitle">for <strong>${subjectDisp}</strong></div>
                  </div>
                  <div class="sja-upvote ${voted}" onclick="toggleVote('${item.id}', ${item.votes}, this)">
                      <svg viewBox="0 0 24 24"><path d="M12 4l-8 8h16z"/></svg>
                      <span class="vote-count">${currentVotes}</span>
                  </div>
              </div>
              
              <div class="sja-card-meta">
                  ${isSJ ? '<span class="sja-meta-tag green">✓ Verified Official</span>' : ''}
                  <span class="sja-meta-tag">${item["Type"]}</span>
              </div>
              
              <p>${item["Description"]}</p>
              
              <div class="sja-card-footer">
                  <div class="sja-tags">
                      <span class="sja-hashtag">#${item["Level"].replace(' & ', ' #').replace(' ', '')}</span>
                      <span class="sja-hashtag">#${item["Subject"].replace(' ', '')}</span>
                  </div>
                  <a href="${item["Link"]}" target="_blank" class="sja-visit-link">
                      Visit 
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </a>
              </div>
          `;
          grid.appendChild(card);
          renderedCount++;
      });
  }

  // Bind events to checkboxes
  document.querySelectorAll('.filter-checkbox input').forEach(cb => {
      cb.addEventListener('change', renderGrid);
  });
  
  searchInput.addEventListener('input', renderGrid);

  renderGrid();
})();
</script>

</body>
</html>
""".replace("DATA_PLACEHOLDER", resources_json)

with open(html_filepath, mode='w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully redesigned to match StartupStash directory UI.")
