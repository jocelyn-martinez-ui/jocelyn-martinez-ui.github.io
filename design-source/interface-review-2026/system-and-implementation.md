# System and implementation

This describes the actual branch, a scoped extension of the existing code-based system. It is not a new Figma library. Existing fonts/licenses are retained; no Figma or Adobe source file is fabricated.

| Surface | Typography | Color | Layout |
| --- | --- | --- | --- |
| Portfolio | Newsreader + DM Sans | Paper `#f5f3ef`, ink `#242923`, green emphasis | Two-column hero/projects; four role routes; single-column projects on small screens |
| ImHere | Plus Jakarta Sans; compact record metadata | Ink `#18334c`, action `#175881`, workspace `#f3f5f5`, inspector `#fffdf8` | 188 px navigation; flexible roster + 300 px inspector; stacked below 1000 px |
| Áurea | Italiana + DM Sans | Ink `#302529`, burgundy `#713c46`, paper `#fcfaf5`, shared-note tint `#ebe7bb` | Narrow row-header column + two comparison columns; full perfume names on narrow layouts |

## Components and behavior

| Component | Implemented states |
| --- | --- |
| ImHere summary | Present/review/unrecorded counts read the same roster; session open/closed is a separate state |
| Roster search/filter | Case-insensitive student/status query combined with status; cursor/focus restored; explicit no-results/reset state |
| Record inspector | Selected row identifies its student and controls the inspector; current status, request context, latest change and proposed status stay together |
| Correction | Current/proposed comparison; required reason bounded to 500 characters; field-linked error; cancel leaves the record intact |
| Save/undo | Save appends a reason and updates the shared record. Undo appends a reversal without erasing the original. Both guard against a newer status. |
| Comparison selectors | Exactly two slots; changing either retains the other; duplicate selections are disabled |
| Comparison rows | Native table with column and row headers; family, opening, heart, base, character and save actions |
| Shared notes | Normalized note names; written shared-note summary; optional highlight so color is not the only cue |
| Pair recovery | Removing one keeps its partner; alternatives appear in place; empty state offers a clear starting action |
| Sampling sheet | Existing paper view reads the current selected pair, including replacements |

ImHere has four illustrative students and visit-only memory. The student workspace represents Student 01; other sample students’ changes appear in faculty history. Multi-account authorization, durable audit storage, institutional policy and location verification are outside the prototype. No private student information is collected.

Áurea has three original sample profiles. Notes describe character, not ingredients, safety or predicted wear. Written journal content is escaped. State resets on reload; a real catalogue and persistent accounts are outside scope.

## Responsive and access rules

- Native buttons, inputs, checkboxes and selects are retained. New primary controls target at least 44 px in their main interaction dimension; this is not a claim that all historical portfolio links meet every access criterion.
- ImHere’s mobile navigation uses three columns/two rows. The inspector stacks below the roster; selecting a record focuses its heading and brings it into view on narrow screens.
- Áurea’s rebuilt comparison has no 610 px minimum width. The row-header column is 16% on larger layouts and 20% on smaller ones; the profiles share the rest. Mobile full-name blocks align above the compact selectors.
- Invalid forms focus their field; view changes focus the main heading; confirmations use the existing status region. Repeated profile actions identify the perfume in accessible labels.
- Existing reduced-motion CSS is retained. The new inspector scroll checks `prefers-reduced-motion`. OS-level preference emulation was not available in this browser surface.
- Screenshots have alt text and dimensions, and adjacent links open the real interfaces. Captures do not replace accessible HTML.

## Source ownership

`experiences/experience.js` owns sample data, rendering and events. New behavior is grouped in `attendanceWorkspace`, `beginCorrection`, `saveAttendanceCorrection`, `comparisonBench`, `replaceComparedSlot`, `bindReconstructionControls` and `reconstructionAction`. `identities/imhere-workbench.css` and `identities/aurea-workbench.css` load last only in their respective entry pages.

`portfolio-edition.css` scopes the homepage. `interface-evidence.css` styles captures in the cases/UI route. `work-paths.js` owns filter groups and URL persistence. Public page captures live in `assets/interface-review/`; review evidence lives beside this document.

The shared script retains older rendering layers. A later cleanup should extract per-project modules and remove unreachable markup after regression checks. That engineering cleanup is not claimed complete here. This review folder is committed to a public repository and contains no private research or user information.
