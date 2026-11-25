# BRUME · Where the light lands.

A self-initiated, AI-assisted design study for Jocelyn Martinez’s portfolio. The fictional studio has one ribbed glass table lamp in Ivory, Amber and Plum. The campaign gives each finish a distinctive environment. The collection lets visitors hold the environment constant as they compare finishes.

## Open the work

| Page | What to inspect |
| --- | --- |
| [Case study](index.html#ivory) | Brief, intended audience, contribution, photography, identity, UX, channels and reflection |
| [Customer collection](collection.html?light=evening#plum) | Nine independently selectable finish and time combinations, same-light comparison, material details and a script-free photographic register |
| [Photographic contact sheet](photography.html) | Sixteen full-size editorial images, including material and hand details and a matched off/on pair |
| [Design notes](research.html#before) | The earlier Ivory beside the reconstruction, three mark studies, local type, color and layout rules |
| [Campaign gallery](campaign.html) | Sixteen editable SVGs, including the complete six-frame carousel |
| [Print and packaging](production.html) | Eleven editable SVGs, the carton net, a two-sided brochure, original label revisions and three photographic placements |
| [Email proofs](email/index.html) | Three HTML letters and plain-text counterparts, images-off proofing and downloadable multipart email sources |
| [Website on screen](screens.html) | The real collection at phone and desktop viewport sizes, retaining the selected finish and hour |

## Maintaining the project

The HTML, CSS, JavaScript, fonts and images are served directly by GitHub Pages. Run a static server from the portfolio root to include the existing site font paths. Edition entry points on the case include `#ivory`, `#amber` and `#plum`. Customer links add a light condition, such as `collection.html?light=afternoon#amber`.

The editable campaign, print and email masters are present in the repository. To change a campaign layout or crop, edit its corresponding source and rebuild the artwork. The print generator, mockup compositor and email exporter have separate inputs. Their dependencies are needed only for authoring.

- [Campaign source and dimensions](social/README.md)
- [Print, carton and mockup specifications](print/PRINT_SPECS.md)
- [Email sources and browser proofing](email/README.md)
- [Design tokens](identity/tokens.css) and [vector register](identity/register.svg)
- [Review, verification and production limits](QA_REPORT.md)

Run the targeted state checks from the repository root with `node --test brume/tests/collection.test.mjs`. The original four JPEG, social, email and print filenames continue to serve their current versions for other portfolio pages.

The product and mockup environments are AI-generated visual studies. The downloadable artwork keeps names, headlines and codes as editable typography. The intended audience and use case are design assumptions. Physical samples, live marketing results and commissioned client work are outside this project.
