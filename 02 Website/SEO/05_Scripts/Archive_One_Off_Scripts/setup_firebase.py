import json

filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# We need to replace the entire <script> block with a new modular script that includes Firebase.
# First, extract everything before <script> and after </script>
parts = html.split('<script>')
html_top = parts[0]
js_and_bottom = parts[1].split('</script>')
original_js = js_and_bottom[0]
html_bottom = js_and_bottom[1]

# Extract rawData from original JS
raw_data_marker = "const rawData ="
start_idx = original_js.find(raw_data_marker) + len(raw_data_marker)
end_idx = original_js.find(";", start_idx)
raw_data_str = original_js[start_idx:end_idx].strip()

new_script = f"""<script type="module">
  import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
  import {{ getDatabase, ref, onValue, runTransaction }} from "https://www.gstatic.com/firebasejs/10.9.0/firebase-database.js";

  // 1. Firebase Configuration from your screenshot
  const firebaseConfig = {{
    apiKey: "AIzaSyBZIof0-5_8TI314K36KEFTKxjT5G7AYf8",
    authDomain: "sj-academy-resource-vault.firebaseapp.com",
    databaseURL: "https://sj-academy-resource-vault-default-rtdb.firebaseio.com", // Added standard RTDB url
    projectId: "sj-academy-resource-vault",
    storageBucket: "sj-academy-resource-vault.firebasestorage.app",
    messagingSenderId: "1004229576995",
    appId: "1:1004229576995:web:c7399ba9ad07f62a99e496"
  }};

  // 2. Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getDatabase(app);

  // 3. Application State & Data
  const rawData = {raw_data_str};
  const grid = document.getElementById('sja-results-grid');
  const searchInput = document.getElementById('sja-search');
  const countDisplay = document.getElementById('sja-count');
  
  let currentFilters = {{ level: 'All', type: 'All', query: '' }};
  let firebaseVotes = {{}}; // Holds live vote offsets

  // Mobile Filter Toggle
  document.getElementById('sja-toggle-filters').addEventListener('click', function() {{
      document.getElementById('sja-sidebar').classList.toggle('open');
  }});

  // 4. Real-Time Listener
  const votesRef = ref(db, 'votes');
  onValue(votesRef, (snapshot) => {{
      firebaseVotes = snapshot.val() || {{}};
      // Instantly update DOM numbers without re-rendering the whole grid
      rawData.forEach(item => {{
          const total = item.votes + (firebaseVotes[item.id] || 0);
          const countEl = document.getElementById('count-' + item.id);
          if (countEl) countEl.innerText = total;
      }});
  }});

  // 5. Upvote Logic (Triggers Firebase Transaction)
  window.toggleVote = function(id, btn) {{
      const storageKey = 'voted_' + id;
      const isVoted = localStorage.getItem(storageKey);
      const voteRef = ref(db, 'votes/' + id);

      if (!isVoted) {{
          localStorage.setItem(storageKey, 'true');
          btn.classList.add('voted');
          runTransaction(voteRef, (currentVotes) => {{
              return (currentVotes || 0) + 1;
          }});
      }} else {{
          localStorage.removeItem(storageKey);
          btn.classList.remove('voted');
          runTransaction(voteRef, (currentVotes) => {{
              return (currentVotes || 0) - 1;
          }});
      }}
  }};

  const adHTML = `
    <h3 style="margin-bottom: 10px;">Stuck on past papers?</h3>
    <p style="margin-bottom: 20px; line-height: 1.6; color: #fff;">
      Master the exact CAIE marking scheme with Karachi's elite faculty from IBA, LUMS, and KGS. Join hundreds of SJ Academy students who secured straight A*s.
    </p>
    <a href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" class="sja-ad-btn">Join Free Demo Class</a>
  `;

  function renderGrid() {{
      grid.innerHTML = '';
      
      const query = searchInput.value.toLowerCase();
      const levelCheckboxes = Array.from(document.querySelectorAll('.sja-chk-level:checked')).map(cb => cb.value);
      const typeCheckboxes = Array.from(document.querySelectorAll('.sja-chk-type:checked')).map(cb => cb.value);

      const filtered = rawData.filter(item => {{
          const matchQuery = item["Resource Name"].toLowerCase().includes(query) || 
                             item["Subject"].toLowerCase().includes(query) ||
                             item["Description"].toLowerCase().includes(query);
                             
          let matchLevel = levelCheckboxes.length === 0;
          if (!matchLevel) {{
              levelCheckboxes.forEach(val => {{
                  if (item["Level"].includes(val)) matchLevel = true;
              }});
          }}
          
          let matchType = typeCheckboxes.length === 0 || typeCheckboxes.includes(item["Type"]);
          return matchQuery && matchLevel && matchType;
      }});

      countDisplay.innerText = `${{filtered.length}} Tools Found`;

      if(filtered.length === 0) {{
          grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 50px; color: #6B7280;">No resources found. Try clearing your filters.</div>`;
          return;
      }}

      let renderedCount = 0;
      filtered.forEach((item) => {{
          if(renderedCount === 2) {{
              const adCard = document.createElement('div');
              adCard.className = 'sja-card sja-ad-card';
              adCard.innerHTML = adHTML;
              grid.appendChild(adCard);
              renderedCount++;
          }}

          const isSJ = item["Is_SJ_Academy_Resource"] === "Yes";
          const imgUrl = item["Image_URL"];
          const domain = item["Link"].replace('https://','').replace('http://','').split('/')[0];
          const fallbackImg = `https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://${{domain}}&size=256`;
          
          let subjectDisp = item["Subject"] === "Multiple" ? "General Studies" : item["Subject"];

          const voted = localStorage.getItem('voted_' + item.id) ? 'voted' : '';
          
          // Calculate live total using baseline + firebase offset
          const liveTotal = item.votes + (firebaseVotes[item.id] || 0);

          const card = document.createElement('div');
          card.className = 'sja-card';
          
          card.innerHTML = `
              <div class="sja-card-header">
                  <img src="${{imgUrl}}" onerror="this.onerror=null; this.src='${{fallbackImg}}';" class="sja-card-logo" alt="${{item["Resource Name"]}} Logo" loading="lazy">
                  <div class="sja-card-title-group">
                      <h3>${{item["Resource Name"]}}</h3>
                      <div class="sja-card-subtitle">for <strong>${{subjectDisp}}</strong></div>
                  </div>
                  <div class="sja-upvote ${{voted}}" onclick="toggleVote('${{item.id}}', this)">
                      <svg viewBox="0 0 24 24"><path d="M12 4l-8 8h16z"/></svg>
                      <span class="vote-count" id="count-${{item.id}}">${{liveTotal}}</span>
                  </div>
              </div>
              
              <div class="sja-card-meta">
                  ${{isSJ ? '<span class="sja-meta-tag green">✓ Verified Official</span>' : ''}}
                  <span class="sja-meta-tag">${{item["Type"]}}</span>
              </div>
              
              <p>${{item["Description"]}}</p>
              
              <div class="sja-card-footer">
                  <div class="sja-tags">
                      <span class="sja-hashtag">#${{item["Level"].replace(' & ', ' #').replace(' ', '')}}</span>
                      <span class="sja-hashtag">#${{item["Subject"].replace(' ', '')}}</span>
                  </div>
                  <a href="${{item["Link"]}}" target="_blank" class="sja-visit-link">
                      Visit 
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </a>
              </div>
          `;
          grid.appendChild(card);
          renderedCount++;
      }});
  }}

  document.querySelectorAll('.filter-checkbox input').forEach(cb => {{
      cb.addEventListener('change', renderGrid);
  }});
  searchInput.addEventListener('input', renderGrid);

  renderGrid();
</script>"""

new_html = html_top + new_script + html_bottom

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Firebase integration successful!")
