import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const pages = [
  'index.html', 'ui-design.html', 'graphic-design.html',
  'ImHere-case-study/imhere-case-study.html', 'aurea.html',
  'experiences/imhere.html', 'experiences/aurea.html',
  'psychictally.html', 'psychictally/welcome-email.html',
  'graphic-editions.html', 'about.html', 'design-profile.html',
  'plain-sight/index.html', 'plain-sight/case-study.html', 'plain-sight/studio.html',
  'plain-sight/gestures.html', 'plain-sight/arrangements.html', 'plain-sight/in-between.html',
  'plain-sight/publication.html', 'plain-sight/email.html', 'plain-sight/motion.html', 'plain-sight/contact.html'
];
const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');

test('all active portfolio page assets and internal destinations resolve', () => {
  for (const page of pages) {
    const html = read(page);
    const ids = new Set(Array.from(html.matchAll(/\bid=["']([^"']+)["']/g), (m) => m[1]));
    for (const match of html.matchAll(/\b(?:href|src)=["']([^"']+)["']/g)) {
      const ref = match[1];
      if (/^(https?:|mailto:|tel:|data:|javascript:)/.test(ref)) continue;
      if (ref.startsWith('#')) {
        assert.ok(ids.has(ref.slice(1)), page + ' missing same-page anchor: ' + ref);
        continue;
      }
      const base = ref.split('#', 1)[0].split('?', 1)[0];
      const resolved = path.resolve(root, path.dirname(page), base);
      assert.ok(resolved.startsWith(root + path.sep), 'External local file path in ' + page + ': ' + ref);
      assert.ok(fs.existsSync(resolved), page + ' missing local reference: ' + ref);
    }
  }
});

test('homepage filter routes include only existing cards and curate four featured projects', () => {
  const index = read('index.html');
  const routes = read('work-paths.js');
  const cards = new Set(Array.from(index.matchAll(/\bdata-project="([^"]+)"/g), (m) => m[1]));
  assert.equal(cards.size, 12);
  assert.ok(cards.has('psychictally'));
  assert.ok(cards.has('plain-sight'));
  assert.ok(fs.existsSync(path.join(root,'plain-sight/downloads/PLAIN_SIGHT_Studies_01-03.pdf')));
  const groups = Array.from(routes.matchAll(/ids:\[([^\]]+)\]/g), (m) =>
    Array.from(m[1].matchAll(/"([^"]+)"/g), (v) => v[1]));
  assert.equal(groups.length, 6);
  assert.equal(groups[0].length, 4);
  assert.equal(groups[1].length, cards.size);
  for (const group of groups) for (const id of group) assert.ok(cards.has(id), 'Missing card ' + id);
});

test('new portfolio images have alt text and prototype is disclosed as illustrative', () => {
  for (const page of ['ui-design.html', 'graphic-design.html', 'psychictally.html']) {
    for (const tag of read(page).match(/<img\b[^>]*>/g) || [])
      assert.match(tag, /\balt=["'][^"']+["']/);
  }
  const caseStudy = read('psychictally.html');
  assert.match(caseStudy, /not wired to PsychicTally's production database/);
  assert.match(caseStudy, /research plan is written/i);
});
