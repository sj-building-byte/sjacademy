// Opens every "Side by side" link on the built pages in the real viewer widget and checks the viewer
// loads the same question paper the row links to.
// Run: node check-side-links.js ../../Pages/o-level-*-past-papers-elementor-widget.html ../../Pages/a-level-urdu-past-papers-elementor-widget.html
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const VIEWER = fs.readFileSync(path.join(__dirname, '..', '..', 'Tools', 'Past Paper Viewer', 'past-paper-viewer-elementor-widget.html'), 'utf8');
const files = process.argv.slice(2);
const decode = (s) => s.replace(/&amp;/g, '&');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.addInitScript("Object.defineProperty(navigator, 'pdfViewerEnabled', { get: () => true })");
  await page.route('**/*', (r) => r.request().url().startsWith('https://www.sjacademy.pk/past-paper-viewer/')
    ? r.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body>' + VIEWER + '</body></html>' })
    : r.abort());
  let total = 0, bad = 0;
  for (const f of files) {
    const html = fs.readFileSync(f, 'utf8');
    // each cell: links then the side link; pair the side link with the QP link in the same cell
    const cells = html.match(/<td data-label="[^"]*"><span>(?:(?!<\/td>).)*class="sjp-side"(?:(?!<\/td>).)*<\/td>/g) || [];
    let n = 0, wrong = [];
    for (const c of cells) {
      const qp = decode((c.match(/href="([^"]+_qp_[^"]+\.pdf)"/) || [])[1] || '');
      const side = decode((c.match(/class="sjp-side" href="([^"]+)"/) || [])[1] || '');
      await page.goto(side);
      const got = await page.getAttribute('#sjpv-left-open', 'href');
      n++;
      if (got !== qp) wrong.push(side + ' -> ' + got + ' (expected ' + qp + ')');
    }
    total += n; bad += wrong.length;
    console.log(path.basename(f) + ': ' + n + ' side by side links, ' + wrong.length + ' wrong' + (wrong.length ? '\n  ' + wrong.slice(0, 5).join('\n  ') : ''));
  }
  console.log(total + ' links checked, ' + bad + ' wrong');
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
