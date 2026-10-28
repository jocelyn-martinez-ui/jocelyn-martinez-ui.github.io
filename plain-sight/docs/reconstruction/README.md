# PLAIN SIGHT — reconstruction evidence

The observation edition rebuilds the real project under `plain-sight/`. It keeps the philosophy and all five original generated scenes, makes eleven derivative crops explicit, and connects the exhibition to a real 24-page publication.

Baseline: `e89df37d6ff1b03bc93bba9efe5be7c08615f1ab`. Review branch: `plain-sight-ux-reconstruction`. This work is prepared for a pull request; it does not authorize merging or deploying the portfolio.

## Review in this order

1. Open `plain-sight/index.html`, choose a study, open focused viewing, then inspect a source in `light-table.html`.
2. Change a source/crop and follow its publication link. Try page selection, chapter links and enlargement.
3. Inspect the case study, before/after captures and the [QA record](qa.md).
4. Review the [source audit](source-audit.md), [28-reference influence matrix](references.md), [three direction/type studies](concepts.html), [journeys and decisions](changes-and-journeys.md), [design system](system.md), [editorial audit](editorial-audit.md) and [critical rubric](assessment.md).

## Files and regeneration

- `src/collection.json`: five source records, their eleven children, honest descriptions and authored notes.
- `assets/model.js`: pure URL state/filter/boundary functions, exercised by Node tests.
- `assets/app.js`: native DOM enhancement, focus/history, comparison and page reader.
- `assets/styles.css`: consolidated visual system; the old editorial override layer is removed.
- `src/build_publication.py`: canonical PDF, exact page previews and extracted text manifest.
- `src/build_site.py`: all eleven static HTML pages, repeated components, embedded manifests and responsive thumbnails.
- `downloads/archive/`: preserved previous publication. `docs/reconstruction/before/`: actual original live-page captures.
- `assets/reconstruction/`: actual reconstructed desktop/mobile captures, not design mockups.

Run the publication generator before the site generator when changing the book. Python requirements are Pillow, ReportLab and pypdf, plus Poppler `pdftoppm`. The site is still buildless at deployment. The committed static files work on ordinary GitHub Pages.

Checks: `node --check plain-sight/assets/app.js`, `node --check plain-sight/assets/model.js`, `node --test tests/plain-sight-edition2.test.mjs`, then the repository quality workflow's complete test command. Exact execution results and limitations are in `qa.md`.

## Scope and honesty

No unrelated portfolio project is edited. No additional photography was needed. The study names and generated-image foundation survive. Research references are credited, inaccessible Pinterest boards are marked, and no interviewed users, real shoots, client outcomes or accessibility certification are invented. The PDF is RGB A4 portrait for digital review, not a preflighted physical edition. The old eight-page identity guide and broader campaign families remain preserved; four SVG masters received specific repairs.
