# PsychicTally — implementation verification

Portfolio review: October 25, 2026. Inspected application commit: `88d44c0dfab4adafb3e1e14cbd3e4645a9659ba2`.

The application source is held separately from this public portfolio. This record summarizes an independent read and local execution of that source. It does not publish private implementation files, credentials or community records.

| Check | Result | What it establishes |
| --- | --- | --- |
| Core Node tests | 73 passed | Fixture-based rendering, data, roles, review and thread behavior |
| DOM journey | 1 passed | Forms, routes and event handlers in jsdom with sample data |
| SQL/PGlite tests | 12 passed | Policies, grants and confidential record boundaries in a local Auth/Storage harness |
| Source check | 25 modules / 85 imports passed | Syntax, local imports and required assets |
| Demo build | Succeeded | Local sample-mode output |
| Production-configuration fixture build | Succeeded | Validation/build with synthetic, non-routable public configuration |
| Build-test discovery | 0 tests | This command currently supplies no regression coverage |

**86 tests passed; zero failed.** Runtime: Node 24.22.1. The builds did not contact a hosted database or deploy anything. A successful command with zero discovered tests is not counted as a passing test suite.

## Design decisions connected to implementation

- **Permission boundaries:** the data service verifies sessions and clears sensitive state on failure. Database policies distinguish contributor, staff and administrator access. This supports a role-dependent UI; hiding a button alone would not enforce privacy.
- **Moderation context:** support messages, staff notes, appeals and standing are distinct records. The SQL tests exercise confidential-note boundaries rather than assuming every authenticated user may read every record.
- **Review information:** source and tests distinguish review publication and insufficient samples. A polished percentage is not substituted for evidence when a sample is too small.
- **Delivery:** the build validates public configuration and rejects privileged server credentials. Deployment acceptance remains a separate test.

## Public entry observation

The public entry at https://psychictally.com/ rendered its signed-out application and community navigation during this review. Displayed records and counts were not treated as adoption or authenticity evidence. No member account was used, no contribution submitted, and no live permission test performed.

## What remains unverified

Live registration, email delivery, hosted Auth callbacks, deployed policies, real-member journeys, production performance, cross-browser accessibility and actual usage outcomes were not established by these local checks. The public portfolio's moderation specimen is a separately authored illustration; it does not expose application records.

The source also bulk-loads substantial sections of visible data. This is an implementation tradeoff to discuss and improve before making scale claims. No commercial scale, research results or security certification is implied.

The next useful UX evidence is a small observed study of finding a discussion, distinguishing a review from a forum post, and recovering from an unsuccessful contribution. The existing evaluation plan remains proposed work.
