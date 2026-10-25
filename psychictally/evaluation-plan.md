# PsychicTally — formative evaluation plan
**Status: planned, not conducted.** Prepared as supporting design documentation for the PsychicTally portfolio case study. No sessions, participants, screenshots, findings or metrics are implied.
## Questions
1. Can a first-time visitor distinguish a discussion thread from a reader review?
2. Can someone find and revisit a saved or followed discussion?
3. Can a contributor understand the privacy implications of a new post?
4. Can an authorized moderator find a report, understand the reported context and predict the consequence of each available action?
## Method
- Obtain informed consent before collecting notes or recordings; avoid real sensitive discussions or account credentials.
- Use a staging workspace with synthetic, disclosed example data. Do not run destructive or role-elevation tests on production.
- Suggested sample: 5–6 participants who match realistic needs; recruitment has **not** occurred.
- Ask participants to verbalize their expectations before each action. Collect observed paths, hesitation points and recovery attempts, not invented satisfaction scores.
- Test keyboard-only navigation, 200% zoom, minimum mobile viewport and at least one assistive-technology path.
## Tasks (draft)
1. "You want to read about a specific topic. Find two discussions and explain how they differ from reviews."
2. "Find a conversation you wish to revisit, save it and locate it again."
3. "Begin creating a post, inspect visibility choices and describe who could read it. Do not publish."
4. "Using a staging moderator account, locate a synthetic report and describe what would happen if you request context versus resolve it."
## Findings table — intentionally blank
| Participant code | Task | Observed behavior | Severity (after review) | Evidence | Proposed change |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | Not yet observed | TBD | TBD | TBD |
## Release checks
- Confirm route parity between direct links, back/forward and refreshed navigation.
- Verify guest, member and moderator boundaries against actual Supabase policies.
- Test hosted sign-up, confirmation, recovery, device changes, CAPTCHA, storage and privacy settings with **disposable test identities**.
- Test real browser/device layouts, focus restoration, screen-reader labels, reduced motion and color contrast.
- Do not claim increased engagement, conversion, accessibility compliance or user satisfaction without measurements.
## Evidence and privacy
The implementation uses a separate, privately maintained GitHub repository. Public portfolio artifacts are visual explanations, and the local report specimen is not connected to user data. Publish findings only with consent and remove identifying information.
