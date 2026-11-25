"""Build standalone, editable BRUME print SVGs. Requires Pillow and the existing site fonts."""
from __future__ import annotations

import base64
from functools import lru_cache
from html import escape
from io import BytesIO
import math
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "svg"
PHOTOS = ROOT.parent / "images" / "plates"
FONT = ROOT.parents[1] / "assets" / "fonts" / "488e956feb1421c4.woff2"
PAPER, INK, ACID, PLUM = "#f4f2e9", "#202521", "#dce58e", "#501f36"
MUTED, LINE = "#545c53", "#a6aba1"
DISPLAY = "Barlow Condensed ExtraBold,Arial Narrow,sans-serif"
SANS = "Arial,Liberation Sans,sans-serif"
MONO = "Courier New,Liberation Mono,monospace"
ED = {
    "ivory": ("Ivory", "BR-02", "Morning", "#e3e8d9", "#253528", "Opal glass", 0),
    "amber": ("Amber", "BR-03", "Afternoon", "#d8a56e", "#2e271c", "Honey glass", 1),
    "plum": ("Plum", "BR-01", "Evening", PLUM, PAPER, "Wine glass", 2),
}
FONT_SRC = base64.b64encode(FONT.read_bytes()).decode("ascii")
FONT_LICENSE = escape("\n".join(line.rstrip() for line in FONT.with_name("barlowcondensed-OFL.txt").read_text(encoding="utf-8").splitlines()))


def n(v):
    return f"{v:.3f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


def rect(x, y, w, h, fill):
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" fill="{fill}"/>'


def rule(x1, y1, x2, y2, color=INK, weight=.27, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="M{n(x1)} {n(y1)}L{n(x2)} {n(y2)}" fill="none" stroke="{color}" stroke-width="{n(weight)}"{d}/>'


def text(x, y, copy, size, fill=INK, face=SANS, *, weight=None, anchor="start", track=0):
    style = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{n(x)}" y="{n(y)}" fill="{fill}" font-family="{face}" '
            f'font-size="{n(size)}" text-anchor="{anchor}" letter-spacing="{n(track)}"{style}>'
            f'{escape(copy)}</text>')


def paras(x, y, lines, size, leading, color=INK):
    return "".join(text(x, y+i*leading, s, size, color) for i,s in enumerate(lines))


def reg(x, y, w, h, phase=1, color=INK):
    """A displaced band crosses the same elliptical density field as the studio mark."""
    paths = []
    count = 22
    band_top = y + h * (.27, .42, .56)[phase]
    band_bottom = band_top + h * .14
    for i in range(count):
        t = i/(count-1)
        u = .035 + .9*(.55*t + .45*t**1.5)
        radius = math.sqrt(max(0, 1-((u-.49)/.51)**2))
        start = y + h*(.5-.49*radius)
        end = y + h*(.5+.49*radius)
        px = x+w*u
        shift = w*.036
        line_width = w*(.008+.003*math.sin(math.pi*t)**2)
        for yy1,yy2,xx in ((start,min(end,band_top),px), (max(start,band_top),min(end,band_bottom),px+shift), (max(start,band_bottom),end,px)):
            if yy2 > yy1:
                paths.append(rule(xx,yy1,xx,yy2,color,line_width))
    return '<g aria-label="Light register">'+ "".join(paths)+"</g>"


@lru_cache(maxsize=None)
def cropped(name, w, h, px, focus=(.5,.5)):
    with Image.open(PHOTOS / (name+".webp")) as im:
        size=(px,max(1,round(px*h/w)))
        frame=ImageOps.fit(im.convert("RGB"),size,method=Image.Resampling.LANCZOS,centering=focus)
        buff=BytesIO()
        frame.save(buff,format="JPEG",quality=81,optimize=True,progressive=False)
    return base64.b64encode(buff.getvalue()).decode("ascii")


def photo(name,x,y,w,h,px=660,focus=(.5,.5)):
    data=cropped(name,w,h,px,focus)
    return (f'<image x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" '
            f'preserveAspectRatio="none" xlink:href="data:image/jpeg;base64,{data}"/>')


def save(stem, w, h, title, desc, art, bleed=3):
    sw, sh = w+2*bleed, h+2*bleed
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
         f'width="{n(sw)}mm" height="{n(sh)}mm" viewBox="{-bleed} {-bleed} {n(sw)} {n(sh)}" '
         'role="img" aria-labelledby="title desc">\n'
         f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>\n'
         f'<metadata>{FONT_LICENSE}</metadata>\n'
         f'<defs><style>@font-face{{font-family:"Barlow Condensed ExtraBold";src:url(data:font/woff2;base64,{FONT_SRC}) format("woff2");font-style:normal;font-weight:400;}}</style></defs>\n'
         + "".join(art)+"\n</svg>\n")
    (OUT/(stem+".svg")).write_text(svg,encoding="utf-8")


def label_art(key, page_bleed=3):
    name, id_, phase, bg, fg, finish, seq=ED[key]
    b=page_bleed
    return [
        rect(-b,-b,100+b*2,150+b*2,bg),
        text(7,16,"BRUME",13,fg,DISPLAY,track=-.2),
        text(93,11.5,id_,3.7,fg,MONO,anchor="end"),
        rule(7,21,93,21,fg,.42),
        text(7,28,"Table light",3.8,fg), text(93,28,"Edition label",3.45,fg,anchor="end"),
        reg(8,40,78,39,seq,fg),
        text(7,105,name,22,fg,DISPLAY,track=-.22),
        text(7,117,phase+" register",4.7,fg),
        rule(7,126,93,126,fg,.37),
        text(7,136,finish,3.9,fg),text(93,136,"Collection 01",3.5,fg,anchor="end"),
        text(7,143,"Ribbed foot / smooth dome",3.4,fg),
    ]


def editions():
    for key, (name, id_, *_) in ED.items():
        save("brume-label-"+key+"-r03",100,150,f"BRUME {name} edition label",
             f"{id_} box label. Trim 100 by 150 millimetres, with 3 millimetres of bleed on each side.",label_art(key))


def poster():
    art = [
        rect(-3,-3,706,1056,ACID),
        text(33,103,"BRUME",91,INK,DISPLAY,track=-1.7),
        text(664,57,"Light register",22,INK,anchor="end"),text(664,90,"BR-01 / PLUM",17,INK,MONO,anchor="end"),
        rule(35,124,665,124,INK,2),
        text(35,158,"A study in coloured glass",20),
        text(665,158,"Evening edition",19,INK,anchor="end"),
        photo("hero",-3,181,706,483,900,(.67,.55)),
        rect(-3,664,706,389,PLUM),
        text(32,791,"The room",125,PAPER,DISPLAY,track=-1.4),
        text(29,911,"after dark.",125,PAPER,DISPLAY,track=-1.7),
        reg(511,744,138,144,2,ACID),
        rule(35,956,665,956,PAPER,1.7),
        text(35,1004,"Ribbed glass",22,PAPER),text(665,1004,"Table light collection",22,PAPER,anchor="end"),
    ]
    save("campaign-poster",700,1050,"The room after dark. BRUME campaign poster",
         "Street poster for the Plum lamp. A green top register introduces a dark room photograph above the large evening headline.",art)


def brochure():
    a=[rect(-3,-3,303,216,PAPER),
       text(8,13,"BRUME",7,INK,DISPLAY),text(139,12,"Material notes / 01",3.3,INK,MONO,anchor="end"),
       rule(8,17,139,17),text(7.5,39,"Follow the rib.",20,INK,DISPLAY,track=-.15),
       photo("macro",-3,47,142,89,650,(.52,.51)),
       text(8,146,"01  /  The foot",3.4,INK,MONO),
       paras(8,159,["A bright line gathers on each ridge.","The adjacent groove falls into shade.","Moving sideways changes their spacing","in the eye."],4.2,6),
       text(8,201,"BRUME   /   Light register",3.45,MUTED),text(138.5,201,"02",3.5,INK,MONO,anchor="end"),
       rule(149,0,149,210,LINE,.2),
       text(157,13,"Surface / silhouette",3.55,INK,MONO),text(288,13,"03",3.5,INK,MONO,anchor="end"),rule(157,17,289,17),
       photo("profile",157,24,143,90,650,(.55,.52)),
       text(157,130,"Then the dome.",15.8,INK,DISPLAY,track=-.1),
       paras(157,140,["The smooth shade returns a broad highlight.","A narrow metal neck separates the two surfaces."],3.8,5.5),
       rule(157,159,289,159),
       text(157,169,"Finish index",3.45,INK,MONO)]
    for i,(key,(name,id_,ph,bg,fg,fin,seq)) in enumerate(ED.items()):
        x=157+45*i
        a.extend([rect(x,176,14,3,{"ivory":"#aebda4","plum":PLUM,"amber":"#ad693e"}[key]),
                  text(x,188,name,6.2,INK,DISPLAY),text(x,198,id_,3.35,INK,MONO)])
    save("brochure-inside",297,210,"BRUME material brochure, inside spread",
         "Four-page folded publication. Left page shows the fluted foot, while the right shows the smooth shade and finish index.",a)
    b=[rect(-3,-3,303,216,PAPER),rect(-3,-3,151.5,216,INK),
       text(8,15,"BRUME",8.4,ACID,DISPLAY),text(138,14,"04",3.5,PAPER,MONO,anchor="end"),
       reg(12,47,107,68,1,ACID),text(8,137,"Reading the light",10.2,PAPER,DISPLAY),
       paras(8,150,["Hold the finish constant and change the","room light. The brightest part of the lamp","moves from its edge towards its centre."],4,5.9,PAPER),
       rule(8,186,138,186,PAPER,.35),text(8,198,"Material notes / Collection 01",3.6,PAPER),
       text(156,16,"BRUME",9,INK,DISPLAY),text(289,14,"Notes / 01",3.5,INK,MONO,anchor="end"),
       rule(156,21,289,21),text(156,48,"A room in",23,INK,DISPLAY,track=-.3),
       text(156,70,"three lights.",23,INK,DISPLAY,track=-.3),
       photo("collection",148.5,81,151.5,90,620),
       text(157,185,"The table light collection",5.2,INK),
       text(157,198,"Ivory, Amber and Plum",3.6,MUTED)]
    save("brochure-outside",297,210,"BRUME material brochure, outside spread",
         "Outside imposition with the back at left and the front at right. A4 sheet folds in half to four pages.",b)


def collateral():
    a=[rect(-3,-3,154,216,PAPER),text(8,17,"BRUME",11,INK,DISPLAY),text(140,15,"BR-02 / IVORY",3.3,INK,MONO,anchor="end"),
       rule(8,22,140,22),text(8,44,"Morning,",20,INK,DISPLAY,track=-.3),
       text(34,64,"held in glass.",20,INK,DISPLAY,track=-.3),
       photo("still-life",-3,73,154,96,620),
       text(8,182,"Ivory",8.4,INK,DISPLAY),reg(112,175,27,13,0),
       paras(8,193,["Daylight traces the smooth shade","and breaks into lines on the foot."],4.05,5.9)]
    save("ad-a5",148,210,"BRUME Ivory magazine advertisement","A5 magazine advertisement introducing the Ivory finish in morning light.",a)
    b=[rect(-3,-3,154,111,INK),photo("shadow",-3,-3,89,111,520,(.52,.5)),
       text(93,13,"BRUME",7.8,ACID,DISPLAY),text(94,30,"Material note",3.4,PAPER,MONO),
       text(92.5,53,"A line",12.7,PAPER,DISPLAY),text(92.5,66,"of light.",12.7,PAPER,DISPLAY),
       rule(94,79,141,79,ACID,.38),text(94,89,"Ribbed glass",3.8,PAPER),text(94,97,"Collection 01",3.45,PAPER)]
    save("postcard-a6",148,105,"A line of light. BRUME A6 postcard","A horizontal shadow photograph paired with a short product introduction on the right.",b)
    c=[rect(-3,-3,111,154,PAPER),text(7,13,"BRUME",8,INK,DISPLAY),text(98,12,"Object card",3.3,INK,MONO,anchor="end"),
       rule(7,17,98,17),text(7,36,"At arm’s length.",13.3,INK,DISPLAY),
       photo("detail",7,43,91,51,450,(.5,.55)),text(7,105,"01  /  Neck and foot",3.65,INK,MONO),
       paras(7,117,["A narrow metal band meets the glass","just above the first flute. The straight","edge makes the curve easier to see."],3.8,5.8),
       rule(7,138,98,138),text(98,144,"Form study   /   01",3.1,INK,MONO,anchor="end")]
    save("insert-a6",105,148,"BRUME form card","A6 insert explaining the visual junction between the metal neck and the glass foot.",c)
    d=[rect(-3,-3,216,303,PAPER),text(11,18,"BRUME",10,INK,DISPLAY),text(198,16,"Collection 01 / Material sheet",3.65,INK,MONO,anchor="end"),
       rule(11,23,199,23),text(11,47,"Table light",22,INK,DISPLAY,track=-.2),text(199,43,"Finish index",5,INK,anchor="end"),
       photo("collection",11,56,188,92,690),
       text(11,161,"Form",7,INK,DISPLAY),
       paras(65,157.5,["A polished-looking dome and a vertically ribbed glass foot","join at a short metal neck."],4,6),rule(11,173,199,173),
       text(11,182,"Edition",3.55,INK,MONO),text(70,182,"Surface",3.55,INK,MONO),text(164,182,"Identifier",3.55,INK,MONO)]
    for i,(key,(name,id_,ph,bg,fg,fin,seq)) in enumerate(ED.items()):
        yy=196+i*16
        d.extend([rect(11,yy-4.3,6,4.3,{"ivory":"#aebda4","plum":PLUM,"amber":"#ad693e"}[key]),text(20,yy,name,5.1),
                  text(70,yy,fin,4),text(164,yy,id_,4.1,INK,MONO),rule(11,yy+5.2,199,yy+5.2,LINE,.3)])
    d.extend([text(11,254,"Project status",6.4,INK,DISPLAY),
              paras(65,252,["Fictional collection. Dimensions, electrical data and","weight await product engineering."],3.9,5.8),
              rule(11,275,199,275),text(11,285,"BRUME    /    Light register",3.6,MUTED),text(199,285,"Finish sheet 01",3.6,INK,MONO,anchor="end")])
    save("sell-sheet-a4",210,297,"BRUME A4 finish and material sheet","Collection photograph above the visual construction notes and the three labeled glass finishes.",d)


def carton():
    # The outline traces one continuous cut around four 240 mm panels.
    # Opposed full-depth lids form a reverse-tuck carton with two dust flaps per end.
    outline=("M0 262H240L250 251L256 174L274 163H447L465 179L474 251L480 262"
             "V22H490Q495 22 497 17L502 3Q503 0 508 0H692Q697 0 699 3L704 17Q706 22 711 22H720V262"
             "L729 251L735 174L753 163H927L944 179L953 251L960 262L980 280V544L960 562"
             "L952 574L945 647L930 661H749L734 645L727 573L720 562H480"
             "L472 574L465 647L450 661H269L254 645L247 573L240 562V802H230Q225 802 223 807"
             "L218 821Q217 824 212 824H28Q23 824 22 821L17 807Q15 802 10 802H0V562Z")
    draw=[f'<path d="{outline}" fill="#eee8d6" stroke="none"/>']
    draw.extend([f'<path d="{outline}" fill="none" stroke="{INK}" stroke-width="1.6"/>',
                 '<path d="M960 262L980 280V544L960 562Z" fill="url(#hatch)" stroke="none"/>'])
    for x in [240,480,720,960]:
        draw.append(rule(x,262,x,562,PLUM,1.25,"8 4"))
    for x1,x2,pos in [(240,480,262),(480,720,262),(720,960,262),(0,240,562),(240,480,562),(720,960,562),(490,710,22),(10,230,802)]:
        draw.append(rule(x1,pos,x2,pos,PLUM,1.25,"8 4"))
    draw.extend([f'<g transform="translate(70 337)">{"".join(label_art("plum",0))}</g>',
                 text(12,282,"FRONT",8,MUTED,MONO),text(252,282,"SIDE A",8,MUTED,MONO),
                 text(492,282,"BACK",8,MUTED,MONO),text(732,282,"SIDE B",8,MUTED,MONO),
                 text(360,417,"240 × 300",14,MUTED,MONO,anchor="middle"),
                 text(600,414,"Label centred on",10,MUTED,anchor="middle"),text(600,431,"front panel",10,MUTED,anchor="middle"),
                 text(600,128,"Top closure",12,MUTED,anchor="middle"),text(120,697,"Bottom closure",12,MUTED,anchor="middle")])
    art=[rect(0,0,1040,972,PAPER),'<defs><pattern id="hatch" patternUnits="userSpaceOnUse" width="7" height="7"><path d="M0 7L7 0" stroke="#767b57" stroke-width="1.2"/></pattern></defs>',
         text(30,35,"BRUME",23,INK,DISPLAY),text(1010,33,"Reverse-tuck study   /   dimensions in mm",12,INK,MONO,anchor="end"),rule(30,50,1010,50),
         '<g transform="translate(30 80)">'+''.join(draw)+'</g>',
         rule(30,935,61,935,INK,1.6),text(68,938,"Cut",11,INK),rule(178,935,209,935,PLUM,1.25,"8 4"),text(216,938,"Fold",11),
         rect(320,928,31,13,"url(#hatch)"),text(358,938,"Glue flap",11),text(1010,938,"Envelope 980 × 824   /   seam 20",10.5,INK,MONO,anchor="end")]
    save("carton-net",1040,972,"BRUME reverse-tuck carton layout",
         "Concept flat. Four 240 mm wide faces, 300 mm tall, twenty-millimetre glue tab and opposed lids. Solid line marks cuts, dashed line marks folds and diagonal hatching marks the glue area.",art,bleed=0)


if __name__=="__main__":
    OUT.mkdir(exist_ok=True)
    editions()
    poster()
    brochure()
    collateral()
    carton()
