from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
from PIL import Image,ImageDraw,ImageEnhance
from reportlab.lib.units import mm
ROOT=Path(__file__).resolve().parents[1]
INK=HexColor('#181917'); PAPER=HexColor('#F2EFE8'); ORANGE=HexColor('#FF542D'); ACID=HexColor('#DBFA36'); SILVER=HexColor('#90958c')
fonts={'I':'/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','B':'/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','M':'/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'}
for name,path in fonts.items():pdfmetrics.registerFont(TTFont('pr'+name,path))
def txt(c,x,y,t,size=11,bold=False,color=INK):
 c.setFillColor(color);c.setFont('prB' if bold else 'prI',size);c.drawString(x,y,t)
def mono(c,x,y,t,size=6.3,color=INK):
 c.setFillColor(color);c.setFont('prM',size);c.drawString(x,y,t)
def image_fit(c,path,x,y,w,h):
 im=Image.open(path).convert('RGB');sw,sh=im.size;r=max(w/sw,h/sh);cw,ch=w/r,h/r;left=(sw-cw)*.5;top=(sh-ch)*.5;im=im.crop((int(left),int(top),int(left+cw),int(top+ch)))
 c.drawImage(ImageReader(im),x,y,w,h)
def base(c,n,w,h,dark=False):
 c.setFillColor(INK if dark else PAPER);c.rect(0,0,w,h,fill=1,stroke=0)
 c.setStrokeColor(PAPER if dark else INK);c.setLineWidth(.5);c.line(17,h-36,w-17,h-36)
 mono(c,18,h-27,'PROOF / ISSUE 01 / DESIGN STUDY',6.7,PAPER if dark else INK)
 mono(c,w-47,18,f'{n:02}/12',6.6,PAPER if dark else INK)
 c.line(18,33,w-18,33)
W,H=148*mm,210*mm
issues=[
 ('COVER','THE ANATOMY','OF A PRINTED IDEA','',0),
 ('EDITORIAL','BETWEEN AN IDEA','AND A FINAL FILE','A record of the decisions that shape graphic communication.',1),
 ('CONTENTS','FOUR MOVEMENTS','ONE CREATIVE SYSTEM','01 / Observe   02 / Compose   03 / Refine   04 / Release',2),
 ('OBSERVE','LOOK CLOSER.','LOOK AGAIN.','The strongest visual decisions begin with careful observation.',3),
 ('OBSERVE','AN IMAGE IS','A DECISION','Cropping determines what the audience sees first.',4),
 ('COMPOSE','FORM FOLLOWS','ATTENTION','Hierarchy is the order in which a reader encounters information.',5),
 ('COMPOSE','ONE IDEA,','MANY FORMATS','One consistent identity. Different uses, ratios and distances.',6),
 ('REFINE','CHANGE WITH','INTENTION','Iteration is valuable when it solves a recognizable problem.',7),
 ('REFINE','THE DETAIL','IS THE DESIGN','Spacing, contrast, copy and imagery are all editorial decisions.',8),
 ('RELEASE','NAME THE','SOURCE OF TRUTH','Production files need unambiguous versions and destinations.',9),
 ('RELEASE','ARTWORK IS','NOT APPROVAL','Physical proofing, substrate and vendor specifications still matter.',10),
 ('COLOPHON','GOOD IDEAS','DESERVE PROOFS','A self-directed conceptual publication on design and production.',11)
]
c=canvas.Canvas(str(ROOT/'PROOF_Issue_01.pdf'),pagesize=(W,H),pageCompression=1)
c.setTitle('PROOF Issue 01 — The Anatomy of a Printed Idea | Portfolio Specimen')
for i,(label,t1,t2,copy,j) in enumerate(issues):
 dark=i in (0,3,7,11);base(c,i+1,W,H,dark)
 if i in (0,3,7,11):
  image_fit(c,ROOT/'assets/hero-studio.webp',18,130,W-36,H-175)
  c.setFillColor(INK);c.rect(0,33,W,120,fill=1,stroke=0)
  mono(c,19,136,f'{label} / 2026',7,ACID)
  txt(c,18,99,t1,21,True,PAPER)
  txt(c,18,71,t2,20,True,ORANGE if i==0 else PAPER)
  if copy:mono(c,19,45,copy[:63],6.2,PAPER)
 elif i in (1,4,8):
  image_fit(c,ROOT/'assets/contact-sheet.webp',W*.45,145,W*.52,H-195)
  mono(c,18,H-63,f'{label} / {i+1:02}',7,ORANGE)
  txt(c,18,H-111,t1,18,True)
  txt(c,18,H-140,t2,17,True)
  for l,text in enumerate([copy,'A frame can disclose a subject','and still conceal its context.']):mono(c,18,104-l*18,text[:51],6.1)
 elif i in (2,6,9):
  mono(c,18,H-61,f'{label} / {i+1:02}',7,ORANGE)
  txt(c,18,H-101,t1,22,True);txt(c,18,H-132,t2,20,True)
  c.setFillColor(ACID if i==2 else ORANGE);c.rect(18,H-166,W-36,13,fill=1,stroke=0)
  image_fit(c,ROOT/'assets/detail-spread.webp',18,110,W-36,H-298)
  mono(c,18,89,copy[:67],6.2)
 else:
  image_fit(c,ROOT/'assets/issue-study.webp',18,H*.32,W-36,H*.52)
  c.setFillColor(PAPER);c.rect(18,82,W-36,126,fill=1,stroke=0)
  mono(c,24,191,f'{label} / CHAPTER {i+1:02}',6.8,ORANGE)
  txt(c,24,158,t1,21,True);txt(c,24,131,t2,20,True)
  mono(c,24,102,copy[:59],6.3)
 c.showPage()
c.save()
# A5 print advertising specimen with known page size and file status in metadata.
c=canvas.Canvas(str(ROOT/'PROOF_Print_Specimens.pdf'),pagesize=(W,H),pageCompression=1)
c.setTitle('PROOF — A5 Advertising Specimens | Not Printer Certified')
base(c,1,W,H,False)
image_fit(c,ROOT/'assets/print-advert.webp',0,60,W,H-60)
mono(c,18,43,'PRINT ADVERTISING / SPECIMEN / A5',7,INK)
mono(c,18,20,'PREPRESS STATUS: CONCEPT / VENDOR REVIEW REQUIRED',5.9,ORANGE)
c.showPage();c.save()
print('Created reading publication and A5 advertising PDF specimens.')
# Compare exploratory vs refined version as actual two separate images.
photo=Image.open(ROOT/'assets/campaign-01.webp').convert('RGB');early=ImageEnhance.Color(photo).enhance(.26)
d=ImageDraw.Draw(early);d.rectangle((0,970,1080,1350),fill='#292b25');d.rectangle((55,1070,600,1090),fill='#ff542d');d.rectangle((55,1110,790,1120),fill='#ff542d');d.rectangle((55,1140,500,1153),fill='#9d9e94')
early.save(ROOT/'assets/campaign-exploration.webp','WEBP',quality=84,method=5)
