// Browser tests for the past paper viewer. The file host is mocked, so this runs without sjacademy.pk.
// Run: node "02 Website/Tools/Past Paper Viewer/tests/viewer-test.js" [widget.html] [screenshot folder]
// Needs Playwright (require('playwright')). Exits with code 1 if any check fails.
const { chromium, devices } = require('playwright');
const fs = require('fs');
const path = require('path');

const WIDGET = process.argv[2] || path.join(__dirname, '..', 'past-paper-viewer-elementor-widget.html');
const SHOTS = process.argv[3] || '';
const fullWidget = fs.readFileSync(WIDGET, 'utf8');
// These tests check the built-in rules against a mocked host, so the real file list is set aside here.
// verify-links.js checks the real list against Backblaze.
const widget = fullWidget.replace(/var FILES = .*;\n/, 'var FILES = {};\n');
const PAGE = 'https://www.sjacademy.pk/past-paper-viewer/';
const FILE = 'https://sjacademy.pk/file/Past-papers-storage/';
const PDF = Buffer.from('%PDF-1.1\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj 3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 300 300]>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF');

// Files that "exist" on the mock host, relative to the storage base
const STORE = new Set([
  'O+Level/Accounts+%287707%29/May+June+2024/7707_s24_qp_12.pdf',
  'O+Level/Accounts+%287707%29/May+June+2024/7707_s24_ms_12.pdf',
  'O+Level/Pakistan+Studies+%282059%29/May+June+2024/2059_s24_qp_01.pdf',
  'O+Level/Pakistan+Studies+%282059%29/May+June+2024/2059_s24_ms_1.pdf',
  'O+Level/Pakistan+Studies+%282059%29/May+June+2024/2059_s24_in_01.pdf',
  'A+Level/Business+%289609%29/May+June+2024/9609_s24_qp_32.pdf',
  'A+Level/Business+%289609%29/May+June+2024/9609_s24_ms_32.pdf',
  'A+Level/Business+%289609%29/May+June+2024/9609_s24_in_32.pdf',
  'A+Level/Business+%289609%29/October+November+2024/9609_w24_qp_43.pdf',
  'A+Level/Physics+%289702%29/May+June+2024/9702_s24_qp_34.pdf',
  'A+Level/Physics+%289702%29/May+June+2024/9702_s24_ms_34.pdf',
  'A+Level/Physics+%289702%29/May+June+2024/9702_s24_ci_34.pdf'
]);

let failed = 0;
function ok(cond, name) { console.log((cond ? 'PASS ' : 'FAIL ') + name); if (!cond) failed++; }

async function open(browser, { query = '', cors = true, ctx = {}, init = '' } = {}) {
  const context = await browser.newContext(ctx);
  const page = await context.newPage();
  const hits = [];
  // Headless Chromium has no PDF viewer; desktop Chrome, Edge, Safari and Firefox do. Simulate them unless a test says otherwise.
  await page.addInitScript(init || "Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true, configurable: true })");
  await page.addInitScript(() => { window.__ev = []; window.gtag = function (a, n, p) { window.__ev.push([n, p]); }; });
  await page.route('**/*', (route) => {
    const url = route.request().url();
    if (url.startsWith(PAGE)) return route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">' + widget + '</body></html>' });
    if (url.startsWith(FILE)) {
      const rel = url.slice(FILE.length).split('#')[0];
      hits.push([route.request().method(), rel]);
      const headers = cors ? { 'access-control-allow-origin': 'https://www.sjacademy.pk' } : {};
      if (STORE.has(rel)) return route.fulfill({ status: 200, contentType: 'application/pdf', headers, body: PDF });
      return route.fulfill({ status: 404, contentType: 'application/json', headers, body: '{"code":"not_found","message":"File with such name does not exist.","status":404}' });
    }
    return route.abort();
  });
  await page.goto(PAGE + query);
  return { page, context, hits };
}

async function pick(page, level, subject, year, paper) {
  await page.selectOption('#sjpv-level', level);
  await page.selectOption('#sjpv-subject', subject);
  if (year) await page.selectOption('#sjpv-year', year);
  if (paper) await page.selectOption('#sjpv-paper', paper);
  await page.waitForTimeout(400);
}
const opts = (page, sel) => page.$$eval(sel + ' option', (o) => o.map((x) => x.textContent));
const src = (page, id) => page.getAttribute(id, 'data-url');
const visible = (page, sel) => page.isVisible(sel);

(async () => {
  const browser = await chromium.launch();
  const errors = [];

  // 1. O Level Accounting: the folder is "Accounts (7707)" in storage
  let { page, context } = await open(browser, { ctx: { viewport: { width: 1366, height: 900 } } });
  page.on('pageerror', (e) => errors.push(e.message));
  await pick(page, 'O Level', 'Accounting', '2024 May/June', 'Paper 1, Variant 2');
  ok((await src(page, '#sjpv-frame-left')).includes('Accounts+%287707%29/May+June+2024/7707_s24_qp_12.pdf'), 'Accounting question paper loads from Accounts (7707)');
  ok((await src(page, '#sjpv-frame-right')).endsWith('7707_s24_ms_12.pdf'), 'Accounting mark scheme loads');
  ok(!(await visible(page, '#sjpv-left-gone')), 'Accounting: no missing-file message');
  ok((await opts(page, '#sjpv-subject')).includes('Accounting (7707)'), 'Subject list shows codes');
  ok(!(await visible(page, '#sjpv-actions')), 'Accounting: no Insert button (7707 Paper 1 has none)');
  // Lock and toggle
  ok(await visible(page, '#sjpv-lock'), 'Mark scheme starts locked');
  await page.click('#sjpv-unlock');
  await page.waitForTimeout(300);
  ok(!(await visible(page, '#sjpv-lock')) && (await page.getAttribute('#sjpv-learn', 'aria-pressed')) === 'true', 'Unlock button reveals the mark scheme');
  await page.click('#sjpv-cheat');
  ok(await visible(page, '#sjpv-lock'), "Don't cheat locks it again");
  await page.click('#sjpv-learn');
  await page.waitForTimeout(300);
  ok(!(await visible(page, '#sjpv-lock')), 'Learn toggle reveals');
  // Missing paper
  await page.selectOption('#sjpv-paper', 'Paper 2, Variant 1');
  await page.waitForTimeout(400);
  ok(await visible(page, '#sjpv-left-gone'), 'Missing paper shows the friendly message');
  ok((await src(page, '#sjpv-frame-left')) === '', 'Missing paper is not loaded into the frame');
  // Full screen
  await page.selectOption('#sjpv-paper', 'Paper 1, Variant 2');
  await page.waitForTimeout(300);
  await page.click('#sjpv-full');
  await page.waitForTimeout(300);
  ok(await page.$eval('#sjpv', (r) => r.classList.contains('is-full')), 'Full screen opens');
  await page.click('#sjpv-full');
  await page.waitForTimeout(300);
  ok(!(await page.$eval('#sjpv', (r) => r.classList.contains('is-full'))), 'Full screen closes');
  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'desktop-accounting.png'), fullPage: true });
  const ev = await page.evaluate(() => window.__ev.map((e) => e[0]));
  ok(['tool_start', 'tool_complete', 'mark_scheme_reveal', 'paper_unavailable', 'fullscreen_open'].every((n) => ev.includes(n)), 'GA4 events fire: ' + [...new Set(ev)].join(', '));
  ok(page.url().includes('level=o-level') && page.url().includes('subject=accounting') && page.url().includes('series=2024-mj') && page.url().includes('paper=12') && !page.url().includes('year='), 'Address bar holds the deep link, with series not year');
  ok(!page.url().includes('marks='), 'A new paper relocks and drops marks=show');
  await page.click('#sjpv-learn');
  ok(page.url().includes('marks=show'), 'Address bar adds marks=show while the mark scheme is open');
  await page.click('#sjpv-cheat');
  ok(!page.url().includes('marks='), "Don't cheat removes marks=show");
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.click('#sjpv-share');
  await page.waitForTimeout(200);
  const shared = await page.evaluate(() => navigator.clipboard.readText());
  ok(shared === 'https://www.sjacademy.pk/past-paper-viewer/?level=o-level&subject=accounting&series=2024-mj&paper=12&marks=show', 'Share copies the link with the mark scheme open: ' + shared);
  ok((await page.textContent('#sjpv-share')) === 'Link copied', 'Share button confirms the copy');
  await context.close();

  // 2. Pakistan Studies: one paper per component, qp_01 and ms_1
  ({ page, context } = await open(browser, { ctx: { viewport: { width: 1366, height: 900 } } }));
  await pick(page, 'O Level', 'Pakistan Studies', '2024 May/June');
  ok(JSON.stringify(await opts(page, '#sjpv-paper')) === JSON.stringify(['Choose paper', 'Paper 1', 'Paper 2']), 'Pakistan Studies offers Paper 1 and Paper 2 (no variants)');
  await page.selectOption('#sjpv-paper', 'Paper 1');
  await page.waitForTimeout(400);
  ok((await src(page, '#sjpv-frame-left')).endsWith('2059_s24_qp_01.pdf'), 'Pakistan Studies question paper is qp_01');
  ok((await src(page, '#sjpv-frame-right')).endsWith('2059_s24_ms_1.pdf'), 'Pakistan Studies mark scheme is ms_1');
  ok(await visible(page, '#sjpv-actions button'), 'Pakistan Studies shows the Insert button');
  // Biology papers by syllabus
  await pick(page, 'O Level', 'Biology', '2024 May/June');
  const bio24 = await opts(page, '#sjpv-paper');
  ok(bio24.includes('Paper 4, Variant 1') && !bio24.some((t) => t.startsWith('Paper 6')), 'Biology 2024 has Paper 4, not Paper 6');
  await page.selectOption('#sjpv-year', '2021 May/June');
  const bio21 = await opts(page, '#sjpv-paper');
  ok(bio21.includes('Paper 6, Variant 1') && !bio21.some((t) => t.startsWith('Paper 4')), 'Biology 2021 has Paper 6, not Paper 4');
  await pick(page, 'A Level', 'Physics', '2024 May/June');
  ok((await opts(page, '#sjpv-paper')).includes('Paper 3, Variant 5'), 'A Level Physics offers practical variants up to 35');
  await page.selectOption('#sjpv-paper', 'Paper 3, Variant 4');
  await page.waitForTimeout(400);
  ok((await page.$$eval('#sjpv-actions button', (b) => b.map((x) => x.textContent))).join() === 'Confidential', 'Physics 34 shows Confidential only (no insert in storage)');
  await pick(page, 'A Level', 'Mathematics', '2024 May/June');
  ok((await opts(page, '#sjpv-paper')).includes('Paper 2, Variant 1'), 'A Level Maths includes Paper 2');
  await context.close();

  // 3. Deep link with insert
  ({ page, context } = await open(browser, { query: '?level=a-level&subject=business&series=2024-mj&paper=32&utm_source=ig', ctx: { viewport: { width: 1280, height: 860 } } }));
  await page.waitForTimeout(500);
  ok((await src(page, '#sjpv-frame-left')).endsWith('9609_s24_qp_32.pdf'), 'Deep link opens Business 9609/32');
  ok(page.url().includes('utm_source=ig'), 'Deep link keeps utm tags');
  await page.click('#sjpv-actions button');
  await page.waitForTimeout(300);
  ok((await src(page, '#sjpv-frame-left')).endsWith('9609_s24_in_32.pdf') && (await page.textContent('#sjpv-left-title')) === 'Insert', 'Insert opens in the left pane');
  const ev3 = await page.evaluate(() => window.__ev.filter((e) => e[0] === 'tool_complete').map((e) => e[1].entry));
  ok(ev3[0] === 'link', 'tool_complete marks entry = link');
  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'desktop-business-insert.png') });
  await context.close();

  // 3b. A shared link opens the paper and the mark scheme
  ({ page, context } = await open(browser, { query: '?level=o-level&subject=pakistan-studies&series=2024-mj&paper=1&marks=show', ctx: { viewport: { width: 1280, height: 860 } } }));
  await page.waitForTimeout(500);
  ok((await src(page, '#sjpv-frame-left')).endsWith('2059_s24_qp_01.pdf') && (await src(page, '#sjpv-frame-right')).endsWith('2059_s24_ms_1.pdf'), 'Shared link loads paper and mark scheme');
  ok(!(await visible(page, '#sjpv-lock')) && (await page.getAttribute('#sjpv-learn', 'aria-pressed')) === 'true', 'Shared link opens with the mark scheme showing');
  await context.close();
  ({ page, context } = await open(browser, { query: '?level=o-level&subject=pakistan-studies&series=2024-mj&paper=1&marks=show', ctx: { ...devices['Pixel 7'] }, init: "Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => false, configurable: true })" }));
  await page.waitForTimeout(500);
  ok(await visible(page, '#sjpv-share'), 'Phone: Share button shows');
  await page.click('#sjpv-bar button[data-k="ms"]');
  ok(!(await visible(page, '#sjpv-lock')) && (await visible(page, '#sjpv-right-open')), 'Phone: shared link opens with the mark scheme unlocked');
  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'phone-shared.png') });
  await context.close();
  ({ page, context } = await open(browser, { query: '?level=a-level&subject=business&year=2024-mj&paper=32', ctx: { viewport: { width: 1280, height: 860 } } }));
  await page.waitForTimeout(400);
  ok((await src(page, '#sjpv-frame-left')).endsWith('9609_s24_qp_32.pdf') && page.url().includes('series=2024-mj') && !page.url().includes('year='), 'Old year= links still open and are rewritten to series=');
  await context.close();

  // 4. File host blocks the check (no CORS): frames still load
  ({ page, context } = await open(browser, { cors: false, ctx: { viewport: { width: 1280, height: 860 } } }));
  await pick(page, 'A Level', 'Business', '2024 May/June', 'Paper 3, Variant 2');
  ok((await src(page, '#sjpv-frame-left')).endsWith('9609_s24_qp_32.pdf'), 'Without CORS the paper still loads');
  await context.close();

  // 5. Phone
  ({ page, context } = await open(browser, { ctx: { ...devices['Pixel 7'] }, init: "Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => false, configurable: true })" }));
  await pick(page, 'O Level', 'Pakistan Studies', '2024 May/June', 'Paper 1');
  ok(await visible(page, '#sjpv-bar'), 'Phone: bottom bar shows');
  ok((await page.getAttribute('#sjpv-left-open', 'href')).endsWith('2059_s24_qp_01.pdf'), 'Phone: open link points at the paper');
  ok((await src(page, '#sjpv-frame-left')) === '', 'Phone: no iframe load');
  ok((await page.$$eval('#sjpv-bar button', (b) => b.map((x) => x.textContent))).join() === 'Paper,Insert,Mark scheme', 'Phone: bar has Paper, Insert, Mark scheme');
  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'phone-paper.png'), fullPage: true });
  await page.click('#sjpv-bar button[data-k="ms"]');
  ok(await visible(page, '#sjpv-lock'), 'Phone: mark scheme locked');
  await page.click('#sjpv-unlock');
  ok(await visible(page, '#sjpv-right-open'), 'Phone: open mark scheme after unlock');
  await page.waitForTimeout(300);
  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, 'phone-ms.png') });
  await context.close();

  // 6. Phone turned sideways and a browser without a PDF viewer get the phone layout
  ({ page, context } = await open(browser, { ctx: { viewport: { width: 915, height: 412 }, hasTouch: true, isMobile: true } }));
  await pick(page, 'O Level', 'Accounting', '2024 May/June', 'Paper 1, Variant 2');
  ok(await page.$eval('#sjpv', (r) => r.classList.contains('is-compact')), 'Landscape phone uses the phone layout');
  await context.close();
  ({ page, context } = await open(browser, { ctx: { viewport: { width: 1280, height: 800 } }, init: "Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => false, configurable: true })" }));
  await pick(page, 'O Level', 'Accounting', '2024 May/June', 'Paper 1, Variant 2');
  ok(await page.$eval('#sjpv', (r) => r.classList.contains('is-compact')) && (await src(page, '#sjpv-frame-left')) === '', 'No built-in PDF viewer: phone layout, no blank frames');
  await context.close();

  // 7. Folder fallback: storage holds the hub name instead
  const alt = 'O+Level/Accounting+%287707%29/May+June+2024/7707_s24_qp_12.pdf';
  STORE.add(alt); STORE.add(alt.replace('qp', 'ms'));
  STORE.delete('O+Level/Accounts+%287707%29/May+June+2024/7707_s24_qp_12.pdf');
  ({ page, context } = await open(browser, { ctx: { viewport: { width: 1280, height: 860 } } }));
  await pick(page, 'O Level', 'Accounting', '2024 May/June', 'Paper 1, Variant 2');
  await page.waitForTimeout(300);
  ok((await src(page, '#sjpv-frame-left')).includes('Accounting+%287707%29'), 'Falls back to the second folder name when the first is missing');
  await context.close();

  // 8. FILES written by check-files.py: dropdowns show exactly the files in storage
  const listed = widget.replace('var FILES = {};', 'var FILES = {"O Level/Accounting":{"f":"Accounts (7707)","s":{"s24":"qp_12 ms_12","w24":"qp_12 ms_12 qp_13 ms_13 qp_22"}}};');
  ok(listed !== widget, 'FILES line found in the widget');
  const context8 = await browser.newContext({ viewport: { width: 1280, height: 860 } });
  const page8 = await context8.newPage();
  await page8.addInitScript("Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true, configurable: true })");
  const heads = [];
  await page8.route('**/*', (route) => {
    const url = route.request().url();
    if (url.startsWith(PAGE)) return route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body style="margin:0">' + listed + '</body></html>' });
    if (url.startsWith(FILE)) { heads.push(route.request().method()); return route.fulfill({ status: 200, contentType: 'application/pdf', body: PDF }); }
    return route.abort();
  });
  await page8.goto(PAGE);
  await pick(page8, 'O Level', 'Accounting');
  ok(JSON.stringify(await opts(page8, '#sjpv-year')) === JSON.stringify(['Choose year', '2024 Oct/Nov', '2024 May/June']), 'FILES: only series in storage are offered');
  await page8.selectOption('#sjpv-year', '2024 Oct/Nov');
  ok(JSON.stringify(await opts(page8, '#sjpv-paper')) === JSON.stringify(['Choose paper', 'Paper 1, Variant 2', 'Paper 1, Variant 3', 'Paper 2, Variant 2']), 'FILES: only papers in storage are offered, variant 3 included');
  await page8.selectOption('#sjpv-paper', 'Paper 2, Variant 2');
  await page8.waitForTimeout(400);
  ok(await page8.isVisible('#sjpv-right-gone'), 'FILES: a missing mark scheme is shown as missing');
  ok(!heads.includes('HEAD'), 'FILES: no background checks needed');
  await context8.close();

  // 9. The real file list in the widget: the two cases Sunyyan reported on 30 October
  if (/var FILES = \{"/.test(fullWidget)) {
    const context9 = await browser.newContext({ viewport: { width: 1280, height: 860 } });
    const page9 = await context9.newPage();
    await page9.addInitScript("Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true, configurable: true })");
    await page9.route('**/*', (route) => {
      const url = route.request().url();
      if (url.startsWith(PAGE)) return route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body style="margin:0">' + fullWidget + '</body></html>' });
      if (url.startsWith(FILE)) return route.fulfill({ status: 200, contentType: 'application/pdf', body: PDF });
      return route.abort();
    });
    await page9.goto(PAGE);
    await pick(page9, 'A Level', 'Biology', '2025 May/June', 'Paper 3, Variant 3');
    ok(!(await page9.isVisible('#sjpv-actions button')), 'Real list: A Level Biology 2025 has no Confidential button (none in storage)');
    await pick(page9, 'O Level', 'Accounting', '2025 Oct/Nov');
    const acc = await opts(page9, '#sjpv-paper');
    ok(!acc.includes('Paper 2, Variant 1') && acc.includes('Paper 1, Variant 2'), 'Real list: O Level Accounting Oct/Nov 2025 offers only stored variants: ' + acc.slice(1).join(', '));
    await page9.selectOption('#sjpv-paper', 'Paper 1, Variant 2');
    await page9.waitForTimeout(300);
    ok((await src(page9, '#sjpv-frame-right')).endsWith('Accounts+%287707%29/October+November+2025/7707_w25_ms_12.pdf'), 'Real list: Accounting 7707_w25_ms_12 (the file in your Backblaze screenshot) opens');
    await pick(page9, 'A Level', 'Urdu', '2025 May/June');
    ok(JSON.stringify((await opts(page9, '#sjpv-paper')).slice(1)) === JSON.stringify(['Paper 2', 'Paper 3', 'Paper 4']), 'Real list: A Level Urdu shows Paper 2, 3, 4');
    await pick(page9, 'A Level', 'Computer Science');
    const csYears = await opts(page9, '#sjpv-year');
    ok(csYears.includes('2021 Oct/Nov (old 9608)') && csYears.includes('2022 May/June') && !csYears.includes('2022 May/June (old 9608)'), 'Real list: Computer Science years up to 2021 are labelled old 9608');
    await context9.close();
    const c10 = await browser.newContext({ viewport: { width: 1280, height: 860 } });
    const p10 = await c10.newPage();
    await p10.addInitScript("Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true, configurable: true })");
    await p10.route('**/*', (route) => route.request().url().startsWith(PAGE) ? route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body>' + fullWidget + '</body></html>' }) : route.fulfill({ status: 200, contentType: 'application/pdf', body: PDF }));
    await p10.goto(PAGE + '?level=a-level&subject=computer-science&series=2021-on&paper=12');
    await p10.waitForTimeout(400);
    ok((await src(p10, '#sjpv-frame-left')).endsWith('9618_w21_qp_12.pdf') && p10.url().includes('series=2021-on'), 'Real list: deep link to an old 9608 series still works');
    await c10.close();
  }

  ok(errors.length === 0, 'No script errors' + (errors.length ? ': ' + errors.join(' | ') : ''));
  await browser.close();
  console.log(failed ? '\n' + failed + ' failed' : '\nAll passed');
  process.exit(failed ? 1 : 0);
})();
