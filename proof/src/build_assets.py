from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageEnhance,ImageFilter
from pathlib import Path
import math,random
ROOT=Path(__file__).resolve().parents[1]; A=ROOT/'assets';A.mkdir(exist_ok=True)
photo=Image.open((ROOT/'src/original-studio-image.png') if (ROOT/'src/original-studio-image.png').exists() else (ROOT/'assets/hero-studio.webp')).convert('RGB')
panel=Image.open((ROOT/'src/original-art-direction-board.png') if (ROOT/'src/original-art-direction-board.png').exists() else (ROOT/'assets/issue-study.webp')).convert('RGB')
INK='#181917';PAPER='#F2EFE8';ORANGE='#FF542D';ACID='#DBFA36';MOSS='#253932';GRAY='#95978B'
regular='/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf';bold='/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf';heavy='/usr/share/fonts/opentype/inter/InterDisplay-Black.otf';mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
for f in (regular,bold,heavy,mono): assert Path(f).exists(),f
font=lambda size,weight='regular':ImageFont.truetype({'regular':regular,'bold':bold,'heavy':heavy,'mono':mono}[weight],size)
def fitcrop(src,sz,center=(.5,.5)):
    w,h=src.size;tw,th=sz;r=max(tw/w,th/h);new=src.resize((math.ceil(w*r),math.ceil(h*r)),Image.Resampling.LANCZOS);nw,nh=new.size
    left=int((nw-tw)*center[0]);top=int((nh-th)*center[1]);return new.crop((left,top,left+tw,top+th))
def text(d,xy,s,sz,color,weight='bold'):
    d.text(xy,s,font=font(sz,weight),fill=color,stroke_width=0)
def tracked(d,x,y,s,sz,color,spacing=5):
    f=font(sz,'mono');
    for ch in s:
        d.text((x,y),ch,font=f,fill=color);x+=d.textlength(ch,font=f)+spacing
def save(img,name,q=86):
    img.save(A/name,'WEBP',quality=q,method=5);print(name,(A/name).stat().st_size)
# Hero crop: studio scene, no fake fonts in website; original generated artwork as photographic concept.
save(photo.resize((1672,941),Image.Resampling.LANCZOS),'hero-studio.webp',86)
# Detail crop and high contrast image strip for editorial and website sections.
save(fitcrop(photo,(1100,800),(.68,.61)),'detail-spread.webp',84)
save(fitcrop(photo,(1050,840),(.2,.7)),'contact-sheet.webp',84)
save(fitcrop(panel,(1300,820),(.58,.30)),'issue-study.webp',82)
# Photo-driven campaign series: original compositions, coordinated copy and common identity.
setups=[
 {'title':['GOOD IDEAS','DESERVE','GOOD PROOFS.'],'num':'01','bg':'photo','highlight':ORANGE,'sub':'THE ANATOMY OF A PRINTED IDEA'},
 {'title':['LOOK','CLOSER.'],'num':'02','bg':'dark','highlight':ACID,'sub':'A DESIGN IS A SERIES OF DECISIONS'},
 {'title':['PROCESS.','PEOPLE.','PRINT.'],'num':'03','bg':'split','highlight':ORANGE,'sub':'BEHIND THE FINAL IMAGE'},
 {'title':['FROM','IDEA TO','EDITION.'],'num':'04','bg':'gallery','highlight':ACID,'sub':'ISSUE 01 / SELF-DIRECTED STUDIO'},
 {'title':['THE DETAILS','ARE THE','DESIGN.'],'num':'05','bg':'paper','highlight':ORANGE,'sub':'CRAFT IS A CREATIVE SKILL'},
 {'title':['READ','BETWEEN','THE MARKS.'],'num':'06','bg':'diagonal','highlight':ACID,'sub':'THE PROOFING ROOM / VERSION 02'},
]
for i,x in enumerate(setups):
 w,h=1080,1350;bg=x['bg'];base=Image.new('RGB',(w,h),INK if bg in ('dark','split','diagonal') else PAPER);d=ImageDraw.Draw(base)
 if bg=='photo':
  base.paste(fitcrop(photo,(w,1010),(.6,.58)),(0,0));d=ImageDraw.Draw(base);d.rectangle((0,970,w,h),fill=INK);col=PAPER;y0=1015;fsize=77
 elif bg=='dark':
  base.paste(fitcrop(photo,(960,630),(.67,.32)),(60,115));d=ImageDraw.Draw(base);d.rectangle((0,745,w,h),fill=INK);col=PAPER;y0=830;fsize=112
 elif bg=='split':
  base.paste(fitcrop(panel,(530,1120),(.55,.38)),(550,0));d=ImageDraw.Draw(base);d.rectangle((0,0,550,h),fill=INK);col=PAPER;y0=230;fsize=78
 elif bg=='gallery':
  base.paste(fitcrop(photo,(990,810),(.36,.67)),(45,270));d=ImageDraw.Draw(base);d.rectangle((0,0,w,270),fill=INK);d.rectangle((0,1080,w,h),fill=INK);col=PAPER;y0=90;fsize=92
 elif bg=='paper':
  base.paste(fitcrop(panel,(940,620),(.81,.56)),(70,525));d=ImageDraw.Draw(base);col=INK;y0=190;fsize=90
 else:
  base.paste(fitcrop(photo,(870,900),(.65,.52)),(210,150));d=ImageDraw.Draw(base);d.rectangle((0,0,215,h),fill=INK);d.rectangle((0,1050,w,h),fill=INK);col=PAPER;y0=1060;fsize=77
 # Detail system with one mark and consistent folio; the image is the main subject.
 d.rectangle((54,55,214,109),fill=x['highlight']);text(d,(70,64),'PROOF',36,INK,'heavy')
 tracked(d,760,73,'ISSUE / 01',17,PAPER if bg not in ('paper',) else INK,1)
 for j,line in enumerate(x['title']):text(d,(67,y0+j*(fsize*.99)),line,fsize,col,'heavy')
 footer_y=1285;d.line([(65,footer_y-18),(1015,footer_y-18)],fill=GRAY,width=2)
 tracked(d,68,footer_y,x['sub'][:47],15,PAPER if bg not in ('paper',) else INK,1)
 tracked(d,930,footer_y,'0'+str(i+1),18,x['highlight'],1)
 save(base,f'campaign-{i+1:02d}.webp',88)
# Story / vertical: 9:16 authored rather than cropped social square.
story=Image.new('RGB',(1080,1920),INK);ds=ImageDraw.Draw(story);story.paste(fitcrop(photo,(1080,1150),(.52,.56)),(0,270));ds=ImageDraw.Draw(story)
ds.rectangle((46,44,328,152),fill=ACID);text(ds,(66,62),'PROOF',75,INK,'heavy');tracked(ds,48,200,'ISSUE 01 / THE PRINTED IDEA',20,PAPER,2)
ds.rectangle((0,1420,1080,1920),fill=INK);text(ds,(55,1500),'A CLOSER',112,PAPER,'heavy');text(ds,(55,1619),'LOOK.',132,PAPER,'heavy');tracked(ds,60,1800,'THE PROOFING ROOM / SELF DIRECTED',22,ACID,1)
save(story,'campaign-story.webp')
# Print-like advertising content 2:1 landscape, source used on site.
ad=Image.new('RGB',(1600,1040),PAPER);da=ImageDraw.Draw(ad);ad.paste(fitcrop(photo,(950,1040),(.62,.58)),(650,0));da=ImageDraw.Draw(ad);da.rectangle((0,0,650,1040),fill=PAPER)
text(da,(80,68),'PROOF.',116,INK,'heavy');tracked(da,84,225,'THE ANATOMY OF A PRINTED IDEA',25,INK,1)
text(da,(84,420),'GOOD IDEAS',78,INK,'heavy');text(da,(84,512),'DESERVE',78,INK,'heavy');text(da,(84,605),'GOOD PROOFS.',73,ORANGE,'heavy')
da.rectangle((84,785,580,797),fill=INK);tracked(da,84,849,'PUBLICATION / CAMPAIGN / PRINT',20,INK,1)
save(ad,'print-advert.webp',91)
