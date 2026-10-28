# PLAIN SIGHT — independent source audit

Audit date: 27 October 2026. Baseline: `e89df37d6ff1b03bc93bba9efe5be7c08615f1ab` on `main`.

This is a source-based specialist review, not interviewed user research, browser testing, accessibility certification or a hiring prediction. The baseline repository remains recoverable at that commit. The implementation owner conducts separate live-interface and publication-render reviews. Findings below describe the **original** version; they are not assertions about the reconstructed edition.

## Scope and method

Read all ten PLAIN SIGHT HTML pages, both stylesheets, the shared script, inline motion script, project documentation, the PLAIN SIGHT test file, shared portfolio route tests and the repository quality workflow. Parsed all HTML links, image attributes, headings and navigation markers; inspected SVG image references; ran the existing three PLAIN SIGHT tests. No applicable `AGENTS.md` was found in the project or its workspace ancestors.

The source is a buildless static site under `plain-sight/`. There is no PLAIN SIGHT framework, package manifest or build step. `.github/workflows/portfolio-quality.yml` runs JavaScript syntax checks and Node tests on pull requests; its push branch filter includes `main` and the older `plain-sight-editorial-v2`. It is a quality workflow, **not** a Pages deployment workflow. Source inspection alone does not verify the repository's Pages settings; match the live page against this source and inspect deployed metadata separately.

The current main commit includes the previously reviewed portfolio changes. This reconstruction should branch from current main and edit only PLAIN SIGHT files plus the tests specifically covering it.

## Measured baseline

| Check | Result | Interpretation |
|---|---:|---|
| HTML pages reviewed | 10 | Homepage, three studies, publication, studio, contact, case study, email and motion |
| Image elements | 60 | Repeated uses, not distinct photographic sources |
| Images missing intrinsic width and height | 56 | Source offers little intrinsic reservation; some CSS ratios/heights still reserve space. This is a risk, not a measured CLS result. |
| Images with `srcset` | 0 | Every viewport receives the same image candidate |
| Images missing an `alt` attribute | 0 | Presence passes; descriptive quality often does not |
| Primary links marked `aria-current` | 0 across 10 pages | No persistent page-location cue |
| Broken local href/src/HTML fragments | 0 | All original destinations resolve in the parser |
| Existing PLAIN SIGHT tests | 3 passed | Mostly source assertions and file integrity, not behavior |
| Asset files under `assets/` | 57 / 7,121,642 bytes | Inventory total, **not** page transfer size |
| SVG files | 35 | 31 embedded raster references; no external SVG image references found |
| Original generated scenes | 5, per existing provenance documents | 2 portraits, 2 still lifes, 1 interior; derivatives must not inflate this count |

Machine-readable results: [`source-inventory.json`](source-inventory.json).

## What should survive

- The three subjects and the observation premise are clear, coherent and sufficiently different to support distinct compositions.
- The five source scenes already support full-frame/context/detail comparisons. Additional generated pictures are not a prerequisite for a useful reconstruction.
- The current pages disclose AI-generated imagery, concept status, unmeasured outcomes and print-production limits. These are useful boundaries to preserve and clarify.
- Real PDF and editable SVG files exist. The project has tangible graphic-design material rather than only marketing mockups.
- Native links, a skip link, one small shared script, visible focus rules, a working small-screen menu, lazy loading below the hero and reduced-motion CSS provide a lightweight starting point.
- The contact page identifies the real creator and email address. Its form explicitly says it is a demonstration.

## Problem inventory

Priorities: P1 = prevents or materially weakens a core task; P2 = substantial clarity/craft/maintenance issue; P3 = lower-value extension or polish. Selectors and quoted labels are used because most HTML/CSS is minified into long lines.

| ID | Priority | Evidence | Problem and consequence | Recommended change |
|---|---|---|---|---|
| PS-01 | P1 | `arrangements.html`, final “Next study” link → `gestures.html` | `gestures → arrangements → gestures` forms a loop; the third study is not part of this path. | Explicit 01/02/03 chapter navigation, current state, previous and next labels. |
| PS-02 | P1 | `publication.html`, “01 / SELECTED PAGES” uses `gesture-fabric-detail.webp`, `arrangement-bloom.webp`, `between-room.webp` and a contact-sheet JPEG | These are raw illustrations, not page previews. A reviewer cannot inspect publication composition from the page that promises it. | Render and display actual PDF pages with page numbers, chapter links, readable enlargement and PDF fallback. |
| PS-03 | P1 | Study pages, repeated `CROP 01 / SELECTED FRAME` captions | In GESTURES, the first card is `gesture-seated.webp`, a separate source from the hero `gesture-fabric.webp`; in ARRANGEMENTS the first card is `arrangement-table.webp`, separate from hero `arrangement-bloom.webp`. Generic crop captions obscure source lineage. | Identify every original with a stable ID and link every derivative to its actual parent. |
| PS-04 | P1 | `publication.html` says “Letter-size landscape”; `docs/PRINT_SPECS.md` says A4 portrait | Contradictory production information undermines confidence under close review. | Verify PDF page boxes, publish the actual format once, then align website and docs. |
| PS-05 | P1 | `assets/editorial-v2.css`, mobile `.poster-strip figure:nth-child(3){display:none}` | The rule also affects the full six-poster publication grid, removing poster 03 on mobile. Base CSS also hides the last poster. | Keep all campaign work reachable at every width; use a simple stacked/grid transformation. |
| PS-06 | P1 | `publication.html`, heading sequence starts with `<h2>` | The document has no h1 and begins at the wrong conceptual level. | One descriptive page h1; meaningful h2/h3 hierarchy below it. |
| PS-07 | P2 | `gestures.html`, `arrangements.html`, `in-between.html`: same `detail-lead`, `detail-photo`, `journal-grid`, repeated “Learn to notice” and “The edit is the idea” | Subject changes, but sequence and information hierarchy largely do not. The source contradicts the case-study's implication of meaningfully distinct study pages. | Preserve shared navigation/controls, give human, object and space chapters different image relationships and pacing. |
| PS-08 | P2 | `assets/app.js` only handles nav, three-card filters and form feedback | There is no focused image navigation, crop comparison, meaningful metadata route, publication viewer or history-aware exploration. | Add one well-scoped light table with source selection, parent-linked crops and authentic framing notes. |
| PS-09 | P2 | All ten topbars omit `aria-current` | A visitor loses page orientation after leaving the homepage, especially on similar study layouts. | Current links, chapter number/title and deterministic return links. |
| PS-10 | P2 | `index.html` contains 17 images; multiple sections restate observation before/after the studies | Long repetition dilutes the study entry task and makes the same small image library feel larger than it is. | Reduce the homepage to encounter → three studies → a sample framing decision → publication → creator. |
| PS-11 | P2 | Both sheets use `@import` Google Fonts; the second overrides variables and most major components | Instrument Serif, DM Sans, Bodoni Moda and IBM Plex Mono all load for overlapping roles. The cascading design history obscures the actual system. | One owned stylesheet, a limited type system and explicit components; remove live dependency on the refinement layer. |
| PS-12 | P2 | `editorial-v2.css`: metadata 10px, small-screen metadata 8px, brand subtitle 7px; `.navtoggle` 11px with no explicit target size | Metadata becomes hard to read; menu target has no robust minimum. This is a source risk, not a measured conformance result. | Readable caption/control floor, 44px practical targets, test 200% text/zoom and narrow reflow. |
| PS-13 | P2 | 56/60 images omit dimensions; every image has one URL | Unreserved intrinsic dimensions and no size selection leave loading/layout behavior under-specified. | Supply actual dimensions/ratios, optimized responsive candidates, hero priority only where justified. Measure, do not invent performance gains. |
| PS-14 | P2 | Crop alt strings include “Editorial gesture fabric fabric image or crop” | File-derived naming does not convey pose, material, framing or what the derivative isolates. | Scene-specific descriptions, with crop identity in the visible caption. |
| PS-15 | P2 | `.topbar nav` is hidden at mobile widths; only JavaScript applies `.is-open` | With script failure/disabled JS, the primary mobile navigation is unavailable. | Keep navigation usable in base HTML; use progressive enhancement to collapse it. |
| PS-16 | P2 | `contact.html` prominently asks name/email/project for a local demonstration; form has no action/method fallback | A collaborator must fill a form that cannot send. Without the JavaScript preventDefault handler, native GET submission can put entered details in the page URL. | Prefer the real email action and an honest copy-address fallback; remove unnecessary data entry. |
| PS-17 | P2 | `publication.html` says SVG artwork links to originals; all SVG `<image>` references inspected are embedded data URIs | Instructions are inaccurate and suggest fragile files when actual files are portable. | State embedded raster + editable vector text/shapes accurately, retain source-image provenance. |
| PS-18 | P2 | `case-study.html` says “code and image assets are bundled in the project ZIP”, but has no ZIP link | Evidence is hard to verify; case-study language outpaces the actual interaction sophistication. | Link source and actual working journeys, show before/after evidence and separate tested facts from intentions. |
| PS-19 | P3 | `motion.html` inline script toggles `paused`, while reduced-motion CSS disables all animation | Reduced-motion users can still see controls that promise to play/pause motion that remains off. | State the preference explicitly, disable or adapt the control, keep motion separate from essential exploration. |
| PS-20 | P3 | Poster/social SVG text fonts are mostly Georgia/Arial while site refinement claims Bodoni/DM/IBM; `CREATIVE_BRIEF.md` still names Instrument Serif/DM | Visual systems drift across surfaces and docs. | Document surface-specific rationale or unify selected production files; do not pretend the existing suite has been fully rebuilt. |

## Page-by-page conclusions

| Page | Principal finding | Preserve | Reconstruction responsibility |
|---|---|---|---|
| `index.html` | Distinct oversized editorial ambition, but too many repeated exposition/campaign sections and only three-card filtering | Three study entry points, imagery and premise | Memorable encounter with an obvious work entry; concise framing demonstration |
| `gestures.html` | Same template as other chapters; source and derivative identities ambiguous | Two human scenes, scale and fabric relationships | Portrait-oriented sequence, distinct source IDs and close framing route |
| `arrangements.html` | Same template and broken next-study sequence | Two still-life scenes, asymmetric balance | Rigorous grid; correct chapter progression; visual light table |
| `in-between.html` | Repeats one scene with generic four-crop sequence and ends by repeating whole frame | Honest single-scene provenance | More generous space; geometry/negative-space explanation; deliberate return |
| `publication.html` | No true page previews; no h1; inaccurate print format and SVG instructions; missing campaign items at mobile | Existing 24-page edition, all campaign masters | Actual page reader, chapter/page deep links and complete campaign access |
| `studio.html` | Honest scope and creator attribution, but mostly an oversized statement and reused image | Transparent provenance | Short method + source-count explanation + real creator route |
| `contact.html` | Real email is clear, but nonfunctional demo form competes with it | Verified visible email | Direct contact and fallback; no fake submission |
| `case-study.html` | Good process intent but little traceable evidence; imagery stands in for interface proof | Scope boundaries, production honesty | Decision→implemented behavior→verification chain, actual captures |
| `email.html` | Explicit specimen; responsive web page rather than verified email-client artifact | Concept label and real work link | Align framing/type without claiming email-client QA |
| `motion.html` | Working pause control and reduced-motion CSS; preference/control mismatch | Small optional motion specimen | Accurate preference messaging; no essential automatic motion |

## Independent specialist perspectives

### Principal UX designer

The original gives visitors three easy chapter links, but the key task after opening a study is merely scrolling a repeated layout. The next-study defect is a concrete journey failure. A five-source collection does not need complex saved filters, accounts, search, three fully separate viewing modes or an autoplay slideshow. A direct study overview plus focused inspection is enough. The most useful innovation is making the relationship between source, crop and editorial purpose legible.

### Principal UI designer

The code shows a considered large-serif identity but an unstable type hierarchy: two generations of tokens, four loaded families and captions shrunk to 7–10px. Excess `nth-child` positioning binds layout to ordering, and mobile visibility rules remove real work. Replace this with named chapter layouts, stable image ratios and generous but readable controls. Visual balance still requires screenshot judgment; source inspection cannot establish whether each hero crop or type overlap succeeds.

### Information architect

There are two different content levels—five source scenes and their derivatives—but the interface flattens them into image cards. That is the central structural problem. Build data around source IDs, chapter, derivative ID, visible label, actual asset path, meaningful description, current framing note and publication destination. The same data should power the overview, focused view and comparison. A derivative must never increment the source count.

### Accessibility lead

The baseline includes useful semantic links, skip navigation, image alt attributes, focus styles, form labels and reduced-motion CSS. Those provisions are not certification. High-priority gaps are publication heading structure, source-specific descriptions, current-location cues, robust control sizing and mobile navigation without JS. A new viewer should use actual buttons/links, clearly named previous/next controls, predictable Escape, returned focus, no focus loss during selection and no mouse-only dragging. An overlay should only be added if its dialog/focus behavior is fully tested.

### Creative frontend engineering lead

The static foundation is suitable. The smallest defensible architecture is a single stylesheet, a small data module, one behavior module and build-time/static HTML generation only if it reduces repeated markup without creating a runtime dependency. Keep every study and publication entry reachable with normal URLs. Parse and clamp invalid URL state, update history deliberately, and ensure Back restores orientation. Testing should target observable state transitions, source/derivative validity, malformed links, empty selections, keyboard behavior and asset integrity, not the exact display font string.

### Design hiring director

The strongest current evidence is the cross-channel output and honest provenance. The weakness is a mismatch between lofty interaction claims and the small script that only toggles navigation, filters three cards and simulates submission. A polished, inspectable crop decision and an honest publication reader would improve the evidence more than more decorative hero sections. The new case study must show the functioning interaction, why it was selected over alternatives and which checks really ran. No conclusion about seniority or likelihood of hiring follows from source quality alone.

## Resolve the competing mode proposals

| Candidate | Useful when | Risk in this project | Recommendation |
|---|---|---|---|
| LOOK, focused sequential exhibition | A visitor wants to enjoy one scene at a time | Only five originals; padding the sequence with derivatives can imply a larger shoot | Use focused viewing inside the study experience with explicit source/crop identity; no autoplay requirement |
| INDEX, overview | A reviewer needs quick orientation and source relationships | A full search/filter UI for five originals is unnecessary | Make a compact contact index the light-table entry, grouped by the three studies |
| READ, editorial explanation | A reviewer wants the rationale behind a crop | A third global mode duplicates chapter and case-study prose | Place concise visible notes beside the current framing; link to deeper case study rather than another app-wide mode |

Preferred core: chapter-led exhibition + one source-aware light table + actual publication reader. Keep “Look / Index / Read” as a design exploration, not an obligatory persistent mode bar.

## Implementation order and acceptance conditions

1. Preserve baseline captures and commit reference; map all five originals and derivatives.
2. Fix chapter sequencing and meaningful current location; maintain no-JS entry links.
3. Consolidate styling and create distinct chapter compositions with readable UI typography.
4. Implement focused inspection and crop/source comparison. Changing a crop must keep its parent explicit; returning must preserve the user's location.
5. Build the PDF reader from actual page renders. Page navigation, direct links, chapter jumps, zoom and download must agree on the same edition.
6. Replace the contact demo with actual usable contact actions; retain email/motion specimens with accurate labels.
7. Document the design choice and evidence in the case study.
8. Verify the six requested visitor journeys, keyboard behavior, reduced motion, loading, narrow widths, text scaling and all local links. Do not claim the unsupported checks passed.

## Baseline tests and their limits

Command run:

```sh
node --test tests/plain-sight-edition2.test.mjs
```

Result: **3 tests passed, 0 failed**.

- Test 1 pins `editorial-v2.css`, exact classes and Google Fonts names; it must be revised when consolidating the system. Its `alt="` assertion only proves some image description is present in each file.
- Test 2 resolves local href/src paths but does not validate remote resources, behavior, all fragment destinations or any CSS/SVG image references.
- Test 3 checks PDF magic bytes/minimum sizes and the presence of text in one SVG. It does not assess page count, layout, crop accuracy, embedded fonts or print readiness.
- Shared `tests/portfolio-paths.test.mjs` covers the existing PLAIN SIGHT page URLs; retain them or provide explicit redirects so portfolio entry points remain valid.
- No current test exercises `app.js`, filter feedback, menu Escape, contact simulation or the motion control.

The separate audit parser validated local HTML fragments and counted all image/heading/nav attributes. Browser/device/assistive-technology testing and before/after visual assessment belong in the final QA record, not inferred from these source checks.
