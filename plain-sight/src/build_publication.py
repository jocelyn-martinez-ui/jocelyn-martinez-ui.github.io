"""Reproducible 24-page editorial edition and its exact web page previews."""
from pathlib import Path
import json, subprocess, shutil
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageDraw
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];W,H=595.2756,841.8898;M=40
PAPER='#f2efe8';INK='#282824';RED='#723e43';MUTED='#62615a';RULE='#b6b3a9'
for name,file in [('Display','BodoniModa-Regular.ttf'),('Italic','BodoniModa-Italic.ttf'),('Body','DMSans-Regular.ttf'),('Medium','DMSans-Medium.ttf')]:pdfmetrics.registerFont(TTFont(name,str(R/'src/fonts'/file)))
D=json.loads((R/'src/collection.json').read_text());records={x['id']:x for s in D for x in [s,*s['crops']]}
output=R/'downloads/PLAIN_SIGHT_Studies_01-03.pdf';archive=R/'downloads/archive/PLAIN_SIGHT_Studies_Edition02.pdf';archive.parent.mkdir(exist_ok=True)
if not archive.exists():shutil.copyfile(output,archive)
c=canvas.Canvas(str(output),pagesize=(W,H),pageCompression=1)
c.setTitle('PLAIN SIGHT — The observation edition');c.setAuthor('Jocelyn Martinez');c.setSubject('Five generated image sources, eleven editorial crops, three photographic studies. Digital review specimen.')
pages=[];cur={}
def txt(text,x,y,size=11,font='Body',color=INK):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,text)
def lines(text,x,y,size=40,font='Display',leading=None,color=INK):
 for t in text.split('\n'):txt(t,x,y,size,font,color);y-=leading or size*1.05
 return y
def para(text,x,y,width=330,size=12,color=INK,font='Body'):
 words=text.split();line=''
 for word in words:
  trial=(line+' '+word).strip()
  if pdfmetrics.stringWidth(trial,font,size)>width and line:txt(line,x,y,size,font,color);y-=size*1.5;line=word
  else:line=trial
 if line:txt(line,x,y,size,font,color);y-=size*1.5
 return y

def line(x,y,w,color=RULE):c.setStrokeColor(HexColor(color));c.setLineWidth(.5);c.line(x,y,x+w,y)
def image(id,x,y,w,h):
 im=Image.open(R/f'assets/images/{id}.webp');iw,ih=im.size;scale=min(w/iw,h/ih);dw,dh=iw*scale,ih*scale;buf=BytesIO();im.convert('RGB').save(buf,format='JPEG',quality=92,optimize=True);buf.seek(0);c.drawImage(ImageReader(buf),x+(w-dw)/2,y+(h-dh)/2,dw,dh,mask='auto');return dw,dh

def base(n,title,chapter,description,source=None,dark=False):
 global cur
 c.setFillColor(HexColor(INK if dark else PAPER));c.rect(0,0,W,H,fill=1,stroke=0)
 col=PAPER if dark else INK
 txt('PLAIN SIGHT / OBSERVATION EDITION',M,H-32,9,'Medium',col);txt(chapter.upper(),W-190,H-32,9,'Body',col)
 line(M,H-45,W-2*M,'#66675f' if dark else RULE)
 line(M,42,W-2*M,'#66675f' if dark else RULE);txt('THE ORDINARY, OBSERVED DIFFERENTLY.',M,25,8,'Body',col);txt(f'{n:02d} / 24',W-78,25,9,'Medium',col)
 cur={'page':n,'title':title,'chapter':chapter,'description':description,'sourceId':source}
 c.bookmarkPage(f'page-{n}');
 if n in [1,5,11,17,23]:c.addOutlineEntry(title,f'page-{n}',0,False)
def done():pages.append(cur.copy());c.showPage()
def source_page(n,s,subtitle):
 base(n,s['title'],s['seriesName'],s['alt'],s['id'])
 txt('ORIGINAL GENERATED SOURCE '+s['number'],M,H-78,10,'Medium',RED)
 lines(s['title'],M,H-123,33)
 image(s['id'],M,170,W-2*M,480)
 para(s['note'],M,134,W-2*M,11)
 txt(subtitle,M,64,9,'Medium',MUTED);done()
def crop_page(n,s,title,desc):
 base(n,title,s['seriesName'],desc,s['id'])
 txt('FRAMING DECISIONS / SOURCE '+s['number'],M,H-78,10,'Medium',RED)
 para(title,M,H-124,W-2*M,35,font='Display')
 # Distinct source/crop hierarchy; two variants never become two exposures.
 cs=s['crops'][:2];gap=24;cw=(W-2*M-gap)/2
 for i,cr in enumerate(cs):
  x=M+i*(cw+gap);image(cr['id'],x,330,cw,305)
  txt('CROP '+str(i+1)+' / FROM SOURCE '+s['number'],x,308,9,'Medium',RED)
  y=para(cr['title'],x,279,cw,20,font='Display')
  para(cr['note'],x,y-18,cw,11)
 txt('Compare both with the original: plain-sight/light-table.html?source='+s['id'],M,64,8,'Body',MUTED);done()
base(1,'A second look','Cover','Cover with a large editorial title and the complete seated portrait.','gesture-seated')
lines('A second',M,H-160,82);lines('look.',M,H-244,98,'Italic',color=RED)
image('gesture-seated',M,195,W-2*M,340)
txt('PLAIN SIGHT',M,148,20,'Medium');para('Five source images. Three studies. A practice of attention.',M,115,310,12);txt('2026 / EDITION 03',W-158,115,10,'Medium');done()
base(2,'Attention is a medium','Editorial','Editorial introduction and transparent source-image provenance.')
lines('Nothing new.\nSomething\nnoticed.',M,H-150,66)
para('A wall beside a seated figure. A stem connecting a dark flower to a clear glass. A chair holding the scale of an empty room.',M,390,390,15)
para('The material does not change when we look again. The relationships do. This edition moves between the whole image, its existing editorial crops and new notes on what those edits make visible.',M,284,410,12)
line(M,170,W-2*M)
para('This is a self-directed studio concept by Jocelyn Martinez. All five original image scenes are AI-generated. The eleven derivatives are crops, not additional photographs. No real shoot, commissioned talent, camera settings or client results are implied.',M,146,W-2*M,10,color=MUTED);done()
base(3,'Five sources, three studies','Index','A five-source image index with chapter and publication page references.')
lines('The source index.',M,H-130,48)
for i,s in enumerate(D):
 y=H-245-i*111;image(s['id'],M,y-24,74,88);txt(s['number'],M+94,y+39,27,'Display',RED);txt(s['title'],M+140,y+43,15,'Medium');txt(s['seriesName']+' / '+str(len(s['crops']))+' derivative crops',M+140,y+20,10);txt('SOURCE PAGE '+str(s['page']).zfill(2),M+140,y-2,9,'Medium',MUTED);line(M,y-38,W-2*M)
done()
base(4,'Observe. Reframe. Read.','Method','Three editorial actions and the relationship between original images and derivatives.',dark=True)
lines('The frame\nis a choice.',M,H-170,71,color=PAPER)
for y,num,title,body in [(415,'01','Observe','Give the whole image time. Notice where the subject sits and what the surrounding space contributes.'),(295,'02','Reframe','Place a crop beside its source. Ask what gains emphasis and what information is lost.'),(175,'03','Read','Follow the sequence. The next image can offer context, sharpen a detail or provide a pause.')]:
 txt(num,M,y,26,'Display',PAPER);txt(title,M+65,y+4,18,'Medium',PAPER);para(body,M+65,y-23,390,11,PAPER)
done()
base(5,'Gestures','Gestures','Chapter opening with the complete fabric portrait, a generous title and a brief human-scale observation.','gesture-fabric')
txt('STUDY 01 / PEOPLE · POSTURE · FABRIC',M,H-84,10,'Medium',RED);lines('Gestures.',M,H-183,82)
image('gesture-fabric',310,170,245,420);lines('A body.\nA fold.\nA pause.',M,400,33,'Italic');para('Two human scenes, observed from different distances. Keep room around the gesture before moving closer.',M,250,220,12);done()
source_page(6,D[0],'SOURCE 01 / FULL COMPOSITION — NO ADDITIONAL CROP')
crop_page(7,D[0],'Presence, or the space beside it.','Two actual crops from the seated source: a close portrait and a wall-led edit.')
source_page(8,D[1],'SOURCE 02 / FULL COMPOSITION — THE FOLD CONNECTS HAND AND BODY')
crop_page(9,D[1],'From gesture to material.','Two derivatives of the fabric portrait: the head and shoulder, then the fabric alone.')
base(10,'Two scenes, one attention','Gestures','The two distinct original human scenes are labelled together, followed by a short editorial reflection.',dark=True)
lines('A gesture\nleaves a trace.',M,H-150,58,color=PAPER)
image('gesture-seated',M,280,290,260);image('gesture-fabric',360,280,195,350)
txt('SOURCE 01 / SEATED',M,252,10,'Medium',PAPER);txt('SOURCE 02 / FABRIC',360,252,10,'Medium',PAPER)
para('These are two original generated scenes. Their four derivative crops explore posture, absence, attention and material. The sequence gets its variety from scale and framing, not a fictional fashion shoot.',M,180,450,12,PAPER);done()
base(11,'Arrangements','Arrangements','Still-life chapter opening with the whole flower composition set against the chapter title.','arrangement-bloom')
txt('STUDY 02 / OBJECTS · TEXTURE · BALANCE',M,H-84,10,'Medium',RED);lines('Arrange-\nments.',M,H-160,63)
image('arrangement-bloom',300,180,255,450)
para('One dark flower.\nOne clear glass.\nA small conversation.',M,390,215,16)
para('Two still lifes organized by the relationships between ordinary things.',M,210,210,11);done()
source_page(12,D[2],'SOURCE 03 / FULL COMPOSITION — FLOWER, GLASS, LINEN, STONE')
crop_page(13,D[2],'The stem, or the weight below.','Two actual crops from the flower source isolate the flower-and-glass relationship and the material base.')
source_page(14,D[3],'SOURCE 04 / FULL COMPOSITION — A HEAVY VASE AND A REACHING BRANCH')
crop_page(15,D[3],'Weight and counterweight.','Two crops from the table source: the clustered objects and the lighter diagonal composition.')
base(16,'A table is a small stage','Arrangements','An editorial pause with material detail from each of the two still-life sources.','arrangement-table',dark=True)
lines('Objects\nare always\nin dialogue.',M,H-150,60,color=PAPER)
image('arrangement-bloom-base',M,150,240,200);image('arrangement-table-objects',310,150,245,200)
txt('FROM SOURCE 03 / BASE',M,125,9,'Medium',PAPER);txt('FROM SOURCE 04 / OBJECTS',310,125,9,'Medium',PAPER);done()
base(17,'In Between','In Between','An unobscured chapter title beside the tall window crop of the room and a short reflection.','between-room')
txt('STUDY 03 / SPACE · GEOMETRY · LIGHT',M,H-84,10,'Medium',RED)
lines('In Between.',M,H-162,67)
image('between-room-window',285,140,270,490)
lines('Almost\nnothing.\nAnd enough.',M,370,31,'Italic');para('One room.\nThree closer readings.',M,200,150,11);done()
source_page(18,D[4],'SOURCE 05 / FULL COMPOSITION — ONE ROOM, NOT SEVERAL LOCATIONS')
base(19,'Make a threshold','In Between','A tall window crop appears beside a small full-source reference and its actual framing note.','between-room')
txt('FRAMING DECISION / SOURCE 05',M,H-84,10,'Medium',RED);lines('Make a threshold.',M,H-137,43)
image('between-room-window',M,145,230,520);image('between-room',330,385,150,225)
txt('ORIGINAL / SOURCE 05',330,365,9,'Medium',MUTED);para(D[4]['crops'][0]['note'],330,310,220,12)
txt('CROP 01 / FROM SOURCE 05',M,112,10,'Medium',RED);done()
base(20,'Scale and the path of light','In Between','The chair crop and floor-shadow crop show two different framings of the same room.','between-room')
txt('FRAMING DECISIONS / SOURCE 05',M,H-84,10,'Medium',RED);lines('A trace of presence.',M,H-137,43)
image('between-room-chair',M,240,230,400);image('between-room-shadow',310,355,245,255)
txt('CROP 02 / CHAIR',M,216,9,'Medium',RED);para(D[4]['crops'][1]['note'],M,190,230,11)
txt('CROP 03 / SHADOW',310,330,9,'Medium',RED);para(D[4]['crops'][2]['note'],310,300,245,11);done()
base(21,'One room, three edits','In Between','A lineage diagram groups the original room image with all three of its actual derivative crops.','between-room')
lines('One room.\nThree readings.',M,H-130,48)
image('between-room',M,285,230,320);txt('ORIGINAL / SOURCE 05',M,262,10,'Medium',RED)
for i,cr in enumerate(D[4]['crops']):
 y=530-i*145;image(cr['id'],325,y-35,100,125);txt('CROP '+str(i+1),445,y+40,9,'Medium',RED);para(['Threshold','Human scale','Light across'][i],445,y+17,110,11)
para('The derivatives stay attached to their parent. A contact sheet can reveal an editorial decision without pretending to document exposures that never happened.',M,175,440,12);done()
base(22,'The same attention','Synthesis','Three labelled original sources connect the human, still-life and architectural studies.')
lines('Different subjects.\nThe same attention.',M,H-130,45)
for i,s in enumerate([D[1],D[2],D[4]]):
 x=M+i*178;image(s['id'],x,270,158,290);txt('SOURCE '+s['number'],x,245,9,'Medium',RED);txt(s['seriesName'],x,223,12,'Medium')
para('A fold, a stem, a band of light. Repeated warmth and directional light connect the image world. Different spatial relationships keep the three studies distinct.',M,160,450,12);done()
base(23,'A transparent edition','Colophon','Production details, image provenance, authorship and the limits of this digital review edition.')
lines('Look once.\nLook again.',M,H-150,65)
y=430
for h,b in [('CREATOR','Jocelyn Martinez / self-directed concept, visual identity, editorial art direction and interface reconstruction.'),('IMAGE PROVENANCE','Five existing AI-generated source scenes. Eleven existing derivative crops. New authored framing notes. No shoot, real models, camera settings, client campaign or user-study findings are implied.'),('PRODUCTION','24 A4 portrait pages, 210 × 297 mm. RGB digital-review PDF; no external bleed, commercial preflight or physical proof. Effective image resolution varies. A printer-ready edition needs source-resolution and color-profile review.'),('TYPE & SOURCE','Bodoni Moda and DM Sans, embedded under SIL Open Font License. Editable layout source: plain-sight/src/build_publication.py. All original source images and the previous edition are preserved.')]:
 txt(h,M,y,10,'Medium',RED);y=para(b,M,y-23,490,11)-30
c.linkURL('https://jocelyn-martinez-ui.github.io/plain-sight/',(M,55,W-M,77),relative=0);txt('Continue the observation online: jocelyn-martinez-ui.github.io/plain-sight/',M,66,10,'Medium');done()
base(24,'The ordinary, observed differently','Back cover','Closing statement and an original still-life composition.','arrangement-table',dark=True)
lines('The ordinary,',M,H-155,55,color=PAPER);lines('observed',M,H-222,62,'Italic',color=PAPER);lines('differently.',M,H-287,58,color=PAPER)
image('arrangement-table',M,170,W-2*M,300);txt('PLAIN SIGHT / STUDIES 01–03',M,115,15,'Medium',PAPER);txt('FIVE SOURCES. ELEVEN CROPS. A SECOND LOOK.',M,86,10,'Body',PAPER);done();c.save()
reader=PdfReader(output)
for info,p in zip(pages,reader.pages):info['text']=p.extract_text()+'\n\nIMAGE DESCRIPTION\n'+info['description']
(R/'src/publication-pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
render=R/'assets/publication';render.mkdir(exist_ok=True)
tmp=Path('/tmp/plain-sight-publication-render');tmp.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-scale-to','1000','-png',str(output),str(tmp/'page')],check=True,stdout=subprocess.DEVNULL)
for i in range(1,25):
 im=Image.open(tmp/f'page-{i:02d}.png').convert('RGB');im.save(render/f'page-{i:02d}.webp',quality=86,method=6);im.resize((212,300),Image.Resampling.LANCZOS).save(render/f'thumb-{i:02d}.webp',quality=80,method=6)
sheet=Image.new('RGB',(1200,1500),'#d6d4cd');draw=ImageDraw.Draw(sheet)
for i in range(1,25):
 im=Image.open(render/f'page-{i:02d}.webp');im.thumbnail((185,263));x=((i-1)%6)*200+7;y=((i-1)//6)*375+28;sheet.paste(im,(x,y));draw.text((x,y-18),f'PAGE {i:02d}',fill='#222222')
out=R/'docs/reconstruction';out.mkdir(exist_ok=True);sheet.save(out/'publication-after-contact-sheet.jpg',quality=90)
shutil.rmtree(tmp)
print('Built',len(reader.pages),'pages;',output.stat().st_size,'PDF bytes')
