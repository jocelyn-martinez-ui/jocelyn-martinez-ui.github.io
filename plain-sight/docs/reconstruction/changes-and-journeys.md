# Decisions, comparisons and visitor journeys

Visitor types are provisional evaluation lenses, not interviewed personas. Creative directors need fast visual comprehension; design hiring reviewers need inspectable work; UX reviewers need functioning states; art viewers need uncomplicated photography; collaborators need real contact.

## Traceable changes

| Before / evidence | Objective and alternative | Implemented choice | Result and verification | Limit |
|---|---|---|---|---|
| Two overriding CSS generations, four font families | Coherent hierarchy; considered all-grotesk and high-contrast editorial | One stylesheet, two local font families; hybrid archive typography | Consistent controls, distinct chapter layouts; source checks and viewport review | Historical campaign masters retain portable fonts |
| Repeated template layouts for all studies | Distinguish people, objects and space; considered three unrelated interfaces | Shared navigation, fluid human sequence, rigorous still-life pairs, spacious architecture | Three different image relationships; complete chapter cycle | Small original library limits sequence variety |
| Generic frame labels and duplicate-source ambiguity | Reveal actual art-direction decisions; considered three global LOOK/INDEX/READ modes | Five-source index, optional focused viewer, dedicated light table with inline notes | Source/crop parent validation, deep links, correct PDF destination | No participant validation of annotation value |
| Homepage primarily presentation and repeated explanation | Immediate encounter plus visible work access | “A second look”, whole image plus same-source detail, three study links | Actual desktop/mobile screenshots in `assets/reconstruction/` | Visual preference is a qualitative judgment |
| Raw photos represented publication pages | Inspect the real book; considered page-turning and spreads | Exact 24-page reader, chapter/page jump, enlargement, transcript, direct PDF | Page bounds, URL history and zoom tested | PDF itself is not a tagged accessible PDF |
| Form could not submit; unnecessary personal fields | Reliable creator contact | Real email link and optional copy with failure message | No form or network submission code | A user's email app/clipboard policy is outside site control |
| Mobile CSS hid artwork | Equal content access across screen sizes | All six posters and social artworks remain in normal document flow | Source and responsive checks | SVG font rendering can vary across systems |

Actual before captures are in `before/`; the archived baseline commit is named in `source-audit.md`. `concepts.html` contains the three visual directions and three typography studies, with twelve comparison criteria. `references.md` contains the influence matrix and 28 evaluated sources, with access limitations.

## Six task walkthroughs

1. **Find a study.** Home → named Gestures / Arrangements / In Between link → chapter title and numbered chapter navigation. Success means the visitor sees both the subject and their place in the collection.
2. **View photographs with orientation.** A source image → focused viewer → source number, title and sequence count → previous/next → Escape/Close. Boundaries disable rather than unexpectedly wrap. Closing returns focus to the opener.
3. **Move from overview to focus.** Home filter → visible originals and live count → focused source → close to the same filtered overview. Browser Back/Forward restores URL-backed states; no new account or save concept.
4. **Understand a crop.** Inspect framing → original and derivative shown in full → choose crop or parent source → compare authored notes and optional rule-of-thirds guides. A mismatched source/crop URL falls back to a valid child of the current parent.
5. **Inspect the publication.** Publication navigation or crop's page link → actual page → chapter/page control → enlargement or text companion → PDF download or return to source. Without JS, the PDF and all page images remain accessible.
6. **Contact the creator.** Header or footer Contact → visible actual email → email app or copy address. No fake confirmation, unnecessary form entry or stored submission.

See `qa.md` for which steps were exercised in the browser and which checks remain unperformed. These are deterministic task walkthroughs by the implementation agent, not participant research or success-rate data.

## Major-section composition checks

| Section | Focal point and reading order | Alignment / deliberate space | Responsive transformation |
|---|---|---|---|
| Home encounter | Display phrase → complete portrait → work actions → derivative | Text left, full source right; small crop reveals the conceptual relation | Stacks, keeps useful actions before long scrolling, avoids oversized overflow |
| Observation index | Three study names → filters → numbered originals | Shared card baseline and source labels; variable image ratios preserve compositions | Two/one-column cards; native wrapping controls |
| Light-table introduction | Comparison purpose → source rail → source/crop images → notes | Two equally grounded inspection mats, consistent IDs | Parent then child stacked; controls remain native and visible |
| Gestures | Full seated scene → space note → fabric portrait/detail | Wide-to-tall rhythm reflects body/material distance | One reading column, full images |
| Arrangements | Flower and short note → table and derivative | Controlled pairs and stronger vertical alignment | Pairs stack without hiding information |
| In Between | Quiet full room → window → chair/light | More negative space around a single source | Image scale becomes available width; generous but bounded gaps |
| Publication | Current page → controls → readable context → full page index | Large fixed-art region beside flexible text | Page fitted to width, controls wrap, enlargement scrolls locally |
| Closing/contact | One invitation and reliable action | Clear separation from provenance/footer links | Short blocks, wrapping email, no multi-column squeeze |
