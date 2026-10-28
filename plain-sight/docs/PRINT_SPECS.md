# PLAIN SIGHT — Print & Production Notes

## Observation edition / 03

- **Document:** `downloads/PLAIN_SIGHT_Studies_01-03.pdf`
- **Actual page count:** 24 complete designed pages (not mocked-up spreads)
- **Trim/page size:** A4 portrait, 210 × 297 mm, 595.28 × 841.89 pt
- **Working safe area:** 40pt (about 14mm) for the main grid; running folios sit outside this area
- **Color:** RGB composite PDF meant for **digital review and print concept evaluation**, not validated commercial CMYK output
- **Bleed:** **No external 3 mm bleed included.** Full-bleed-looking compositions reach the document trim edge only; a commercial printer would require extending artwork to a supplied bleed size.
- **Raster source size:** Primarily ~1024–1400 px on long dimensions; variable effective DPI. Suitable for screen presentation; not guaranteed at 300 DPI for a full A4 page.
- **Fonts:** Bodoni Moda and DM Sans are embedded by ReportLab under the SIL Open Font License. License copies are preserved in `src/fonts/`.
- **Printer/supplier proof:** None. No spot colors, Pantone system or physical proof is claimed.

## Previous-edition identity guide

- **Document:** `downloads/PLAIN_SIGHT_Identity_and_Production_Guide.pdf`
- **Status:** Preserved historical guide; the reconstruction system is documented in `reconstruction/system.md`.
- **Pages:** 8
- **Format:** A4 landscape. Illustrated color, typography, composition and scope notes.

## Posters and social

- **Six posters:** `assets/posters/poster-01.svg` through `poster-06.svg` at an 840 × 1150 design viewBox. Vector type, embedded WebP source imagery. They are editable visual masters, **not press-preflight files**.
- **Six square campaigns:** `assets/social/social-01.svg` through `social-06.svg` at 1080 × 1080 px.
- **Two carousels:** `assets/carousels/` contains 12 SVG slide masters at 1080 × 1350 px.
- **Four stories:** `assets/stories/` at 1080 × 1920 px.
- **Web banners:** `assets/banners/` 1600 × 420, 1200 × 628 and 970 × 250.

## To prepare for physical production

1. Confirm production substrate, vendor profiles and actual finished size.
2. Create final design with 3 mm bleed and vendor-safe marks when required.
3. Replace any full-size images whose effective resolution is below the printer's agreed threshold.
4. Perform ICC-aware CMYK/spot-color conversion with a proofing workflow, if required.
5. Export PDF/X format if requested and embed/outlining policy as agreed with the printer.
6. Run font/bleed/color/overprint preflight and obtain a physical proof.

These steps are not represented as completed.

The previous 24-page publication is preserved in `downloads/archive/PLAIN_SIGHT_Studies_Edition02.pdf`. Rebuild the new PDF and exact previews with `src/build_publication.py`, then regenerate the website with `src/build_site.py`.
