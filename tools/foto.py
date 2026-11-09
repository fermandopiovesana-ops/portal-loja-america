"""Otimiza fotos enviadas pelos Irmãos para o portal.
Uso: python3 tools/foto.py ORIGEM.jpg site/fotos/AAAA-evento-descricao.webp
Gira pela orientação EXIF, limita a 1400 px no maior lado e grava WebP q76."""
import sys
from PIL import Image, ImageOps
src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
im.thumbnail((1400, 1400), Image.LANCZOS)
im.save(dst, 'WEBP', quality=76, method=6)
print(dst, im.size)
