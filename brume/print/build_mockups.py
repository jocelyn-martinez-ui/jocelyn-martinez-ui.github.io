"""Register BRUME's print artwork to its generated blank plates.

Run after build_print.py. Dependencies are Inkscape, Pillow and NumPy. Install
Barlow Condensed ExtraBold for Inkscape exports; SVGs also embed the face for browsers.
"""
from pathlib import Path
import subprocess
import tempfile
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
PLATES = ROOT / 'plates'
MASTER = ROOT / 'svg'
DEST = ROOT / 'mockups'


def render(stem, width_mm, height_mm, px, folder):
    source = MASTER / (stem+'.svg')
    png = folder / (stem+'.png')
    subprocess.run(['inkscape',str(source),f'--export-filename={png}',f'--export-width={px}'],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    with Image.open(png) as im:
        # Each printable master carries an extra three millimetres on all edges.
        scale_x,scale_y=im.width/(width_mm+6),im.height/(height_mm+6)
        bounds=(round(3*scale_x),round(3*scale_y),round((3+width_mm)*scale_x),round((3+height_mm)*scale_y))
        return im.convert('RGB').crop(bounds)


def homography(dest, src):
    rows, targets = [], []
    for (x,y),(u,v) in zip(dest,src):
        rows.extend(([x,y,1,0,0,0,-u*x,-u*y],[0,0,0,x,y,1,-v*x,-v*y]))
        targets.extend((u,v))
    return np.linalg.solve(np.array(rows),np.array(targets))


def print_layer(photo, plate, page, quad, sticker=False):
    # Apply real ink to the plate's own shadow and surface texture.
    q=np.array(quad,dtype=float)
    origin=np.floor(q.min(axis=0)).astype(int)-2
    end=np.ceil(q.max(axis=0)).astype(int)+3
    box=(*origin,*end)
    local=q-origin
    corners=((0,0),(page.width,0),(page.width,page.height),(0,page.height))
    coefficients=homography(local,corners)
    art=page.transform(tuple(end-origin),Image.Transform.PERSPECTIVE,coefficients,
                       Image.Resampling.BICUBIC,fillcolor=(255,255,255))
    base=np.asarray(plate.crop(box)).astype(np.float32)
    ink=np.asarray(art).astype(np.float32)/255
    if sticker:
        # A solid-colour paper label sits on top of the darker uncoated board.
        luminance=base @ np.array([.21,.72,.07])
        surface=np.clip(.9 + (luminance-np.median(luminance))*.0025, .66, 1.0)
        result=(ink*249+3)*surface[:,:,None]
    else:
        result=base*(.025+.975*ink)
    mask=Image.new('L',tuple((end-origin)*2))
    ImageDraw.Draw(mask).polygon([tuple(z*2) for z in local],fill=255)
    mask=mask.resize(tuple(end-origin),Image.Resampling.LANCZOS)
    photo.paste(Image.fromarray(np.uint8(np.clip(result,0,255))),tuple(origin),mask)


def surface_point(face, x, y):
    a,b,c,d=np.array(face)
    return tuple((a*(1-x)+b*x)*(1-y)+(d*(1-x)+c*x)*y)


def main():
    DEST.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        t=Path(t)
        poster=render('campaign-poster',700,1050,1250,t)
        label=render('brume-label-plum-r03',100,150,650,t)
        spread=render('brochure-inside',297,210,1960,t)
        wall=Image.open(PLATES/'gallery-wall-blank.webp').convert('RGB')
        scene=wall.copy()
        print_layer(scene,wall,poster,[(298,121),(746,121),(746,807),(298,808)])
        scene.save(DEST/'gallery-wall.webp',quality=85,method=6)
        carton=Image.open(PLATES/'carton-blank.webp').convert('RGB')
        face=[(425,178),(959,186),(956,892),(426,873)]
        q=[surface_point(face,x,y) for x,y in [(70/240,.25),(170/240,.25),(170/240,.75),(70/240,.75)]]
        scene=carton.copy()
        print_layer(scene,carton,label,q,sticker=True)
        scene.save(DEST/'carton.webp',quality=85,method=6)
        paper=Image.open(PLATES/'open-brochure-blank.webp').convert('RGB')
        # Divide the fold near its centre so the design shares the photographed curvature.
        # Text stays editable in the native flat; only this placement is rasterised.
        strips=[(0,(256,53),(144,836)),(.25,(530,82),(430,866)),
                (.45,(750,106),(661,889)),(.5,(803,122),(721,897)),
                (.56,(871,119),(791,904)),(.76,(1100,141),(1025,928)),(1,(1373,180),(1303,957))]
        scene=paper.copy()
        for (s,top,bot),(e,top2,bot2) in zip(strips,strips[1:]):
            page=spread.crop((round(s*spread.width),0,round(e*spread.width),spread.height))
            print_layer(scene,paper,page,[top,top2,bot2,bot])
        scene.save(DEST/'open-brochure.webp',quality=85,method=6)


if __name__=='__main__':
    main()
