# NODO — Marketing & production portfolio handoff

## Why this project was chosen

The original repository already demonstrates sophisticated conceptual branding, editorial layouts and UX prototyping, especially through **AFTERFORM, INTERVAL, ImHere and PROOF**. The hiring-role gap is more specifically **repeatable commercial execution**: social campaign formats, HTML email production, print version control and label-family QA. NODO develops those tasks as an independently distinguishable product family rather than creating a ninth generic application.

**Strategy considered:**
1. Extend AFTERFORM with digital campaign assets. Lower production overhead, but adds more work to an already heavily represented brand.
2. Create two unrelated brands for marketing and print. Maximum visual variety, but weaker demonstration of cross-channel consistency and twice the speculative scope.
3. **Selected:** one new product identity with two complete case studies—marketing and print—demonstrating how one brief flows through multiple teams, platforms, revisions and dimensions.

This prioritizes coherent evidence for in-house graphic design hiring.

## Brief

**Fictional brand:** NODO. **Products:** CLIP 06, WRAP 04, GUIDE 02—nonpowered desk cable-organization concepts.

**Creative statement:** MAKE ROOM FOR THE WORK. The visual conceit is a cable-like continuous line used as a system mark across type-led campaign artwork.

**Audience hypothesis:** independent creators, small creative teams, hybrid office workers. No primary research or quantitative target audience validation was performed.

**Business problem (hypothetical):** help people distinguish three small products and understand the practical use of each without repeating the same visual ad fourteen times.

**Marketing objective (unmeasured):** awareness → product recognition → educational consideration → deliberate browsing.

**Tone:** graphic, direct, energetic; the practical object remains understandable. Source files are original editable SVG with familiar-system font fallback.

## Concept direction comparison

- **Quiet office:** quiet ivory fields and restrained lifestyle imagery. Too close to existing editorial projects and hides functional distinction.
- **Technical handbook:** grids, engineering codes and monochrome product rules. Strong information hierarchy but too cold for a consumer campaign.
- **Bold utility (selected):** oversized typography, graphic cable path, distinct product colors and coded labels. Distinctive in social feeds while retaining production precision.

These are internal design explorations, not claims of client approval or research evidence.

## Deliverables

| Family | Count | Final source |
| --- | ---: | --- |
| Social SVG posts | 4 | social/feed-*.svg |
| Social carousel | 6 | social/carousel-*.svg |
| Vertical stories | 3 | social/story-*.svg |
| Professional landscape | 1 | social/linkedin-01.svg |
| Responsive marketing email | 3 HTML + 3 TXT | email/ |
| Product-label masters | 3 | print/source/label-*-r03.svg |
| Print collateral masters | 4 | print/source/ad-a5.svg, postcard-a6.svg, insert-a6.svg, sell-sheet-a4.svg |
| Archived label revisions | 2 | print/archive/ |

### Social production considerations

- Feed and carousel: 1080×1350 (4:5); stories 1080×1920 (9:16); professional landscape 1200×627.
- Story safe zones, interfaces, current ad policies and mobile legibility have **not** been verified in target platform placement previews.
- Platform masters are editable, but they have **not** been posted and no audience metrics have been measured.

### Email production considerations

- Three original, standalone HTML email templates. Key content is text rather than graphic-only. Layout is table-first with inline CSS and Outlook conditional max-width scaffolding. Includes preheader, descriptive headings, mobile viewport styles and text-only alternatives.
- Sample CTAs use `https://example.com/nodo` explicitly as nonfunctional destinations.
- Rendering across live Outlook, Gmail, Apple Mail and dark-mode variants must be tested. A sending system, sender identity, regulatory mailing address, unsubscribe integration and subscriber permissions are **not provided**.
- HTML previews in the portfolio show approximate browser rendering rather than real client screenshots.

### Print production considerations

- Source SVGs use explicit millimeter dimensions with a 3 mm margin for illustrative bleed.
- A separate downloadable ChatGPT package contains vector CMYK PDF specimens with TrimBox/BleedBox and embedded DejaVu typefaces. They are examples only: no vendor ICC output profile, PDF/X certificate, substrate or die proof, barcodes, legal text, physical preflight approval or manufacturing constraints.
- R01→R02→R03 includes a **deliberately simulated mismatch** between label count and sample SKU, to show content QA and archiving. It is not actual client feedback.
- Source design and export formats are not falsely represented as native Adobe Illustrator or InDesign files.

## Production file structure

```text
nodo/
  index.html             # Marketing case study
  production.html        # Print production case study
  nodo.css               # Shared authored web styles
  manifest.json          # Asset and status inventory
  social/                # 14 SVG masters + social brief
  email/                 # 3 HTML + 3 text alternatives + build notes
  print/
    source/              # 7 current SVG masters
    archive/             # 2 historical label states
    README.md            # Bleed, trim, assumptions and vendor checklist
```

## Final review checklist

- Inspect all artwork and spacing at phone, tablet and desktop sizes.
- Check email in actual Gmail / Apple Mail / Outlook clients and with images off; validate CTA links and legal footer before live use.
- Confirm platform aspect ratio and safe zones against actual placement options.
- Read each label and verify quantity, SKU, product info, font minimums at printed size.
- Run printer-specific preflight with ICC, PDF/X policy, trapping/overprint rules, and physical proofs.
- Check page links and alternative text; this repository uses static relative paths.
- Document any authentic client collaboration or observed outcomes in a later revision, not retroactively.

## What this does not establish

This project does not establish advanced native Adobe proficiency, empirical campaign performance, real client collaboration, regulatory packaging expertise or real vendor print release. Those remain valuable areas for professional practice.
