from pathlib import Path
from PIL import Image
src=Path('assets/icon-source.png'); out=Path('assets/asm-autoradio.ico')
im=Image.open(src).convert('RGBA')
# Crop transparent/near-background borders if alpha exists, then square-pad.
bbox=im.getbbox()
if bbox: im=im.crop(bbox)
w,h=im.size; s=max(w,h)
canvas=Image.new('RGBA',(s,s),(0,0,0,0)); canvas.paste(im,((s-w)//2,(s-h)//2),im)
canvas.save(out, sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
print(out)
