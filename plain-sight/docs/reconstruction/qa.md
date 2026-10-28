# Verification record — observation edition

Scope: the eleven PLAIN SIGHT HTML pages and their real assets, canonical 24-page PDF, four repaired SVG masters and PLAIN SIGHT tests. Baseline `e89df37d6ff1b03bc93bba9efe5be7c08615f1ab`; reconstruction prepared 27–28 October 2026 (UTC). Browser evidence is from a local static preview in Chromium, not the published GitHub Pages site. No production deployment was made during this work.

## Automated checks

The following commands are the intended review checks, with final execution recorded in `test-results.txt`:

```sh
node --check plain-sight/assets/app.js
node --check plain-sight/assets/model.js
node --test tests/*.test.mjs proof/*.test.mjs proof/marketing/qa.test.mjs nodo/qa.test.mjs
git diff --check
```

The full suite contains 47 tests, including 15 PLAIN SIGHT tests. Tests cover parent/child integrity, all eleven crop selections, invalid and cross-parent URL state, source filters, bounded sequences and publication paging, URL preservation, actual preview/transcript files, chapter cycle, one H1/stylesheet per page, local links/assets/fragments, genuine contact routing and preserved originals. They use the actual shared model, rather than a duplicate implementation.

The initial run identified missing evidence files still being assembled. The final linked files were added before the recorded completion run. A full repository path test also checks the surrounding portfolio routes; no unrelated implementation was changed.

## Responsive browser matrix

All eleven pages were measured at iframe widths **320, 375, 390, 768, 1024, 1440 and 1920px**: 77 combinations. The iframe harness preserves the specified CSS layout width; large widths are visually scaled to fit the browser. These are controlled viewport-layout checks, **not physical-device tests**. Chromium's vertical scrollbar reduces the available layout width by 15px in recorded states.

Initial results in `layout-initial.json` found a publication selector overflow and a studio image/caption track overflow at 320px. Fixes constrained the selector and its flex item, made the two-image grid tracks shrinkable, and allowed captions to wrap. Final results in `layout-final.json` show **zero document horizontal overflows**, one H1 on each page, and no failed already-loaded images across all 77 states. Lazy images outside the viewport are additionally covered by filesystem/path checks; the matrix is not a claim that every lazy image was scrolled into view.

Actual captures: homepage, light table and mobile Gestures in `assets/reconstruction/`; publication reader and campaign repair review in this evidence folder. Before captures remain in `before/`. Three typographic specimen captures are `concept-type-a.jpg`, `concept-type-b.jpg`, `concept-type-c.jpg`.

## Browser task/state checks

| Check | Observed result |
|---|---|
| Home category filter | People/Objects each show two original sources; URL reflects the category. Back/Forward restored the selected category. |
| Focused viewer | Opens native dialog, focuses Close, shows source identity and position. Arrow navigation works, end controls disable, Close and Escape restore the opening link in normal tested paths. Tab from Close reaches the inspection link inside the dialog. |
| Viewer narrow layout | At 320px the dialog's scroll width equalled its width; no horizontal overflow. Content remains vertically scrollable. |
| Mobile navigation | Menu expands the real navigation; Escape collapses it and returns focus to Menu. |
| Light-table selection | Source 03 plus base crop displayed the matching original/derivative and notes. Source 05 plus shadow crop also worked at 320px. Rule-of-thirds checkbox displayed guides. |
| Light-table history | Back restored the previous crop; Forward restored the base crop. |
| Crop → publication | Flower base crop's link opened actual page 13, with the correct page title and preview. |
| Publication controls | Page select and next/previous updated content. Page 1 disables Previous; page 24 disables Next. Back restored page 13. |
| Publication enlargement | Image enlarged to 1000px inside a local scroll region; document did not overflow. Fit restored the ordinary layout. |
| Contact | Real mailto link remains present. Clipboard copying was unavailable in this preview context; the tested failure state gave accurate manual-copy/email instructions. No message was sent. |
| No JavaScript | At 390px, home/light-table/publication/contact retained visible primary navigation and no horizontal overflow. Light table exposed all original/crop notes through its fallback. Publication retained 24 full-page image links and the direct PDF. Results in `nojs-results.json`. |
| Motion preference | CSS and JS include reduced-motion disabling, static status and change listener. OS preference emulation was not available; no end-to-end preference test is claimed. The specimen is static by default. |
| Campaign artwork | Browser render review of repaired poster 02 and social 01/04/05 confirmed complete titles, separation from footers and readable text fields. |

One attempt to wait for the browser's PDF download event timed out in the automation runtime. The PDF file, href and 24-page structure are verified; a completed browser download event is **not** claimed. This is retained as a verification limit rather than described as a successful download test.

## Publication / asset integrity

- Canonical PDF: 24 A4 portrait pages, 595.28 × 841.89pt; approximately 3.12MB.
- All 24 pages rendered with Poppler. Full contact sheet inspected, then pages 7, 13, 21 and 23 inspected at larger scale. Corrected wrapped titles and the source caption touching the page-21 image; re-render verified.
- All page previews and text companions derive from the same PDF. No page-turning simulation or raw-photo substitute.
- Five original generated images preserved unchanged. Eleven existing derivatives retain actual parent IDs. No invented exposure, camera or production metadata.
- Previous publication and repaired SVG originals preserved. Existing campaign families retained and the historical identity guide clearly labelled.

## Accessibility checks and limits

Primary text color calculations using the WCAG relative-luminance formula: ink/paper **12.89:1**, muted/paper **5.42:1**, muted/panel **4.86:1**, accent/paper **7.36:1**, focus/paper **6.32:1**. These checks support the principal text palette; they do not constitute a full contrast audit of every artwork or rendered state.

Semantic labels, native controls, image descriptions, skip link, one-H1 page structure, current states, basic modal/menu keyboard behavior and no-JS fallbacks were inspected. No screen-reader session, Safari/Firefox matrix, physical phone/tablet, 200% text zoom, axe certification, tagged-PDF remediation or full WCAG 2.2 conformance evaluation was completed. PDF page text and image descriptions are offered through HTML, but the PDF itself is not a tagged accessible edition.

## Performance evidence

Current uncompressed source sizes: CSS approximately 27.5KB; application JS 12.7KB; pure model 1.6KB; all three local font files together approximately 68KB. Images reserve dimensions and use 480px candidates where appropriate; below-fold content is lazy loaded. The full-page PDF is downloaded on request and is not embedded as an initial page resource.

These are asset/implementation facts, **not** LCP, CLS or INP measurements. No standardized throttled Lighthouse run, field Core Web Vitals data, CPU profile or measured before/after loading improvement is claimed. A useful next performance gate is a repeatable mobile trace of home, light table and reader under the actual GitHub Pages deployment.

## Next validation

Have first-time viewers identify original versus crop and find the matching publication page without coaching; observe their wording and route. Run NVDA/VoiceOver and physical-device checks. Measure deployed page performance. Commission a physical proof only after resolution/color/bleed preflight. These are pending tasks, not implied completed research.
