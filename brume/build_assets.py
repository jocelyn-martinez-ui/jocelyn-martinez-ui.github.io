from PIL import Image,ImageOps,ImageEnhance,ImageFilter
from pathlib import Path
import random, math, json, textwrap, os, base64
from xml.sax.saxutils import escape
import cairosvg

root=Path(__file__).resolve().parent
for p in ['images','social','email','print/svg','print/pdf','print/archive','source','research']:(root/p).mkdir(parents=True,exist_ok=True)
# Existing AI-generated photographic masters are committed with this project.
# They must be present before any SVG export is regenerated.
for name in ('wine-room','sun-room','collection','hand-detail'):
 if not (root/'images'/f'{name}.jpg').is_file():
  raise FileNotFoundError(f'Missing original campaign photo: {name}.jpg')

palette={'ink':'#2B201B','paper':'#EEE8DE','wine':'#582C3A','honey':'#D8A765','rust':'#A56841','fog':'#C8B9A6','light':'#FAF4E8'}
serif='Georgia,serif';sans='Arial,Helvetica,sans-serif'

# The SVGs embed photographic JPEG layers so embedded <img> rendering is reliable; text and shapes remain editable.
layouts=[
('01-launch',1080,1350,'wine-room','photo-left','Light, after hours.','AN OBJECT FOR THE HOURS THAT MATTER.'),
('02-maroon',1080,1350,'wine-room','photofull','For the last chapter of the day.','01 / PLUM'),
('03-cream',1080,1350,'sun-room','split','The gentler kind of bright.','02 / IVORY'),
('04-amber',1080,1350,'hand-detail','photo-frame','Meet the warmer side.','03 / AMBER'),
('05-collection',1080,1350,'collection','cover-soft','Three moods. One silhouette.','THE STUDIO EDITION'),
('carousel-01',1080,1350,'collection','photo-left','An object, not a fixture.','THE FORM / 01'),
('carousel-02',1080,1350,'wine-room','photofull','A room can change at dusk.','THE LIGHT / 02'),
('carousel-03',1080,1350,'sun-room','split','A warmer surface.','THE MATERIAL / 03'),
('carousel-04',1080,1350,'hand-detail','photo-frame','Small gestures matter.','THE MOMENT / 04'),
('carousel-05',1080,1350,'collection','cover-soft','Choose the atmosphere.','THE COLORS / 05'),
('carousel-06',1080,1350,'wine-room','photo-left','Bring the evening closer.','THE COLLECTION / 06'),
('story-01',1080,1920,'wine-room','story-photo','The room changes here.','STUDIO NOTES / AFTER HOURS'),
('story-02',1080,1920,'collection','story-cover','An evening in three tones.','PLUM  /  IVORY  /  AMBER'),
('story-03',1080,1920,'hand-detail','story-photo','A detail worth staying for.','EXPLORE THE OBJECTS'),
('landscape-01',1200,627,'sun-room','landscape','Lighting, as a material.','BRUME / STUDIO COLLECTION')
]
# image fill with SVG preserved aspectRatio

def text_svg(t,x,y,sz,color='ink',style='serif',weight='normal',anchor='start',spacing=0):
 family=serif if style=='serif' else sans
 return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{sz}" font-weight="{weight}" letter-spacing="{spacing}" fill="{palette.get(color,color)}" text-anchor="{anchor}">{escape(t)}</text>'

def svga(layout):
 key,w,h,pic,kind,headline,caption=layout
 embedded='data:image/jpeg;base64,'+base64.b64encode((root/'images'/f'{pic}.jpg').read_bytes()).decode('ascii')
 im=f'<image href="{embedded}" x="{{x}}" y="{{y}}" width="{{w}}" height="{{h}}" preserveAspectRatio="xMidYMid slice"/>'
 image=lambda x,y,ww,hh:im.format(x=x,y=y,w=ww,h=hh)
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="BRUME concept campaign artwork: {escape(headline)}">',f'<rect width="{w}" height="{h}" fill="{palette["paper"]}"/>']
 if kind=='photo-left':
  parts += [image(0,0,w,h*.72),f'<rect x="0" y="{h*.72}" width="{w}" height="{h*.28}" fill="{palette["paper"]}"/>',text_svg('BRUME',72,h*.79,45,'ink','serif',spacing=13),text_svg(headline,72,h*.89,62,'ink','serif'),text_svg(caption,76,h*.95,18,'rust','sans',spacing=2)]
 elif kind=='photofull':
  parts += [image(0,0,w,h),f'<rect x="36" y="35" width="{w-72}" height="120" fill="{palette["ink"]}" opacity=".87"/>',text_svg('B R U M E',75,115,44,'light','serif',spacing=3),f'<rect x="36" y="{h-260}" width="{w-72}" height="215" fill="{palette["ink"]}" opacity=".87"/>',text_svg(headline,68,h-159,47,'light','serif'),text_svg(caption,70,h-101,18,'honey','sans',spacing=4)]
 elif kind=='split':
  parts += [image(0,0,w*.73,h),f'<rect x="{w*.73}" y="0" width="{w*.27}" height="{h}" fill="{palette["wine"]}"/>',f'<rect x="0" y="{h*.68}" width="{w*.89}" height="{h*.22}" fill="{palette["paper"]}"/>',text_svg('BRUME',60,h*.77,48,'ink','serif',spacing=10),text_svg(headline,60,h*.84,42,'ink','serif'),text_svg(caption,60,h*.945,20,'light','sans')]
 elif kind=='photo-frame':
  parts += [f'<rect width="{w}" height="{h}" fill="{palette["wine"]}"/>',image(95,115,w-190,h*.61),text_svg('BRUME',100,75,51,'light','serif',spacing=11),text_svg(headline,100,h*.85,59,'light','serif'),text_svg(caption,104,h*.918,21,'honey','sans',spacing=2)]
 elif kind=='cover-soft':
  parts += [image(0,0,w,h*.63),f'<rect x="0" y="{h*.63}" width="{w}" height="{h*.37}" fill="{palette["fog"]}"/>',text_svg('B R U M E',70,h*.71,45,'ink','serif',spacing=6),text_svg(headline,70,h*.81,60,'ink','serif'),text_svg(caption,75,h*.91,21,'ink','sans',spacing=3)]
 elif kind=='story-photo':
  parts += [image(0,0,w,h),f'<rect x="60" y="80" width="{w-120}" height="152" fill="{palette["paper"]}" opacity=".95"/>',text_svg('B R U M E',100,178,60,'ink','serif',spacing=9),f'<rect x="60" y="{h-500}" width="{w-120}" height="280" fill="{palette["ink"]}" opacity=".88"/>',text_svg(headline,100,h-388,53,'light','serif'),text_svg(caption,100,h-302,22,'honey','sans',spacing=3)]
 elif kind=='story-cover':
  parts += [image(0,0,w,h*.70),f'<rect x="0" y="{h*.70}" width="{w}" height="{h*.30}" fill="{palette["paper"]}"/>',text_svg('B R U M E',70,h*.765,51,'ink','serif',spacing=6),text_svg(headline,70,h*.83,51,'ink','serif'),text_svg(caption,75,h*.9,25,'wine','sans',spacing=2)]
 elif kind=='landscape':
  parts += [image(w*.42,0,w*.58,h),f'<rect x="0" y="0" width="{w*.45}" height="{h}" fill="{palette["ink"]}"/>',text_svg('B R U M E',50,95,48,'honey','serif',spacing=7),text_svg('Lighting,',50,280,66,'light','serif'),text_svg('as a material.',50,354,57,'light','serif'),text_svg(caption,55,h-69,18,'honey','sans',spacing=2)]
 parts.append('</svg>')
 return '\n'.join(parts)

for l in layouts:
 name=l[0]; src=svga(l)
 (root/'social'/f'{name}.svg').write_text(src)
 try:
  preview=src
  cairosvg.svg2png(bytestring=preview.encode(),write_to=str(root/'social'/f'{name}.png'),output_width=l[1],output_height=l[2])
 except Exception as e:print('SVG render problem',name,str(e)[:100])

# Make specimen photographed presentations of the 3 color variants: same fictional base silhouette, no manufacturing claims.
# Vector print label templates with live editable text and trim/bleed guides in separate proof sheet.
variants=[('PLUM','BR-01','AUBERGINE GLASS','#582C3A','01'),('IVORY','BR-02','OPAQUE WARM GLASS','#E2D4BC','02'),('AMBER','BR-03','HONEYED TRANSLUCENT GLASS','#B46939','03')]

def label_svg(v,revision=3):
 name,sku,material,color,idx=v
 if revision==1:desc='COLORED GLASS LAMP';edition='SAMPLE / 00'
 elif revision==2:desc=material;edition='SAMPLE / 00'
 else:desc=material;edition='STUDIO EDIT / 01'
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="106mm" height="156mm" viewBox="0 0 106 156"><rect width="106" height="156" fill="{palette['paper']}"/><rect x="3" y="3" width="100" height="150" fill="none" stroke="{palette['fog']}" stroke-width=".4"/><text x="10" y="23" font-family="Georgia,serif" font-size="12" letter-spacing="2" fill="{palette['ink']}">BRUME</text><path d="M10 30H96" stroke="{palette['ink']}" stroke-width=".6"/><rect x="10" y="38" width="86" height="46" fill="{color}"/><circle cx="53" cy="58" r="17" fill="none" stroke="{palette['light']}" stroke-width=".7"/><path d="M36 58H70M53 41V75" stroke="{palette['light']}" stroke-width=".35"/><text x="10" y="99" font-family="Georgia,serif" font-size="15" fill="{palette['ink']}">{name}</text><text x="10" y="111" font-family="Arial" font-size="3.7" letter-spacing=".25" fill="{palette['ink']}">TABLE LIGHT / CONCEPT OBJECT</text><path d="M10 117H96" stroke="{palette['ink']}" stroke-width=".45"/><text x="10" y="125" font-family="Arial" font-size="3.3" fill="{palette['ink']}">{desc}</text><text x="10" y="132" font-family="Arial" font-size="3.3" fill="{palette['ink']}">{edition}</text><text x="10" y="141" font-family="Arial" font-size="3.4" fill="{palette['ink']}">{sku} / REV {revision:02d}</text><text x="10" y="147" font-family="Arial" font-size="2.7" fill="{palette['wine']}">FICTIONAL PRODUCT / NOT FOR RETAIL USE</text></svg>'''
for v in variants:(root/'print/svg'/f'brume-label-{v[0].lower()}-r03.svg').write_text(label_svg(v))
for i in [1,2]:(root/'print/archive'/f'brume-label-plum-r0{i}.svg').write_text(label_svg(variants[0],i))

manifest={'name':'BRUME — Light after hours','date':'2026-10-24','status':'self-directed AI-assisted fictional lighting brand','photography':'AI-generated concept images; no manufactured lamps or commissioned photoshoot','images':list(photos),'social':len(layouts),'email':3,'print_current':7,'print_archived':2,'variants':[{'color':v[0],'sku':v[1]} for v in variants],'external_validation':{'email_clients':False,'printer':False,'product_safety':False,'commercial_results':False}}
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('built',len(layouts),'social vectors and pngs, photos',len(photos),'label sources')
