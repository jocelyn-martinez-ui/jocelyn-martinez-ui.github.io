# BRUME print and packaging sources

Jocelyn Martinez’s self-initiated lighting identity uses a mark derived from the lamp’s vertically ribbed foot. A horizontal displacement crosses the mark high on Ivory, centrally on Amber and low on Plum. Moving the band identifies the time of day associated with the edition. It indicates a design choice, without expressing a photometric measurement.

## Trim and bleed

Dimensions are in millimetres. Each consumer-facing SVG includes three millimetres beyond the trim on all four sides. Its viewBox places the trim origin at 0,0. Each file contains live editable type. Photographic crops and the display face are embedded so each file can be opened independently.

| Artwork | Intended trim | SVG extent |
| --- | --- | --- |
| Gallery poster | 700 × 1050 | 706 × 1056 |
| Brochure, inside and outside | 297 × 210 | 303 × 216 |
| Edition label | 100 × 150 | 106 × 156 |
| Magazine ad | 148 × 210 | 154 × 216 |
| Postcard front | 148 × 105 | 154 × 111 |
| Product card | 105 × 148 | 111 × 154 |
| Finish sheet | 210 × 297 | 216 × 303 |

The A4 brochure folds at 148.5 mm into A5-format leaves. The outside spread puts the back cover at left and front at right. The inside spread places the detail and silhouette on facing pages. Foreground type is set away from the fold. Both spreads have one outer perimeter of bleed and an uninterrupted central fold.

The poster photograph is cropped for a large reading distance. The scene mockups and RGB embedded photographs were prepared for screen review. A full-size poster proof would establish an appropriate image resolution and viewing distance. The artwork uses an RGB palette and has no printer-assigned output intent. Uncoated, lightly textured paper is the proposed finish. Samples should establish ink coverage, colour, legible small type and fold performance on a chosen stock.

## Folding carton and edition labels

The reverse-tuck concept proposes an outer carton of 240 × 240 × 300 mm. The one-piece outer net occupies an envelope of 980 × 824 mm. Its explanatory drawing page is 1040 × 972 mm with a separate key. Inspect the SVG at full size to read the 20 mm side-seam glue flap, four equal 240 mm face widths, 300 mm body height, opposing 240 mm major flaps and 22 mm tucks. Dust flaps appear on both side panels at each end.

Cut is solid, fold is dashed and glue is hatched. Diagram marks and notes on the explanatory drawing belong on a non-printing technical layer in a production file. A centred applied label starts 70 mm from each vertical edge and 75 mm from the top and bottom of the front face. The proposed stock is an uncoated board with an opaque paper label.

| Edition | Identifier | Printed label |
| --- | --- | --- |
| Ivory | BR-02 | Pale mineral field, high register |
| Amber | BR-03 | Copper field, centre register |
| Plum | BR-01 | Wine field, low register |

Lamp dimensions, protective cushioning and drop resistance need engineering and physical samples. A real vendor would supply a substrate-calibrated CAD net and finish proofs. The collection is fictional. Electrical data, commercial release and manufacturing approval fall outside the scope of these design studies.

## Mockups and reconstruction

All three blank settings were generated for this project. The photographed poster frame, paper spread and carton contain no generated lettering. The actual trim artwork is rasterised and registered to each photographed surface. The two brochure pages follow separate strips into the crease. Surface shading carries through the printed artwork. Original blank plates are in [plates](plates/) and placed comparisons are in [mockups](mockups/).

- [Editable flat artwork](svg/) contains the current poster, brochure, carton diagram, seven label and collateral masters.
- [Earlier label versions](archive/) contains the two Plum drafts from the prior identity.
- [Build the editable SVGs](build_print.py) reads the site's bundled Barlow Condensed display font and new lamp photography. Run this script with Python and Pillow.
- [Rebuild photographic placements](build_mockups.py) reads the current flat artwork, trims the bleed and applies the actual composition. It requires Inkscape, Barlow Condensed ExtraBold installed for raster export, Pillow and NumPy.

The SVGs, placements and specifications are digital proofs. The public package includes the actual current source artwork.
