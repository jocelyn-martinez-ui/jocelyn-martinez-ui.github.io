# Portfolio implementation audit — 21 November 2026

**Repository:** [Jocelyn Martinez portfolio](https://github.com/jocelyn-martinez-ui/jocelyn-martinez-ui.github.io)  
**Review branch:** `design/portfolio-recruiter-edition` / [PR #14](https://github.com/jocelyn-martinez-ui/jocelyn-martinez-ui.github.io/pull/14)  
**Scope:** 32 distinct portfolio pieces. Existing work remains on `main`; this branch is not merged or published.

## What this pass actually implemented

- Rebuilt four standalone web studies in their original file paths (ÉLAN VERDE, RED ARCHIVE, Aura & Form, Rose Prick).
- Kept all six archived PNG studies and created a new editable, responsive graphic or interactive artifact for each in `studio-reframes.html`. Rebuilt `playground.html` to link the original and revision.
- Created nine different CSS/vector production specimens and eight distinct browser-local interaction specimens in `production-specimens.html` and `service-specimens.html`.
- Added visible, semantically labeled cross-links from 17 original case and collection pages to the appropriate new specimen.
- Strengthened ImHere's actual faculty/student prototype and case-study opening; required the review form, exposed recent explanations on the student view, and added source assertions. Corrected Nutriva's singular ingredient labels and Holland's illustration description in the shared prototype.
- Retained previous PR #14 work on PROOF, BRUME, PLAIN SIGHT, Holland, and ImHere instead of overwriting it.

**Completion boundary:** Every piece below has a traceable implemented change or existing PR #14 lead-case improvement. This is not equivalent to having independently redesigned and browser-verified every original source package or print deliverable. For 17 smaller cases, the new specimen is an intentionally separate, linked refinement, not a modification of every original poster or prototype.

## 32-piece inventory and evidence

| # | Project | Type | Revised artifact | Concrete design change | Scope status |
| --- | --- | --- | --- | --- | --- |
| 1 | ImHere | Lead case | [Open](ImHere-case-study/imhere-case-study.html) | Student-visible history, mandatory written context, save/undo demonstration | Expanded this pass; case and prototype edited |
| 2 | Holland Walking Tour | Lead case | [Open](Holland-Walking-Tour-site/holland-walking-tour-case-study.html) | Existing two-stop pause/resume and CMS review workflow; illustration provenance corrected | Existing PR14 redesign plus source edit |
| 3 | PROOF campaign | Lead case | [Open](proof/index.html#campaign) | Existing portrait/wide typography comparisons; now links early studio proofs | Existing PR14 redesign plus linked specimens |
| 4 | BRUME | Lead case | [Open](brume/index.html) | Existing artwork/email evidence and HTML source | Existing PR14 redesign |
| 5 | PLAIN SIGHT | Lead case | [Open](plain-sight/case-study.html) | Existing publication sequence and navigable reader | Existing PR14 redesign |
| 6 | PsychicTally | Service | [Open](service-specimens.html#psychictally) | New split review/discussion choice and local moderator context request | New linked interactive specimen |
| 7 | AFTERFORM | Service | [Open](service-specimens.html#afterform) | New AF–014 repair-scope comparison with readable garment tag approval | New linked interactive specimen |
| 8 | INTERVAL | Service | [Open](service-specimens.html#interval) | New 20-minute conflict and 30-minute break recovery | New linked interactive specimen |
| 9 | Áurea | Service | [Open](service-specimens.html#aurea) | New two-scent note swap and explicit overlap/no-overlap labels | New linked interactive specimen |
| 10 | Loopline | Service | [Open](service-specimens.html#loopline) | New 12-container preference vs acceptance handoff | New linked interactive specimen |
| 11 | Novella | Service | [Open](service-specimens.html#novella) | New blind excerpt, reveal and visit-only save interaction | New linked interactive specimen |
| 12 | Nutriva | Service | [Open](service-specimens.html#nutriva) | New pantry/recipe/grocery dependency; grammar corrected in original prototype | New interactive specimen plus source fix |
| 13 | NODO | Visual/production | [Open](production-specimens.html#nodo) | New three-object cable paths readable with labels hidden | New linked graphic specimen; original NODO remains archived |
| 14 | Night Shift | Visual/production | [Open](production-specimens.html#night-shift) | New four-panel flat with destination, route and fold order | New linked graphic specimen |
| 15 | Solace Press | Visual/production | [Open](production-specimens.html#solace) | New distinct book covers and shared imprint at small scale | New linked graphic specimen |
| 16 | Common Ground | Visual/production | [Open](production-specimens.html#common-ground) | New readable chart using model CSV values 41,34,26,22,17,14 | New linked graphic specimen |
| 17 | Civic Bloom | Visual/production | [Open](production-specimens.html#civic-bloom) | New directional sign with large legible destination and arrow | New linked graphic specimen |
| 18 | Thresholds | Visual/production | [Open](production-specimens.html#thresholds) | New translucent-layer cover with opaque high-contrast typography | New linked graphic specimen |
| 19 | PROOF review workspace | Earlier PROOF | [Open](service-specimens.html#proof-workspace) | New approved-art/preflight-blocked checklist and release recovery | New linked interactive specimen |
| 20 | PULP | Earlier PROOF | [Open](production-specimens.html#pulp) | New one/two-plate simulated overprint poster comparison | New linked graphic specimen |
| 21 | FIELD | Earlier PROOF | [Open](production-specimens.html#field) | New repeated leaf contour from cover to divider | New linked graphic specimen |
| 22 | TERRA | Earlier PROOF | [Open](production-specimens.html#terra) | New source-checked R02 T–07 / 10 mm vs R03 T–01 / 12 mm label pair | New linked graphic specimen |
| 23 | Bauhaus Design | Legacy PNG | [Open](studio-reframes.html#bauhaus) | New editorial architectural grid/circle flat and readable detail | New source-editable HTML/CSS; original PNG retained |
| 24 | Aether Essence | Legacy PNG | [Open](studio-reframes.html#aether) | New silk-inspired vector editorial opener | New source-editable HTML/SVG; original PNG retained |
| 25 | Digital Poetics | Legacy PNG | [Open](studio-reframes.html#poetics) | New coral headline and working case transition | New source-editable HTML/CSS; original PNG retained |
| 26 | Solstice Studio | Legacy PNG | [Open](studio-reframes.html#solstice) | New window-shadow composition with legible product text | New source-editable HTML/CSS; original PNG retained |
| 27 | Village Auto | Legacy PNG | [Open](studio-reframes.html#village) | New three-stage repair status and next action | New source-editable HTML/JS; original PNG retained |
| 28 | Nebula Systems | Legacy PNG | [Open](studio-reframes.html#nebula) | New selectable Haptics/Mechanics/Motion states | New source-editable HTML/JS; original PNG retained |
| 29 | ÉLAN VERDE | Standalone page | [Open](poster.html) | Rebuilt as printable original hand/seed/jar vector composition | Original page replaced; historical version in Git |
| 30 | RED ARCHIVE | Standalone page | [Open](website.html) | Rebuilt as indexed links to four real artifacts, no placeholder identity | Original page replaced; historical version in Git |
| 31 | Aura & Form | Standalone page | [Open](websiteex.html) | Rebuilt with botanical vector plate, field notes and real anchors | Original page replaced; historical version in Git |
| 32 | Rose Prick | Standalone page | [Open](roseedit.html) | Rebuilt as fictional original scent editorial with three working note stages | Original page replaced; historical version in Git |

## Verify in this order

1. **Design-lead route:** Open [ImHere](ImHere-case-study/imhere-case-study.html), [Holland](Holland-Walking-Tour-site/holland-walking-tour-case-study.html), [PROOF](proof/index.html), [BRUME](brume/index.html), and [PLAIN SIGHT](plain-sight/case-study.html). Inspect the actual demonstration, export, or publication pages; do not rely on hero mockups alone.
2. **Graphic/production route:** Inspect [nine visual samples](production-specimens.html) and the [Graphic Design collection](graphic-editions.html). Compare TERRA against [R02](proof/commissions/terra/archive/label-mist-r02.svg) and [R03](proof/commissions/terra/label-mist-r03.svg). The CSV used for Common Ground is [here](Common_Ground_Illustrative_Data.csv).
3. **Product/service route:** Try [eight interaction samples](service-specimens.html). Repeat each control to check return/reset behavior; separately use the actual ImHere, Holland, Áurea, Nutriva, Novella and Loopline prototypes.
4. **Visual archive route:** Open the [Playground](playground.html). Each historical PNG should lead to a source-editable redesign with its original preserved.
5. **Standalone route:** Open the four rebuilt standalone pages and inspect mobile reflow, keyboard focus, original vector labels, working links and print layout for ÉLAN VERDE.

## Verification actually performed

- GitHub source was fetched from this PR branch; all new and edited paths were committed through the connected GitHub account.
- Source-level checks found all six image-only sections, nine production sections, eight interaction sections and five lead cases, totaling 32 distinct briefs.
- The new inline scripts and existing prototype JavaScript passed JavaScript parsing checks.
- Added regression assertions in `tests/portfolio-paths.test.mjs` for all 32 entries, source/provenance labels, case-to-specimen routes, interactive-state strings and removal of placeholders. **GitHub Actions `Portfolio quality` completed successfully** for source commit [`cee2208`](https://github.com/jocelyn-martinez-ui/jocelyn-martinez-ui.github.io/commit/cee2208c252a9115d2c8fd5f1e227733b1c6a7c1), including changed script checks and route/workflow/artifact-integrity checks. [View CI run](https://github.com/jocelyn-martinez-ui/jocelyn-martinez-ui.github.io/actions/runs/44911630649).
- The source CSV confirms the exact Common Ground model values. The CSV contains no units; the redesigned chart explicitly avoids treating them as documented percentages.
- The TERRA SVG source shows R02 = T–07 / 10 mm and R03 = T–01 / 12 mm; the new pair uses those values.

## Verification not performed / remaining risk

- No Chromium/Safari/Firefox rendered screenshot pass, no genuine 360/768/desktop layout review, and no physical-device or assistive-technology test has been performed in this environment.
- No PDF preflight, vector production separation review, paper prototype or actual vendor proof was completed for the print work.
- No email-client rendering or image-disabled email screenshot pass was run here.
- The revised files were **not** merged into `main` or deployed to the public GitHub Pages site.
- Revisions are self-directed and sometimes AI-assisted; use the case source to distinguish documented project contributions from new portfolio-only demonstration work. Never present sample data, synthetic artwork or imagined commercial outcomes as actual client evidence.

## Five useful job-application paths

| Role | Shareable review destination | Evidence |
| --- | --- | --- |
| Junior graphic / production designer | [PROOF](graphic-design.html#production) | Reformatting social/print and linked release/preflight, TERRA and PULP examples |
| Visual / marketing designer | [Graphic collection](graphic-design.html) | PROOF, BRUME, PLAIN SIGHT and additional production samples |
| HTML email designer | [BRUME email](brume/email/01-introduction.html) | Inspect the actual HTML email and text fallback from its case |
| Web / digital content coordinator | [Holland editor](experiences/holland.html?view=cms) | Show the review checklist and readiness transitions |
| Junior UX/UI / web designer | [ImHere correction](experiences/imhere.html?scene=1&view=correction) | Enter a reason, save, undo, and inspect the student history |

**Recommended next task:** Run a real browser screenshot/interaction test at phone, tablet and desktop widths, then correct any visual clipping, timing, contrast, or script errors before deciding whether to merge PR #14.
