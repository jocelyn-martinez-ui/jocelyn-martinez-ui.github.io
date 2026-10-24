# PROOF / Production and handoff checklist

This is a technical **concept specimen**. No file has been certified for a press, manufactured, approved by a vendor, or submitted to an external production partner.

| Deliverable | Intended trim | Master size | Sample bleed | Source |
| --- | --- | --- | --- | --- |
| TERRA 3 label fronts | 90 × 130 mm | 96 × 136 mm | 3 mm / each side | `commissions/terra/label-*-r03.svg` |
| TERRA A5 advertisement | 148 × 210 mm | 154 × 216 mm | 3 mm / each side | `commissions/terra/ad-a5.svg` |
| TERRA A4 sell sheet | 210 × 297 mm | 216 × 303 mm | 3 mm / each side | `commissions/terra/sell-sheet-a4.svg` |
| FIELD editorial pages | A5 / 148 × 210 mm | 148 × 210 mm | None included in individual page source | `commissions/field/page-*.svg` |
| PULP poster concepts | Screen-sized source only | 850 × 1100 px | None | `commissions/pulp/0*.svg` |
| PULP social masters | 1080 × 1350 px, 1080 × 1920 px | Same | n/a | `commissions/pulp/social-*.svg` |

The FIELD pages are **not** commercial bleed-ready, and PULP source is display art only. They are not to be sent to a printer as finished press files.

## TERRA revision sequence (simulated)
- **R01:** “T-07 / OLD COPY”, a placeholder code and incomplete description.
- **R02:** “T-07 / 10 MM”, outdated nominal material thickness.
- **R03:** “T-01 / 12 MM”, concept-current Mist information. Not verified product data.

Both prior states are archived. The revision sequence is a fictional QA exercise, not feedback from an actual manufacturer.

## What must be checked before any physical production
1. Genuine supplier dieline, die tolerance, stock, substrate and adhesive.
2. Product grade, dimensions, tolerances, finish, legal claims, geographic language, SKU system and mandatory manufacturer information.
3. Print method, spot colors and separations; artwork currently uses RGB SVG hex swatches, not printer-approved CMYK plates.
4. Font rights, outlines/embedding, optical scale, legibility at printed size, missing image links and overprint/trapping.
5. Exact TrimBox, BleedBox, PDF/X output intent, ICC profile and vendor-specific required settings.
6. Physical press or contract color proof and sign-off before real print distribution.

## Local demo semantics
The website preflight guides illustrate concepts at scale relative to a browser viewport; they are **not measured press guides** and the sample checklist does not confirm real vendor readiness.

## Source organization
- `commissions/pulp/` editable marketing SVGs and 12-page brand guide.
- `commissions/pulp/email/` 3 responsive HTML email files and text-only alternatives.
- `commissions/field/` 12 A5 SVG page sources.
- `commissions/terra/` 3 label sources and 2 collateral sources; `archive/` keeps historical states.
- `workspace.html` previous working local approval prototype.

## Print packet status
A printable PDF sample packet, if provided separately as a downloadable ChatGPT artifact, is a **portfolio proof document** until validated against actual source geometry and printer specifications. Do not confuse a viewer-rendered sample with press-authorized production artwork.
