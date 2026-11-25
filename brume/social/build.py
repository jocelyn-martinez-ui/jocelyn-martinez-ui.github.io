"""Rebuild the editable BRUME campaign sheets. Run with Python 3 and Pillow."""

import base64
from functools import lru_cache
from html import escape
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFont, ImageOps


HERE = Path(__file__).resolve().parent
FONT_DIR = HERE.parents[1] / "assets" / "fonts"
IMAGES = HERE.parent / "images"
PAPER = "#f4f2e9"
INK = "#202521"
LEAF = "#dce58e"
WINE = "#501f36"
CLAY = "#e2aa77"
MID = "#a8a9a1"

# Use the same local, licensed type as the case. Embedding the font makes each
# download portable. The live text remains individually selectable in an editor.
FONTS = (
    ("BRUME Art Display", "600", "808d8d26b49135ab.woff2", "barlowcondensed-OFL.txt"),
    ("BRUME Art Sans", "400 800", "713ca32c3c8b2ada.woff2", "dmsans-OFL.txt"),
)


def encode(data):
    return base64.b64encode(data).decode("ascii")


@lru_cache(maxsize=1)
def embedded_type():
    styles, licenses = [], []
    for family, weight, filename, license_file in FONTS:
        data = encode((FONT_DIR / filename).read_bytes())
        styles.append(f"@font-face{{font-family:'{family}';font-style:normal;"
                      f"font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
        license_text = (FONT_DIR / license_file).read_text(encoding="utf-8")
        licenses.append("\n".join(line.rstrip() for line in license_text.split("\n")))
    styles += [".display{font-family:'BRUME Art Display','Barlow Condensed SemiBold','Barlow Condensed','Arial Narrow','Liberation Sans Narrow',sans-serif;font-weight:600}",
               ".label{font-family:'BRUME Art Sans','DM Sans 9pt','DM Sans',Arial,sans-serif;font-weight:500}"]
    return "".join(styles), "\n\n".join(licenses)


@lru_cache(maxsize=90)
def type_metric(style, size):
    filename = FONTS[0 if style == "display" else 1][2]
    return ImageFont.truetype(str(FONT_DIR / filename), size)


@lru_cache(maxsize=64)
def photo_crop(source, width, height, center):
    directory = "register" if source.startswith("register/") else "plates"
    file = IMAGES / directory / (source.rsplit("/", 1)[-1] + ".webp")
    with Image.open(file) as image:
        factor = min(1, 1050 / max(width, height))
        size = (max(1, round(width * factor)), max(1, round(height * factor)))
        crop = ImageOps.fit(image.convert("RGB"), size, Image.Resampling.LANCZOS, centering=center)
    data = BytesIO()
    crop.save(data, "JPEG", quality=83, optimize=True, progressive=True, subsampling=0)
    return encode(data.getvalue())


class Sheet:
    def __init__(self, name, title, alternative, color=PAPER, width=1080, height=1350):
        self.name = name
        self.width, self.height = width, height
        self.title, self.alternative = title, alternative
        self.layers = []
        self.rect(0, 0, width, height, color)

    def rect(self, x, y, width, height, color):
        self.layers.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}"/>')

    def rule(self, x1, y1, x2, y2, color=INK, width=2):
        self.layers.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    def text(self, x, y, value, size, color=INK, style="label", anchor="start", tracking=None):
        if tracking is None:
            tracking = -size * .018 if style == "display" else -size * .022
        length = type_metric(style,size).getlength(value) + tracking * max(0,len(value)-1)
        self.layers.append(f'<text class="{style}" x="{x}" y="{y}" font-size="{size}" fill="{color}" '
                           f'textLength="{length:.2f}" lengthAdjust="spacingAndGlyphs" '
                           f'letter-spacing="{tracking:.2f}" text-anchor="{anchor}">{escape(value)}</text>')

    def display(self, x, y, value, size, color=INK, **options):
        self.text(x, y, value, size, color, "display", **options)

    def mark(self, x, y, w, h, color=INK, band=.43, lines=17):
        # A fluted edge in three segments: a displaced central band creates the register.
        top, bottom = y+h*band, y+h*min(.88,band+.16)
        offset = min(w*.078, h*.20)
        span = w-offset-1
        paths = []
        for i in range(lines):
            t=i/(lines-1)
            rib=x+.5+span*(.29*t+.71*t**1.47)
            inset=h*.23*abs(2*t-1)**2.4
            paths.append(f'M{rib:.2f},{y+inset:.2f}V{top:.2f}M{rib+offset:.2f},{top:.2f}V{bottom:.2f}M{rib:.2f},{bottom:.2f}V{y+h-inset:.2f}')
        self.layers.append(f'<path d="{" ".join(paths)}" fill="none" stroke="{color}" stroke-width="{min(4,max(2.15,span/lines*.21)):.2f}"/>')

    def photo(self, name, x, y, w, h, center=(.5,.5)):
        data = photo_crop(name, w, h, center)
        self.layers.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" '
                           f'preserveAspectRatio="xMidYMid meet" xlink:href="data:image/jpeg;base64,{data}"/>')

    def save(self):
        styles, licenses = embedded_type()
        preamble = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
                    f'width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" '
                    f'role="img" aria-labelledby="sheet-title sheet-description">\n'
                    f'<title id="sheet-title">BRUME — {escape(self.title)}</title>\n'
                    f'<desc id="sheet-description">{escape(self.alternative)}</desc>\n'
                    f'<metadata>BRUME fictional lighting collection. AI-generated concept photography.\n{escape(licenses)}</metadata>\n'
                    f'<defs><style>{styles}</style></defs>')
        (HERE / f'{self.name}.svg').write_text(preamble+'\n'+'\n'.join(self.layers)+'\n</svg>\n',encoding="utf-8")


def mast(s, color=INK, x=55, y=85):
    s.display(x, y, "BRUME", 65, color, tracking=-1.9)


def frame_label(s, frame, title, color=INK):
    s.rule(56, 1233, 1024, 1233, color)
    s.text(56, 1300, f"BRUME  /  {title}", 36, color)
    s.text(1024, 1300, f"{frame}  /  6", 36, color, anchor="end")


def launch():
    s=Sheet("01-launch", "Where the light lands", "Plum glass in a shaft of light above a wine-red field. The headline reads Where the light lands.", WINE)
    s.photo("hero",0,0,1080,766,(.61,.48))
    s.rect(0,0,284,119,PAPER); mast(s)
    s.display(55,951,"Where the",165,LEAF)
    s.display(55,1113,"light lands.",165,LEAF)
    s.rule(57,1185,1022,1185,PAPER)
    s.text(56,1264,"Glass table light",43,PAPER)
    s.mark(849,1221,171,63,LEAF,.57,23)
    s.save()


def finishes():
    s=Sheet("03-cream", "Ivory / Window light", "Ivory in morning light. A large Window light headline sits above a separate product photograph and an opal-glass caption.")
    mast(s); s.text(1025,80,"BR–02  /  Ivory",40,anchor="end")
    s.rule(55,121,1025,121)
    s.display(52,302,"Window light.",159)
    s.photo("morning",0,369,1080,752,(.51,.49))
    s.mark(57,1175,148,79,INK,.25,20)
    s.text(1018,1208,"Morning on opal glass.",43,anchor="end")
    s.text(1018,1265,"The first register",34,anchor="end")
    s.save()

    s=Sheet("04-amber", "Amber / Long light", "A narrow afternoon view and a wider crop of amber glass share a warm field under the words Long light.", CLAY)
    mast(s); s.text(1024,83,"BR–03  /  Amber",40,anchor="end")
    s.photo("register/amber-afternoon",57,189,681,658,(.49,.53))
    s.photo("hand",762,347,318,500,(.52,.47))
    s.display(50,1055,"Long light.",177)
    s.rule(55,1110,1024,1110)
    s.text(56,1184,"Late afternoon",42)
    s.text(56,1248,"Through amber glass",38)
    s.mark(853,1167,169,83,INK,.43,24)
    s.save()

    s=Sheet("02-maroon", "Plum / A light left on", "Plum glass in an evening interior. A thin strip of flutes follows the lower edge of the photograph; below it large type reads A light left on.", WINE)
    mast(s,PAPER); s.text(1024,82,"BR–01  /  Plum",40,PAPER,anchor="end")
    s.photo("evening",111,176,969,740,(.56,.49))
    s.mark(52,680,108,212,LEAF,.65,15)
    s.display(50,1110,"A light left on.",147,PAPER)
    s.rule(56,1170,1023,1170,PAPER)
    s.text(55,1255,"Evening in smoked plum glass.",39,PAPER)
    s.save()


def family():
    s=Sheet("05-collection", "The finish index", "Ivory, Amber and Plum appear in three consecutive photographic bands with a label and product ID beside each.", INK)
    mast(s,PAPER); s.text(1025,82,"Collection index",40,PAPER,anchor="end")
    s.display(53,241,"The finish index",136,PAPER)
    for y,source,name,sku,tone in [(316,"ivory-morning","Ivory","BR–02",PAPER),(631,"amber-afternoon","Amber","BR–03",CLAY),(946,"plum-evening","Plum","BR–01",LEAF)]:
        s.rule(56,y-12,1024,y-12,tone)
        s.photo("register/"+source,56,y+16,366,267,(.5,.49))
        s.text(488,y+84,sku,40,tone)
        s.display(482,y+211,name,114,tone)
    s.save()


def carousel():
    s=Sheet("carousel-01", "1 / Start with the room", "An architectural wide view sets the distance. The first headline asks the reader to start with the room.")
    s.display(51,188,"Start with",151)
    s.display(51,331,"the room.",151)
    s.mark(818,135,203,151,INK,.42,28)
    s.photo("architecture",0,408,1080,755,(.54,.52))
    frame_label(s,"1","Room study"); s.save()

    s=Sheet("carousel-02", "2 / Read the outline", "A side profile shows the dome, the short metal collar and the fluted foot. A vertical list names each part.", CLAY)
    s.display(53,184,"Read the outline.",127)
    s.photo("profile",56,266,644,848,(.50,.53))
    for y,n,label in [(419,"01","Dome"),(692,"02","Collar"),(966,"03","Foot")]:
        s.rule(743,y-45,1024,y-45)
        s.text(745,y,n,34); s.display(740,y+86,label,81)
    frame_label(s,"2","Silhouette"); s.save()

    s=Sheet("carousel-03", "3 / Follow a rib", "Extreme close-up of the ribbed glass. A displaced-line register is drawn underneath the photograph.", LEAF)
    s.photo("macro",0,0,1080,716,(.54,.5))
    s.display(54,904,"Follow a rib.",151)
    s.mark(60,988,417,151,INK,.48,42)
    s.text(541,1040,"One ridge catches",41)
    s.text(541,1095,"a line of light.",41)
    frame_label(s,"3","Surface"); s.save()

    s=Sheet("carousel-04", "4 / Switch the light", "Two matched views of the same object show the lamp off and on. The photo labels identify both states.", INK)
    s.display(54,191,"Switch the light.",133,PAPER)
    s.photo("unlit",56,310,473,619,(.15,.52))
    s.photo("lit",551,310,473,619,(.15,.52))
    s.text(56,1005,"Lamp off",46,PAPER)
    s.text(551,1005,"Lamp on",46,LEAF)
    s.text(56,1156,"Same viewpoint. Same finish.",39,PAPER)
    frame_label(s,"4","Light states",PAPER); s.save()

    s=Sheet("carousel-05", "5 / Three ways to hold it", "The complete collection is pictured together beneath a title. Beneath the photograph an edition key lists the three finishes.")
    s.text(56,88,"The collection",42)
    s.display(51,270,"Three ways to hold it.",117)
    s.photo("collection",0,344,1080,668,(.5,.50))
    for x,name,tone in [(56,"Ivory",INK),(389,"Amber","#864622"),(726,"Plum",WINE)]:
        s.rect(x,1081,27,27,tone);s.text(x+45,1108,name,43)
    frame_label(s,"5","Finishes"); s.save()

    s=Sheet("carousel-06", "6 / Return to the room", "A shadow photograph and a large Return to the room headline close the sequence. The invitation is Compare the finishes.", WINE)
    s.mark(61,65,264,92,LEAF,.65,28)
    s.display(51,371,"Return to",179,PAPER)
    s.display(51,534,"the room.",179,PAPER)
    s.photo("shadow",289,629,791,414,(.53,.52))
    s.text(56,1161,"Compare the finishes",50,LEAF)
    frame_label(s,"6","Light register",PAPER); s.save()


def stories():
    s=Sheet("story-01", "Ivory story / First light", "An Ivory morning interior sits between the bright First light headline and a caption about opal glass.", PAPER,height=1920)
    mast(s,x=74,y=302);s.text(997,302,"BR–02  /  Ivory",39,anchor="end")
    s.display(69,532,"First light.",175)
    s.photo("morning",0,622,1080,699,(.50,.54))
    s.mark(77,1411,149,116,INK,.26,23)
    s.text(284,1464,"Window light",52);s.text(284,1531,"on opal glass.",52)
    s.save()

    s=Sheet("story-02", "The three-register story", "A vertical index pairs morning with Ivory, afternoon with Amber and evening with Plum.", INK,height=1920)
    mast(s,PAPER,x=74,y=302);s.text(1002,302,"Finish index",41,PAPER,anchor="end")
    s.display(71,522,"Across a day.",150,PAPER)
    for y,source,name,time,tone in [(626,"ivory-morning","Ivory","Morning",PAPER),(931,"amber-afternoon","Amber","Afternoon",CLAY),(1236,"plum-evening","Plum","Evening",LEAF)]:
        s.rule(74,y-14,1009,y-14,tone)
        s.photo("register/"+source,74,y+14,338,242,(.50,.50));s.text(474,y+83,time,37,tone);s.display(468,y+199,name,101,tone)
    s.save()

    s=Sheet("story-03", "Plum story / After the window darkens", "An intimate crop of the evening lamp is followed by an invitation to see Plum under three kinds of light.", WINE,height=1920)
    s.photo("evening",0,0,1080,800,(.55,.50))
    s.rect(72,248,248,92,PAPER);s.display(93,313,"BRUME",59)
    s.display(74,1022,"After the",173,PAPER);s.display(74,1178,"window darkens.",124,PAPER)
    s.rule(75,1300,1004,1300,LEAF)
    s.text(75,1408,"See Plum in three lights",51,LEAF)
    s.mark(78,1488,182,90,LEAF,.68,21)
    s.save()


def landscape():
    s=Sheet("landscape-01", "Where the light lands / landscape", "The campaign line in large pale type on wine sits beside the plum lamp. Three rib segments sit underneath the title.", WINE,width=1200,height=627)
    s.photo("hero",550,0,650,627,(.65,.50))
    s.display(42,88,"BRUME",70,PAPER)
    s.display(39,272,"Where the",107,LEAF);s.display(39,377,"light lands.",107,LEAF)
    s.mark(45,443,217,77,LEAF,.51,25)
    s.text(45,582,"Glass table light",34,PAPER)
    s.save()


def distance_study():
    s=Sheet("light-study", "Room / Object / Touch", "An architectural view, a close side profile and a hand beside the glass move from the scale of a room to the scale of a fingertip.", INK)
    mast(s,PAPER);s.text(1025,82,"Three distances",39,PAPER,anchor="end")
    s.photo("architecture",56,143,969,363,(.50,.50));s.text(56,572,"Room",46,PAPER)
    s.photo("profile",56,640,460,351,(.52,.50));s.photo("hand",541,640,484,351,(.52,.50))
    s.text(56,1055,"Object",46,PAPER);s.text(541,1055,"Touch",46,PAPER)
    s.rule(56,1132,1025,1132,LEAF);s.display(52,1260,"A change in scale.",115,LEAF)
    s.save()


if __name__ == "__main__":
    launch()
    finishes()
    family()
    carousel()
    stories()
    landscape()
    distance_study()
