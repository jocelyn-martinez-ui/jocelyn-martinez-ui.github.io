# BRUME — Photography-led portfolio replacement

This is a complete self-directed, AI-assisted design concept for a fictional sculptural lighting studio, replacing the rejected NODO art direction.

- `index.html` — photographic campaign case study, 15 live-image SVG artwork masters and three HTML emails.
- `production.html` — 3 edition labels, 4 print collateral pieces, simulated archived revisions and technical print caveats.
- `research.html` — portfolio differentiation, three moodboard approaches and cited original creative references.
- `social/*.svg` — editable compositions with linked AI-generated photographic assets; `social/*.png` are flattened counterparts.
- `images/*.jpg` — four conceptual image-generated product scenes. Images do **not** document manufactured lighting products or a real photo shoot.
- `email/*.html` & `email/*.txt` — three standalone table-based mock emails, with sample links. Clients and legal footer not validated for a real send.
- `print/svg/` & `print/pdf/` — dimensioned source graphics and specimen vector PDFs; print-specific CMYK spot decisions, output profiles, packaging dies, and electrical safety not validated.
- `build_assets.py`, `build_email_print.py`, `build_site.py` — reproducible authoring scripts. These use system-installed fonts; font files are not included.

## Visual change

NODO = flat vectors / loud display sans / color blocks / product-icons. BRUME = photographed glass / warm cinematic atmosphere / small editorial serif / material and context. The campaign emphasizes different photographic crops and rhythms rather than repeating one layout.

## Scope and verification

Source assets, relative paths, responsive rules and PDF geometry are programmatically inspectable. Full professional accessibility, actual email-client QA, real printer preflight, physical production and user testing have not been completed.

To preview: run `python -m http.server` from this directory and open `index.html`. GitHub Pages can serve the files as a static `/brume/` subdirectory.

## Browser SVG image-loading fix

As of 24 October 2026, all 15 social SVG masters and four photo-based print SVGs embed their photographic JPEG layers as `data:image/jpeg;base64,...`. An externally linked `<image href="../images/...">` can be blocked by browsers when the SVG is displayed through an HTML `<img>` element. The original JPEG files remain in `images/`, and the typography/vector components of the SVGs remain editable. The Python generators preserve embedding on rebuild. Email artwork loads from an absolute HTTPS URL for real email-client interoperability (still requires client testing and the user's consent before any actual sending).
