"""Render the four second-edition PDFs as web previews. Requires Poppler and Pillow."""
from pathlib import Path
from PIL import Image
import tempfile,subprocess
root=Path(__file__).resolve().parent.parent.parent
site=(root/'dist/afterform') if (root/'dist').exists() else root/'afterform'
pdfs={'AFTERFORM-On-Keeping-Second-Edition.pdf':'edition','AFTERFORM-Identity-Standards.pdf':'manual','AFTERFORM-Service-Paper-System.pdf':'service','AFTERFORM-Environmental-Communication.pdf':'environment'}
with tempfile.TemporaryDirectory(prefix='afterform-previews-') as tmp:
 for name,stem in pdfs.items():
  path=Path(tmp)/stem;path.mkdir()
  subprocess.run(['pdftoppm','-jpeg','-r','110',str(site/'downloads'/name),str(path/'page')],check=True)
  for i,p in enumerate(sorted(path.glob('page-*.jpg')),1):
   im=Image.open(p).convert('RGB');im.thumbnail((1250,1500));im.save(site/'assets/system'/f'{stem}-{i:02}.webp',quality=88)
