(function () {
  var root = document.getElementById('sj');
  var app = root && root.querySelector('[data-sji]');
  if (!app || app.getAttribute('data-ready')) { return; }
  app.setAttribute('data-ready', '1');
  var S = SJI, $ = function (sel, el) { return (el || app).querySelector(sel); };
  var $$ = function (sel, el) { return Array.prototype.slice.call((el || app).querySelectorAll(sel)); };
  var KEY = 'sj-ibcc-v3', WA = '__WA__';
  var YEARS = [[2028, '2028 (forecast)'], [2027, '2027 (forecast)'], [2026, '2026'], [2025, '2025'], [2024, '2024'], [2023, '2023'], [2022, '2022'], [2021, '2021'], [2020, '2006 to 2020']];
  var esc = function (t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var name = function (id) { return S.SUBJ[id] || ''; };
  var yearLabel = function (y) { for (var i = 0; i < YEARS.length; i++) { if (YEARS[i][0] === Number(y)) { return YEARS[i][1]; } } return String(y); };
  var fresh = function () { return { target: null, route: 'pk', group: '', oYear: null, aYear: 2026, oType: 'letter', multi: false, rows: {} }; };

  var st = fresh();
  try { var saved = JSON.parse(localStorage.getItem(KEY) || 'null'); if (saved && saved.st) { st = saved.st; } } catch (e) { }
  var q = /[?&]level=([oa])/.exec(location.search);
  if (q && !st.target) { st.target = q[1] === 'o' ? 'ssc' : 'hssc'; }
  var save = function () { try { localStorage.setItem(KEY, JSON.stringify({ st: st })); } catch (e) { } };
  var sent = false;

  function options(list, value, blank) {
    return (blank ? '<option value="">' + blank + '</option>' : '') + list.map(function (o) {
      return '<option value="' + o[0] + '"' + (String(o[0]) === String(value) ? ' selected' : '') + '>' + esc(o[1]) + '</option>';
    }).join('');
  }

  /* ---------- grade rows ---------- */
  function renderRows() {
    var ready = st.target && (st.target === 'ssc' || st.group);
    var list = ready ? S.rows(st) : [];
    ['O', 'A'].forEach(function (lvl) {
      var mine = list.filter(function (r) { return r.level === lvl; });
      var wrap = $('[data-block="' + lvl + '"]');
      wrap.hidden = !mine.length;
      var grades = lvl === 'O' && st.oType === 'number' ? S.NUMBERS : S.LETTERS;
      $('[data-rows="' + lvl + '"]').innerHTML = mine.map(function (r) {
        var d = st.rows[r.id] || {}, subjCell;
        if (r.choose) {
          var opts = r.choose;
          var val = d.subj && opts.indexOf(d.subj) > -1 ? d.subj : '';
          subjCell = '<select class="sj-select sji-subj" data-subj="' + r.id + '" aria-label="Subject">' +
            options(opts.map(function (o) { return [o, name(o)]; }), val, 'Choose subject') + '</select>';
        } else {
          subjCell = '<label class="sji-name" for="g-' + r.id + '">' + esc(name(r.alt && d.subj === 'ethics' ? 'ethics' : r.fixed)) + '</label>';
        }
        var yearCell = st.multi ? '<select class="sj-select sji-y" id="y-' + r.id + '" aria-label="Exam year">' +
          options(YEARS.map(function (y) { return [y[0], y[0] === 2020 ? '2006-20' : String(y[0])]; }), d.year || (lvl === 'O' ? st.oYear : st.aYear)) + '</select>' : '';
        return '<div class="sji-r' + (st.multi ? ' sji-r3' : '') + (d.grade ? ' is-done' : '') + '" data-row="' + r.id + '">' + subjCell + yearCell +
          '<select class="sj-select sji-g" id="g-' + r.id + '" aria-label="Grade for ' + esc(name(r.fixed) || 'this subject') + '">' +
          options(grades.map(function (g) { return [g, g]; }), d.grade, 'Grade') + '</select></div>';
      }).join('');
    });
    $('[data-pick]').hidden = !(st.target === 'hssc' && !st.group);
    syncDupes();
  }

  function syncDupes() {
    ['O', 'A'].forEach(function (lvl) {
      var sels = $$('[data-rows="' + lvl + '"] select.sji-subj');
      var used = sels.map(function (s) { return s.value; });
      sels.forEach(function (s, i) {
        $$('option', s).forEach(function (o) { o.disabled = !!o.value && o.value !== 'other' && used.some(function (u, j) { return j !== i && u === o.value; }); });
      });
    });
  }

  function renderForm() {
    $$('input[name="sji-target"]').forEach(function (i) { i.checked = i.value === st.target; });
    $('[data-setup]').hidden = !st.target;
    $$('[data-hssc]').forEach(function (el) { el.hidden = st.target !== 'hssc'; });
    if (st.target && !st.oYear) { st.oYear = st.target === 'ssc' ? 2026 : 2025; }
    $('#sji-route').value = st.route;
    $('#sji-group').value = st.group || '';
    $('#sji-oy').value = st.oYear || 2026;
    $('#sji-ay').value = st.aYear || 2026;
    $('#sji-multi').checked = st.multi;
    $('#sji-nums').checked = st.oType === 'number';
    $('#sji-eth').checked = (st.rows['o-isl'] || {}).subj === 'ethics';
    $('[data-eth]').hidden = st.route !== 'pk';
    renderRows();
  }

  /* ---------- result ---------- */
  var RULE = {
    ssc_pk: '8 O Levels, scaled from 800 to 900',
    ssc_exempt: '5 O Levels (no Urdu, Islamiyat or Pak Studies), scaled from 500 to 900',
    legacy_pk: '8 O Levels + 3 A Levels, out of 1100',
    legacy_exempt: '5 O Levels + 3 A Levels, scaled from 800 to 1100',
    new_pk: 'New 2026 rule: 5 compulsory O Levels + 3 A Levels, scaled from 800 to 1100',
    new_exempt: 'New 2026 rule: English, Maths + 3 A Levels, scaled from 500 to 1100'
  };
  var FLAG = {
    forecast: 'Sessions after 2026 are a forecast: IBCC has not published their A* marks yet, so A* uses the 2026 values.',
    nine: 'Grade 9 uses the subject’s A* marks, as IBCC lists 9 and A* together.',
    a_na: 'IBCC gives no A Level A* figure for English, Urdu, Islamiyat or Pakistan Studies, so we used its “other subjects” value.',
    addm: 'Additional Maths keeps you in the Science group (IBCC FAQ).',
    new_scale: 'IBCC has not published an example for the 2026 rule, so the marks are an estimate. The percentage is the solid figure.',
    cs_abroad: 'IBCC’s overseas text lists Physics, Chemistry and Maths for this group. Check with IBCC.'
  };

  function waLink(level, subj, ref) {
    var msg = ['Hi SJ Academy, I used your IBCC calculator and I’d like a free demo class.', 'Level: ' + (level || ''),
      'Subject: ' + (subj || ''), 'Mode (in class or online): ', '(Ref: ' + ref + ')', 'My name is '].join('\n');
    return WA + encodeURIComponent(msg);
  }

  function renderResult() {
    var res = S.compute(st), box = $('[data-result]'), bar = $('[data-bar]');
    var ready = st.target && (st.target === 'ssc' || st.group);
    var list = ready ? S.rows(st) : [];
    var need = list.length, done = list.filter(function (r) { return st.rows[r.id] && st.rows[r.id].grade; }).length;
    $$('.sji-r').forEach(function (el) { el.classList.toggle('is-done', !!(st.rows[el.getAttribute('data-row')] || {}).grade); el.classList.remove('is-error'); });
    var title = st.target === 'ssc' ? 'Matric (SSC)' : 'FSc (HSSC)';
    var lvlName = function (l) { return l === 'O' ? 'O Level' : 'A Level'; };
    var html;
    if (res.status === 'invalid') {
      res.errors.forEach(function (e) { var el = $('[data-row="' + e.id + '"]'); if (el) { el.classList.add('is-error'); } });
      html = '<div class="sj-alert sj-alert-err" role="alert"><b>Same subject twice</b><p>Pick a different subject in the highlighted row.</p></div>';
      bar.innerHTML = '<span>Check your subjects</span>';
    } else if (res.status !== 'ok') {
      var left = need - done;
      var msg = !st.target ? 'Choose O Level or A Level to start.' : !ready ? 'Pick your FSc group.' :
        left > 0 ? 'Add ' + left + ' more ' + (left === 1 ? 'grade' : 'grades') + ' to see your marks.' : 'Choose a subject for each elective.';
      html = '<p class="sj-eyebrow">Your ' + (st.target ? title + ' ' : '') + 'marks</p><p class="sji-big sji-dim">&ndash;</p><p>' + msg + '</p>' +
        (need ? '<div class="sji-prog" aria-hidden="true"><i style="width:' + Math.round(done / need * 100) + '%"></i></div>' : '');
      bar.innerHTML = '<span>' + (need ? done + ' of ' + need + ' grades' : 'Your marks') + '</span><b>See result</b>';
    } else {
      var t = S.tip(st, res);
      var notes = [];
      if (res.rule.indexOf('legacy') === 0 && res.group !== 'Humanities') { notes.push('Your O Levels finished before 2026, so IBCC’s February 2026 rule does not apply and all your O Levels count.'); }
      if (res.rule.indexOf('legacy') === 0 && res.group === 'Humanities' && res.oFinish >= 2026) { notes.push('The February 2026 rule covers science groups only, so Humanities still counts all your O Levels.'); }
      if (res.newRule) { notes.push('You finish O Levels in ' + res.oFinish + ', so IBCC’s February 2026 rule applies: your O Level electives need a pass but do not count.' + (st.multi ? ' If you only resat a subject in 2026, ask IBCC which rule applies.' : '')); }
      res.flags.forEach(function (f) { if (FLAG[f]) { notes.push(FLAG[f]); } });
      var aYears = res.items.filter(function (i) { return i.level === 'A'; }).map(function (i) { return i.year; });
      if (aYears.length && Math.min.apply(null, aYears) <= res.oFinish && res.oFinish > 2020) { notes.push('Check your years: your A Levels are set to the same year as your O Levels or earlier.'); }
      if (st.target === 'ssc') { notes.push('Why out of 900? IBCC’s own worked examples use 900. <a class="sj-link" href="#sji-faq-900">More on this</a>'); }
      var rowsHtml = res.items.map(function (i) {
        return '<tr' + (i.counted ? '' : ' class="sji-off"') + '><td>' + esc(name(i.subj)) + ' <span class="sj-small">' + lvlName(i.level) + ' ' + esc(yearLabel(i.year)) + '</span></td><td>' + esc(i.grade) + '</td><td class="sj-num">' + (i.counted ? i.marks : 'not counted') + '</td></tr>';
      }).join('');
      var maths = res.max === res.scale ? 'Total: ' + res.raw + ' / ' + res.max :
        res.raw + ' / ' + res.max + ' &times; ' + res.scale + ' = ' + (Math.round(res.raw * res.scale / res.max * 100) / 100) + ', rounded to ' + res.marks;
      var warn = res.flags.indexOf('forecast') > -1 || res.newRule;
      html = '<p class="sj-eyebrow">Your ' + title + ' marks</p>' +
        '<p class="sji-big"><b>' + res.marks + '</b><span> / ' + res.scale + '</span></p>' +
        '<p class="sji-pct"><span class="sj-chip sj-chip-yellow">' + res.pct.toFixed(2) + '%</span> <span class="sj-small">' + esc(res.group) + ' group</span></p>' +
        (res.ssc ? '<p class="sji-also">Matric (SSC): <b>' + res.ssc.marks + ' / 900</b> (' + res.ssc.pct.toFixed(2) + '%)</p>' : '') +
        (warn ? '<p class="sji-warn">' + (res.newRule ? 'Uses IBCC’s new 2026 rule' : 'Includes a 2027/2028 forecast') + ', so treat this as an estimate.</p>' : '') +
        '<details class="sji-work"><summary>How we worked it out</summary><p class="sj-small"><b>Rule:</b> ' + RULE[res.rule] + '</p><div class="sj-table-wrap"><table class="sj-table"><thead><tr><th scope="col">Subject</th><th scope="col">Grade</th><th scope="col" class="sj-num">Marks</th></tr></thead><tbody>' + rowsHtml + '</tbody></table></div><p class="sj-small">' + maths + '</p>' +
        '<ul class="sji-notes">' + notes.map(function (n) { return '<li>' + n + '</li>'; }).join('') + '</ul></details>';
      var tipLevel = t ? lvlName(t.level) : (st.target === 'ssc' ? 'O Level' : 'A Level');
      html += '<div class="sji-tip">' + (t ?
        '<p><b>Quickest win:</b> ' + esc(tipLevel + ' ' + name(t.subj)) + ' ' + t.from + ' &rarr; ' + t.to + ' gets you <b>' + t.marks + ' / ' + res.scale + '</b> (' + t.pct.toFixed(2) + '%).</p>' :
        '<p><b>Top marks in every subject.</b> Well done.</p>') +
        '<a class="sj-btn sj-btn-primary sj-btn-block" target="_blank" rel="noopener" data-loc="result_tip" href="' + esc(waLink(tipLevel, t ? name(t.subj) : '', 'IBCC-RESULT')) + '">Get help with a free demo class</a>' +
        '<p class="sj-small">On WhatsApp. In class at DHA Phase 7, Karachi, or online from anywhere.</p></div>' +
        '<p class="sji-acts sj-small"><button type="button" class="sji-lnk" data-act="share">Share result</button> &middot; <button type="button" class="sji-lnk" data-act="reset">Start again</button></p>';
      bar.innerHTML = '<span>' + title + '</span><b>' + res.marks + ' / ' + res.scale + ' &middot; ' + res.pct.toFixed(2) + '%</b>';
      if (!sent) {
        sent = true;
        var g = window['gt' + 'ag'];
        if (typeof g === 'function') { g('event', 'calculation_complete', { calc_level: st.target, calc_rule: res.rule, page_family: root.getAttribute('data-family') || '' }); }
      }
      app._last = res;
    }
    box.innerHTML = html;
    app.classList.toggle('is-empty', !st.target);
    $('[data-live]').textContent = res.status === 'ok' ? 'Result: ' + res.marks + ' out of ' + res.scale + ', ' + res.pct.toFixed(2) + ' percent.' : '';
    bar.hidden = !st.target;
    save();
  }

  function update(full) { if (full) { renderForm(); } renderResult(); }

  /* ---------- events ---------- */
  app.addEventListener('change', function (e) {
    var el = e.target, n = el.name || '', id = el.id || '';
    if (n === 'sji-target') { if (st.target !== el.value) { st.target = el.value; st.oYear = null; } return update(true); }
    if (id === 'sji-route') { st.route = el.value; return update(true); }
    if (id === 'sji-group') { st.group = el.value; return update(true); }
    if (id === 'sji-oy' || id === 'sji-ay') {
      var pre = id === 'sji-oy' ? 'o-' : 'a-';
      st[id === 'sji-oy' ? 'oYear' : 'aYear'] = Number(el.value);
      if (!st.multi) { Object.keys(st.rows).forEach(function (k) { if (k.indexOf(pre) === 0) { delete st.rows[k].year; } }); }
      return update(true);
    }
    if (id === 'sji-multi') {
      st.multi = el.checked;
      if (!el.checked) { Object.keys(st.rows).forEach(function (k) { delete st.rows[k].year; }); }
      return update(true);
    }
    if (id === 'sji-nums') {
      st.oType = el.checked ? 'number' : 'letter';
      var ok = el.checked ? S.NUMBERS : S.LETTERS;
      Object.keys(st.rows).forEach(function (k) { if (k.indexOf('o-') === 0 && st.rows[k].grade && ok.indexOf(st.rows[k].grade) < 0) { delete st.rows[k].grade; } });
      return update(true);
    }
    if (id === 'sji-eth') { (st.rows['o-isl'] = st.rows['o-isl'] || {}).subj = el.checked ? 'ethics' : 'isl'; return update(true); }
    if (id.indexOf('y-') === 0) { var r = id.slice(2); (st.rows[r] = st.rows[r] || {}).year = Number(el.value); return update(false); }
    if (id.indexOf('g-') === 0) { var g = id.slice(2); (st.rows[g] = st.rows[g] || {}).grade = el.value; return update(false); }
    if (el.classList.contains('sji-subj')) { var s = el.getAttribute('data-subj'); (st.rows[s] = st.rows[s] || {}).subj = el.value; syncDupes(); return update(false); }
  });

  app.addEventListener('click', function (e) {
    var link = e.target.closest ? e.target.closest('a[href^="#sji-faq"]') : null;
    if (link) { var d = document.getElementById(link.getAttribute('href').slice(1)); if (d) { d.open = true; } return; }
    var b = e.target.closest ? e.target.closest('[data-act],[data-bar]') : null;
    if (!b) { return; }
    if (b.hasAttribute('data-bar')) { $('[data-result]').scrollIntoView({ behavior: 'smooth', block: 'start' }); return; }
    var act = b.getAttribute('data-act');
    if (act === 'reset') { st = fresh(); sent = false; update(true); app.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    if (act === 'share' && app._last) {
      var r = app._last;
      var text = 'My IBCC ' + (st.target === 'ssc' ? 'Matric (SSC)' : 'FSc (HSSC)') + ' equivalence: ' + r.marks + '/' + r.scale + ' (' + r.pct.toFixed(2) + '%). Work out yours:';
      var url = '__URL__';
      if (navigator.share) { navigator.share({ title: 'IBCC equivalence', text: text, url: url }).catch(function () { }); }
      else if (navigator.clipboard) { navigator.clipboard.writeText(text + ' ' + url).then(function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Share result'; }, 2000); }); }
    }
  });

  update(true);
})();
