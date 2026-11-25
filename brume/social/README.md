# BRUME campaign artwork

Open [the campaign gallery](../campaign.html) to see the artwork, design notes and individual downloads. Every SVG contains live type, embedded concept photography and the open-font licenses for Barlow Condensed and DM Sans. For desktop editors that require local fonts, install those families before editing text.

| Artwork | Canvas | Purpose |
| --- | --- | --- |
| `01-launch.svg` | 1080 × 1350 | Introduce the campaign line and the ribbed lamp. |
| `03-cream.svg`, `04-amber.svg`, `02-maroon.svg` | 1080 × 1350 | Introduce Ivory in morning light, Amber in late afternoon and Plum in the evening. The original filenames remain usable. |
| `05-collection.svg` | 1080 × 1350 | Pair each finish with its product identifier. |
| `carousel-01.svg` through `carousel-06.svg` | 1080 × 1350 | Follow the room, silhouette, rib, off/on comparison, finish family and returning shadow. |
| `story-01.svg` through `story-03.svg` | 1080 × 1920 | Present an edition, compare finishes, then introduce the collection experience. |
| `landscape-01.svg` | 1200 × 627 | Introduce the collection in a wide placement. |
| `light-study.svg` | 1080 × 1350 | Compare the lamp at architectural, object and hand scale. |

## Artwork rules

The window-light portrait uses an open mineral field. Amber pairs a product view with a crop of the hand. Plum extends the evening photograph to one edge of the wine field. The register takes its rhythm from the ribbed foot. Each finish moves the displaced section to a different height.

The story layouts reserve the first and last 240 pixels for platform controls and place essential type inside the central area. The artwork is a self-initiated campaign study. Platform-specific previews and paid placement testing would be needed for a live campaign.

## Rebuilding

Run `python brume/social/build.py` from the repository root with Pillow installed. It crops the photographs from `brume/images/plates/` and `brume/images/register/`, then embeds them in each SVG. No build step is needed to browse the site. The three web pages involved in the campaign are the [case study](../index.html), [campaign gallery](../campaign.html) and [customer collection](../collection.html).
