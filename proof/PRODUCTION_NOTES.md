# PROOF / Error to Edition — production and design handoff

Self-directed, AI-assisted portfolio project, October 2026. All physical artifacts depicted in AI-generated photographs are **fictional**. They are art-direction studies, not photographs of real prints.

## Why this direction

The preceding PROOF version was dominated by flat abstract SVGs, a heavy application-style layout and several unrelated fictional visual brands. This replacement uses one visual family with an art-directed high-contrast print-studio vocabulary: near-black `#181917`, warm paper `#F2EFE8`, orange `#FF542D`, acid green `#DBFA36`, and mono production metadata. The accent colors appear in artwork as translucent proofing films and contact-sheet marks, not scattered decorative badges.

Unlike BRUME's sculptural-glass lifestyle photography, AFTERFORM's softer fashion/reuse direction and INTERVAL's cultural promotion, this has a raw, architectural, process-oriented studio identity. The central commercial problem is how to communicate one issue coherently across print, social, email and a controlled revision process.

## Inspectable deliverables

- Source photography: two generated original concept photographs by OpenAI ImageGen. `assets/hero-studio.webp` and related deliberate crops, plus a secondary art-direction board crop. Generated source files are in the `src/` companion files in the ZIP; images do not prove a physical studio or real printed work.
- Social: six **1080 × 1350** authored WebP designs. `assets/campaign-01.webp` through `campaign-06.webp`. Separate story in **1080 × 1920** `assets/campaign-story.webp`. Each is a final raster composition, with editable authoring source in `src/build_assets.py`, not a native layered Photoshop file.
- Email: two browser-testable, table-based, live-text HTML email files and TXT fallbacks. Links and image URLs are *local demo* paths; replace them with hosted assets, working preference controls, sender identity, unsubscribe and compliance information before any live mailing.
- Publication: `PROOF_Issue_01.pdf`, **12 individual A5 reading pages (148 × 210 mm)** with original conceptual editorial copy and picture placement. These pages currently have no commercial bleed/imposition. The text and layout are reproducible from `src/build_print.py`.
- Print advertisement: `PROOF_Print_Specimens.pdf`, one A5 visual specimen (148 × 210 mm). The image itself is designed as a raster print-creative at 1600×1040 master. Not PDF/X-certified or printer-approved.
- Interactive review room: slider showing toned preliminary vs revised campaign graphic, print guide toggles, keyboard-accessible controls, with DOM source in `app.js`.

## Before production

1. Confirm supplier, page count, imposition, trim, binding, stock and required bleed.
2. Resolve all required real material and legal copy. No fictional physical product statements should be represented as real facts.
3. Verify licensed fonts, suitable image resolution at physical output size, color profile, spot colors, trapping and overprinting.
4. Export to supplier-requested CMYK/PDF/X profile with correct TrimBox/BleedBox, outlined or embedded fonts, and appropriate color proofs.
5. Review actual Gmail, Outlook, Apple Mail rendering, image-off mode, dark mode, destination and opt-out controls before email distribution.
6. Preview social placements at actual mobile size and platform safe zones.
7. Inspect a physical printed proof before claiming production completion.

## Art direction research

- [Studio Format (2026)](https://www.behance.net/gallery/241992867/Studio-Format) — publishing systems, legibility, real material processes. *Principle referenced, not copied.*
- [Mohawk — The Art of Digital Paper](https://www.behance.net/gallery/234048335/MohawkThe-Art-of-Digital-Paper) — paper-centered photography and finishing choices. *Principle referenced, not copied.*
- [Pinterest Creative Best Practices](https://create.pinterest.com/fundamentals/) — mobile-first composition, clear thumbnails, image-led hierarchy.
- [PRINT Awards 2025](https://www.printmag.com/print-awards/the-best-of-the-2025-print-awards-from-tactile-irl-encounters-to-lush-digital-worlds/) — categories for commercial print, in-house marketing, identity and motion.

Pinterest boards are inspiration categories, not a claim that specific inaccessible boards were directly inspected or copied.
