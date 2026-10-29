/* SJ Academy IBCC equivalence engine. Pure functions, no DOM.
   Sources (checked 20 Oct 2026):
   - IBCC grade conversion and yearly A* tables: ibcc.edu.pk/conversion-for-equivalence/
   - IBCC British system requirements and E2 form (subjects, groups, exemptions)
   - IBCC notification IBCC/EC-176/Imp-05/7-2/2026, 17 Feb 2026 (science groups, O Level 2026 cohort onward)
   - IBCC worked examples (O Level x/800*900 = 844, A Level 1030/1100 and 750/800*1100 = 1031) */
var SJI = (function () {
  'use strict';

  var LETTER = { 'A': 85, 'B': 75, 'C': 65, 'D': 55, 'E': 45 };
  var NUMBER = { '8': 87, '7': 82, '6': 77, '5': 70, '4': 60, '3': 50, '2': 40 };
  var LETTERS = ['A*', 'A', 'B', 'C', 'D', 'E'];
  var NUMBERS = ['9', '8', '7', '6', '5', '4', '3', '2'];

  /* A* (and grade 9) marks by level, session and subject. "_" is IBCC's "other subjects" value.
     2020 stands for every session from 2006 to 2020, when A* counted as 90. */
  var ASTAR = {
    O: {
      2020: { _: 90 },
      2021: { math: 95, pst: 93, eng: 93, urdu: 93, _: 94 },
      2022: { cs: 96, _: 95 },
      2023: { math: 95, isl: 95, urdu: 93, _: 94 },
      2024: { phy: 94, chem: 94, bio: 94, cs: 94, math: 94, eng: 93, urdu: 93, pst: 93, isl: 94, _: 94 },
      2025: { phy: 94, chem: 94, bio: 94, cs: 94, math: 94, eng: 93, urdu: 93, pst: 93, isl: 94, _: 94 },
      2026: { phy: 94, chem: 94, bio: 94, cs: 94, math: 94, eng: 93, urdu: 93, pst: 94, isl: 94, _: 94 }
    },
    A: {
      2020: { _: 90 },
      2021: { bio: 94, _: 93 },
      2022: { bio: 94, cs: 94, math: 94, chem: 95, phy: 95, _: 95 },
      2023: { phy: 95, _: 94 },
      2024: { phy: 95, chem: 94, bio: 94, cs: 94, math: 95, _: 94 },
      2025: { phy: 95, chem: 94, bio: 94, cs: 93, math: 94, _: 94 },
      2026: { phy: 95, chem: 94, bio: 94, cs: 93, math: 94, _: 94 }
    }
  };
  var LATEST = 2026;      /* newest session IBCC has published */
  var FORECAST = 2027;    /* first unpublished session: it and later ones use LATEST values, flagged */
  /* A Level subjects IBCC lists as "NA" in the A* table */
  var A_NA = { eng: 1, englit: 1, urdu: 1, isl: 1, pst: 1 };

  var SUBJ = {
    eng: 'English Language', urdu: 'Urdu', isl: 'Islamiyat', ethics: 'Ethics', pst: 'Pakistan Studies',
    math: 'Mathematics', phy: 'Physics', chem: 'Chemistry', bio: 'Biology', cs: 'Computer Science',
    addm: 'Additional Mathematics', ict: 'ICT / Information Technology', acc: 'Accounting', bus: 'Business Studies',
    econ: 'Economics', comm: 'Commerce', soc: 'Sociology', englit: 'English Literature', geo: 'Geography',
    hist: 'History', envm: 'Environmental Management', art: 'Art and Design', stats: 'Statistics',
    arab: 'Arabic', fren: 'French', psy: 'Psychology', fmath: 'Further Mathematics', law: 'Law',
    media: 'Media Studies', it: 'Information Technology', mar: 'Marine Science', other: 'Other academic subject'
  };
  var O_ELECTIVES = ['phy', 'chem', 'bio', 'cs', 'addm', 'ict', 'acc', 'bus', 'econ', 'comm', 'soc', 'englit', 'geo',
    'hist', 'envm', 'art', 'stats', 'arab', 'fren', 'mar', 'other'];
  var A_SUBJECTS = ['phy', 'chem', 'bio', 'math', 'fmath', 'cs', 'it', 'bus', 'econ', 'acc', 'psy', 'soc', 'law',
    'englit', 'eng', 'urdu', 'hist', 'geo', 'media', 'art', 'envm', 'mar', 'other'];
  var GROUPS = {
    pm: { name: 'Pre-Medical', a: ['phy', 'chem', 'bio'], o3: ['bio'], science: true },
    pe: { name: 'Pre-Engineering', a: ['phy', 'chem', 'math'], o3: ['bio', 'cs', 'addm'], science: true },
    cs: { name: 'Computer Science', a: ['phy', 'math', 'cs'], o3: ['bio', 'cs', 'addm'], science: true },
    hum: { name: 'Humanities', a: null, o3: null, science: false }
  };
  var SSC_SCIENCE_THIRD = { bio: 1, cs: 1, ict: 1, addm: 1 };

  function exempt(target, route) {
    if (route === 'foreign') { return true; }
    if (route === 'abroad') { return true; }   /* SSC: O Levels abroad. HSSC: both O and A Levels abroad */
    return false;                              /* 'pk' and HSSC 'mixed' must pass Urdu, Islamiyat, Pak Studies */
  }

  /* The rows the student must fill, in display order */
  function rows(s) {
    var out = [];
    var ex = exempt(s.target, s.route);
    out.push({ id: 'o-eng', level: 'O', fixed: 'eng', kind: 'comp' });
    out.push({ id: 'o-math', level: 'O', fixed: 'math', kind: 'comp' });
    if (!ex) {
      out.push({ id: 'o-urdu', level: 'O', fixed: 'urdu', kind: 'comp' });
      out.push({ id: 'o-isl', level: 'O', fixed: 'isl', alt: ['isl', 'ethics'], kind: 'comp' });
      out.push({ id: 'o-pst', level: 'O', fixed: 'pst', kind: 'comp' });
    }
    var g = s.target === 'hssc' ? GROUPS[s.group] : null;
    if (s.target === 'hssc' && !g) { return out; }
    if (g && g.o3) {
      out.push({ id: 'o-e1', level: 'O', fixed: 'phy', kind: 'elec' });
      out.push({ id: 'o-e2', level: 'O', fixed: 'chem', kind: 'elec' });
      if (g.o3.length === 1) { out.push({ id: 'o-e3', level: 'O', fixed: g.o3[0], kind: 'elec' }); }
      else { out.push({ id: 'o-e3', level: 'O', choose: g.o3, kind: 'elec' }); }
    } else {
      ['o-e1', 'o-e2', 'o-e3'].forEach(function (id) { out.push({ id: id, level: 'O', choose: O_ELECTIVES, kind: 'elec' }); });
    }
    if (g) {
      if (g.a) { g.a.forEach(function (sub, i) { out.push({ id: 'a-' + (i + 1), level: 'A', fixed: sub, kind: 'a' }); }); }
      else { ['a-1', 'a-2', 'a-3'].forEach(function (id) { out.push({ id: id, level: 'A', choose: A_SUBJECTS, kind: 'a' }); }); }
    }
    return out;
  }

  function sessionKey(level, year) {
    var y = Number(year);
    if (y >= FORECAST) { return LATEST; }
    if (y <= 2020) { return 2020; }
    return ASTAR[level][y] ? y : null;
  }

  /* One grade to marks. Returns {marks, flags} or {error} */
  function marks(level, year, subj, grade) {
    var flags = [];
    if (grade in LETTER) { return { marks: LETTER[grade], flags: flags }; }
    if (level === 'O' && grade in NUMBER) { return { marks: NUMBER[grade], flags: flags }; }
    if (grade === 'A*' || (grade === '9' && level === 'O')) {
      var k = sessionKey(level, year);
      if (k === null) { return { error: 'year' }; }
      var t = ASTAR[level][k];
      var key = subj === 'ethics' ? '_' : subj;   /* Ethics is not listed separately */
      if (level === 'A' && A_NA[subj]) { flags.push('a_na'); key = '_'; }
      if (Number(year) >= FORECAST) { flags.push('forecast'); }
      if (grade === '9') { flags.push('nine'); }
      return { marks: key in t ? t[key] : t._, flags: flags };
    }
    return { error: 'grade' };
  }

  function round(x) { return Math.round(x + 1e-9); }
  function pct(v, of) { return Math.round(v / of * 10000) / 100; }

  /* s: {target:'ssc'|'hssc', route:'pk'|'abroad'|'foreign'|'mixed', group, oYear, aYear,
         rows:{id:{subj, grade, year}}} */
  function compute(s) {
    var res = { status: 'incomplete', missing: [], errors: [], flags: [], items: [] };
    if (!s.target) { res.missing.push('target'); return res; }
    if (!s.route || (s.target === 'ssc' && s.route === 'mixed')) { res.missing.push('route'); return res; }
    if (s.target === 'hssc' && !GROUPS[s.group]) { res.missing.push('group'); return res; }
    var list = rows(s), seen = {}, data = s.rows || {}, flagSet = {};
    list.forEach(function (r) {
      var d = data[r.id] || {};
      var subj = r.fixed || null;
      if (r.alt && d.subj && r.alt.indexOf(d.subj) > -1) { subj = d.subj; }
      if (r.choose) { subj = (d.subj && r.choose.indexOf(d.subj) > -1) ? d.subj : null; }
      var year = Number(d.year || (r.level === 'O' ? s.oYear : s.aYear)) || null;
      var item = { id: r.id, level: r.level, kind: r.kind, subj: subj, grade: d.grade || null, year: year };
      res.items.push(item);
      if (!subj) { res.missing.push(r.id + ':subj'); return; }
      var dupKey = r.level + ':' + subj;
      if (seen[dupKey] && subj !== 'other') { res.errors.push({ id: r.id, code: 'dup' }); }
      seen[dupKey] = 1;
      if (!year) { res.missing.push(r.id + ':year'); return; }
      if (!item.grade) { res.missing.push(r.id + ':grade'); return; }
      var m = marks(r.level, year, subj, item.grade);
      if (m.error) { res.errors.push({ id: r.id, code: m.error }); return; }
      item.marks = m.marks;
      m.flags.forEach(function (f) { flagSet[f] = 1; });
    });
    if (res.errors.length) { res.status = 'invalid'; return res; }
    if (res.missing.length) { return res; }

    var ex = exempt(s.target, s.route);
    var O = res.items.filter(function (i) { return i.level === 'O'; });
    var A = res.items.filter(function (i) { return i.level === 'A'; });
    var sum = function (l) { return l.reduce(function (t, i) { return t + i.marks; }, 0); };

    /* SSC part: every O Level row counts (8 in Pakistan, 5 when exempt), scaled to 900 */
    var oRaw = sum(O), oMax = O.length * 100;
    var elec = O.filter(function (i) { return i.kind === 'elec'; }).map(function (i) { return i.subj; });
    var sciSsc = elec.indexOf('phy') > -1 && elec.indexOf('chem') > -1 && elec.some(function (x) { return SSC_SCIENCE_THIRD[x]; });
    var ssc = { raw: oRaw, max: oMax, scale: 900, marks: round(oRaw * 900 / oMax), group: sciSsc ? 'Science' : 'Arts' };
    ssc.pct = pct(ssc.marks, 900);
    if (elec.indexOf('addm') > -1 && elec.indexOf('bio') < 0 && elec.indexOf('cs') < 0 && elec.indexOf('ict') < 0 && sciSsc) { flagSet.addm = 1; }

    if (s.target === 'ssc') {
      res.status = 'ok';
      res.rule = ex ? 'ssc_exempt' : 'ssc_pk';
      res.raw = oRaw; res.max = oMax; res.scale = 900; res.marks = ssc.marks; res.pct = ssc.pct; res.group = ssc.group;
      res.items.forEach(function (i) { i.counted = true; });
      res.flags = Object.keys(flagSet);
      return res;
    }

    /* HSSC */
    var g = GROUPS[s.group];
    var oFinish = Math.max.apply(null, O.map(function (i) { return i.year; }));
    var newRule = g.science && oFinish >= 2026;
    var counted = [];
    res.items.forEach(function (i) {
      var c = i.level === 'A' || i.kind === 'comp' || !newRule;
      i.counted = c;
      if (c) { counted.push(i); }
    });
    var raw = sum(counted), max = counted.length * 100;
    res.status = 'ok';
    res.rule = (newRule ? 'new' : 'legacy') + (ex ? '_exempt' : '_pk');
    res.newRule = newRule;
    res.oFinish = oFinish;
    res.raw = raw; res.max = max; res.scale = 1100;
    res.marks = round(raw * 1100 / max);
    res.pct = pct(res.marks, 1100);
    res.group = g.name;
    res.ssc = ssc;
    if (newRule) { flagSet.new_scale = 1; }
    if (s.group === 'cs' && ex) { flagSet.cs_abroad = 1; }
    res.flags = Object.keys(flagSet);
    return res;
  }

  /* Next grade up for tips */
  function nextUp(grade) {
    var l = LETTERS.indexOf(grade); if (l > 0) { return LETTERS[l - 1]; }
    var n = NUMBERS.indexOf(grade); if (n > 0) { return NUMBERS[n - 1]; }
    return null;
  }

  /* Best single improvement: the counted subject with the lowest marks that can still go up.
     For HSSC, A Levels win ties because students can still resit them. */
  function tip(s, res) {
    if (res.status !== 'ok') { return null; }
    var best = null;
    res.items.forEach(function (i) {
      if (!i.counted) { return; }
      var up = nextUp(i.grade); if (!up) { return; }
      var score = i.marks - (i.level === 'A' ? 0.5 : 0);
      if (!best || score < best.score) { best = { item: i, up: up, score: score }; }
    });
    if (!best) { return null; }
    var copy = JSON.parse(JSON.stringify(s));
    copy.rows = copy.rows || {};
    copy.rows[best.item.id] = copy.rows[best.item.id] || {};
    copy.rows[best.item.id].grade = best.up;
    if (best.item.subj && !copy.rows[best.item.id].subj) { copy.rows[best.item.id].subj = best.item.subj; }
    var r2 = compute(copy);
    return { id: best.item.id, level: best.item.level, subj: best.item.subj, from: best.item.grade, to: best.up,
      marks: r2.marks, pct: r2.pct, gain: r2.marks - res.marks };
  }

  return { compute: compute, rows: rows, marks: marks, tip: tip, exempt: exempt, ASTAR: ASTAR, LETTER: LETTER,
    NUMBER: NUMBER, LETTERS: LETTERS, NUMBERS: NUMBERS, SUBJ: SUBJ, GROUPS: GROUPS, O_ELECTIVES: O_ELECTIVES,
    A_SUBJECTS: A_SUBJECTS, LATEST: LATEST, FORECAST: FORECAST };
})();
if (typeof module !== 'undefined') { module.exports = SJI; }
