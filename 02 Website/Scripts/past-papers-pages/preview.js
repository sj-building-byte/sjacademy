// Renders a built past papers page with the shared stylesheet, checks it, and saves screenshots.
// Run: node preview.js ../../Pages/o-level-pakistan-studies-past-papers-elementor-widget.html [screenshot folder]
// Prints the PDF links to links-<file>.txt next to the screenshots for check-files.py style verification.
const { chromium, devices } = require('playwright');
const fs = require('fs');
const path = require('path');

const FILE = process.argv[2];
const SHOTS = process.argv[3] || '.';
const widget = fs.readFileSync(FILE, 'utf8');
const css = fs.readFileSync(path.join(__dirname, '..', '..', '..', '01 Brand', 'sj-brand.css'), 'utf8');
const PAGE = 'https://www.sjacademy.pk/preview/';
const name = path.basename(FILE, '.html');
let failed = 0;
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) failed++; };

(async () => {
  const browser = await chromium.launch();
  for (const [label, ctx] of [['desktop', { viewport: { width: 1366, height: 900 } }], ['phone', devices['Pixel 7']]]) {
    const page = await (await browser.newContext(ctx)).newPage();
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.addInitScript(() => { window.__ev = []; window.gtag = (a, n, p) => window.__ev.push([n, p]); });
    await page.route('**/*', (r) => r.request().url().startsWith(PAGE)
      ? r.fulfill({ contentType: 'text/html', body: '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>' + css + '</style></head><body style="margin:0">' + widget + '</body></html>' })
      : r.abort());
    await page.goto(PAGE);
    await page.waitForTimeout(300);
    if (label === 'desktop') {
      ok((await page.$$('h1')).length === 1, 'One H1');
      const tabs = await page.$$eval('[role=tab]', (t) => t.map((x) => x.textContent));
      ok(tabs.length > 0 && (await page.isVisible('#sjp-tabs')), 'Year tabs show: ' + tabs.join(' '));
      const visiblePanels = await page.$$eval('.sjp-year', (p) => p.filter((x) => !x.hidden).length);
      ok(visiblePanels === 1, 'One year shown at a time');
      await page.click('[role=tab]:last-child');
      ok(await page.$eval('.sjp-year:last-of-type', (p) => !p.hidden), 'Clicking the last tab shows the oldest year');
      const pick = await page.$$eval('input[name="sjp-p"]', (i) => i.map((x) => x.value).filter(Boolean)[1]);
      await page.click('input[name="sjp-p"][value="' + pick + '"]', { force: true });
      const shown = await page.$$eval('.sjp-year:not([hidden]) tr[data-paper]', (r) => r.filter((x) => !x.hidden).map((x) => x.getAttribute('data-paper')));
      ok(shown.length > 0 && shown.every((p) => p === pick), 'Paper filter shows only Paper ' + pick);
      const links = await page.$$eval('a[href$=".pdf"]', (a) => a.map((x) => x.href));
      fs.writeFileSync(path.join(SHOTS, 'links-' + name + '.txt'), links.join('\n') + '\n');
      ok(links.length > 0, links.length + ' PDF links in the HTML');
      const ld = await page.$$eval('script[type="application/ld+json"]', (s) => s.map((x) => JSON.parse(x.textContent)['@type']));
      ok(ld.join() === 'CollectionPage,BreadcrumbList,FAQPage', 'Structured data parses: ' + ld.join(', '));
      await page.click('input[name="sjp-p"][value=""]', { force: true });
      await page.click('[role=tab]:first-child');
    }
    await page.screenshot({ path: path.join(SHOTS, name + '-' + label + '.png'), fullPage: true });
    ok(errors.length === 0, label + ': no script errors ' + errors.join(' | '));
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    ok(overflow <= 0, label + ': no sideways scroll (' + overflow + 'px)');
  }
  await browser.close();
  process.exit(failed ? 1 : 0);
})();
