"""La variante cambia colores/fondo, no geometría ni originales."""
import hashlib
import json
from pathlib import Path
import sys
import unittest
from PIL import Image,ImageChops

sys.dont_write_bytecode=True
GUI=Path(__file__).resolve().parents[1];ROOT=GUI.parents[1]
sys.path.insert(0,str(GUI/'fuente'))
import marcas

class BrandVariants(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'assets/images/brand/variants.json').read_text(encoding='utf-8'))
        cls.tokens=json.loads((ROOT/'packages/design-tokens/preview.json').read_text(encoding='utf-8'))

    def test_originales_no_sobrescritos(self):
        expected={'enterprise':'81061f9327ed3b7639b50be111d7fa83b3d11a5dcb300bb4f080548c3c3d2db9','product':'d854fd96a92bb3d1e8513d00a014671ba3cfcc1444f12104438611135174e5bd'}
        for kind,sha in expected.items():self.assertEqual(hashlib.sha256((ROOT/self.manifest['logos'][kind]['original']).read_bytes()).hexdigest(),sha)

    def test_mismas_coordenadas_cobertura_y_transparencia_sin_placa(self):
        for item in self.manifest['logos'].values():
            src=Image.open(ROOT/item['original']).convert('RGB');dark=Image.open(ROOT/item['dark'])
            self.assertEqual(src.size,dark.size);self.assertEqual(dark.mode,'RGBA')
            r,g,b=src.split();minimum=ImageChops.darker(ImageChops.darker(r,g),b)
            expected=minimum.point(lambda v:255 if v<marcas.WHITE_MATTE else 0)
            actual=dark.getchannel('A').point(lambda v:255 if v else 0)
            self.assertIsNone(ImageChops.difference(expected,actual).getbbox())
            self.assertEqual(dark.getpixel((0,0))[3],0)
            self.assertEqual(dark.getchannel('A').crop((0,0,1600,200)).getbbox(),None)
            for color in dark.getcolors(1000000):self.assertIn(color[1][:3],[(74,125,232),(255,255,255)])

    def test_generacion_determinista_con_roles_existentes(self):
        self.assertEqual(self.tokens['branding']['dark'],{'blue':'skyLaser','neutral':'white','background':'transparent'})
        for item in self.manifest['logos'].values():
            actual=Image.open(ROOT/item['dark']);rebuilt=marcas.derive(Image.open(ROOT/item['original']),(74,125,232),(255,255,255))
            self.assertEqual(actual.tobytes(),rebuilt.tobytes())

if __name__=='__main__':unittest.main()
