// Lists every file link the viewer can open, by working through every Level, Subject, Year and Paper
// in a browser, plus each Insert and Confidential button. The links then go to check-files.py --verify.
// Run: node "02 Website/Tools/Past Paper Viewer/tests/list-links.js" > links.txt
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const WIDGET = process.argv[2] || path.join(__dirname, '..', 'past-paper-viewer-elementor-widget.html');
const widget = fs.readFileSync(WIDGET, 'utf8');
const PAGE = 'https://www.sjacademy.pk/past-paper-viewer/';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 860 } });
  await page.addInitScript("Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true })");
  await page.route('**/*', (route) => {
    if (route.request().url().startsWith(PAGE)) return route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body>' + widget + '</body></html>' });
    return route.abort();
  });
  await page.goto(PAGE);
  const links = await page.evaluate(() => {
    const $ = (id) => document.getElementById('sjpv-' + id);
    const set = (sel, v) => { sel.value = v; sel.dispatchEvent(new Event('change')); };
    const vals = (sel) => Array.from(sel.options).map((o) => o.value).filter(Boolean);
    const out = [];
    vals($('level')).forEach((lv) => {
      set($('level'), lv);
      vals($('subject')).forEach((su) => {
        set($('subject'), su);
        vals($('year')).forEach((yr) => {
          set($('year'), yr);
          vals($('paper')).forEach((pp) => {
            set($('paper'), pp);
            const tag = [lv, su, yr, pp].join(' | ');
            out.push(tag + ' | paper | ' + ($('left-gone').hidden ? 'offered' : 'marked missing') + ' | ' + $('left-open').href);
            out.push(tag + ' | mark scheme | ' + ($('right-gone').hidden ? 'offered' : 'marked missing') + ' | ' + $('right-open').href);
            Array.from($('actions').querySelectorAll('button')).map((b) => b.textContent).forEach((name) => {
              const b = Array.from($('actions').querySelectorAll('button')).find((x) => x.textContent === name);
              b.click();
              out.push(tag + ' | ' + name.toLowerCase() + ' | ' + ($('left-gone').hidden ? 'offered' : 'marked missing') + ' | ' + $('left-open').href);
              $('actions').querySelector('button').click();
            });
          });
        });
      });
    });
    return out;
  });
  process.stdout.write(links.join('\n') + '\n');
  await browser.close();
})();
