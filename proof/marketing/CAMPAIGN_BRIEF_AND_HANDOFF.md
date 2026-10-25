# PROOF / The Integrated Campaign
**Edition:** October 25, 2026 · **Nature:** fictional self-directed AI-assisted graphic design work.

## The commercial brief
- **Concept client:** PROOF, a fictional independent editorial/design-publishing concept; no actual commissioning organization exists.
- **Product:** PROOF Issue 01, a 12-page conceptual publication about the decisions behind graphic design.
- **Audience (hypothesis):** young design practitioners, curious visually literate readers and creative producers; no customer research was conducted.
- **Communication challenge:** promote a design publication while making process and production interesting enough to read across different channels.
- **Campaign promise:** GOOD IDEAS DESERVE GOOD PROOFS.
- **Desired action:** visit the portfolio's publication or graphic case study, not make a purchase.
- **No invented metrics:** No email was delivered, no ad ran, and no engagement, CTR, ROAS or commercial outcome is asserted.

## Visual direction / why this is different
The selected direction is **Signal + Evidence**: monochrome contact-sheet / print-studio photographs interrupted by fluorescent orange and acid yellow; a steady wordmark; structural technical labels; and strong typographic hierarchy. Graphic imagery is sourced from original, AI-generated PROOF project assets already held in the user's GitHub repository, not scraped from Pinterest.

Other directions examined conceptually:
1. Quiet independent magazine editorial — strong typography but too similar to the softer portfolio identities (BRUME/AFTERFORM).
2. Full ink-texture/halftone experiment — bold but susceptible to the same repeated abstract poster problem in earlier rejected PROOF versions.
3. **Selected:** photographic proof-sheet art direction with sharp signal color and format-led recomposition; more distinctive for a graphic-production role.

## Researched references and transferable principles
- [Pentagram / Paula Scher / The Public Theater](https://www.pentagram.com/work/the-public-theater/story) — a strong typographic identity able to adapt from posters to multiple public-space applications. Useful principle: hold the identity steady while changing composition.
- [Pentagram / Shakespeare in the Park 2023](https://www.pentagram.com/work/shakespeare-in-the-park-2023/story) — an explicitly documented flexible kit of elements applied to posters, signs, social graphics and animations. Useful principle: campaign toolkit, not one template.
- [Studio Dumbar / Modyfi](https://studiodumbar.com/work/modyfi) — a coherent system of layered symbols, grids and visual modifiers that translates into motion. Useful principle: motion and modifiers should belong to the identity.
- [Pinterest / experimental editorial graphic design](https://www.pinterest.com/ideas/experimental-editorial-graphic-design/947597997389/) — thematic discovery for publication and visual hierarchy.
- [Pinterest / creative social media marketing collage](https://www.pinterest.com/ideas/creative-social-media-marketing-collage/927167074445/) — exploration of photography and editorial composition.
- [Pinterest / social media campaign design](https://www.pinterest.com/ideas/social-media-campaign-design/960259697892/) — format and compositional inspiration.
- [Pinterest / risograph poster typography](https://www.pinterest.com/ideas/risograph-poster-typography/950422155736/) — print-derived layering used critically rather than randomly.
These Pinterest pages were retrieved as search/discovery collections, **not** a verified 25-reference individually credited image board. None of the reference images or branded compositions were reproduced in the source assets.

## Media architecture
| Deliverable | Count | Source | Role |
| --- | ---: | --- | --- |
| Carousel A | 6 | `social/carousel-a-*.svg` | educate about design review and production |
| Carousel B | 6 | `social/carousel-b-*.svg` | demonstrate compositional adaptation |
| Story masters | 2 | `social/story-*.svg` | original 9:16 art direction |
| Digital ads | 4 | `ads/*.svg` | square, portrait, landscape and wide adaptation |
| Email marketing | 4 HTML + 4 TXT | `email/` | launch, editorial, revisions, follow-up |
| Print promotional art | 3 | `print/*.svg` | A5 ad, A6 mailer front, A4 sheet |
| Browser motion concepts | 2 | `motion/*.html` | meaningful photographic reveal and typographic intervention |

All **18 new social/ad SVG masters** contain base64-embedded first-party project photographs, editable text and vector shapes, with no dependency on external SVG image references. Print pieces have the same source structure and provisional document geometry.

## Email lifecycle logic
1. **Launch:** visual introduction, key promise and opening the existing publication PDF.
2. **Editorial discovery:** overview of content, moving to the full case study.
3. **Revision process:** clear before-and-after idea connected to the review lab.
4. **Format system:** follow-up educational content linking to the interactive format studio.

One sender identity, one footer/component language, different content structures. HTML uses live copy and hosted HTTPS images; the latter would require a real asset CDN and real sender approval in commercial use.

## Reusable graphic system
- **Ink:** `#181917`.
- **Paper:** `#F2EFE8`.
- **Signal orange:** `#FF542D`.
- **Acid yellow:** `#DBFA36`.
- **Functional type:** Arial/Helvetica for display; Georgia for longer editorial reading; Courier New for specification labels.
- **Grid rule:** baseline brand band, editorial image field, hierarchy of one headline and one supporting statement, version/size labels; recomposition is required by each format.
- **Art direction:** distinguish image-led campaign compositions from reading-first email and short-lived display placements.

## Source/export and handoff naming
`PROOF_[CHANNEL]_[CAMPAIGN]_[FORMAT]_[SEQUENCE]_[REVISION].[EXT]`
Examples:
- `PROOF_SOCIAL_ANATOMY_FEED_SLIDE-01_R01.svg`
- `PROOF_EMAIL_LAUNCH_RESPONSIVE_R01.html`
- `PROOF_PRINT_POSTCARD-A6_FRONT_R01.svg`
- `PROOF_MOTION_CONTACT-TO-TITLE_R01.html`

The repository uses shorter working paths but these identifiers are represented in the manifest/creative handoff.
**Current status:** authored concept masters, not real marketing approval, campaign performance, print preflight certification or production-delivered evidence.

## Review and release checks
1. Proof copy, alt descriptions, image licensing/provenance and final destination URLs.
2. Current platform dimensions and story safe zones.
3. Inspect social artworks in mobile device preview to confirm no cropping or illegible small text.
4. Real email-client rendering in Outlook, Gmail and Apple Mail, including images disabled and dark-mode behavior; confirm sending permissions, sender details and working unsubscribe.
5. Print vendor profiles, physical proof, effective image resolution, material specification and PDF/X/CMYK requirements.
6. For motion, encode actual videos and check duration, audio/captions, looping and file limits. The existing prototypes are working CSS browser animations, **not** exported video files.

## Hiring manager evaluation
- **Useful evidence:** distinct campaign compositions, actual HTML email production, adaptability across five output shapes, photography-driven art direction, editable vector source artwork, consistent creative system, source/version organization and honest preflight boundaries.
- **Remaining gaps:** real marketing deadlines/collaboration, Adobe native-file workflows, email-client screenshot testing, verified vendor printing, measured customer results and native video exports.
- **How to discuss this honestly:** present PROOF as a self-directed commercial-design simulation, and describe each real file and its limitations. Do not claim the skills of a live production team without that experience.
