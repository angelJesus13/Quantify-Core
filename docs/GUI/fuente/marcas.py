"""Derivados de color autorizados: sin redibujar, recortar ni remuestrear.

El JPEG original conserva todas las coordenadas. Se extrae su cobertura de tinta
contra el mate casi blanco y se aplica Sky Laser / Optical White. Solo Pillow es
necesario para decodificar el JPEG y escribir el PNG con alfa.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image

WHITE_MATTE=245
OPAQUE_INK=40

def derive(original,blue,neutral):
    """Devuelve RGBA a la misma resolución, sin operaciones geométricas."""
    src=original.convert('RGB');raw=src.tobytes();result=bytearray(src.width*src.height*4)
    for i in range(src.width*src.height):
        r,g,b=raw[i*3:i*3+3];minimum=min(r,g,b)
        alpha=max(0,min(255,round((WHITE_MATTE-minimum)*255/(WHITE_MATTE-OPAQUE_INK))))
        # El tinte azulado de los grises JPEG no es azul de marca. La relación
        # con la distancia al blanco conserva también los bordes suavizados.
        is_blue=b-r>max(10,.18*(255-minimum)) and b-g>1
        color=blue if is_blue else neutral
        result[i*4:i*4+4]=bytes((*color,alpha))
    return Image.frombytes('RGBA',src.size,bytes(result))

def generate(root):
    tokens=json.loads((root/'packages/design-tokens/preview.json').read_text(encoding='utf-8'))
    cfg=tokens['branding']['dark'];colors=tokens['colors']
    def rgb(key):return tuple(int(colors[key][i:i+2],16) for i in (1,3,5))
    destination=root/'assets/images/brand';destination.mkdir(exist_ok=True)
    manifest={'version':1,'authorization':'Variantes de color/fondo autorizadas por el propietario el 29/10/2026. Sin cambios de dibujo o composición.','colors':cfg,'method':{'whiteMatte':WHITE_MATTE,'opaqueInk':OPAQUE_INK,'geometry':'Mismas dimensiones y coordenadas; sin recorte, interpolación, vectorizado ni tipografía nueva.'},'logos':{}}
    for kind in ('enterprise','product'):
        source=root/f'assets/images/{kind}Logo.jpeg'
        original=Image.open(source);variant=derive(original,rgb(cfg['blue']),rgb(cfg['neutral']))
        target=destination/f'{kind}-dark.png';variant.save(target,optimize=True)
        manifest['logos'][kind]={'original':str(source.relative_to(root)).replace('\\','/'),'dark':str(target.relative_to(root)).replace('\\','/'),'sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'darkSHA256':hashlib.sha256(target.read_bytes()).hexdigest(),'size':list(original.size)}
    # Una referencia documental antigua utiliza un recorte cuadrado de la
    # misma marca. Mantener sus 640 × 640 evita modificar su encuadre en claro.
    source=root/'docs/quantifyLogo.jpeg';original=Image.open(source)
    target=destination/'product-legacy-dark.png'
    derive(original,rgb(cfg['blue']),rgb(cfg['neutral'])).save(target,optimize=True)
    manifest['logos']['productLegacy']={'original':'docs/quantifyLogo.jpeg','dark':'assets/images/brand/product-legacy-dark.png','sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'darkSHA256':hashlib.sha256(target.read_bytes()).hexdigest(),'size':list(original.size)}
    (destination/'variants.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':generate(Path(__file__).resolve().parents[3])
