# BRUME studio letters

Open `index.html` to read each subject line, preheader and message. The proof viewer displays the same underlying HTML at up to 360 CSS pixels on mobile and 640 CSS pixels on desktop. Small screens keep the mobile text at its intended size. The desktop overview scales down to the available area. Its images-off control substitutes each photograph’s description and hides the decorative identity mark. All three HTML and plain-text files also open directly.

| Letter | Reader’s decision | Photograph | Destination |
| --- | --- | --- | --- |
| `01-introduction` | Follow the launch into the room | Plum at a window after dusk | Plum under evening illumination |
| `02-material` | Look at the ribbed foot and the smooth dome | Macro of the Amber ribs | Collection materials section |
| `03-detail` | Choose a finish by time of day | Three glass editions in one frame | Each finish and the comparison section |

## Source and delivery

The HTML files are the editable masters. They use presentation tables, system type, inline styles, a conditional 600-pixel wrapper for Microsoft Office rendering and hosted JPEG photographs. Essential content and links remain live. The plain-text files carry the same message and destinations. The HTML links are relative for branch reviews and local previews. Plain-text links point to the portfolio’s canonical GitHub Pages address.

The `sources` directory contains three unsent multipart `.eml` files. Each combines `text/plain` and `text/html` with a subject line and uses absolute HTTPS links for images, documents and calls to action on GitHub Pages. Merging the matching site version makes those URLs resolve to the corresponding artwork and collection pages. Rebuild these files after editing the HTML or TXT masters with `python3 brume/email/build_delivery.py` from the repository root.

Chrome browser checks covered 360- and 640-pixel proofs, keyboard operation, the images-off alternative, Back navigation and links into the matching material and finish views. Inbox-client rendering, dark-mode behavior and delivery remain untested. The campaign is a proposed sequence for a fictional studio.
