# Critical assessment and weighted rubric

These are qualitative design judgments, **not measured user outcomes or independent professional endorsements**. The original source review was delegated separately; the final implementation critique below is the implementation agent's simulated review through the requested specialist lenses. No external hiring panel or research participants were recruited. Evidence is source inspection, original/after captures, rendered publication pages and the checks recorded in `qa.md`. Confidence is medium unless a narrower claim is backed by a deterministic check.

## Ten specialist lenses

| Perspective | Concrete original weakness | Reconstruction judgment and unresolved weakness |
|---|---|---|
| Principal UX | Arrangements returned to Gestures, bypassing In Between; the form did not send | Complete chapter cycle and direct email remove unnecessary work. The light table is useful in a task walkthrough, but visitors may prefer a simple gallery; external validation is still needed. |
| Principal UI | Four type families, two CSS generations and tiny caption rules; missing mobile artwork | Two font roles and one styling system clarify hierarchy. The large display voice still requires care for future long headings; the 320px selector overflow was caught and fixed. |
| Creative director | Strong warm image world, but familiar editorial presentation with little concept expressed through behavior | Source-to-crop inspection makes “observed differently” tangible. The five generated scenes remain a small and aesthetically familiar library; originality resides more in framing relationships than new photographic authorship. |
| Interactive art director | Mostly scroll-and-hover interaction; optional motion control could contradict reduced-motion CSS | Manual focus and visible comparison help attention without scroll interruption. Image transitions are intentionally modest; this is not an elaborate motion showcase. |
| Editorial director | Raw images stood in for real pages; page 17 heading collision; ambiguous frame numbering | Actual page reader and consistent source IDs make work inspectable. The 24-page sequence still repeats five scenes; paragraph density on annotation pages should be tested at actual reading scale. |
| Photography director | Derivatives could be mistaken for distinct originals; subject descriptions were generic | Complete originals remain available, derivatives stay attached, meaningful source descriptions replace filename text. Existing generated material cannot substantiate real shoot, camera, casting or lighting-production expertise. |
| Information architect | Originals, crops and applications were flattened into similar image cards | Shared manifest defines source → derivative → page relationships. Five originals do not justify search, saved collections or richer taxonomies; those features were rejected. |
| Accessibility lead | Mobile navigation depended on script, no publication H1, weak current-location signals | Native links/selects/dialog, no-JS fallback, text companion and current states improve the foundation. Screen-reader combinations, OS reduced-motion emulation and tagged-PDF accessibility remain unverified. No certification is claimed. |
| Frontend lead | Override stylesheet, repeated markup and source-level tests that missed real journeys | Shared generation and a pure state model reduce drift; behavior/boundary tests and browser checks add meaningful coverage. Browser QA is reproducible in its recorded steps but is not yet an automated cross-browser suite. |
| Hiring director | Polished artifacts with weak evidence of real interaction reasoning | A reviewer can inspect actual source/crop/page behavior and before/after evidence. The case study must keep its simulated-review and generated-image boundaries; no client success or seniority guarantee follows from these scores. |

## UX quality — 100 possible

| Criterion | Max | Original | Rebuilt | Evidence / confidence |
|---|---:|---:|---:|---|
| Discoverability and orientation | 15 | 9 | 13 | Named study entry points, current chapter, source IDs, viewer position; browser walkthrough / medium |
| Information architecture | 15 | 9 | 14 | Manifest separates five originals from eleven derivatives; source/crop tests / high for integrity, medium for comprehension |
| Journey clarity | 15 | 9 | 13 | Complete chapter cycle, crop-to-page route, real email; deterministic journeys / medium |
| Interaction feedback | 10 | 5 | 8 | Count, current controls, live status, copy fallback, image-error text / medium |
| Error prevention/recovery | 10 | 6 | 8 | Invalid state fallbacks, bounded paging, direct images/PDF, no fake form / high for implemented behavior |
| Accessibility | 15 | 8 | 11 | Keyboard/semantics/no-JS/contrast checks; assistive-tech and OS preference gaps / medium-low |
| Mobile usability | 10 | 6 | 9 | Seven-width reflow check, narrow comparison/menu tests; physical devices untested / medium |
| Evidence and decision quality | 10 | 5 | 9 | Original preservation, reference access levels, alternatives and recorded failures/fixes / medium |
| **Total** | **100** | **57** | **85** | **Qualitative; overall medium confidence** |

## UI quality — 100 possible

| Criterion | Max | Original | Rebuilt | Evidence / confidence |
|---|---:|---:|---:|---|
| Typography | 20 | 13 | 17 | Two explicit roles, readable captions, rendered headline review / medium |
| Spatial hierarchy/composition | 20 | 13 | 17 | Three chapter relationships, complete-image mats, actual captures / medium |
| Component quality | 15 | 8 | 12 | Native controls and shared generation; no broad usability testing / medium |
| Responsive execution | 15 | 8 | 13 | 77 width states; two 320px failures found and repaired / medium-high for geometry |
| Interaction states | 10 | 5 | 8 | Current/disabled/expanded/pressed/error states; manual checks / medium |
| Visual consistency | 10 | 6 | 8 | Single CSS and shared data; historical SVG font mismatch retained / medium |
| Accessible controls | 10 | 6 | 8 | Labels, visible focus, practical button targets, native keyboard use / medium |
| **Total** | **100** | **59** | **83** | **Qualitative; overall medium confidence** |

## Graphic and art direction — 100 possible

| Criterion | Max | Original | Rebuilt | Evidence / confidence |
|---|---:|---:|---:|---|
| Original visual concept | 20 | 14 | 17 | Source/derivative relationship shapes interface, not only copy / medium |
| Typography/composition | 20 | 13 | 17 | Web/PDF role alignment and render corrections / medium |
| Photography direction | 15 | 11 | 12 | More accountable selection/cropping; no new scenes or real shoot / medium-low |
| Editorial storytelling | 15 | 9 | 12 | Whole/detail/pause sequence, clearer chapter transitions / medium |
| Identity coherence | 10 | 6 | 8 | Repeated language, palette and IDs; legacy guide/campaign fonts remain / medium |
| Campaign/publication craft | 10 | 6 | 8 | 24 pages rebuilt; four SVG repairs; no physical proof / medium |
| Distinctiveness | 10 | 6 | 8 | Useful light-table concept; editorial serif aesthetic remains familiar / medium-low |
| **Total** | **100** | **65** | **82** | **Qualitative; overall medium confidence** |

## Engineering quality — 100 possible

| Criterion | Max | Original | Rebuilt | Evidence / confidence |
|---|---:|---:|---:|---|
| Functional completeness | 20 | 12 | 17 | Working index, viewer, comparison, page reader, real contact / medium-high |
| Code clarity | 15 | 8 | 12 | Separate pure model, DOM controller, content and generators; page generator still substantial / medium |
| Accessibility implementation | 20 | 10 | 15 | Semantic controls, fallback, focus, native dialog, text companion; manual AT gaps / medium |
| Responsive behavior | 15 | 9 | 13 | Width matrix and narrow state checks / medium-high |
| Performance | 15 | 9 | 10 | Local fonts, smaller image candidates and lazy loading; no field CWV or standardized Lighthouse result / low |
| Maintainability | 10 | 5 | 9 | One stylesheet, reusable generation, manifest-driven relationships / medium |
| Verification | 5 | 2 | 4 | Behavior tests plus browser and PDF evidence; no broad browser automation / medium |
| **Total** | **100** | **55** | **80** | **Qualitative; overall medium confidence** |

Scores compare design/implementation coverage under this rubric. They do not establish percentage gains, usability success rates, performance improvements or hiring probability. The strongest evidence concerns working paths and data integrity; the weakest concerns preference, external comprehension and unmeasured performance.

## Three simulated hiring reviews

**Graphic design director.** The complete-image discipline, repeated source identity and more deliberate book sequence are defensible. The print/web relationship is now inspectable. Weaknesses: five generated originals constrain range; legacy SVG typography is not fully unified; no physical material/proof evidence supports production mastery. Recommend close review of actual page scale and a later print prototype.

**Senior UI/UX designer.** The meaningful contribution is a clear model of originals, derivatives and editorial decisions. Deep links, history, bounded controls and honest contact behavior provide credible detail. Weaknesses: annotation usefulness has only been assessed through agent walkthroughs, and users may not discover the light table's purpose without the introduction. Next test: first-time identification of an original, then finding a crop's publication page without coaching.

**Creative technology director.** Vanilla progressive enhancement suits this collection and keeps the interactions inspectable. The native dialog and generated PDF/preview parity are stronger than a decorative slideshow. Weaknesses: no cross-browser/assistive-tech test matrix, no field performance evidence, and automated DOM interaction tests remain future work. More animation would not resolve those weaknesses.
