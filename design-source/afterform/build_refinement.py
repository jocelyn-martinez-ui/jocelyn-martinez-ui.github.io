"""AFTERFORM second-pass artwork. Run from the checkout or exported website root.
Requires reportlab, Pillow, fonttools. Writes four RGB design-proof PDFs and SVG masters.
AFTERFORM_SITE_URL controls sample-record QR links; a real public URL requires reproofing.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from fontTools.ttLib import TTFont as Font
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image
import json, os, html, base64, io
R=Path(__file__).resolve().parent
ROOT=R.parent.parent
SITE=(ROOT/'dist/afterform') if (ROOT/'dist').exists() else ROOT/'afterform'
OUT=SITE/'downloads'; AS=SITE/'assets'; EX=AS/'system'; EX.mkdir(parents=True,exist_ok=True)
M=72/25.4
C={'plum':'#38233f','red':'#bd3b2f','lilac':'#d6c6ec','paper':'#faf7f8','muted':'#6b586f','line':'#cdbfce','wash':'#ece4f3','white':'#ffffff','black':'#171319','success':'#2b614c'}
for n in ['Display','DisplayBold','Body','Medium','Bold','Mono']:pdfmetrics.registerFont(TTFont(n,str(R/'fonts'/f'{n}.ttf')))
BASE=os.environ.get('AFTERFORM_SITE_URL','https://jocelyn-design-portfolio.josie-mochi.chatgpt.site/afterform/').rstrip('/')+'/'
photo=R/'art/repair-editorial.png';denim=R/'art/denim-detail.png'
manifest={};warnings=[];current=[]
def newpdf(name):
 global current
 current=[];manifest[name]=current
 c=canvas.Canvas(str(OUT/name),pageCompression=1);c.setTitle(name.replace('-',' ').replace('.pdf',''));c.setAuthor('Jocelyn Martinez / self-directed, AI-assisted concept');return c
class P:
 def __init__(self,c,w,h,title,bg='paper'):
  self.c=c;self.w=w;self.h=h;self.info={'title':title,'width_mm':w,'height_mm':h,'text':[]};current.append(self.info);c.setPageSize((w*M,h*M));self.box(0,0,w,h,bg)
 def col(self,k):return HexColor(C.get(k,k))
 def box(self,x,y,w,h,color,outline=None):
  self.c.setFillColor(self.col(color));self.c.setStrokeColor(self.col(outline or color));self.c.setLineWidth(.5);self.c.rect(x*M,(self.h-y-h)*M,w*M,h*M,fill=1,stroke=bool(outline))
 def line(self,x,y,x2,y2,color='plum',weight=.6,dash=None):
  self.c.setStrokeColor(self.col(color));self.c.setLineWidth(weight);self.c.setDash(dash or []);self.c.line(x*M,(self.h-y)*M,x2*M,(self.h-y2)*M);self.c.setDash([])
 def text(self,x,y,s,size=12,font='Body',color='plum',width=None):
  if width:
   size=min(size,width*M/max(.1,pdfmetrics.stringWidth(s,font,size))*size)
  self.c.setFillColor(self.col(color));self.c.setFont(font,size);self.c.drawString(x*M,(self.h-y)*M,s);self.info['text'].append(s)
  if x+pdfmetrics.stringWidth(s,font,size)/M>self.w+1 or y>self.h-1:warnings.append((self.info['title'],s,x,y,size))
 def para(self,x,y,s,w,size=11,font='Body',color='plum',leading=None):
  lead=(leading or size*1.45)/M;lines=[];line=''
  for word in s.split():
   new=(line+' '+word).strip()
   if pdfmetrics.stringWidth(new,font,size)>w*M and line:lines.append(line);line=word
   else:line=new
  if line:lines.append(line)
  before=len(self.info['text'])
  for line in lines:self.text(x,y,line,size,font,color);y+=lead
  self.info['text'][before:]=[s]
  return y
 def image(self,path,x,y,w,h):
  im=Image.open(path);iw,ih=im.size;k=max(w*M/iw,h*M/ih);dw,dh=iw*k,ih*k;self.c.saveState();q=self.c.beginPath();q.rect(x*M,(self.h-y-h)*M,w*M,h*M);self.c.clipPath(q,stroke=0);self.c.drawImage(ImageReader(im),x*M+(w*M-dw)/2,(self.h-y-h)*M+(h*M-dh)/2,dw,dh,mask='auto');self.c.restoreState()
 def mark(self,x,y,size=34,color='plum'):
  self.text(x,y,'afterform',size,'DisplayBold',color)
 def qr(self,url,x,y,size=32):
  widget=qr.QrCodeWidget(url,barLevel='M');a=widget.getBounds();w=a[2]-a[0];h=a[3]-a[1];d=Drawing(size*M,size*M,transform=[size*M/w,0,0,size*M/h,0,0]);d.add(widget);self.box(x,y,size,size,'white');renderPDF.draw(d,self.c,x*M,(self.h-y-size)*M)
 def footer(self,n,label='ON KEEPING / SECOND EDITION',color='plum'):
  self.line(16,self.h-18,self.w-16,self.h-18,color,.45);self.text(16,self.h-10,label,8,'Mono',color);self.text(self.w-24,self.h-10,str(n).zfill(2),9,'Mono',color)
 def done(self):self.c.showPage()
 def arrow(self,x,y,w=16,color='plum'):
  self.line(x,y,x+w,y,color,2);self.line(x+w-5,y-5,x+w,y,color,2);self.line(x+w-5,y+5,x+w,y,color,2)
def eyebrow(p,s,color='red'):p.text(16,25,s,9,'Mono',color)
def head(p,lines,y=50,size=44,color='plum'):
 for line in lines:p.text(16,y,line,size,'Display',color,width=p.w-32);y+=size*.40
 return y
def rows(p,items,y=100,x=16,w=138,step=29,color='plum'):
 for i,(a,b) in enumerate(items):
  yy=y+i*step;p.line(x,yy-8,x+w,yy-8,'line');p.text(x,yy,a,14,'Medium',color);p.para(x,yy+9,b,w,10.5,'Body',color)

# 24-page publication. The first edition remains available as a separate artifact.
c=newpdf('AFTERFORM-On-Keeping-Second-Edition.pdf')
def book(n,title,bg='paper'):return P(c,170,240,title,bg)
p=book(1,'On keeping / cover','lilac');p.mark(16,30,39);p.text(17,44,'A STUDIO GUIDE / SECOND EDITION',9,'Mono');p.text(12,95,'On',112,'Display');p.text(12,134,'keeping.',82,'Display',width=146);p.image(photo,16,150,138,56);p.text(16,222,'THE PIECE. THE CHANGE. THE NEXT CHAPTER.',8.8,'Mono');p.done()
p=book(2,'Inside cover / an honest premise','plum');eyebrow(p,'A REPAIR BEGINS WITH A PERSON.','lilac');head(p,['Something','you reach for.'],64,47,'paper');p.para(16,116,'Not every piece has a grand story. Sometimes it is simply the shirt that fits, the jacket you borrow or the jeans you already know.',133,17,'Display','paper',22);p.line(16,173,154,173,'lilac');p.para(16,188,'This guide helps you describe a change without needing the technical name. The actual garment and a repairer determine what is possible.',132,11,'Body','paper');p.footer(2,color='lilac');p.done()
p=book(3,'Contents / a guide in four parts');eyebrow(p,'CONTENTS');head(p,['Keep the piece.','Understand the change.'],51,37)
for y,no,title,desc in [(103,'04','01 / The piece','What makes it worth keeping.'),(132,'08','02 / The choice','Finish, repair type and a clear request.'),(161,'14','03 / The agreement','Changes, questions and explicit decisions.'),(190,'18','04 / The next chapter','Records, care information and return visits.')]:
 p.line(16,y-8,154,y-8,'line');p.text(16,y,no,19,'DisplayBold','red');p.text(36,y,title,13,'Medium');p.text(36,y+8,desc,10,'Body','muted')
p.footer(3);p.done()
p=book(4,'Opening / keep the good part','red');eyebrow(p,'01 / THE PIECE','paper');head(p,['Keep','the good','part.'],72,73,'paper');p.para(18,187,'The familiar weight. The right sleeve. The way it falls. Start with what you want to keep.',128,14,'Medium','paper',20);p.footer(4,color='paper');p.done()
p=book(5,'Opening / a detail is enough');p.image(photo,0,0,170,165);p.text(16,185,'A detail is enough.',35,'Display');p.para(16,199,'A considered repair protects what matters while making the change understandable. Illustrative garment, not a documented repair result.',137,10.5);p.footer(5);p.done()
p=book(6,'Material study / a closer look','plum');p.image(denim,0,0,170,204);p.text(16,219,'A CLOSER LOOK / ILLUSTRATIVE DARNING STUDY',8.5,'Mono','paper');p.text(148,232,'06',9,'Mono','paper');p.done()
p=book(7,'Material study / what the cloth decides','lilac');eyebrow(p,'LOOK BEFORE YOU LABEL IT.','plum');head(p,['The cloth','has a say.'],59,54);p.para(16,124,'A photo can explain where the problem is. It cannot confirm the strength of the surrounding cloth, the feel of the repair or the best method.',135,17,'Display','plum',22);rows(p,[('Describe, do not diagnose.','The studio needs your observation, not an expert conclusion.'),('Keep uncertainty visible.','“Not sure” is a useful answer about fibre, method or finish.')],y=175,step=27);p.footer(7);p.done()
p=book(8,'Finish / closest practical match');eyebrow(p,'02 / THE CHOICE');head(p,['Quiet repair.'],55,45);p.para(16,77,'Let attention stay on the piece.',130,15,'Medium');p.line(16,106,154,106,'line');p.line(54,106,115,106,'plum',3);p.para(16,130,'A close colour match and familiar construction can reduce the contrast of a repair. It may still be visible, and the material may feel different.',136,12);p.text(16,177,'ASK BEFORE YOU AGREE',9,'Mono','red');p.para(16,189,'What is the closest practical match? What will still be visible? Could the finish affect how the piece falls?',135,15,'Display');p.footer(8);p.done()
p=book(9,'Finish / deliberate contrast','plum');eyebrow(p,'TWO INTENTIONS. NO PROMISED INVISIBILITY.','lilac');head(p,['New','character.'],65,62,'paper');p.line(16,123,154,123,'lilac');p.line(54,123,115,123,'lilac',4,[6,4]);p.para(16,148,'A contrasting thread, patch or fastening can make the repair part of the piece. The colour is a preference; suitability still depends on the garment.',134,12,'Body','paper');p.para(16,194,'Ask to see a sample. A beautiful contrast still needs a practical method.',134,15,'Display','lilac');p.footer(9,color='lilac');p.done()
p=book(10,'Taxonomy / useful codes','lilac');eyebrow(p,'A CODE HELPS THE STUDIO. WORDS HELP YOU.','plum');p.text(11,113,'M01',143,'DisplayBold','plum',width=145);p.text(16,139,'A hole or worn patch.',25,'Medium');p.para(16,165,'The code is an index, not a diagnosis. The description stays next to it on the screen, tag and work ticket.',134,13);p.para(16,202,'Not sure which kind? Begin with Q01: an assessment.',135,11);p.footer(10);p.done()
p=book(11,'Taxonomy / repair index');eyebrow(p,'THE REPAIR INDEX');head(p,['Start with what','you notice.'],48,37)
for i,(code,title,desc) in enumerate([('M01','A hole or worn patch','Fabric is thin or has opened up.'),('M02','An open seam','Two pieces of cloth are separating.'),('F01','A zip that will not work','The pull, teeth or slider needs attention.'),('F02','A missing button','A fastening needs a closer look.'),('A01','A length to adjust','A fitting comes before cutting.'),('Q01','Help me work it out','No technical name required.')]):
 y=94+i*20;p.line(16,y-7,154,y-7,'line');p.text(16,y,code,12,'Mono','red');p.text(38,y,title,12.5,'Medium');p.text(38,y+7,desc,9.5,'Body','muted')
p.footer(11);p.done()
p=book(12,'Request / three details');eyebrow(p,'BEFORE AN ASSESSMENT');head(p,['Three details.','A better start.'],50,42)
for y,n,title,desc in [(111,'01','Name the piece.','Use a name you will recognise: “My everyday shirt” is enough.'),(148,'02','Describe the place.','Elbow, seam, fastening or edge. Say “Not sure” when needed.'),(185,'03','Explain the intention.','Close match, visible contrast or advice before choosing.')]:
 p.text(16,y,n,25,'DisplayBold','red');p.text(38,y,title,15,'Medium');p.para(38,y+10,desc,112,11)
p.footer(12);p.done()
p=book(13,'Request / paper and screen','lilac');eyebrow(p,'BRING THE DETAILS INTO THE CONVERSATION.','plum');head(p,['A request','you can carry.'],52,43);p.box(16,105,138,89,'paper');p.mark(24,125,26);p.text(24,138,'AF-L001 / REVISION 1',10,'Mono');p.line(24,144,146,144,'line');p.text(24,157,'The everyday shirt',20,'Display');p.text(24,168,'M01 / elbow or sleeve',11,'Body');p.text(24,179,'Preference: closest practical match',10,'Body');p.para(16,207,'The prototype prints saved details. Local requests have no public QR. This brief is not permission to begin work.',136,10);p.footer(13);p.done()
p=book(14,'Agreement / requested intention');eyebrow(p,'03 / THE AGREEMENT');head(p,['You asked for…'],58,46);p.text(16,92,'A close match at the elbow.',18,'Medium');rows(p,[('Finish','Keep attention on the original garment.'),('Scope','The area you can see, before assessment.'),('Price and timing','Not confirmed by describing a repair.')],y=126,step=31);p.footer(14);p.done()
p=book(15,'Agreement / assessed proposal','lilac');eyebrow(p,'…AND THE ASSESSMENT ADDS CONTEXT.','plum');head(p,['Here is what','would change.'],58,44);rows(p,[('Finish','A small visible difference may remain.'),('Scope','A wider reinforcement may be needed.'),('Price and timing','Review the complete proposal before deciding.')],y=126,step=31);p.footer(15);p.done()
p=book(16,'Decision / a useful pause','plum');eyebrow(p,'UNCERTAINTY IS A REASON TO ASK.','lilac');head(p,['A pause','is useful.'],84,68,'paper');p.para(16,173,'A request describes the intention. A proposal explains the practical limits. The decision belongs after the comparison.',134,17,'Display','lilac',23);p.footer(16,color='lilac');p.done()
p=book(17,'Decision / three paths');eyebrow(p,'NO SILENT AGREEMENTS');head(p,['One clear','next step.'],50,43);rows(p,[('I understand the change.','Review the whole proposal, then record a decision.'),('I need to ask something.','Keep the proposal pending while the question is resolved.'),('The details changed again.','Review the new scope. An earlier approval is not carried forward.')],y=112,step=35);p.footer(17);p.done()
p=book(18,'Record / a stable reference','lilac');eyebrow(p,'04 / THE NEXT CHAPTER','plum');head(p,['Keep the','useful details.'],57,48);p.text(16,125,'AF-S01',49,'Mono');p.line(16,138,154,138);p.text(16,156,'The everyday shirt',23,'Display');p.para(16,174,'A stable reference travels with the piece. A repair code describes the type; a revision number describes a changing proposal. They are different kinds of information.',135,12);p.footer(18);p.done()
p=book(19,'Record / paper to digital');eyebrow(p,'SCAN, OR TYPE THE ID.');p.qr(BASE+'#passport/AF-S01',16,43,56);p.text(84,58,'AF-S01',19,'Mono');p.para(84,72,'The everyday shirt. An illustrative garment record.',68,12);p.line(16,115,154,115,'line');head(p,['The record stays.','The story continues.'],139,34);p.para(16,178,'The sample record opens from its printed tag or typed ID. A new repair request can begin with these garment details without changing the old record.',134,11);p.para(16,208,'Preview QR requires access to the portfolio. Repoint and scan-test before public printing.',136,8.8,'Body','muted');p.footer(19);p.done()
p=book(20,'Care / a boundary worth keeping');eyebrow(p,'INFORMATION HAS LIMITS.');head(p,['Keep the','original label.'],54,46);p.para(16,118,'The repair record adds context. It does not replace garment-specific care instructions, confirm an unknown fibre content or create new wash symbols.',135,14);rows(p,[('Known','The garment ID and the documented repair description.'),('Still to check','The original label and any repair-specific advice from the repairer.')],y=179,step=27);p.footer(20);p.done()
p=book(21,'Follow-up / something changed','paper');p.image(denim,16,20,138,93);head(p,['Notice something','different?'],139,38);p.para(16,177,'Keep the record and describe the place that needs attention. A new request starts a fresh assessment; it does not rewrite the earlier repair.',134,11.5);p.para(16,209,'Uncertainty is welcome at every stage.',134,11,'Medium','red');p.footer(21);p.done()
p=book(22,'At a glance / a useful checklist','lilac');eyebrow(p,'KEEP THIS PAGE CLOSE.','plum');head(p,['Before you agree.'],55,44)
for i,(h,b) in enumerate([('The piece','We are talking about the same garment and location.'),('The change','I understand the proposed finish and scope.'),('The commitment','Price and timing have been explained.'),('The next step','I know how to ask a question or review a revision.')]):
 y=100+i*29;p.box(16,y-4,4,4,'lilac','plum');p.text(28,y,h,14,'Medium');p.para(28,y+8,b,122,10.5)
p.footer(22);p.done()
p=book(23,'Colophon / production and evidence');eyebrow(p,'ABOUT THIS EDITION');head(p,['A considered','design proof.'],51,43);p.para(16,105,'170 × 240 mm. Twenty-four pages. Proposed saddle stitch. Six folded sheets. Pages are supplied in reading order; the printer performs imposition after paper and binding are confirmed.',135,11.5);p.para(16,145,'Proposed stock: uncoated 120 gsm text with a 200 gsm cover. Check grain, creep, gutter and colour on a physical proof. This RGB PDF is not a press-certified file.',135,11);p.para(16,179,'Concept and implementation: Jocelyn Martinez, with AI assistance. Bodoni Moda, Karla and Inconsolata are used under the SIL Open Font License. Material images are original generated illustrations.',135,10);p.para(16,210,'No operating studio, customer research, repair results or environmental savings are claimed.',135,9,'Body','muted');p.footer(23);p.done()
p=book(24,'Back cover / another chapter','plum');p.mark(16,34,40,'lilac');head(p,['Keep the','clothes.'],91,64,'paper');head(p,['Change','the ending.'],165,54,'lilac');p.text(16,222,'REPAIR / REWEAR / RECORD',10,'Mono','lilac');p.done();c.save()

# Brand manual, concise rules with visible applications; 230 x 180 mm, 16 pages.
c=newpdf('AFTERFORM-Identity-Standards.pdf')
def manual(n,title,bg='paper'):
 p=P(c,230,180,title,bg)
 if n not in [1,16]:p.footer(n,'AFTERFORM / IDENTITY STANDARDS', 'lilac' if bg=='plum' else 'plum')
 return p
p=manual(1,'Identity standards / cover','plum');p.mark(16,40,66,'lilac');p.text(18,58,'SECOND IMPRESSION / IDENTITY STANDARDS / 02',10,'Mono','paper');head(p,['Keep the character.','Clarify the change.'],107,44,'paper');p.text(18,168,'A SYSTEM FOR PRINT, PRODUCT AND THE STUDIO.',9,'Mono','lilac');p.done()
p=manual(2,'Concept / design grammar');eyebrow(p,'01 / THE IDEA');head(p,['One piece. One change.','One clear next step.'],51,38);p.para(16,96,'A named garment anchors the story. One visible intervention expresses the repair. A practical information rail carries the ID, repair type and next action. Quiet space separates the emotional invitation from operational detail.',193,13);p.line(16,137,213,137);p.text(16,148,'NAME THE PIECE',10,'Mono');p.text(90,148,'SHOW THE CHANGE',10,'Mono','red');p.text(166,148,'KEEP THE RECORD',10,'Mono');p.done()
p=manual(3,'Identity / useful configurations');eyebrow(p,'02 / RESPONSIVE LOGO ARCHITECTURE');p.mark(16,68,74);p.text(17,84,'PRIMARY WORDMARK / EDITORIAL & ENTRANCE',9,'Mono');p.mark(16,121,43);p.text(17,135,'REPAIR & REWEAR',10,'Mono');p.box(165,100,40,40,'plum');p.text(173,130,'af',43,'DisplayBold','lilac');p.text(151,152,'AVATAR / COMPACT',9,'Mono');p.done()
p=manual(4,'Identity / clear space');eyebrow(p,'03 / CLEAR SPACE IS PART OF THE MARK')
ff=Font(R/'fonts/DisplayBold.ttf');gs=ff.getGlyphSet();cm=ff.getBestCmap();upm=ff['head'].unitsPerEm
def wordbounds(size,x,y,track=0):
 pen=BoundsPen(gs);at=x;k=size/upm
 for ch in 'afterform':
  gn=cm[ord(ch)];gs[gn].draw(TransformPen(pen,(k,0,0,-k,at,y)));at+=(gs[gn].width+track)*k
 return pen.bounds
xp=BoundsPen(gs);gs[cm[ord('x')]].draw(xp);xh=xp.bounds[3]-xp.bounds[1]
bx1,by1,bx2,by2=wordbounds(79/M,40,99);pad=(79/M)*xh/upm/2
p.box(bx1-pad,by1-pad,bx2-bx1+2*pad,by2-by1+2*pad,'lilac');p.mark(40,99,79)
for xx in [bx1,bx2]:p.line(xx,by1-pad-4,xx,by2+pad+4,'red',.5,[2,2])
for yy in [by1,by2]:p.line(bx1-pad-4,yy,bx2+pad+4,yy,'red',.5,[2,2])
p.text(16,137,'x = lowercase height. Minimum clear space = 0.5x.',12,'Medium');p.para(16,149,'Measure from the visible outline, not the exported SVG bounds. Keep rules, copy and die cuts outside that space.',195,10);p.done()
p=manual(5,'Identity / optical adaptation');eyebrow(p,'04 / DIFFERENT SIZES, DIFFERENT INFORMATION');p.mark(16,63,65);p.text(16,81,'WORDMARK / 144 px digital or 35 mm print minimum target',9,'Mono');p.mark(16,122,35);p.text(16,139,'SERVICE LOCKUP / 220 px or 50 mm',9,'Mono');p.box(165,104,14,14,'plum');p.box(167,106,4,10,'lilac');p.box(173,106,4,10,'lilac');p.line(170,110,174,110,'lilac',2);p.line(170,114,174,114,'lilac',2);p.text(153,137,'16 / 24 / 32 px',9,'Mono');p.para(153,146,'Join symbol replaces fine letterforms.',58,9);p.done()
p=manual(6,'Identity / correct and incorrect use');eyebrow(p,'05 / PROTECT THE DRAWN PROPORTIONS');p.box(16,44,95,54,'plum');p.mark(24,80,43,'lilac');p.text(16,113,'USE / one colour, clear contrast',11,'Medium');p.box(124,44,90,54,'lilac');p.mark(132,80,39,'red');p.line(130,48,206,94,'red',1.5);p.text(124,113,'AVOID / small red-on-lilac mark',10.5,'Medium');p.para(16,136,'Use supplied outlines. Never distort width, add an outline or shadow, fill letters with a photo, or rearrange the word into a new symbol. The wordmark is a licensed type-based design, not custom lettering.',193,11);p.done()
p=manual(7,'Colour / behaviour');eyebrow(p,'06 / COLOUR HAS A JOB');
for x,col,fg,title,sub in [(16,'plum','paper','Dominant','Plum + lilac'),(66,'paper','plum','Quiet','Poplin + plum'),(116,'red','paper','Campaign','Vermilion + poplin'),(166,'lilac','plum','Supporting','Lilac + plum')]:
 p.box(x,47,48,78,col,'line');p.text(x+5,102,title,12,'Medium',fg,width=38);p.text(x+5,115,sub,8.5,'Mono',fg,width=38)
p.para(16,142,'Use vermilion for one emphasis. It is not the only status signal. Avoid normal-size vermilion copy on lilac (3.43:1). Keep essential reading on the quiet combination (13.32:1).',193,11);p.done()
p=manual(8,'Typography / five useful scales');eyebrow(p,'07 / TYPE CHANGES WITH THE TASK');p.text(16,66,'Another chapter.',59,'Display',width=197);p.text(16,91,'Display / Bodoni Moda, optical sizing on',10,'Mono');p.text(16,112,'Describe the place that needs attention.',22,'Medium');p.text(16,129,'Body: Karla 17/27 px. Label: Karla 14/20 px. Code: Inconsolata 13/18 px.',10.5);p.text(16,145,'Print body: 11/16 pt. Essential tag text: 9/12 pt minimum target.',10.5);p.done()
p=manual(9,'Graphic language / not decoration');eyebrow(p,'08 / THE JOIN AND THE RECORD');p.line(16,59,102,59,'plum',1);p.line(47,59,77,59,'plum',3);p.text(16,78,'Closest practical match',12,'Medium');p.line(124,59,210,59,'plum',1);p.line(152,59,183,59,'red',3,[5,3]);p.text(124,78,'Visible contrast',12,'Medium');p.box(16,103,198,32,'lilac');p.text(24,124,'AF-S01',20,'Mono');p.text(91,124,'M01 / WORN AREA',11,'Mono');p.text(169,124,'REV 01',11,'Mono');p.para(16,148,'Identity, classification and version are separate. Never use the repair code as a garment ID.',193,11);p.done()
p=manual(10,'Labels / anatomy');eyebrow(p,'09 / THREE ZONES. ONE READING ORDER.');
for y,a,b in [(54,'01 / OBJECT','Stable ID and recognisable garment name.'),(87,'02 / ATTENTION','Plain-language problem, then the repair code.'),(120,'03 / NEXT ACTION','Review, ask, approve a version, or collect.')]:
 p.box(16,y-10,68,24,'lilac');p.text(22,y+5,a,11,'Mono');p.para(99,y,b,111,13)
p.text(16,150,'Add a status word, never colour alone. Keep personal data off exterior labels.',10.5);p.done()
p=manual(11,'Grid / shared rhythm, different layouts');eyebrow(p,'10 / STRUCTURE WITHOUT MONOTONY');
for x,w,label,n in [(16,57,'PUBLICATION / 2',2),(85,60,'SCREEN / 6',6),(157,57,'LABEL / 1',1)]:
 p.box(x,46,w,79,'wash');gap=3;col=(w-12-gap*(n-1))/n
 for i in range(n):p.box(x+6+i*(col+gap),52,col,67,'lilac')
 p.text(x,139,label,9,'Mono')
p.text(16,154,'4 px UI base. 6 mm editorial rhythm. Equal margins are a choice, not a law.',10.5);p.done()
p=manual(12,'Image system / material before spectacle');eyebrow(p,'11 / SHOW THE PIECE, THEN THE DETAIL');p.image(photo,16,42,86,94);p.image(denim,110,42,104,61);p.para(110,115,'Soft side light. Realistic material scale. One legible intervention. No invented hands, tools or documentary claims.',104,11);p.text(16,152,'Generated illustration is labelled. Exact copy lives in authored flat artwork.',10.5);p.done()
p=manual(13,'Interface / status grammar');eyebrow(p,'12 / A STATUS SHOULD SAY WHAT HAPPENS NEXT');
for y,num,a,b,col in [(55,'01','Needs review','Read the proposed change.','plum'),(82,'02','Scope changed','A new revision needs a fresh decision.','red'),(109,'03','Agreement recorded','Show the version; allow reversal in the prototype.','plum')]:
 p.text(16,y,num,22,'Mono',col);p.text(38,y,a,15,'Medium',col);p.para(120,y,b,94,11)
p.text(16,149,'A digital example approval never authorises a real-world repair.',11,'Medium');p.done()
p=manual(14,'Motion / explicit and quiet','plum');eyebrow(p,'13 / MOTION FOLLOWS A CHANGE.','lilac');head(p,['Join.','Then settle.'],67,49,'paper');p.para(114,55,'160 ms: colour and border feedback.\n280 ms: a joining-rule reveal.\nNo delay before form feedback.\nNo automatic cinematic entrance.',98,13,'Body','paper');p.para(114,112,'Brand demonstration: user-triggered, one pass, then a still frame. Reduced motion displays the result immediately.',98,11,'Body','lilac');p.done()
p=manual(15,'Production / practical boundaries');eyebrow(p,'14 / PROOF BEFORE PRODUCTION');head(p,['Beautiful is also','legible and usable.'],53,39);p.para(16,100,'PDFs use RGB colours with embedded type. Confirm the printer, substrate and profile before separation. Do not invent a Pantone match. Supply 3 mm bleed when required; keep essential text 5 mm from trim and holes.',193,11.5);p.para(16,135,'Print tags at actual size. Test glare, reading distance, hole placement and QR scanning. Packaging nets are dimensioned prototypes, not supplier-approved cutting dies.',193,11);p.done()
p=manual(16,'Toolkit / use the system','lilac');p.mark(16,41,65);head(p,['A shared language.','Many useful forms.'],89,43);p.text(17,143,'SVG MASTERS / PDF PROOFS / TOKENS / WORKING HTML',10,'Mono');p.text(17,165,'SELF-DIRECTED CONCEPT / JOCELYN MARTINEZ / EDITION 02',9,'Mono');p.done();c.save()

# Practical service kit. Four status labels are examples, not certification stamps.
c=newpdf('AFTERFORM-Service-Paper-System.pdf')
p=P(c,148,210,'Intake brief / A5');p.mark(12,25,33);p.text(12,38,'REPAIR BRIEF / AF-L001 / REVISION 1',9,'Mono');head(p,['The everyday','shirt.'],64,34);p.text(16,100,'M01 / WORN ELBOW',12,'Mono','red');rows(p,[('The piece','Shirt / cotton or linen, not independently checked.'),('The intention','Closest practical match; discuss any visible change.'),('For the assessment','Check cloth strength and confirm the final method.')],y=120,x=16,w=116,step=25);p.para(16,188,'Local example. A description is not permission to begin work.',116,9);p.done()
p=P(c,148,210,'Proposal comparison / A5');p.mark(12,25,33);p.text(12,38,'ASSESSMENT / AF-L001 / REVISION 1',9,'Mono');p.text(12,59,'What would change?',28,'Display');p.box(12,70,124,43,'wash');p.text(19,83,'REQUESTED',9,'Mono');p.para(19,94,'A close match at the elbow.',110,12,'Medium');p.box(12,119,124,52,'lilac');p.text(19,132,'EXAMPLE PROPOSED APPROACH',8.8,'Mono');p.para(19,143,'Reinforce a wider area. A small visible difference may remain. Illustrative price: $35 USD. Timing is not confirmed.',109,11);p.para(12,184,'Next action: review or ask a question. This sample does not record a real agreement.',124,10);p.done()
p=P(c,100,150,'Work ticket / 100 x 150 mm','paper');p.mark(8,21,28);p.text(8,35,'WORK TICKET / SAMPLE',9,'Mono');p.text(8,53,'AF-S01',25,'Mono');p.line(8,62,92,62);p.text(8,76,'M01 / worn area',13,'Medium');p.para(8,88,'The everyday shirt. Elbow reinforcement. Vermilion visible patch.',84,11);p.text(8,119,'MATCH BEFORE HANDOVER',9,'Mono','red');p.para(8,130,'Check the garment ID against the record. Retain the original care label.',84,9);p.done()
p=P(c,72,115,'Object tag / front','lilac');p.c.setStrokeColor(HexColor(C['plum']));p.c.circle(36*M,(115-7)*M,2*M,stroke=1,fill=0);p.mark(7,27,30);p.text(7,42,'AF-S01',18,'Mono');p.line(7,50,65,50);p.text(7,70,'M01',37,'DisplayBold');p.para(7,82,'The everyday shirt',58,12,'Medium');p.text(7,100,'Elbow / visible patch',9,'Body');p.text(7,110,'SAMPLE RECORD',8,'Mono');p.done()
p=P(c,72,115,'Object tag / reverse');p.text(7,22,'KEEP THE RECORD.',11,'Mono');p.qr(BASE+'#passport/AF-S01',15,30,42);p.text(7,85,'AF-S01',18,'Mono');p.para(7,96,'Scan or type the ID. Keep the original care label.',58,9);p.done()
for num,title,detail,bg,fg in [('01','Needs review','Read scope, finish and price.','paper','plum'),('02','Scope changed','Review the revised proposal.','paper','red'),('03','Agreement recorded','Match the approved revision.','lilac','plum'),('04','Ready to collect','Match the garment and record.','plum','paper')]:
 p=P(c,90,65,'Workflow label / '+title,bg);p.text(6,11,num+' / '+title.upper(),9,'Mono',fg,width=78);p.line(6,16,84,16,fg);p.text(6,27,'AF-S01 / M01',14,'Mono',fg);p.text(6,39,'The everyday shirt',12,'Medium',fg);p.text(6,51,detail,9,'Body',fg,width=78);p.text(6,60,'ILLUSTRATIVE WORKFLOW / REV 01',7.7,'Mono',fg);p.done()
p=P(c,50,50,'Envelope seal / 50 x 50 mm','plum');p.text(6,14,'RECORD',20,'Medium','paper');p.text(6,25,'INSIDE',20,'Medium','paper');p.line(6,32,44,32,'lilac');p.text(6,42,'KEEP WITH THE PIECE',7.5,'Mono','lilac',width=38);p.done()
p=P(c,164,151,'Spare fastening envelope / proposed net');p.text(12,12,'SPARE FASTENING / 60 × 80 mm FINISHED',9,'Mono');x,y=12,36;p.box(x,y,10,80,'wash');p.box(x+10,y,60,80,'lilac');p.box(x+70,y,60,80,'paper');p.box(x+10,y-20,60,20,'lilac');p.box(x+10,y+80,120,15,'lilac');p.mark(x+16,y+18,25);p.text(x+16,y+34,'AF-S03',14,'Mono');p.para(x+16,y+49,'Spare fastening',47,16,'Display');p.text(x+16,y+69,'KEEP WITH THE JACKET',7.5,'Mono',width=47);p.text(x+77,y+15,'A USEFUL EXTRA.',9,'Mono');p.para(x+77,y+30,'Store a spare with the garment record. Ask the studio before fitting an unknown replacement.',45,10);p.text(x+77,y+71,'SAMPLE / NOT A TOY',7.5,'Mono',width=46)
# One continuous boundary with a 20 mm closing flap, 10 mm side glue tab and 15 mm bottom flap.
pts=[(x,y),(x+10,y),(x+10,y-20),(x+70,y-20),(x+70,y),(x+130,y),(x+130,y+95),(x+10,y+95),(x+10,y+80),(x,y+80),(x,y)]
for a,b in zip(pts,pts[1:]):p.line(*a,*b,'red',.55)
for off in [10,70]:p.line(x+off,y,x+off,y+80,'red',.55,[3,3])
p.line(x+10,y,x+70,y,'red',.55,[3,3]);p.line(x+10,y+80,x+130,y+80,'red',.55,[3,3]);p.text(12,141,'RED: TRIM / DASH: FOLD / 10 mm GLUE TAB. FIT-TEST FIRST.',8,'Mono',width=140);p.done()
p=P(c,105,148,'Follow-up card / A6','lilac');p.mark(10,23,32);p.text(10,45,'Keep the',38,'Display');p.text(10,61,'conversation.',31,'Display',width=85);p.para(10,82,'Notice a loose edge or a change in the finish? Keep the garment record and describe the place that needs attention.',85,12);p.line(10,118,95,118);p.text(10,131,'START WITH THE RECORD ID',8.5,'Mono');p.text(10,141,'SAMPLE / NO LIVE REPAIR SERVICE',8,'Mono');p.done();c.save()

# Environmental hierarchy. Dimensioned design studies, not a claim of installed signs.
c=newpdf('AFTERFORM-Environmental-Communication.pdf')
p=P(c,600,900,'Studio window invitation / 600 x 900 mm','plum');p.mark(45,96,126,'lilac');p.text(48,145,'GARMENT REPAIR & REWEAR',31,'Mono','paper');p.text(35,337,'Good',230,'Display','paper');p.text(35,445,'clothes.',230,'Display','paper');p.text(45,597,'Another',169,'Display','lilac');p.text(45,681,'chapter.',169,'Display','lilac');p.line(48,734,552,734,'lilac',2);p.text(48,800,'Start with what needs attention.',42,'Medium','paper',width=504);p.text(48,865,'ILLUSTRATIVE STUDIO / NO REAL ADDRESS OR HOURS',15,'Mono','lilac');p.done()
p=P(c,500,400,'Studio directory / 500 x 400 mm');p.mark(32,57,85);p.text(32,91,'START AT THE STUDIO DESK',23,'Mono');
for y,num,txt in [(161,'01','Assessments'),(249,'02','Proposal review'),(337,'03','Collections')]:
 p.line(32,y-39,468,y-39,'line',1);p.text(32,y,num,48,'Mono','red');p.text(101,y,txt,53,'Medium',width=270);p.arrow(414,y-10,38)
p.text(32,384,'DIRECTION STUDY / ARROWS REQUIRE A REAL SITE PLAN',13,'Mono','muted');p.done()
p=P(c,210,148,'Proposal desk / A5 landscape','lilac');p.text(16,26,'02 / PROPOSAL REVIEW',12,'Mono');p.text(16,62,'Questions welcome.',38,'Display',width=178);p.para(16,86,'A change is a conversation. Read the scope, finish and price together before deciding.',178,16);p.text(16,137,'ILLUSTRATIVE COUNTER SIGN',9,'Mono');p.done()
p=P(c,400,200,'Collection point / 400 x 200 mm','plum');p.text(28,41,'03 / COLLECTIONS',21,'Mono','lilac');p.text(28,102,'Your piece.',87,'Medium','paper');p.text(28,145,'Its next chapter.',64,'Display','lilac');p.text(28,185,'MATCH THE ID. KEEP THE RECORD.',19,'Mono','paper');p.done();c.save()

# Portable vector masters: outlined type, intentionally no decorative raster scenes.
F={n:Font(R/'fonts'/f'{n}.ttf') for n in ['Display','DisplayBold','Body','Medium','Mono']}
def st(s,x,y,size,font='Body',color='plum',tracking=0):
 f=F[font];g=f.getGlyphSet();cm=f.getBestCmap();k=size/f['head'].unitsPerEm;pen=SVGPathPen(g)
 for ch in s:
  gn=cm.get(ord(ch),'.notdef');g[gn].draw(TransformPen(pen,(k,0,0,-k,x,y)));x+=(g[gn].width+tracking)*k
 return f'<path fill="{C.get(color,color)}" d="{pen.getCommands()}"/>'
def rect(x,y,w,h,col):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.get(col,col)}"/>'
def line(x,y,w,col='plum',h=2):return rect(x,y,w,h,col)
def img(n,x,y,w,h):
 buf=io.BytesIO();Image.open(AS/(n+'.webp')).convert('RGB').save(buf,format='JPEG',quality=94);data=base64.b64encode(buf.getvalue()).decode();return f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" xlink:href="data:image/jpeg;base64,{data}"/>'
def svg(name,w,h,parts,title):(EX/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" role="img"><title>{html.escape(title)}</title>'+''.join(parts)+'</svg>')
svg('lockup-horizontal',970,230,[st('afterform',16,132,163,'DisplayBold',tracking=-16),line(18,164,900,'plum',1.5),st('REPAIR & REWEAR',20,213,29,'Mono')],'Afterform service lockup')
svg('lockup-stacked',650,320,[st('afterform',20,153,133,'DisplayBold',tracking=-16),st('REPAIR',24,238,45,'Mono'),st('& REWEAR',24,290,45,'Mono')],'Afterform stacked lockup')
svg('avatar',160,160,[rect(0,0,160,160,'plum'),st('af',26,121,116,'DisplayBold','lilac',-16)],'Afterform compact avatar')
for name,bg,fg in [('micro-mark','plum','lilac'),('micro-mono','white','black')]:
 svg(name,32,32,[rect(0,0,32,32,bg),rect(6,6,7,20,fg),rect(19,6,7,20,fg),rect(12,11,8,3,fg),rect(12,18,8,3,fg)],'Afterform joining symbol')
bx1,by1,bx2,by2=wordbounds(160,155,246,-16);pad=160*xh/upm/2
parts=[rect(0,0,1100,410,'paper'),rect(bx1-pad,by1-pad,bx2-bx1+2*pad,by2-by1+2*pad,'lilac'),st('afterform',155,246,160,'DisplayBold',tracking=-16)]
for xx in [bx1,bx2]:parts.append(rect(xx,by1-pad-12,1,by2-by1+2*pad+24,'red'))
for yy in [by1,by2]:parts.append(line(bx1-pad-12,yy,bx2-bx1+2*pad+24,'red',1))
parts.append(st('CLEAR SPACE = HALF THE LOWERCASE HEIGHT',103,376,24,'Mono'))
svg('clear-space',1100,410,parts,'Wordmark clear-space specimen measured from the visible glyph outline')
svg('brand-system-board',1600,1100,[rect(0,0,1600,1100,'paper'),rect(0,0,1020,460,'plum'),st('afterform',64,212,190,'DisplayBold','lilac',-16),st('KEEP THE CHARACTER.',70,302,38,'Mono','paper'),st('CLARIFY THE CHANGE.',70,358,38,'Mono','paper'),rect(1020,0,580,460,'lilac'),st('af',1160,320,300,'DisplayBold','plum',-16),st('AF-S01',65,612,104,'Mono'),st('M01 / WORN AREA',69,683,34,'Mono','red'),st('The everyday shirt',66,778,69,'Display'),line(65,821,700),st('OBJECT → ATTENTION → NEXT ACTION',67,894,30,'Mono'),rect(910,525,625,340,'lilac'),st('01 / NEEDS REVIEW',950,608,34,'Mono'),st('One clear',949,717,74,'Display'),st('next step.',949,796,74,'Display'),line(950,645,542,'plum',2),rect(0,995,530,105,'plum'),rect(530,995,530,105,'red'),rect(1060,995,540,105,'lilac')],'AFTERFORM identity system: wordmark, compact signature, garment index, action label and colour roles')
# Role-specific campaign formats. Every text element is real outlined typography.
svg('social-announcement',1080,1350,[rect(0,0,1080,1350,'plum'),st('afterform',80,155,112,'DisplayBold','lilac',-16),st('A STUDIO FOR THE CLOTHES YOU KEEP',84,228,25,'Mono','paper'),st('Another',73,472,159,'Display','paper'),st('chapter',73,628,159,'Display','paper'),st('starts here.',77,786,132,'Display','lilac'),line(84,914,912,'lilac'),st('Describe the piece.',84,1021,46,'Medium','paper'),st('Explore the finish. Decide together.',84,1097,37,'Body','paper'),st('SELF-DIRECTED STUDIO CONCEPT',84,1270,24,'Mono','lilac')],'Announcement: another chapter starts here')
svg('social-editorial',1080,1350,[rect(0,0,1080,1350,'paper'),img('denim-detail',0,0,1080,820),rect(0,820,1080,530,'paper'),st('01 / THE MATERIAL HAS A SAY',80,909,25,'Mono','red'),st('Look closer.',75,1059,121,'Display'),st('Describe what you notice.',80,1155,37,'Medium'),st('The method follows an assessment.',80,1220,33),st('AFTERFORM / ILLUSTRATIVE MATERIAL STUDY',80,1290,21,'Mono')],'Editorial campaign: the material has a say')
svg('social-information',1080,1350,[rect(0,0,1080,1350,'lilac'),st('02 / A CLEARER CONVERSATION',82,111,26,'Mono'),st('Three things',78,292,106,'Display'),st('to bring.',78,412,124,'Display'),line(84,488,912),st('01',84,610,43,'Mono','red'),st('The piece.',230,610,61,'Medium'),st('A name you will recognise.',231,676,33),st('02',84,816,43,'Mono','red'),st('The place.',230,816,61,'Medium'),st('Where does it need attention?',231,882,33),st('03',84,1022,43,'Mono','red'),st('The intention.',230,1022,61,'Medium'),st('A close match, contrast or advice.',231,1088,32),st('afterform',82,1271,88,'DisplayBold',tracking=-16)],'Information carousel: piece, place and intention')
svg('story-guide',1080,1920,[rect(0,0,1080,1920,'plum'),st('afterform',82,256,111,'DisplayBold','lilac',-16),st('THE NEXT CHAPTER',87,356,29,'Mono','paper'),img('repair-editorial',84,433,912,762),st('Keep the',78,1360,119,'Display','paper'),st('good part.',78,1485,119,'Display','lilac'),st('Begin with what needs attention.',86,1591,36,'Body','paper'),line(84,1660,912,'lilac'),st('EXPLORE THE REPAIR DESK',87,1719,29,'Mono','paper')],'Story format: keep the good part, with top and bottom interface safe areas')
svg('reel-cover',1080,1920,[rect(0,0,1080,1920,'lilac'),img('denim-detail',0,0,1080,1920),rect(74,620,932,688,'plum'),st('A CLOSER LOOK',118,713,32,'Mono','lilac'),st('The detail',112,874,122,'Display','paper'),st('that stays.',112,1000,122,'Display','paper'),st('afterform',118,1202,85,'DisplayBold','lilac',-16)],'Reel cover: central title remains inside the feed crop')
svg('return-reminder',1080,1350,[rect(0,0,1080,1350,'paper'),st('afterform',84,153,111,'DisplayBold',tracking=-16),st('KEEP THE USEFUL DETAILS',87,241,26,'Mono'),st('AF-S01',78,477,176,'Mono'),line(84,540,912),st('The piece.',80,710,126,'Display'),st('The record.',80,849,126,'Display','red'),st('The next chapter.',80,984,93,'Display'),st('Use the ID when you return.',84,1150,39,'Medium'),st('ILLUSTRATIVE GARMENT RECORD / M01',84,1270,25,'Mono')],'Follow-up campaign: a stable garment ID connects the next visit')
# Four useful additional pictograms; retain the existing six action icons.
icons={'print':'M6 8V3h12v5M6 17H3V8h18v9h-3M6 14h12v7H6zM17 11h1','label':'M3 3h8l10 10-8 8L3 11zM7 7h.1','revise':'M4 10a8 8 0 0 1 14-5l3 3M21 3v5h-5M20 14a8 8 0 0 1-14 5l-3-3M3 21v-5h5','piece':'M8 3l4 2 4-2 6 5-4 5-2-2v10H8V11l-2 2-4-5z'}
for name,path in icons.items():
 (AS/'icons'/f'{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{C["plum"]}" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><title>{name}</title><path d="{path}"/></svg>')
tokens={'color':C,'type':{'display':'Bodoni Moda','body':'Karla','code':'Inconsolata'},'spacing_px':[4,8,12,16,24,32,48,64,96],'radius_px':0,'border_px':1,'focus_px':3,'motion_ms':{'feedback':160,'join':280},'label_zones':['object','attention','next action'],'repair_codes':['M01','M02','F01','F02','A01','Q01'],'rules':{'logo_minimum_px':144,'logo_clear_space':'0.5 × lowercase height','essential_label_text_pt':9,'category_color':'Codes and words carry category meaning; do not introduce colour-only categories.'}}
(EX/'tokens.json').write_text(json.dumps(tokens,indent=2));(R/'refinement-artwork.json').write_text(json.dumps(manifest,indent=2));(EX/'publication-text.json').write_text(json.dumps(manifest['AFTERFORM-On-Keeping-Second-Edition.pdf'],indent=2))
assert not warnings,warnings
print(json.dumps({'pdfs':{k:len(v) for k,v in manifest.items()},'svg_masters':len(list(EX.glob('*.svg'))),'overflow_warnings':warnings},indent=2))
