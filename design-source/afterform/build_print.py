from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from fontTools.ttLib import TTFont as FTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image
import json, math, html, os
ROOT=Path(__file__).resolve().parent; SITE=ROOT.parent.parent/'afterform'; OUT=SITE/'downloads'; AS=SITE/'assets'; OUT.mkdir(exist_ok=True)
for n in ['Display','DisplayBold','Body','Medium','Bold','Mono']:pdfmetrics.registerFont(TTFont(n,str(ROOT/'fonts'/f'{n}.ttf')))
M=72/25.4
C={'plum':'#38233f','red':'#bd3b2f','lilac':'#d6c6ec','paper':'#faf7f8','muted':'#6b586f','line':'#cdbfce','wash':'#ece4f3','white':'#ffffff'}
class Page:
 def __init__(self,c,w,h,bg='paper'):self.c=c;self.w=w;self.h=h;c.setPageSize((w*M,h*M));self.box(0,0,w,h,bg)
 def col(self,k):return HexColor(C.get(k,k))
 def box(self,x,y,w,h,col,stroke=None):
  self.c.setFillColor(self.col(col)); self.c.setStrokeColor(self.col(stroke or col));self.c.rect(x*M,(self.h-y-h)*M,w*M,h*M,fill=1,stroke=bool(stroke))
 def line(self,x,y,x2,y2,col='plum',width=.6,dash=None):
  self.c.setStrokeColor(self.col(col));self.c.setLineWidth(width);self.c.setDash(dash or []);self.c.line(x*M,(self.h-y)*M,x2*M,(self.h-y2)*M);self.c.setDash([])
 def t(self,x,y,s,size=12,font='Body',col='plum'):
  self.c.setFillColor(self.col(col));self.c.setFont(font,size);self.c.drawString(x*M,(self.h-y)*M,s)
 def p(self,x,y,s,w,size=12,font='Body',col='plum',leading=None):
  leading=leading or size*1.45;words=s.split();lines=[];line=''
  for word in words:
   test=(line+' '+word).strip()
   if pdfmetrics.stringWidth(test,font,size)>w*M and line:lines.append(line);line=word
   else:line=test
  if line:lines.append(line)
  for l in lines:self.t(x,y,l,size,font,col);y+=leading/M
  return y
 def image(self,path,x,y,w,h):
  im=Image.open(path);iw,ih=im.size;scale=max(w*M/iw,h*M/ih);dw,dh=iw*scale,ih*scale;self.c.saveState();q=self.c.beginPath();q.rect(x*M,(self.h-y-h)*M,w*M,h*M);self.c.clipPath(q,stroke=0);self.c.drawImage(ImageReader(im),x*M+(w*M-dw)/2,(self.h-y-h)*M+(h*M-dh)/2,dw,dh,mask='auto');self.c.restoreState()
 def qr(self,url,x,y,size=26):
  widget=qr.QrCodeWidget(url,barLevel='M');bounds=widget.getBounds();w=bounds[2]-bounds[0];h=bounds[3]-bounds[1];d=Drawing(size*M,size*M,transform=[size*M/w,0,0,size*M/h,0,0]);d.add(widget);self.box(x,y,size,size,'white');renderPDF.draw(d,self.c,x*M,(self.h-y-size)*M)
 def mark(self,x,y,size=34,col='plum',lockup=False):
  self.t(x,y,'afterform',size,'DisplayBold',col)
  if lockup:self.t(x+.5,y+6,'REPAIR & REWEAR',7.5,'Mono',col)
 def foot(self,n,label='ON KEEPING / THE STUDIO GUIDE',col='plum'):
  self.line(16,222,154,222,col,.5);self.t(16,229,label,8,'Mono',col);self.t(147,229,f'{n:02}',9,'Mono',col)
 def arrow(self,x,y,length=18,col='plum',width=2):
  self.line(x,y,x+length,y,col,width);self.line(x+length-6,y-6,x+length,y,col,width);self.line(x+length-6,y+6,x+length,y,col,width)
 def done(self):self.c.showPage()
def pdf(name):
 c=canvas.Canvas(str(OUT/name),pageCompression=1);c.setAuthor('Jocelyn Martinez · self-directed portfolio concept');c.setTitle(name.replace('-',' ').removesuffix('.pdf'));return c
photo=ROOT/'art/repair-editorial.png';denim=ROOT/'art/denim-detail.png'
base=os.environ.get('AFTERFORM_SITE_URL','https://jocelyn-design-portfolio.josie-mochi.chatgpt.site/afterform/').rstrip('/')+'/'
book=[]
def bookpage(n,bg='paper'):
 p=Page(c,170,240,bg);book.append({'page':n,'background':bg});return p
c=pdf('AFTERFORM-On-Keeping-Studio-Guide.pdf')
p=bookpage(1,'lilac');p.mark(16,28,38);p.t(17,43,'A STUDIO GUIDE / NO. 01',9,'Mono');p.t(15,83,'On',91,'Display');p.t(15,117,'keeping.',87,'Display');p.image(photo,16,133,138,72);p.t(17,219,'GOOD CLOTHES. ANOTHER CHAPTER.',10,'Mono');p.t(17,231,'A self-directed service concept',8,'Body');p.done()
p=bookpage(2);p.t(16,25,'INSIDE',10,'Mono','red');p.t(16,52,'A little more',42,'Display');p.t(16,69,'life in a piece.',42,'Display');p.p(16,88,'This guide begins with what you notice, not what you know about sewing. It helps you describe a repair, choose a direction and keep the useful details afterward.',130,12)
for i,(n,title,sub) in enumerate([('03','The piece you keep','Start with the garment, not the fault.'),('04','Two honest finishes','A close match or a visible detail.'),('06','Where to begin','A plain-language repair index.'),('08','The second conversation','Review a proposal before agreeing.'),('10','A record worth keeping','Paper and digital, side by side.')]):
 y=133+i*16;p.line(16,y-5,154,y-5,'line');p.t(16,y+1,n,11,'Mono','red');p.t(32,y+1,title,13,'Medium');p.t(32,y+6,sub,9,'Body','muted')
p.foot(2);p.done()
p=bookpage(3,'red');p.t(16,28,'WHY REPAIR?',10,'Mono','paper');p.t(14,63,'Keep',80,'Display','paper');p.t(14,94,'the good',70,'Display','paper');p.t(14,125,'part.',92,'Display','paper');p.p(18,157,'The right sleeve. The familiar weight. The way it falls. A garment can be worth keeping for reasons a price tag cannot explain.',128,18,'Medium','paper',24);p.p(18,204,'We start with that reason. Then we work out what the cloth can support.',125,11,'Body','paper');p.foot(3,col='paper');p.done()
p=bookpage(4);p.t(16,25,'01 / CHOOSE A DIRECTION',9,'Mono','red');p.t(16,49,'Quiet repair.',43,'Display');p.p(16,66,'A finish that belongs to the garment as it is.',130,14,'Medium');p.line(16,85,154,85,'plum',1);p.line(16,90,154,90,'line',.5);p.line(50,85,120,85,'plum',3);p.p(16,110,'A close colour match, familiar stitching and a considered placement can keep attention on the piece. A repair may still be visible. “Blends in” is an intention, not an invisible-repair promise.',130,12)
p.t(16,158,'ASK THE STUDIO',9,'Mono','red');p.p(16,171,'What is the closest practical match? Could the repair change the drape or feel? What will still be visible?',130,16,'Display');p.p(16,207,'Best discussed with the actual garment and a sample of the available finish.',130,10,'Body','muted');p.foot(4);p.done()
p=bookpage(5,'plum');p.image(denim,0,0,170,131);p.t(16,151,'New character.',43,'Display','lilac');p.p(16,169,'A contrasting patch or thread can acknowledge the repair. The finish becomes an intentional part of the piece.',135,12,'Body','paper');p.p(16,198,'Ask to see the colour and method before deciding. A beautiful contrast still needs to suit the cloth.',135,11,'Body','paper');p.foot(5,col='lilac');p.done()
p=bookpage(6);p.t(16,25,'02 / A PLAIN-LANGUAGE INDEX',9,'Mono','red');p.t(16,49,'Start with what',40,'Display');p.t(16,65,'you notice.',40,'Display')
for i,(code,title,sub) in enumerate([('M01','A hole or worn patch','Fabric is thin or has opened up.'),('M02','A seam coming undone','Two pieces of cloth are separating.'),('F01','A zip that will not work','The pull, teeth or slider needs attention.'),('F02','A missing button','A fastening needs a closer look.'),('A01','A length to adjust','A hem or sleeve needs a different length.'),('Q01','Help me work it out','You do not need the technical name.')]):
 y=88+i*20;p.line(16,y-6,154,y-6,'line');p.t(16,y+1,code,12,'Mono','red');p.t(38,y+1,title,13,'Medium');p.t(38,y+7,sub,10,'Body','muted')
p.foot(6);p.done()
p=bookpage(7,'lilac');p.t(16,25,'03 / BEFORE THE ASSESSMENT',9,'Mono');p.t(16,50,'A clear request.',43,'Display');p.p(16,67,'Three useful details are better than a technical diagnosis.',132,14,'Medium')
for n,(title,body) in enumerate([('The garment','Name the item so you can recognise it later. “My everyday shirt” is useful.'),('The place','Point to the elbow, seam, fastening or edge. If you are unsure, say so.'),('The intention','Would you prefer a close match, a visible detail or advice before choosing?')]):
 y=100+n*35;p.t(16,y,str(n+1).zfill(2),26,'DisplayBold','red');p.t(36,y,title,17,'Medium');p.p(36,y+9,body,112,11)
p.p(16,208,'No fibre percentages? No problem. Keep the original label and let the studio check it.',136,10);p.foot(7);p.done()
p=bookpage(8);p.t(16,25,'04 / THE SECOND CONVERSATION',9,'Mono','red');p.t(16,49,'A change deserves',37,'Display');p.t(16,65,'a conversation.',37,'Display');p.p(16,84,'A worn area may be larger than it first appears. The material may need a different method. Neither change should be a surprise.',132,12)
p.box(16,114,138,72,'wash');p.t(23,126,'YOUR REQUEST',9,'Mono');p.t(23,139,'A close match at the elbow.',14,'Medium');p.line(23,147,147,147,'line');p.t(23,158,'EXAMPLE ASSESSED APPROACH',9,'Mono','red');p.p(23,169,'A wider reinforcement area, with a small visible difference in the finish.',123,12)
p.p(16,200,'Read the changed scope, finish and price together. Ask a question if any part is unclear. Approve only after that review.',135,11);p.foot(8);p.done()
p=bookpage(9,'plum');p.t(16,25,'05 / NO SILENT AGREEMENTS',9,'Mono','lilac');p.t(15,58,'A pause',61,'Display','paper');p.t(15,82,'is useful.',61,'Display','paper');
for i,(head,body) in enumerate([('What would be different?','Compare the proposal with the original request.'),('Is anything still unclear?','Save a question before giving approval.'),('Have the details changed again?','A revised request needs a fresh decision.')]):
 y=113+i*31;p.line(16,y-7,154,y-7,'#715777');p.t(16,y,head,15,'Medium','lilac');p.p(16,y+10,body,133,11,'Body','paper')
p.p(16,211,'In the prototype, decisions are examples saved in your browser. No service is booked.',136,9,'Body','lilac');p.foot(9,col='lilac');p.done()
p=bookpage(10);p.t(16,25,'06 / THE GARMENT RECORD',9,'Mono','red');p.t(16,51,'Keep the details.',43,'Display');p.p(16,69,'The small ID on a paper tag opens a readable digital record. Keep either version with the piece.',130,12)
p.box(16,102,138,92,'lilac');p.mark(24,123,26);p.t(24,136,'AF-S01 / M01',13,'Mono');p.line(24,142,146,142,'plum');p.t(24,153,'The everyday shirt',18,'Display');p.p(24,165,'Elbow reinforcement. Visible patch in vermilion. Original care label retained.',80,11);p.qr(base+'#passport/AF-S01',113,150,31)
p.p(16,205,'Scan the sample record or type AF-S01 in the garment-record lookup. The ID remains useful without a QR reader.',137,10);p.foot(10);p.done()
p=bookpage(11);p.t(16,25,'07 / THE NEXT CHAPTER',9,'Mono','red');p.image(photo,16,38,138,88);p.t(16,148,'Care begins with',38,'Display');p.t(16,163,'the original label.',38,'Display');p.p(16,181,'A repair record adds information. It does not replace the garment maker’s instructions or confirm an unknown fibre content. Keep the original care label, and ask a qualified repairer when a finish needs specific care.',135,11);p.foot(11);p.done()
p=bookpage(12,'lilac');p.mark(16,29,38);p.t(16,68,'Keep the',66,'Display');p.t(16,94,'clothes.',72,'Display');p.t(16,137,'Change',66,'Display','red');p.t(16,163,'the ending.',61,'Display','red');p.line(16,180,154,180,'plum');p.t(16,194,'REPAIR / REWEAR / RECORD',10,'Mono');p.p(16,207,'Self-directed portfolio concept by Jocelyn Martinez. Illustrative imagery and example records. No repair results, research participants or impact metrics are claimed.',135,9);p.done();c.save()
# Five compositions, one typographic and information system.
c=pdf('AFTERFORM-Five-Poster-Campaign.pdf')
for i in range(1,6):
 p=Page(c,297,420,'lilac' if i in [1,3] else 'paper' if i==4 else 'plum')
 if i==1:
  p.mark(22,38,40);p.t(23,61,'A STUDIO FOR THE CLOTHES YOU KEEP',12,'Mono');p.t(18,140,'KEEP',157,'DisplayBold');p.t(18,198,'THE',157,'DisplayBold');p.t(18,256,'GOOD',150,'DisplayBold','red');p.t(18,315,'PART.',157,'DisplayBold');p.line(23,344,274,344);p.p(23,364,'Describe the garment. Explore the finish. Decide together.',180,20,'Medium');p.t(23,401,'REPAIR & REWEAR / A PORTFOLIO CONCEPT',10,'Mono')
 elif i==2:
  p.image(photo,0,0,297,256);p.t(21,286,'Worn.',72,'Display','paper');p.t(21,318,'Worth keeping.',68,'Display','paper');p.p(23,350,'A contrasting repair can become part of the piece.',178,21,'Body','paper');p.mark(22,398,33,'lilac');p.t(180,398,'REPAIR & REWEAR',11,'Mono','paper')
 elif i==3:
  p.mark(22,39,40);p.t(23,60,'TWO FINISHES. ONE CONSIDERED CHOICE.',12,'Mono');p.t(21,119,'Quiet',85,'Display');p.t(21,151,'repair.',85,'Display');p.line(22,173,274,173,'plum',1);p.line(96,173,183,173,'plum',4);p.t(84,229,'New',85,'Display','red');p.t(84,260,'character.',79,'Display','red');p.line(22,285,274,285,'plum',1);p.line(96,285,183,285,'red',4,[7,5]);p.p(23,320,'A close match or a deliberate contrast. The right finish begins with the cloth, and a conversation.',222,23,'Body');p.t(23,399,'FIND YOUR DIRECTION / AFTERFORM STUDIO CONCEPT',10,'Mono')
 elif i==4:
  p.t(22,40,'Clarity first.',63,'Display');p.t(22,66,'Commitment later.',57,'Display','red');
  for k,(h,b) in enumerate([('Describe the piece.','Start with what you notice. Technical vocabulary is optional.'),('Consider the proposal.','Read the scope, finish and price together. Ask before agreeing.'),('Keep the record.','Take the useful details into the garment’s next chapter.')]):
   y=117+k*85;p.line(22,y-12,274,y-12);p.t(22,y+5,f'0{k+1}',52,'DisplayBold','red');p.t(77,y,h,29,'Display');p.p(77,y+15,b,182,18)
  p.mark(22,397,32);p.t(186,397,'REPAIR & REWEAR',11,'Mono')
 elif i==5:
  p.t(22,35,'THE REPAIR INDEX / M01',13,'Mono','lilac');p.t(14,126,'M01',191,'DisplayBold','lilac');p.image(denim,22,153,145,145);p.t(181,173,'A hole.',30,'Display','paper');p.t(181,189,'A patch.',30,'Display','paper');p.t(181,205,'A start.',30,'Display','paper');p.p(181,237,'You do not need the technical name. Tell us what you notice.',90,17,'Body','paper');p.t(22,337,'Another chapter',61,'Display','paper');p.t(22,362,'starts here.',61,'Display','paper');p.mark(22,401,32,'lilac');p.t(181,401,'REPAIR & REWEAR',11,'Mono','paper')
 p.done()
c.save()
# Tags, labels, garment record and intake receipt at their actual proposed sizes.
c=pdf('AFTERFORM-Labels-Tags-and-Records.pdf');ids=[('AF-S01','M01','The everyday shirt','Elbow / visible patch'),('AF-S02','M01','The familiar jeans','Worn panel / lilac darn'),('AF-S03','F02','The borrowed jacket','Fastening / closest match')]
for j,(id,code,name,finish) in enumerate(ids):
 p=Page(c,60,100,'lilac' if j!=1 else 'paper');p.c.setStrokeColor(HexColor(C['plum']));p.c.setLineWidth(.5);p.c.circle(30*M,94*M,2*M,stroke=1,fill=0);p.mark(6,23,24);p.t(6,34,id,14,'Mono');p.line(6,40,54,40);p.t(6,54,code,32,'DisplayBold','red');p.p(6,66,name,47,11,'Medium');p.p(6,78,finish,47,8.5);p.t(6,93,'SAMPLE / NOT A CARE LABEL',6.2,'Mono');p.done()
 p=Page(c,60,100);p.t(6,17,'KEEP THE RECORD.',9,'Mono');p.qr(base+'#passport/'+id,11,25,38);p.t(6,72,id,15,'Mono');p.p(6,82,'Open the sample garment record. Keep the original care label.',47,8.8);p.done()
# 90 x 45 work label, three variations
for id,code,name,finish in ids:
 p=Page(c,90,45);p.box(0,0,15,45,'plum');p.c.saveState();p.c.translate(10*M,6*M);p.c.rotate(90);p.c.setFillColor(HexColor(C['paper']));p.c.setFont('Mono',9);p.c.drawString(0,0,'AFTERFORM');p.c.restoreState();p.t(21,11,id,12,'Mono');p.t(66,11,code,12,'Mono','red');p.line(21,15,84,15,'line');p.t(21,23,name,12,'Medium');p.p(21,30,finish,61,9);p.t(21,40,'ILLUSTRATIVE STUDIO RECORD',6.5,'Mono');p.done()
p=Page(c,85,120,'lilac');p.mark(7,18,29);p.t(7,31,'GARMENT RECORD / AF-S01',8,'Mono');p.t(7,49,'The everyday',25,'Display');p.t(7,60,'shirt.',25,'Display');p.line(7,67,78,67);p.p(7,76,'M01 / Elbow reinforcement. Visible patch in vermilion. Keep the original care label.',70,10);p.qr(base+'#passport/AF-S01',7,93,20);p.p(32,98,'Scan or enter AF-S01 in the digital record lookup.',44,8.5);p.t(7,116,'ILLUSTRATIVE RECORD',6,'Mono');p.done()
p=Page(c,80,160);p.mark(7,22,29);p.t(7,35,'ASSESSMENT RECEIPT / SAMPLE',7.5,'Mono');p.line(7,42,73,42);p.t(7,55,'A request is',24,'Display');p.t(7,65,'a beginning.',24,'Display');
for y,label,detail in [(82,'ITEM','Everyday shirt'),(100,'ATTENTION','Elbow / worn area'),(118,'PREFERENCE','Studio advice')]:p.t(7,y,label,7.5,'Mono','red');p.t(7,y+7,detail,10.5)
p.line(7,134,73,134);p.p(7,141,'No work is authorised by this receipt. Review a proposal before agreeing.',64,8.5);p.done();c.save()
# Packaging panels: real proportional dielines and artwork, not an image of a closed box.
c=pdf('AFTERFORM-Packaging-Panels.pdf');p=Page(c,456,142)
p.t(18,11,'01 / RETURN BAND — PROPOSED FLAT ARTWORK',9,'Mono');p.t(18,18,'420 × 90 mm · 30 mm overlap · 3 mm bleed shown · fit-test before production',8,'Body','muted')
x,y=18,30;p.box(x-3,y-3,426,96,'lilac');p.box(x,y,420,90,'lilac');p.box(x+270,y,120,90,'plum');p.mark(x+12,y+29,43);p.t(x+12,y+49,'Keep the clothes.',21,'Display');p.t(x+12,y+60,'Change the ending.',21,'Display','red');p.t(x+12,y+80,'REPAIR / REWEAR / RECORD',9,'Mono');p.t(x+174,y+23,'AF-S01',15,'Mono');p.p(x+174,y+39,'The everyday shirt',77,16,'Display');p.p(x+174,y+58,'M01 / Elbow reinforcement. A visible patch in vermilion.',77,10);p.mark(x+280,y+21,26,'lilac');p.p(x+280,y+39,'A record for the next chapter.',58,14,'Display','paper');p.qr(base+'#passport/AF-S01',x+350,y+44,29);p.p(x+280,y+61,'Keep the original care label. Sample record: AF-S01.',65,9,'Body','paper');p.t(x+397,y+47,'JOIN',9,'Mono');p.t(x+397,y+54,'HERE',9,'Mono');
# exact trim and fold indications sit outside reading area
p.c.setStrokeColor(HexColor(C['red']));p.c.setLineWidth(.5);p.c.rect(x*M,(p.h-y-90)*M,420*M,90*M,stroke=1,fill=0)
for off in [150,270,390]:p.line(x+off,y-3,x+off,y+93,'red',.5,[3,3])
for off,label in [(0,'FRONT 150'),(150,'SIDE / BACK 120'),(270,'RECORD PANEL 120'),(390,'OVERLAP 30')]:p.t(x+off+2,128,label,7,'Mono')
p.t(18,138,'Solid red: trim. Dashed red: nominal folds. Adjust folds after testing the packed garment. 120–150 gsm uncoated stock; avoid adhesive on cloth.',7,'Body');p.done()
# 110 x155mm sleeve, 12mm glue flap, 22mm bottom flap, actual fold net
p=Page(c,272,217);p.t(14,12,'02 / RECORD SLEEVE — 110 × 155 mm FINISHED',9,'Mono');p.t(14,19,'Proposed net · 12 mm glue tab · 22 mm bottom flap · validate with a paper prototype',8,'Body','muted');x,y=14,29
p.box(x,y,12,155,'wash');p.box(x+12,y,110,155,'lilac');p.box(x+122,y,110,155,'paper');p.box(x+12,y+155,220,22,'lilac');p.mark(x+23,y+29,38);p.t(x+24,y+63,'A little',45,'Display');p.t(x+24,y+82,'more life.',45,'Display');p.t(x+24,y+120,'THE GARMENT RECORD',9,'Mono');p.t(x+24,y+133,'AF-S01 / SAMPLE',12,'Mono','plum');p.mark(x+134,y+24,27);p.t(x+134,y+44,'KEEP WITH THE PIECE.',10,'Mono');p.p(x+134,y+61,'A repair record remembers the useful details: what changed, where it changed and what to ask next time.',82,12);p.qr(base+'#passport/AF-S01',x+134,y+99,32);p.p(x+171,y+104,'Scan the sample record or enter AF-S01 online.',46,9);p.p(x+134,y+143,'The original care label stays with the garment.',85,9)
# trim perimeter
pts=[(x,y),(x+232,y),(x+232,y+177),(x+12,y+177),(x+12,y+155),(x,y+155),(x,y)]
for a,b in zip(pts,pts[1:]):p.line(*a,*b,'red',.55)
for off in [12,122]:p.line(x+off,y,x+off,y+155,'red',.55,[3,3])
p.line(x+12,y+155,x+232,y+155,'red',.55,[3,3]);p.t(x+14,y+166,'BOTTOM FLAP / FOLD INWARD',8,'Mono');p.c.saveState();p.c.translate((x+7)*M,(p.h-y-146)*M);p.c.rotate(90);p.c.setFillColor(HexColor(C['muted']));p.c.setFont('Mono',7);p.c.drawString(0,0,'GLUE TAB / KEEP FREE OF CONTENT');p.c.restoreState();p.t(14,213,'Red lines are production guides. Remove guides from final press art after a supplier checks the net, stock and adhesive.',7,'Body','muted');p.done();c.save()
# Signage, genuine scale varies by installation; no invented address/opening hours.
c=pdf('AFTERFORM-Studio-Signage.pdf');p=Page(c,600,300,'plum');p.mark(40,116,150,'lilac');p.t(43,164,'REPAIR & REWEAR',28,'Mono','paper');p.line(43,200,557,200,'lilac',1);p.t(43,248,'A studio for the clothes you keep.',40,'Body','paper');p.done()
p=Page(c,420,180,'lilac');p.t(26,48,'Assessments',62,'Medium');p.arrow(345,36,42,'plum',4);p.line(26,76,394,76,'plum',1);p.t(26,118,'Collections',62,'Medium');p.arrow(345,106,42,'plum',4);p.t(28,158,'PLEASE START AT THE STUDIO DESK',15,'Mono');p.done()
p=Page(c,148,210);p.mark(14,31,36);p.t(14,61,'New to',42,'Display');p.t(14,78,'repair?',42,'Display');p.p(14,100,'Start with what you notice. We can work out the technical name together.',119,15);p.qr(base+'#repair/assess',14,134,37);p.p(59,143,'Explore the sample repair desk.',72,12,'Medium');p.t(14,190,'Q01 / ASK FOR AN ASSESSMENT',9,'Mono');p.t(14,202,'PORTFOLIO CONCEPT / NO LIVE SERVICE',7,'Mono','muted');p.done();c.save()
# Outlined mark files: editable vector outlines, no font dependencies.
font=FTFont(ROOT/'fonts/DisplayBold.ttf');gs=font.getGlyphSet();cmap=font.getBestCmap();upm=font['head'].unitsPerEm

def svgword(text,out,color,bg=None,size=100):
 scale=size/upm;pen=SVGPathPen(gs);x=0
 for ch in text:
  gn=cmap[ord(ch)];tp=TransformPen(pen,(scale,0,0,-scale,x,90));gs[gn].draw(tp);x+=(gs[gn].width-16)*scale
 paths=pen.getCommands();w=x+8
 data=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} 116" role="img" aria-label="{html.escape(text)}">'+(f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else '')+f'<path d="{paths}" fill="{color}"/></svg>'
 (AS/out).write_text(data)
svgword('afterform','wordmark-plum.svg',C['plum']);svgword('afterform','wordmark-reversed.svg',C['lilac'],C['plum']);svgword('afterform','wordmark-mono.svg','#000000');svgword('af','compact-mark.svg',C['plum'])
# Exact 24 px functional icon set; these communicate actions, never stand in for garment imagery.
icons={'assess':'M10 3a7 7 0 1 0 0 14a7 7 0 0 0 0-14M15 15l6 6','approve':'M3 12l6 6L21 5','record':'M6 3h12v18H6zM9 8h6M9 12h6M9 16h4','return':'M8 5L3 10l5 5M3 10h12a6 6 0 0 1 0 12','join':'M2 5h7v14H2M22 5h-7v14h7M7 8h10M7 12h10M7 16h10','question':'M9 8a3 3 0 1 1 5 2c-2 1-2 2-2 4M12 18v1'}
(AS/'icons').mkdir(exist_ok=True)
for name,d in icons.items():(AS/'icons'/f'{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{C["plum"]}" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter" role="img" aria-label="{name}"><path d="{d}"/></svg>')
(ROOT/'print-manifest.json').write_text(json.dumps({'book':book,'pdfs':[p.name for p in OUT.glob('*.pdf')],'font_licences':'SIL Open Font License; local files included','production':'RGB design proofs. Packaging nets require physical fit test and supplier preflight. Printed QR codes point to owner-controlled portfolio previews; update for public launch.'},indent=2))
print('Created 5 PDFs: guide 12 pages, campaign 5, labels 11, packaging 2, signage 3; vector wordmark family and 6 functional icons.')
