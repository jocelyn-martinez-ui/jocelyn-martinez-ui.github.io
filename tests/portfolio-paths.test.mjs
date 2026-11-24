import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const pages = [
  'index.html', 'ui-design.html', 'graphic-design.html',
  'playground.html', 'studio-reframes.html', 'production-specimens.html', 'service-specimens.html',
  'poster.html', 'website.html', 'websiteex.html', 'roseedit.html',
  'Holland-Walking-Tour-site/holland-walking-tour-case-study.html',
  'ImHere-case-study/imhere-case-study.html', 'aurea.html',
  'experiences/imhere.html', 'experiences/aurea.html',
  'psychictally.html', 'psychictally/welcome-email.html',
  'graphic-editions.html', 'about.html', 'design-profile.html',
  'proof/index.html', 'brume/index.html',
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

test('the first four visible home projects match the enhanced featured selection', () => {
  const home = read('index.html');
  const visible = Array.from(home.matchAll(/<article\b[^>]*data-project="([^"]+)"[^>]*>/g))
    .filter(([tag]) => !/\shidden\b/.test(tag))
    .map(([, id]) => id);
  assert.deepEqual(visible, ['imhere', 'brume', 'holland', 'plain-sight']);
  const featured = read('work-paths.js').match(/featured:\{ids:(\[[^\]]+\])/);
  assert.deepEqual(JSON.parse(featured[1]), visible);
});

test('shareable sections keep the relevant original artifact in the section', () => {
  const routes = [
    ['graphic-design.html', 'production', ['proof/assets/campaign-01.webp', 'proof/assets/print-advert.webp', 'proof/PRODUCTION_NOTES.md', 'proof/emails/01-launch.html']],
    ['graphic-design.html', 'email', ['brume/email/01-introduction.html', 'brume/email/01-introduction.txt']],
    ['graphic-design.html', 'editorial', ['plain-sight/publication.html?page=6#reader', 'plain-sight/publication.html?page=8#reader']],
    ['ui-design.html', 'content', ['experiences/holland.html?view=cms']],
    ['ui-design.html', 'interaction', ['experiences/imhere.html?scene=1&amp;view=correction']]
  ];
  for (const [page, id, destinations] of routes) {
    const section = read(page).split('id="' + id + '"')[1]?.split('</section>')[0];
    assert.ok(section, page + '#' + id);
    for (const href of destinations)
      assert.ok(section.includes('href="' + href + '"'), page + '#' + id + ' must link to ' + href);
  }
});


test('ImHere records expose the saved correction to students and require written context for requests', () => {
  const page = read('ImHere-case-study/imhere-case-study.html');
  const app = read('experiences/experience.js');
  assert.match(page, /What the student can see/);
  assert.match(page, /Needs review → Present/);
  assert.match(page, /Present → Needs review/);
  assert.match(app, /studentExplanations\.slice\(-2\)\.reverse\(\)/);
  assert.match(app, /if\(a==='request-review'\)\{go\('excuse'\);return;\}/);
  assert.match(app, /if\(!context\)\{fieldError/);
  assert.match(app, /studentCorrectionNotes\(\)/);
  assert.doesNotMatch(app, /if\(a==='request-review'\)\{roster\[0\]='Needs review'/);
});


test('all 32 distinct pieces have a reachable studio or active case specimen', () => {
  const archive = read('playground.html');
  const reframe = read('studio-reframes.html');
  const production = read('production-specimens.html');
  const service = read('service-specimens.html');

  for (const [name, png, anchor] of [
    ['Bauhaus Design','bauhaus.png','bauhaus'],
    ['Aether Essence','aetheressence.png','aether'],
    ['Digital Poetics','digitalpoetics.png','poetics'],
    ['Solstice Studio','Solsticestudio.png','solstice'],
    ['Village Auto','villageauto.png','village'],
    ['Nebula Systems','nebulasystems.png','nebula']
  ]) {
    assert.ok(archive.includes(name) && archive.includes('studio-reframes.html#' + anchor));
    assert.ok(reframe.includes('id="' + anchor + '"'), name);
    assert.ok(reframe.includes('href="' + png + '"'), name + ' historical image kept');
  }
  for (const p of ['poster.html','website.html','websiteex.html','roseedit.html'])
    assert.ok(archive.includes('href="' + p + '"'), p);

  const graphicIds = ['nodo','night-shift','solace','common-ground','civic-bloom','thresholds','pulp','field','terra'];
  for (const id of graphicIds) assert.ok(production.includes('id="' + id + '"'), id);
  const serviceIds = ['psychictally','afterform','interval','aurea','loopline','novella','nutriva','proof-workspace'];
  for (const id of serviceIds) assert.ok(service.includes('id="' + id + '"'), id);

  for (const lead of [
    'ImHere-case-study/imhere-case-study.html',
    'Holland-Walking-Tour-site/holland-walking-tour-case-study.html',
    'proof/index.html', 'brume/index.html', 'plain-sight/case-study.html'
  ]) assert.ok(fs.existsSync(path.join(root,lead)), 'lead project exists: ' + lead);
  assert.equal(6 + 4 + graphicIds.length + serviceIds.length + 5, 32);
});

test('archive replacements remove unsourced consumer metrics and dead gallery destinations', () => {
  const rose = read('roseedit.html');
  const red = read('website.html');
  const aura = read('websiteex.html');
  assert.doesNotMatch(rose,/4,200 votes|Guillaume Flavigny|images\.unsplash\.com/);
  assert.match(rose,/fictional scent profile/i);
  assert.doesNotMatch(red,/hello@youremail\.com|Your Name|href="#"/);
  assert.match(red,/proof\/index\.html#campaign/);
  assert.match(red,/plain-sight\/publication\.html/);
  assert.doesNotMatch(aura,/href="#"|структур|images\.unsplash\.com/);
  assert.match(aura,/field notes/i);
});

test('every new specimen is linked from its original case or a collection page', () => {
  const routePairs = [
    ['psychictally.html','service-specimens.html#psychictally'],
    ['afterform.html','service-specimens.html#afterform'],
    ['interval.html','service-specimens.html#interval'],
    ['aurea.html','service-specimens.html#aurea'],
    ['loopline.html','service-specimens.html#loopline'],
    ['novella.html','service-specimens.html#novella'],
    ['nutriva.html','service-specimens.html#nutriva'],
    ['proof/workspace.html','../service-specimens.html#proof-workspace'],
    ['nodo/index.html','../production-specimens.html#nodo'],
    ['night-shift.html','production-specimens.html#night-shift'],
    ['solace-press.html','production-specimens.html#solace'],
    ['common-ground-editorial-rebuild/common-ground.html','../production-specimens.html#common-ground'],
    ['civic-bloom-portfolio-package/civic-bloom.html','../production-specimens.html#civic-bloom'],
    ['thresholds-portfolio-package/thresholds.html','../production-specimens.html#thresholds'],
    ['proof/index.html','../production-specimens.html#pulp'],
    ['proof/index.html','../production-specimens.html#field'],
    ['proof/index.html','../production-specimens.html#terra']
  ];
  for (const [file,href] of routePairs) {
    const html=read(file);
    assert.ok(html.includes('href="' + href + '"'), file + ' missing revision link: ' + href);
    assert.ok(html.includes('specimen-bridge.css'), file + ' missing bridge style');
  }
});

test('interactive examples expose the requested states without invented backends', () => {
  const html=read('service-specimens.html');
  assert.match(html,/30-minute break does not fit/);
  assert.match(html,/40-minute gap/);
  assert.match(html,/Awaiting partner review/);
  assert.match(html,/1 ingredient/);
  assert.match(html,/0 ingredients/);
  assert.match(html,/Context requested/);
  assert.match(html,/No campaign published/);
  assert.match(html,/role="status"/);
  const production=read('production-specimens.html');
  assert.match(production,/T–07/);
  assert.match(production,/10 mm/);
  assert.match(production,/T–01/);
  assert.match(production,/12 mm/);
  assert.match(production,/units not specified|Measurement unit is not specified/);
  assert.match(production,/Common_Ground_Illustrative_Data\.csv/);
});
