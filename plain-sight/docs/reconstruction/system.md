# PLAIN SIGHT — observation edition design system

This system supports eleven static pages, a five-source archive and a 24-page digital publication. It is deliberately smaller than a generic component library. The public HTML is generated from `src/build_site.py`; the committed result works on GitHub Pages without a runtime build.

## Foundations

| Role | Decision | Reason |
|---|---|---|
| Paper / panel / white | `#f2efe8` / `#e7e3da` / `#fcfaf5` | Warm exhibition field; separate inspection mats without shadows |
| Ink / secondary | `#282824` / `#62615a` | Clear reading hierarchy without extremely pale captions |
| Accent | `#723e43` | Restrained wine tone shared with the flower imagery |
| Focus | `#115b8b`, visible outline with offset | Distinct from selected and hovered states |
| Display | Locally served Bodoni Moda normal and italic, regular | Expressive entry and editorial rhythm; not used for controls |
| Functional type | Locally served DM Sans | Body, labels, controls, captions and tabular source numbers |
| Main grid | Twelve-column relationships expressed through named layouts and fractional CSS tracks | Common alignment, different chapter pacing |
| Outer space | Fluid gutters, 20px at narrow widths; bounded wide content | Prevents edge crowding and overlong reading lines |
| Text measure | Approximately 40–65 characters for editorial reading; shorter annotations | Keeps the photograph primary and notes readable |
| Spacing | Repeated 8/12/16/24/32/48/64/96px relationships, fluid section spacing | Local precision and slower chapter pacing |
| Breakpoints | 1100 / 760 / 400px content-driven transformations | Grid simplification, stacked inspection, mobile navigation |
| Motion | Short feedback transitions; optional manually started specimen | No forced introduction, autoplay gallery or scroll hijacking |
| Layering | Page, mobile navigation, native dialog top layer | Native modal focus/inert behavior instead of custom z-index machinery |

Exact implementation values are authoritative in `assets/styles.css`; this is the rationale, not a second token source.

## Typography roles

| Role | Treatment |
|---|---|
| Display / homepage H1 | Bodoni, fluid large scale; italic accent within an intentional two-line phrase |
| Page H1 | Bodoni, fluid approximately 54–150px according to page purpose |
| H2 | Bodoni, fluid editorial scale; no all-caps body-length headlines |
| H3 | Bodoni for source-card titles, DM Sans for utility headings |
| H4 | No required fourth-level component; use semantic hierarchy when future content needs it |
| Editorial quotes / interludes | Bodoni italic, generous leading; brief phrases |
| Body | DM Sans, 16px or larger in primary reading blocks, approximately 1.5–1.65 line height |
| Captions | DM Sans, usually 12–14px; source ID remains distinct from image title |
| Navigation / controls | DM Sans, approximately 14px; clear underlines, borders or button fills |
| Metadata / source numbering | DM Sans with restrained tracking and tabular numerals; generally 11–13px |
| Publication annotation | Embedded DM Sans, 9–12pt; Bodoni chapter/display roles |
| Contact | Large wrapping real email link plus ordinary copy button; no form typography needed |

The three comparative type specimens are in [concepts.html](concepts.html). Instrument Serif and IBM Plex Mono were removed from this product's web font stack because their additional roles were redundant. The historical SVG campaign files still use portable Georgia/Arial text; this is documented rather than misrepresented as full cross-medium font conversion.

## Components and state contracts

| Component | Default / hover / focus | Selected / expanded | Recovery and boundaries |
|---|---|---|---|
| Navigation | Native links, visible hover and focus | Current page indicated; mobile Menu button exposes `aria-expanded` | Base HTML navigation stays visible without JS; Escape closes enhanced mobile menu and returns focus |
| Study card | Link names the chapter and subject | Current chapter navigation names 01/02/03 | Complete next-study cycle; All studies always available |
| Source card | Full image, meaningful description, stable source ID | Category filter changes actual source visibility and count | Invalid series returns all; no empty results for fixed categories |
| Focused viewer | Native dialog, complete source image, close/previous/next buttons | Source identity, position and note update together | No wrap at boundaries; Escape/Close restores opener; direct image link and image-error text |
| Filter links | Ordinary deep links without JS | `aria-current`, count announcement, URL state | Back/Forward restores filter; filter counts originals only |
| Light table | Full original beside an existing derivative, with notes | Source link selected; native crop select; optional guides | Invalid source/cross-parent crop resolves to a valid parent-child pair; image-error message includes direct-image route |
| Composition guides | Explicit checkbox, no drag or hover requirement | Rule-of-thirds overlay on each displayed frame | Guides are a present-day viewing aid, not claimed capture metadata; notes remain usable without guides |
| Publication reader | Actual PDF page raster plus page title, description and text companion | Native select, page/chapter links, current thumbnail | Next/previous disabled at ends; enlarge within local scroll area; direct PDF and image links survive without JS |
| Copy email | Hidden until handler exists | Live status announces copied address | Failure tells visitor to select/copy the visible address; nothing is sent |
| Optional motion | Static by default | Play/Pause and accurate pressed state | Reduced-motion preference disables animation and describes the static state |

Image loading reserves intrinsic space. The interface does not add a fake progress percentage or block content behind a loader. Broken-image notices are available in interactive inspection surfaces. No user data, selections or preferences are saved to a server or local storage; URL state can be shared.

## Content and implementation contract

`collection.json` owns five originals and eleven child crops. Each record includes ID, title, meaningful alternative text, actual dimensions, authored framing note and publication destination. The pure model validates incoming URL values. The DOM renderer uses `textContent`, ordinary links and native controls; it does not interpret URL text as markup.

`build_publication.py` creates the canonical PDF, exact page previews and page-text manifest. `build_site.py` embeds those manifests and generates static pages, shared markup and 480px thumbnail candidates. Preserve original source images. Do not register a crop as an original or create new images solely to expand the count.

Regeneration order: publication first, website second. Required Python libraries: Pillow, ReportLab, pypdf; Poppler's `pdftoppm` must be on PATH. The Node behavior tests use only built-in modules. The site needs no package install, framework or external font CDN.
