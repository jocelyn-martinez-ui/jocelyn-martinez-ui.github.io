# BRUME · Design review and verification

## Review against the brief

These points express an editorial assessment of the portfolio, using the weights in the brief. User testing, fabrication and measured lighting performance would require separate work.

| Criterion | Points / available | Evidence and remaining constraint |
| --- | --- | --- |
| Creative originality | 12 / 15 | The same observation about split reflections drives the register mark and the light-comparison interface. The mushroom silhouette is familiar. |
| Art direction and photography | 16 / 20 | The reeded Ivory window, Amber’s long edge shadow and the localized illumination on Plum establish three distinct scenes. The matched register keeps the camera steady. Rendered gloss can look unusually pristine, and glass transmission has no measured reference. |
| Graphic design and typography | 16 / 20 | The wall poster reads at a distance, the editorial spread moves from rib to silhouette, and edition codes hold position on the labels. Fine lines and small print type still need a physical proof. |
| Brand identity and consistency | 8 / 10 | A displaced band recurs on the cover, three labels and graphic artwork. The band also shifts height by edition. Its reduction to a very small physical mark awaits proofing. |
| UX/UI and accessibility | 12 / 15 | A visitor can hold room light constant, compare all finishes, share a specific view and revisit it with Back. A static register exposes the nine images. A moderated comparison task and screen-reader testing would add evidence. |
| Mockups and campaign presentation | 8 / 10 | The outdoor placement, open brochure and carton each have an inspectable flat counterpart. Blank scenes retain separate artwork layers during composition. Material, scale and folds are proposed. |
| Technical execution | 4 / 5 | Static relative assets, local fonts, automated state tests, working fragment links and separate build sources support the existing Pages site. Browser proofing covered Chromium. |
| Portfolio effectiveness | 4 / 5 | An opening credit and brief establish the project’s scope, and viewers can reach the working interface or flat assets directly. Recruiter response has not been measured. |
| **Total** | **80 / 100** | **Design review of this edition.** |

## Refinement record

1. **Concept.** Reviewed the earlier case, four photographs, selectors, editable artwork and email HTML. The original coupled each finish with one room. The reconstruction separates campaign mood from finish comparison.
2. **Photography.** Grounded new shots in the original dome, neck and glass foot. Checked a 3 × 3 contact sheet and removed residual daylight reflections in the evening views. The separate Amber off/on pair retains the object and setting.
3. **Graphic design.** Compared three mark directions. Rendered the social artwork in a vector editor, adjusted headline fit, and registered editable print artwork to blank photographic scenes. Flat files are directly accessible.
4. **Interaction.** Verified independent finish and light changes, comparison, deep links, keyboard operation, Back and refresh. Script-disabled collection markup exposes the full nine-image register. Corrected glyph rendering, input states and a redundant history entry in the email proof viewer.
5. **Story.** Added a before/after photographic comparison, a stated audience assumption and a role statement. Moved full galleries off the main case so each featured piece illustrates a decision.
6. **Polish.** Checked responsive browser frames, refined typography and control wrapping for enlarged text, and paired the outdoor, brochure and carton mockups with full-size flat files.

## Checks performed

- All 58 portfolio and BRUME Node tests passed, including four collection-state regressions.
- At 200% text size, all 11 pages fit the available width in 320, 390, 768 and 1440 pixel Chromium frames. The campaign controls and navigation wrap as their labels grow.
- Checked local HTML link paths, fragments, CSS resource paths, heading counts, duplicate IDs and image alt attributes across the 11 HTML pages. Parsed the 27 current art masters as SVGs and decoded the embedded photographic layers.
- Checked the campaign carousel using a keyboard, direct frame links and refresh. The story templates reserve 240 pixels above and below their essential copy on a 1080 × 1920 canvas.
- Checked the collection at 320, 390, 768 and 1440 CSS pixels. Its phone and desktop presentation retained the selected finish and light at 390 × 844 and 1280 × 800.
- Read the three letters in a browser at 360 and 640 pixels. Tested images-off proofing and links into the intended product state. Parsed the downloadable multipart specimens for matching HTML and plain-text bodies.
- The physical carton, lamp, color reproduction, electrical performance and shipping protection have not been tested. The email studies have no actual sends or cross-client inbox tests. A physical-device, screen-reader and moderated buyer review remain open.
