"""Render the six exact outlined SVG campaign masters at delivery dimensions.
Requires PyMuPDF. No photograph retouching or generative image operations occur.
"""
from pathlib import Path
import fitz,re
root=Path(__file__).resolve().parent.parent.parent
site=(root/'dist/afterform') if (root/'dist').exists() else root/'afterform'
for name in ['social-announcement','social-editorial','social-information','story-guide','reel-cover','return-reminder']:
 p=site/'assets/system'/f'{name}.svg';source=p.read_text();box=re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',source);w,h=map(float,box.groups())
 d=fitz.open(p);pdf=fitz.open('pdf',d.convert_to_pdf());page=pdf[0];page.get_pixmap(matrix=fitz.Matrix(w/page.rect.width,h/page.rect.height),alpha=False).save(p.with_suffix('.png'))
 print(name,int(w),int(h))
