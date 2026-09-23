from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image
import base64,json
r=Path(__file__).resolve().parent;d=r.parent.parent/'afterform/assets';fonts={n:TTFont(r/'fonts'/f'{n}.ttf') for n in ['Display','DisplayBold','Body','Medium','Mono']}
plum='#38233f';lilac='#d6c6ec';red='#bd3b2f';paper='#faf7f8'
def txt(s,x,y,size,font='Body',col=plum):
 f=fonts[font];gs=f.getGlyphSet();cmap=f.getBestCmap();scale=size/f['head'].unitsPerEm;pen=SVGPathPen(gs)
 for ch in s:
  gn=cmap.get(ord(ch),'.notdef');gs[gn].draw(TransformPen(pen,(scale,0,0,-scale,x,y)));x+=gs[gn].width*scale
 return '<path fill="'+col+'" d="'+pen.getCommands()+'"/>'
def rect(x,y,w,h,c):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
def photo(n,x,y,w,h):
 data=base64.b64encode((d/(n+'.webp')).read_bytes()).decode();return f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" href="data:image/webp;base64,{data}"/>'
def save(n,parts,w=1080,h=1350,title='Afterform campaign'):(d/f'{n}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><title>{title}</title>'+''.join(parts)+'</svg>')
p=[rect(0,0,1080,1350,lilac),txt('afterform',80,125,90,'DisplayBold'),txt('THE FINISH IS A CONVERSATION. / 01',84,196,24,'Mono'),txt('Quiet repair.',78,324,110,'Display'),txt('New character.',78,438,100,'Display',red),photo('denim-detail',80,490,920,610),txt('Two intentions. One piece worth keeping.',82,1180,34,'Medium'),txt('Explore the repair desk',82,1250,30,'Body')];save('social-01',p,title='Two repair directions: quiet repair and new character')
p=[rect(0,0,1080,1350,paper),txt('afterform',80,125,90,'DisplayBold'),txt('CHOOSE WITH THE CLOTH. / 02',84,196,24,'Mono'),txt('Keep it quiet.',80,336,97,'Display'),txt('Ask for the closest practical match.',84,412,36),rect(84,467,912,2,plum),rect(370,463,350,10,plum),txt('Make it part',80,660,97,'Display',red),txt('of the piece.',80,760,97,'Display',red),txt('Ask to see the contrasting finish.',84,845,36),rect(84,896,912,2,plum)]
for x in range(370,720,38):p.append(rect(x,892,23,10,red))
p.extend([txt('Not sure? Keep both possibilities open.',84,1080,36,'Medium'),txt('The assessment comes before the decision.',84,1155,33),txt('REPAIR & REWEAR / AFTERFORM',84,1270,25,'Mono')]);save('social-02',p,title='A close match or a visible repair: compare before choosing')
p=[rect(0,0,1080,1350,plum),txt('afterform',80,125,90,'DisplayBold',lilac),txt('CLARITY BEFORE COMMITMENT. / 03',84,196,24,'Mono',paper),txt('Your piece.',78,375,123,'Display',paper),txt('Your choice.',78,510,123,'Display',lilac),rect(84,590,912,2,lilac)]
for i,(num,h,sub) in enumerate([('01','Read the changes.','Scope, finish and price belong together.'),('02','Ask the question.','Uncertainty is a reason to pause.'),('03','Decide together.','A revised request needs a fresh review.')]):
 y=695+i*159;p+=[txt(num,84,y,45,'Mono',lilac),txt(h,206,y,53,'Display',paper),txt(sub,208,y+56,31,'Body',paper)]
p.append(txt('KEEP THE CLOTHES. CHANGE THE ENDING.',84,1270,25,'Mono',lilac));save('social-03',p,title='Read changes, ask questions and decide together')
p=[rect(0,0,1600,600,lilac),photo('repair-editorial',900,0,700,600),txt('afterform',70,103,70,'DisplayBold'),txt('Good clothes.',65,247,115,'Display'),txt('Another chapter.',65,364,108,'Display',red),txt('Start with what needs attention.',72,459,32,'Medium'),txt('REPAIR & REWEAR',73,541,24,'Mono')];save('digital-banner',p,1600,600,'Good clothes. Another chapter. Afterform repair studio')
def lum(h):
 v=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v];return .2126*v[0]+.7152*v[1]+.0722*v[2]
pairs=[]
for fg,bg,label in [(plum,paper,'Primary text / paper'),(plum,lilac,'Primary text / lilac'),(red,paper,'Accent text / paper'),(red,lilac,'Large display only / lilac'),(paper,red,'Reversed text / vermilion'),('#6b586f',paper,'Secondary text / paper'),('#2b614c',paper,'Success / paper')]:
 a,b=sorted([lum(fg),lum(bg)]);pairs.append({'pair':label,'foreground':fg,'background':bg,'ratio':round((b+.05)/(a+.05),2)})
(r/'contrast.json').write_text(json.dumps(pairs,indent=2));print(json.dumps(pairs))
