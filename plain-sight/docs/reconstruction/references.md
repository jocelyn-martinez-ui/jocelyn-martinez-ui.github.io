# PLAIN SIGHT — research and influence ledger

Research date: 27 October 2026. This is a practical design study, not a claim that the referenced designers participated in this project.

The ledger contains **28 evaluated references**: twelve requested designer influences and sixteen exhibition, archive, publication or implementation references. The five supplied Pinterest links and two discovery platforms are recorded separately because inaccessible pages are not evidence. Sources were read through their public pages, museum records, original studio descriptions and official documentation. **No reference site was exhaustively usability-tested in this research pass.** A site's own claims about its interface are identified as such; awards and reported traffic are not evidence of suitability for PLAIN SIGHT.

“Translation” below means a new design proposal for PLAIN SIGHT. It is our inference, not a recommendation made by the source. Typography and composition observations drawn from descriptions are distinguished from a direct visual audit. No reference artwork, photograph, proprietary font or code has been copied into the product.

## Decision from the research

Use **the Observation Index as the structure, the Digital Exhibition as the viewing treatment, and the Living Publication as a connected artifact**. Keep an overview and a focused viewer; put reading notes next to the image they explain. Three equally prominent LOOK / INDEX / READ modes would make a small collection appear more complex than it is.

The distinctive interaction should be a source-and-crop light table: one source image, its real derivative treatments, a visible relationship between them, and concise composition notes written during this redesign. It should reveal how attention changes when the frame changes. The index must count unique source images separately from crops. A visitor should never have to understand the light table to enjoy a chapter.

Adopt a shared page grid, visible image numbering and stable controls. Let chapter composition vary: portrait rhythm for Gestures; comparative arrangement for Arrangements; larger pauses and spatial frames for In Between. Keep captions out of important image details. No sound, webcam, fisheye lens, scroll interception, artificial film negatives or automatic slideshow is justified by this material.

## The twelve designer influences

For historical printed objects, “navigation” refers to reading order; there is no interactive behavior to reproduce. Accessibility implications are our assessment of translating the work to a contemporary website, not a retrospective certification of the original.

| # / designer and specific work | Verified source and evidence | Problem / underlying principle | Type, image and reading order | Original PLAIN SIGHT translation | Avoid / accessibility consequence |
| --- | --- | --- | --- | --- | --- |
| 01 — Josef Müller-Brockmann, **Beethoven** concert poster, 1955 | [Smithsonian / Cooper Hewitt record](https://collections.si.edu/search/detail/edanmdm:chndm_2019-22-6). Museum text identifies the designer, date, concentric structure and central information. | Make an abstract musical event perceptible through ordered rhythm. Repetition can organize attention rather than decorate it. | Museum description: expanding/contracting concentric intervals focus information. This is a hierarchy reference, not a web grid specification. | Use repeatable image numbers, margins and a twelve-column alignment system; vary spans and intervals to create chapter pacing. | Do not reproduce the rings or diagonal poster composition. Keep reading order linear in the DOM even when visual columns differ. |
| 02 — Armin Hofmann, **Giselle, Basler Freilichtspiele**, 1959 | [MoMA collection record](https://www.moma.org/collection/works/6775). Object, date and medium verified; image record retrieved. | Reduce a complex performance to one forceful image/type relationship. | A photographic poster is the relevant format. The proposal takes contrast and reduction as an interpretive principle, not its exact letter placement. | Let a single body/fabric source carry the Gestures opener; use one quiet caption and controlled surrounding space. | No copied dancer silhouette or layout. Do not convert essential headings to image-only lettering or use thin display type for controls. |
| 03 — Massimo Vignelli, **National Park Service Unigrid**, 1977; Lella Vignelli also credited by MoMA | [NPS history](https://www.nps.gov/subjects/hfc/a-brief-history-of-the-unigrid.htm); [MoMA object](https://www.moma.org/collection/works/89304). Primary institutional explanations. | Reduce routine production choices while allowing very different subject matter to remain coherent. | Modular panels, a controlled typographic system and predictable information placement serve varying maps and imagery. | One token and component system across web and publication, with chapter-specific spans rather than separate UI conventions. | Do not copy NPS bands, arrowhead or brochure formats. Consistency should help users predict controls, not force every photograph into one aspect ratio. |
| 04 — Wim Crouwel, **New Alphabet**, 1967 | [The Foundry Types specimen and history](https://www.thefoundrytypes.com/fonts/new-alphabet/), produced in collaboration with Crouwel. Full text read. | Treat a medium's constraints as design material. | The foundry describes letterforms shaped by electronic display limitations and a modular construction. | Make the image's real dimensions and crop relationship visible in the light table. Let the grid explain the medium rather than imitate a film scanner. | Do not use New Alphabet for readable interface text or copy its glyph construction. Experimental display treatment must have ordinary text equivalents. |
| 05 — Herb Lubalin with Tom Carnase, **Avant Garde magazine logotype**, 1968 | [Mindy Seu's publication archive](https://avantgarde.110west40th.com/), with commentary by Lubalin Center curator Alexander Tochilovsky and Steven Heller. Full archive text read. | A wordmark can embody the publication's proposition; optical relationships matter more than arbitrary tracking. | The archive explains tightly fitted letterforms and the logotype's expansion into a typeface, including misuse of ligatures. | Treat PLAIN SIGHT as a deliberate two-word composition; adjust spacing at display size while leaving navigation typesetting neutral. | Do not reproduce Avant Garde ligatures. Do not apply headline spacing tricks to captions or paragraph text. The wordmark remains legible and has an accessible name. |
| 06 — Neville Brody, **The Face, no. 37**, May 1983 | [Design Reviewed physical archive record](https://designreviewed.com/artefacts/the-face-no-37-may-1983/); [National Portrait Gallery attribution](https://www.npg.org.uk/collections/search/person/mp65954/neville-brody); [Brody Associates' Supreme project](https://www.brody-associates.com/work/supreme) confirms reuse of his Face-era graphics. Record/text, not a complete spread-by-spread examination. | Editorial identity can change register between stories without losing authorship. | Expressive titles are a compositional layer; they need not dictate body typography or the navigation model. | Give each chapter a different title/image relationship and pace while preserving the same controls and caption hierarchy. | No lifted Face lettering, emblems or distressed motifs. Do not make the current chapter unrecognizable when its art direction changes. |
| 07 — Irma Boom, **SHV Think Book 1996–1896**, 1996 | [MoMA collection and curatorial account](https://www.moma.org/collection/works/110948). Full text read. | The structure of a book can create discovery instead of merely containing information. | MoMA describes reverse chronology, edge imagery, material experiments and deliberate omission of conventional navigation aids. | Sequence the 24-page publication from whole frame to detail and back to spatial context; make chapter changes visible in the web reader. | Crucially, **reject the omitted index/page numbers** for this public web experience. Borrow structural storytelling, not deliberate disorientation or its physical format. |
| 08 — Paula Scher, **The Public Theater identity** | [Pentagram case study](https://www.pentagram.com/work/the-public-theater). Original studio text read; one requested image fetch was blocked. | A cultural institution needs a recognizable voice that works across changing programmes. | Pentagram describes active typographic juxtaposition and later structural refinement. | A confident, repeatable PLAIN SIGHT wordmark and numbered chapter language should carry from screen to poster and publication. | Avoid Public Theater lettering, density and palette. The source supports an identity principle; it does not justify making every control loud. |
| 09 — April Greiman, **Does It Make Sense?**, Design Quarterly 133, 1986, and **alt&lt;DQ**, 2024 | [Greiman's own project account](https://www.aprilgreiman.com/books/alt-dq-does-it-make-sense); [SFMOMA record of the 1986 work](https://www.sfmoma.org/artwork/96.366/). | Let a medium open new relationships between information, image and space. | Original digitally assembled collage and a later spatial reinterpretation are described by the designer. | Connect image, crop and annotation as inspectable layers; reveal a framing decision through an optional guide overlay. | Do not mimic collage density or add AR to satisfy novelty. Guides must switch off, and the same explanation must be available as text. |
| 10 — Dieter Rams, **606 Universal Shelving System**, 1960 | [Vitsœ product explanation](https://www.vitsoe.com/us/606); [Rams's principles via Vitsœ](https://www.vitsoe.com/us/about/good-design). Primary manufacturer text. | A restrained system can adapt to different uses without becoming a different product. | A kit of parts and repeatable structural relationships provide order; this is a functional-system reference, not a typography specimen. | Reuse an image frame, caption, button and navigation pattern; allow different chapter assemblies. Add only interactions that answer a visitor task. | Do not reproduce Braun-style controls or industrial styling. Avoid hiding essential actions merely to appear minimal. |
| 11 — Don Norman, **The Design of Everyday Things**, revised edition, 2013 | [Author's book page and detailed contents](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/). | Close the gap between what someone intends and what they can understand or do. | The author explicitly identifies signifiers, mapping, feedback, constraints, conceptual models and recovery. This is an interaction reference, not a visual treatment. | Show source title, chapter and position; use visible Previous/Next/Close controls; explain which crop is active; return focus to the originating image. | Do not rely on a custom cursor, an unexplained icon, hover or gesture alone. A state change should be apparent without animation. |
| 12 — Susan Kare, **Happy Macintosh and original Macintosh icon language** | [Kare's own site](https://kareprints.com/), including named Happy Macintosh prints and her explanation of pixel-grid icons. | Make an abstract computer operation approachable and memorable. | Small, economical visual signs work because their meaning is clear, not because they contain detail. | Simple original grid, expand and arrow marks paired with visible words. Keep the same icon/label relationship in every chapter. | Do not reproduce Kare's icons. Icons cannot replace labels where the meaning is ambiguous; decorative strokes should be hidden from assistive technology. |

## Exhibition, archive and publication references

### 13 — Arc / RemyShoots

[Original studio case study](https://www.arcmarumo.com/work/remyshoots). Evidence: studio text, not a hands-on test of the live site.

- **Problem and idea:** make photographic work easy to see while preserving a strong existing identity.
- **Type and composition:** the studio describes prominent red/type, spacious image presentation and edge-to-edge project stills.
- **Interaction/navigation:** three browsing presentations—slider, grid and list—are described, with optional sound, a lens effect and camera gestures.
- **Translate:** explicit overview-to-focused-view choice and a clear next project. **Avoid:** lens distortion, sound entry choices and camera access; they add cost without explaining PLAIN SIGHT's crops. Accessibility must not depend on those optional mechanisms.

### 14 — Studio375 / Richard Prescott

[Original studio case study](https://375.studio/en/projects/richard-prescott). Evidence: studio text and named media; no WebGL performance audit.

- **Problem and idea:** make a photographer's own work the dominant experience.
- **Type and composition:** the case describes a simple, consistent visual language and image-centred structure; exact typefaces are not established by the retrieved text.
- **Interaction/navigation:** animations and fluid WebGL movement are reported; navigation behavior was not independently tested.
- **Translate:** controlled image scale and a restrained frame around the photograph. **Avoid:** adding WebGL to a five-source archive. Native images, semantic controls and reduced-motion support are more proportionate.

### 15 — Aitchd Studio / Memento

[Original studio case study](https://aitchd.studio/work/memento). Evidence: studio account of a self-initiated gallery.

- **Problem and idea:** make a photographic journal feel curated rather than an undifferentiated feed.
- **Type and composition:** the studio describes asymmetry, full-bleed images and deliberate whitespace; typography specifics remain unverified.
- **Interaction/navigation:** sequential scrolling, reveals and subtle parallax are described.
- **Translate:** distinct pacing within each chapter, with a direct index route available at all times. **Avoid:** mandatory reveals or a long sequence hiding navigation. Content should already be visible when animation is disabled or fails.

### 16 — Rijksmuseum / Collection Online comparator

[Museum's explanation](https://www.rijksmuseum.nl/en/about-collection-online). Evidence: first-party feature description.

- **Problem and idea:** connect artworks, details and interpretation while supporting deliberate comparison.
- **Type and composition:** image-plus-context relationships; precise visual styling was not audited.
- **Interaction/navigation:** the museum describes side-by-side comparison, zoom, theme discovery and personal collections.
- **Translate:** put a source and its actual crop side by side with an explicit shared identifier. **Avoid:** accounts, personal collections, automatic videos or AI suggestions for a small set of studies. Provide a stacked mobile comparison and text explanation.

### 17 — International Center of Photography / Magnum Contact Sheets

[Exhibition description](https://www.icp.org/exhibitions/magnum-contact-sheets). Evidence: curator/institution text and labelled image records.

- **Problem and idea:** reveal photographic editing decisions that the final selected image normally conceals.
- **Type and composition:** sequential sheets establish the relationship between candidates; selected images gain meaning from surrounding material.
- **Interaction/navigation:** a physical exhibition/publication, not a tested web viewer.
- **Translate:** show each original generated composition once, then its derivative crops as subordinate variants. **Avoid:** faux frame numbers, nonexistent film negatives, invented shoot notes or pretending crops are additional exposures. Explain the origin in plain language.

### 18 — Mirador image viewer

[Project documentation](https://projectmirador.org/). Evidence: primary feature documentation, not an accessibility certification.

- **Problem and idea:** inspect and compare related image resources without losing metadata.
- **Type and composition:** content windows with contextual information; type styling is not the transferable feature.
- **Interaction/navigation:** comparison, zoom/pan, book/gallery/scroll views, contents and annotations are documented.
- **Translate:** a bounded light table with one selected source and one selected derivative, plus visible reset/return controls. **Avoid:** multiple floating windows and an extensible research workstation for a very small collection. Do not add the framework merely to copy its feature list.

### 19 — IIIF Presentation API 3

[Official specification](https://iiif.io/api/presentation/3.0/). Evidence: technical primary source.

- **Problem and idea:** separate an object's identity from its pages/views and annotations.
- **Type and composition:** not a visual specimen; the useful structure is collection → object → view with human-readable labels and ordered ranges.
- **Interaction/navigation:** sequential and hierarchical navigation can share the same structured content.
- **Translate:** use one small local manifest for source images, derivatives, chapter membership and publication-page relationships. **Avoid:** claiming IIIF compliance without implementing it, or adding a service when local JSON is sufficient. Labels and notes must remain human-readable.

### 20 — Google Arts & Culture / Art Camera

[Project overview](https://artsandculture.google.com/project/art-camera). Evidence: first-party overview and named “closer look” experiences.

- **Problem and idea:** help viewers notice details they would otherwise miss.
- **Type and composition:** the page pairs artwork discovery with explanatory detail entries; exact viewer styling not audited.
- **Interaction/navigation:** selectable close-looking stories and zoomable artworks are described/listed.
- **Translate:** authored crop notes with a simple source/selection relationship. **Avoid:** unsupported gigapixel claims, automatic tours or arbitrary zoom beyond available resolution. Every highlighted feature needs a meaningful written description.

### 21 — NYPL Digital Collections data model

[Official archival API documentation](https://api.repo.nypl.org/). Evidence: legacy documentation read; **the page states the API was discontinued from 1 August 2026**. The live collections About page returned 403.

- **Problem and idea:** keep collection, item, capture and rights information distinct.
- **Type and composition:** a metadata model, not a visual reference.
- **Interaction/navigation:** the documentation distinguishes records from captures and image links; no current live API behavior is claimed.
- **Translate:** maintain a source/derivative/provenance manifest in the repository. **Avoid:** connecting to this discontinued API, importing unrelated archival images or inventing rights metadata. Provenance should be accessible without inspecting code.

### 22 — Internet Archive / BookReader

[Official reading and thumbnail guidance](https://archivesupport.zendesk.com/hc/en-us/articles/360016638171-Books-and-Texts-Tips-Troubleshooting); [developer documentation](https://openlibrary.org/dev/docs/bookreader) was indexed but timed out on direct retrieval.

- **Problem and idea:** let a reader orient across a whole book and then inspect one page.
- **Type and composition:** actual page images are the artifact, while separate reader controls remain ordinary interface text.
- **Interaction/navigation:** thumbnail overview and access to original files are documented; indexed developer material describes single-page and two-page modes.
- **Translate:** actual 24-page previews, page count, chapter jumps, a readable focused page and a PDF download. **Avoid:** page-curl effects, text trapped only in low-resolution previews or downloading every full-size page at initial load.

## Implementation references that constrain the design

These references have no visual style to imitate. Their purpose is to make the chosen art direction usable. In each case typography must remain readable, images must not obscure the controls, and navigation must be operable with standard input devices.

| # / source | Problem and pattern | PLAIN SIGHT application | Exclude / verification consequence |
| --- | --- | --- | --- |
| 23 — [W3C ARIA APG: modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | A focused overlay must establish a clear keyboard boundary and a way out. The guide describes moving focus inside and retaining the tab sequence there. | Prefer native dialog semantics for focused image inspection; visible close, Escape and restoration to the trigger. Caption and position belong inside the dialog. | No overlay built only from a styled div. Verify keyboard entry, traversal, exit and return; use native semantics only where supported and tested. |
| 24 — [W3C carousel tutorial](https://www.w3.org/WAI/tutorials/carousels/) | A sequence needs structure, controls and perceivable changes; automatic movement requires user control. | Manual Previous/Next, clear “image x of y” text and a concise status announcement. No autoplay means no unnecessary play/pause UI. | No swipe-only navigation or repeated disruptive announcements. Test boundaries and state changes with the keyboard. |
| 25 — [W3C images tutorial](https://www.w3.org/WAI/tutorials/images/) | Alternative text depends on the image's information and function. | Describe a source's meaningful subject and spatial relationships; describe a crop's new emphasis. Use empty alt only for a true duplicate/decorative image whose information is already available. | No keyword-stuffed or generic “editorial photograph” text. A button's accessible name must communicate its action as well as identify the image. |
| 26 — [W3C WCAG 2.2: understanding reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Enlarged content should remain usable without two-dimensional page scrolling. The AA criterion uses the equivalent of 320 CSS pixels for vertical content. | Stack comparison panels, wrap labels, allow text to grow and keep controls inside the viewport. | Do not hide content to pass an overflow check. Responsive iframe checks are useful evidence but do not replace real browser zoom or assistive-technology testing. |
| 27 — [MDN: working with the History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API) | Dynamic content can break expected Back/Forward behavior unless URL state and rendering are coordinated. | Deep-link selected image/page and restore it on Back/Forward; handle initial and invalid state explicitly. Use normal links for ordinary page navigation. | Do not create a large client-side router or a history entry for every guide toggle. Verify reload, invalid ID, Back and Forward with actual browser actions. |
| 28 — [web.dev: optimize Cumulative Layout Shift](https://web.dev/articles/optimize-cls) | Images without reserved dimensions, fonts and inserted content can move the page after it appears. | Supply correct image dimensions/aspect ratios, reserve viewer space, and avoid blocking first content on animation. Size image variants for their displayed use. | Do not claim a Core Web Vitals score from source review. Measure a deployed visit separately; document lab/field distinctions. |

## Requested discovery sources and access limits

| Supplied source | Result on 27 October 2026 | Treatment |
| --- | --- | --- |
| [Le Vernis photography website board](https://it.pinterest.com/levernisblog/photography-website/) | 403 Forbidden | Not visually reviewed; not counted among evaluated references. |
| [Portfolio vibe reference board](https://id.pinterest.com/filling___thegaps/portfolio-vibe-reference/) | 403 Forbidden | Not visually reviewed; no inferred moodboard or attribution. |
| [Pin 323414817006575279](https://in.pinterest.com/pin/323414817006575279/) | 403 Forbidden | Not used as evidence. |
| [Supplied portfolio pin](https://in.pinterest.com/pin/portfolio–643311128052831884/) | URL inaccessible; supplied slug includes an en dash | The URL was attempted as supplied. No unseen image description is claimed. |
| [Supplied type-swiss / sophiemeret pin](https://jp.pinterest.com/pin/type-swiss-on-instagram-editorial-design-by-sophiemeret-type-editorial-grid-graphicdesign-swissdesign–608760074626623142/) | URL inaccessible; supplied slug includes an en dash | No work attributed to a creator without retrieving the pin or original source. |
| [Awwwards](https://www.awwwards.com/) | Direct page timed out | Used only as a discovery target. The three supplied studios' own accounts were read instead; awards were not used to score PLAIN SIGHT. |
| [Behance](https://www.behance.net/) | 403 Forbidden | A search-indexed “Lens — Editorial Photography Website UI/UX Design” concept was found, but its full project also returned 403. It was not treated as a visually inspected or functioning product. |

The ledger meets the numeric range through verifiable design records and product/technical sources. It is **not** a 28-site visual teardown or a Pinterest moodboard. A later visual reference board could use licensed thumbnails or links after direct access, but no such board is claimed here.

## Resolving the influences

1. **Boom versus Norman:** retain surprising sequencing inside the work, but retain chapter names, page numbers and an index. Surprise concerns what is seen, not how to escape.
2. **Scher/Brody versus image primacy:** expressive typography belongs to entry and chapter moments. Caption and control typography stays calm; no text covers important photographic detail.
3. **Crouwel/Greiman versus Rams:** use the medium to reveal source/crop relationships, then stop. A small, real comparison is more defensible than a technically elaborate effect.
4. **Memento versus the archive:** a curated sequence is an invitation, while the index is an equally clear route. Neither forces the other task.
5. **Magnum versus generated imagery:** take the idea of inspectable editing, but make the material's actual origin explicit. No simulated documentary production history.
6. **Mirador/Rijksmuseum versus collection size:** use their separation of image and context. Reject the full workstation, account and curation feature set for this collection.

## Research-to-product checks

- Can someone enter any of the three studies without learning a new navigation system?
- Does one original image keep the same identity when it appears as a crop or a publication page?
- Can a reviewer see the image first and request interpretation second?
- Is the comparison understandable with no dragging, hover, animation or color discrimination?
- Does a publication thumbnail correspond to an actual PDF page rather than an unrelated mockup?
- Are original/generated images, derivative crops and new editorial notes labelled distinctly?
- Does the source contain one coherent styling system rather than another override layer?
- Does the browser's Back button behave as a visitor expects?

These checks guide implementation; the separate QA record should say which were actually verified and which remain open.
