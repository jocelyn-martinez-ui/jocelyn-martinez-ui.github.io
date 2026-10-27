# Verification record

Final review: 27 October 2026. These checks support this bounded branch; they are not a WCAG certification, user study or production-readiness claim.

## Automated checks

Commands:

```sh
node --check experiences/experience.js
node --test tests/*.test.mjs proof/qa.test.mjs proof/marketing/qa.test.mjs nodo/qa.test.mjs
git diff --check
```

Result: **30 passing tests**, including eleven new workflow/rendering tests. Checks cover bounded required explanations, cancel, shared record updates, history-preserving undo, stale-save/undo guards, invalid proposals, intersected search/status, empty inspector, HTML escaping, comparison-slot preservation/duplicate prevention, shared-note and incomplete-pair rendering, and key deep-linked views across all six shared-script applications. Existing asset/route, PLAIN SIGHT and campaign checks also pass.

The new Node tests use production functions with a small DOM double. They test state/rendering logic, not layout or assistive technology. The command is explicit: it does not claim every historical or archived test in the repository was run.

## Browser tasks

Verified through actual local-preview controls during this work:

| Task | Observation |
| --- | --- |
| Submit empty correction | Record unchanged, written error shown, reason field receives focus |
| Explain and save | Present count changes 2 → 3, review count 1 → 0; reason appears beside the updated record |
| Undo then inspect history | Original correction and reversal both remain; previous status restored |
| Replace Áurea’s second perfume | First selection stays Vesper Rose; Sol Mist appears; shared Bergamot is written and highlighted |
| Remove a perfume | Remaining profile stays visible with available alternatives |
| Keyboard after selector | Tab reaches the named profile control with visible focus |
| Homepage Visual/Digital | Shows PROOF, BRUME, PLAIN SIGHT and INTERVAL in that order |
| Homepage All work | All twelve project cards appear |

## Widths and visual review

The browser API did not offer physical-device/viewport emulation. A local same-origin iframe harness supplies CSS widths; desktop captures use the browser’s 1348 × 926 viewport. Large specimens are visually scaled in the harness, but the iframe’s internal CSS width remains the requested width. Content width can be 15 px less where a scrollbar is present.

| Page | 320 | 375 | 390 | 768 | 1024 | 1440 | 1920 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Homepage | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| UI selection | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| ImHere roster | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| ImHere correction | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Áurea comparison | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| ImHere case | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Áurea case | Pass | Pass | Pass | Pass | Pass | Pass | Pass |

“Pass” here means no document-level horizontal overflow in the recorded measurement and no completed image loads with zero natural width. It does not mean every offscreen state was visually inspected. Raw observations are in [layout-checks.json](layout-checks.json). Desktop interface/home views, the 320 px comparison, and the desktop/390 px ImHere case were also visually inspected. Final narrow-name alignment and summary consolidation were spot-checked after the matrix.

Screenshots are viewport captures, so long screens continue below the image. The narrow comparison image includes the local harness surroundings. The baseline and after Áurea captures intentionally use different second perfumes to demonstrate replacement/shared-note behavior.

## Limits and remaining checks

- A browser zoom shortcut did not change the reported CSS viewport. **Actual 200% browser zoom is not verified.** Narrow-width reflow is not presented as an equivalent test.
- Reduced-motion rules and the scroll preference guard were reviewed in source; the OS preference was not emulated.
- No physical iOS/Android, Safari/Firefox, VoiceOver/NVDA, color-vision study or manual screen-reader table review was completed.
- No real student, fragrance user, institution or partner study was conducted. No measured improvement in trust, completion, conversion or hiring is claimed.
- The large shared renderer remains a maintenance risk despite scoped styles and regression checks. Persistent backend behavior, authorization and concurrent data integrity are not implemented by these visit-only prototypes.
- Browser logs contained extension metadata errors from `chrome-extension://...`; these are separate from site JavaScript. No site-origin exception was observed in the inspected task flows.
