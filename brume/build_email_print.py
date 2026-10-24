from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, PCMYKColor
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pypdf import PdfReader,PdfWriter
from PIL import Image
import json, textwrap
root=Path(__file__).resolve().parent
for sub in ['email','print/pdf','print/archive']:(root/sub).mkdir(exist_ok=True,parents=True)
P={'ink':'#2B201B','paper':'#EEE8DE','wine':'#582C3A','honey':'#D8A765','rust':'#A56841','fog':'#C8B9A6','light':'#FAF4E8'}
mailplans=[('01-introduction','The evening looks different from here','Meet BRUME: a table light made for the hours after work.','A small change in light. An entirely different room.','wine-room','THE EVENING, RECONSIDERED.','Discover the studio edition.'),('02-material','Light is a material','Plum, ivory or amber: three interpretations of a familiar silhouette.','A study in color, glass and the spaces around it.','collection','ONE SHAPE, THREE ATMOSPHERES.','Explore the color studies.'),('03-detail','The detail you stay for','A closer look at the pieces and the moments they create.','The warm reflection, the curve of the glass, the passing light.','hand-detail','AN OBJECT TO LIVE BESIDE.','See the concept collection.')]
for slug,subject,pre,headline,img,strap,cta in mailplans:
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{subject} — BRUME email concept</title><style>@media screen and (max-width:640px){{.email-wrap{{width:100%!important;max-width:100%!important}}.mobile-gutter{{padding-left:22px!important;padding-right:22px!important}}.hero-title{{font-size:38px!important;line-height:40px!important}}.email-visual{{height:auto!important}}.stack{{display:block!important;width:100%!important}}}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}</style></head><body style="margin:0;background:#e4ddd5;padding:0"><div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;color:#e4ddd5">{pre}&nbsp;&zwnj;&nbsp;&zwnj;</div><center style="background:#e4ddd5;width:100%;padding:24px 0"><table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:#e4ddd5"><tr><td align="center"><!--[if mso]><table width="600" align="center" role="presentation" cellpadding="0" cellspacing="0"><tr><td><![endif]--><table class="email-wrap" role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="width:600px;max-width:600px;background:#EEE8DE"><tr><td class="mobile-gutter" style="padding:30px 40px;border-bottom:1px solid #96877B"><table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr><td align="left" style="font:normal 29px Georgia,serif;letter-spacing:7px;color:#2B201B">BRUME</td><td align="right" style="font:normal 11px Arial,sans-serif;letter-spacing:2px;color:#582C3A">STUDIO / EDITION 01</td></tr></table></td></tr><tr><td><img class="email-visual" src="../images/{img}.jpg" width="600" alt="Conceptual photograph of a sculptural ribbed glass table lamp" style="display:block;border:0;max-width:100%;height:auto"/></td></tr><tr><td class="mobile-gutter" style="padding:42px 40px 34px"><p style="font:normal 12px Arial,sans-serif;letter-spacing:2px;color:#A56841;margin:0 0 16px">BRUME / LIGHT OBJECTS</p><h1 class="hero-title" style="font:normal 50px/1.04 Georgia,serif;color:#2B201B;letter-spacing:-1px;margin:0 0 23px">{headline}</h1><p style="font:normal 17px/1.65 Arial,sans-serif;color:#40342F;margin:0 0 30px">{strap}</p><table role="presentation" cellspacing="0" cellpadding="0"><tr><td bgcolor="#582C3A"><a href="https://example.com/brume" style="display:inline-block;padding:15px 24px;font:bold 13px/18px Arial,sans-serif;letter-spacing:1px;color:#FFFFFF;text-decoration:none">{cta} &rarr;</a></td></tr></table></td></tr><tr><td class="mobile-gutter" style="padding:24px 40px 35px;background:#C8B9A6"><p style="font:italic 23px Georgia,serif;color:#2B201B;margin:0 0 10px">A room is made of its little hours.</p><p style="font:normal 13px/1.6 Arial,sans-serif;color:#2B201B;margin:0">Photography is AI-generated concept art. Lamp products are fictional and have not been manufactured or electrically certified.</p></td></tr><tr><td class="mobile-gutter" style="padding:24px 40px 32px"><p style="font:normal 11px/1.6 Arial,sans-serif;color:#62564D;margin:0">Self-directed portfolio demonstration only. This email has not been sent. The CTA is a nonfunctional example URL. No actual subscription service, postal address or unsubscribe infrastructure exists; add all required sender details and opt-out systems before real sending.</p></td></tr></table><!--[if mso]></td></tr></table><![endif]--></td></tr></table></center></body></html>'''
 (root/'email'/f'{slug}.html').write_text(html)
 (root/'email'/f'{slug}.txt').write_text(f'Subject: {subject}\nPreheader: {pre}\n\n{headline}\n\n{strap}\n\n{cta}: https://example.com/brume (example only)\n\nBRUME is a fictional, AI-assisted portfolio concept. No actual email has been sent.\n')
# PDF design
pdfmetrics.registerFont(TTFont('Garamond','/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf'))
pdfmetrics.registerFont(TTFont('GaramondBold','/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
mm=72/25.4
rgb=lambda s:HexColor(s)
# CMYK approximations illustrative; real ICC profile must be matched by vendor
cmyk={
 'ink':PCMYKColor(0,25,35,83),
 'paper':PCMYKColor(0,2,6,7),
 'wine':PCMYKColor(0,50,32,65),
 'honey':PCMYKColor(0,22,53,15),
 'rust':PCMYKColor(0,37,61,35),
 'fog':PCMYKColor(0,5,13,22),
 'light':PCMYKColor(0,1,4,2)
}

def makepdf(name,trim_w,trim_h,render,rev='03'):
 page_w,page_h=trim_w+6,trim_h+6
 path=root/'print/pdf'/f'{name}.pdf'; c=canvas.Canvas(str(path),pagesize=(page_w*mm,page_h*mm),pageCompression=1)
 c.setAuthor('Jocelyn Martinez / BRUME fictional concept')
 c.setTitle(f'BRUME {name} / TECHNICAL SPECIMEN, NOT PRESS APPROVED')
 c.setSubject('Provisional 3 mm bleed; NOT retail-ready or printer certified')
 render(c,page_w*mm,page_h*mm,trim_w*mm,trim_h*mm)
 c.showPage();c.save()
 reader=PdfReader(str(path));writer=PdfWriter();writer.append(reader)
 page=writer.pages[0];page.trimbox.lower_left=(3*mm,3*mm);page.trimbox.upper_right=((trim_w+3)*mm,(trim_h+3)*mm)
 page.bleedbox.lower_left=(0,0);page.bleedbox.upper_right=(page_w*mm,page_h*mm)
 page.cropbox.lower_left=(0,0);page.cropbox.upper_right=(page_w*mm,page_h*mm)
 with open(path,'wb') as f:writer.write(f)
 return path

def rect(c,x,y,w,h,color):c.setFillColor(cmyk[color]);c.rect(x,y,w,h,stroke=0,fill=1)
def t(c,x,y,text,size=12,font='Garamond',color='ink'):
 c.setFillColor(cmyk[color]);c.setFont(font,size);c.drawString(x,y,text)
def photo(c,name,x,y,w,h):
 # Image here is sourced from AI-generated RGB photography; genuine CMYK proof conversion would require vendor ICC.
 im=root/'images'/f'{name}.jpg'
 from PIL import Image
 w0,h0=Image.open(im).size
 ratio=max(w/w0,h/h0)
 dw,dh=w0*ratio,h0*ratio
 c.saveState();clip=c.beginPath();clip.rect(x,y,w,h);c.clipPath(clip,stroke=0,fill=0)
 c.drawImage(str(im),x-(dw-w)/2,y-(dh-h)/2,width=dw,height=dh,mask='auto');c.restoreState()

for (name,sku,mat,color,idx) in [('PLUM','BR-01','AUBERGINE GLASS','wine','01'),('IVORY','BR-02','OPAQUE WARM GLASS','fog','02'),('AMBER','BR-03','HONEY TRANSLUCENT GLASS','rust','03')]:
 def draw(c,W,H,TW,TH,name=name,sku=sku,mat=mat,color=color):
  rect(c,0,0,W,H,'paper');rect(c,12*mm,60*mm,W-24*mm,54*mm,color)
  t(c,12*mm,H-23*mm,'B R U M E',34,'Garamond','ink');t(c,12*mm,H-33*mm,'LIGHT OBJECTS / STUDIO EDITION',8,'DejaVu')
  t(c,12*mm,H-79*mm,name,38,'GaramondBold','light' if name=='PLUM' else 'ink')
  t(c,12*mm,H-115*mm,'TABLE LIGHT / CONCEPT OBJECT',8,'DejaVu')
  t(c,12*mm,H-123*mm,mat,8,'DejaVu')
  t(c,12*mm,H-134*mm,sku+'   /   REV 03',8,'DejaVu')
  t(c,12*mm,H-141*mm,'FICTIONAL PRODUCT. NOT FOR RETAIL USE.',6,'DejaVu','wine')
 makepdf('label-'+name.lower()+'-r03',100,150,draw)
# archived revisions only plum
for rev,desc in [(1,'COLORED GLASS LIGHT / EDIT 00'),(2,'AUBERGINE GLASS / EDIT 00')]:
 def draw(c,W,H,TW,TH,rev=rev,desc=desc):
  rect(c,0,0,W,H,'paper');rect(c,12*mm,60*mm,W-24*mm,54*mm,'wine');t(c,12*mm,H-23*mm,'B R U M E',34)
  t(c,12*mm,H-79*mm,'PLUM',38,'GaramondBold','light');t(c,12*mm,H-123*mm,desc,8,'DejaVu')
  t(c,12*mm,H-134*mm,f'BR-01 / REV 0{rev}',8,'DejaVu');t(c,12*mm,H-141*mm,'ARCHIVED SAMPLE / NOT RETAIL',6,'DejaVu','wine')
 makepdf(f'archive-label-plum-r0{rev}',100,150,draw,rev=str(rev))

def ad(c,W,H,TW,TH):
 photo(c,'wine-room',0,0,W,H);rect(c,0,0,W,48*mm,'ink');t(c,14*mm,H-17*mm,'B R U M E',27,'Garamond','light');t(c,14*mm,23*mm,'Light, after hours.',28,'Garamond','light');t(c,14*mm,14*mm,'LUMINOUS OBJECTS / STUDIO EDITION',8,'DejaVu','honey')
makepdf('a5-magazine-ad',148,210,ad)

def postcard(c,W,H,TW,TH):
 photo(c,'sun-room',0,0,W,H);rect(c,0,0,79*mm,H,'paper');t(c,10*mm,H-15*mm,'B R U M E',25);t(c,10*mm,H-45*mm,'An hour worth',25);t(c,10*mm,H-56*mm,'staying for.',25);t(c,10*mm,14*mm,'A CONCEPT STUDY IN LIGHT',7,'DejaVu','wine')
makepdf('a6-postcard',148,105,postcard)

def insert(c,W,H,TW,TH):
 rect(c,0,0,W,H,'paper');t(c,10*mm,H-19*mm,'B R U M E',24);t(c,10*mm,H-32*mm,'STUDIO NOTES / 01',8,'DejaVu','wine');t(c,10*mm,H-47*mm,'An object of light.',27)
 photo(c,'hand-detail',10*mm,48*mm,W-20*mm,42*mm)
 t(c,10*mm,39*mm,'DISPLAY STUDY ONLY / PRODUCT NOT MANUFACTURED',6.5,'DejaVu')
 t(c,10*mm,29*mm,'NO ELECTRICAL SAFETY CERTIFICATION OR USAGE',6,'DejaVu','wine')
 t(c,10*mm,22*mm,'INSTRUCTIONS HAVE BEEN ESTABLISHED.',6,'DejaVu','wine')
makepdf('a6-concept-insert',105,148,insert)

def sell(c,W,H,TW,TH):
 rect(c,0,0,W,H,'paper');t(c,13*mm,H-20*mm,'B R U M E',28);t(c,13*mm,H-32*mm,'THE STUDIO EDITION',9,'DejaVu','wine')
 photo(c,'collection',12*mm,114*mm,W-24*mm,116*mm);t(c,13*mm,102*mm,'ONE SILHOUETTE. THREE ATMOSPHERES.',15,'GaramondBold')
 for i,(name,sku,mat,_,__) in enumerate([('PLUM','BR-01','AUBERGINE GLASS','wine',1),('IVORY','BR-02','OPAQUE WARM GLASS','fog',2),('AMBER','BR-03','HONEY TRANSLUCENT GLASS','rust',3)]):
  y=(86-i*18)*mm;t(c,13*mm,y,name,17,'GaramondBold');t(c,78*mm,y+2*mm,sku+' / '+mat,8,'DejaVu')
 t(c,13*mm,20*mm,'ILLUSTRATIVE PRODUCT FAMILY / NO VERIFIED SPECS OR RETAIL PRICING',7,'DejaVu','wine')
makepdf('a4-product-sheet',210,297,sell)
# Combined proof PDF
writer=PdfWriter()
for p in sorted((root/'print/pdf').glob('*.pdf')):writer.append(str(p))
with open(root/'print'/'BRUME-ALL-PROOFS.pdf','wb') as f:writer.write(f)
print('Built',len(mailplans),'email HTMLs,',len(list((root/'print/pdf').glob('*.pdf'))),'PDFs')
