"""Regresiones de inventario, correspondencia y separación de fidelidades.

Solo biblioteca estándar. Ejecutar desde raíz con unittest discover.
La exportación del navegador verifica además cajas de texto reales y fuente.
"""
import json
from pathlib import Path
import re
import struct
import sys
import unittest
import xml.etree.ElementTree as ET

sys.dont_write_bytecode=True
GUI=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(GUI/'fuente'))
import generar as g
import movil

NS='{http://www.w3.org/2000/svg}'

class MobileDesign(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((GUI/'prototipos/movil/catalogo.json').read_text(encoding='utf-8'))
        cls.scenes={}
        for spec in movil.CATALOG:
            cls.scenes[spec['id']]={}
            for fidelity,theme in [('sketch','light'),('wireframe','light'),('mockup','light'),('mockup','dark')]:
                cls.scenes[spec['id']][fidelity,theme]=ET.fromstring(movil.render(spec,fidelity,theme,g.Canvas,g.C,g.ICONS,g.logos,g.photo))

    def test_20_pantallas_distintas_y_80_archivos(self):
        self.assertEqual(len(self.manifest),20)
        self.assertEqual(len({s['id'] for s in self.manifest}),20)
        self.assertEqual(len({s['intent'] for s in self.manifest}),20)
        self.assertEqual([s['number'] for s in self.manifest],list(range(1,21)))
        for folder in ['sketches','wireframes','mockups/light','mockups/dark']:
            self.assertEqual(len(list((GUI/'prototipos/movil'/folder).glob('*.png'))),20)
        for s in self.manifest:
            self.assertEqual(set(s['assets']),{'sketch:none','wireframe:none','mockup:light','mockup:dark'})
            for rel in s['assets'].values():
                raw=(GUI/rel).read_bytes()
                self.assertEqual(raw[:8],b'\x89PNG\r\n\x1a\n')
                self.assertEqual(struct.unpack('>II',raw[16:24]),(390,844))

    def test_correspondencia_de_todos_los_bloques_y_destinos(self):
        ids={s['id'] for s in self.manifest}
        for spec in movil.CATALOG:
            geometries=[]
            for svg in self.scenes[spec['id']].values():
                geometries.append([(n.attrib['data-block'],n.attrib['data-kind'],n.attrib['data-box']) for n in svg.iter(NS+'g') if 'data-block' in n.attrib])
            self.assertTrue(all(items==geometries[0] for items in geometries[1:]),spec['id'])
            self.assertEqual(len(geometries[0]),len(spec['blocks']))
            for block in spec['blocks']:
                if 'target' in block:self.assertIn(block['target'],ids)

    def test_sketches_solo_cuadros_y_lineas_sin_texto_imagenes_ni_color(self):
        for ident,scenes in self.scenes.items():
            svg=scenes['sketch','light']
            self.assertEqual(len(list(svg.iter(NS+'text'))),0,ident)
            for n in svg.iter():
                self.assertIn(n.tag.removeprefix(NS),{'svg','title','desc','g','rect','polyline','path'})
                if n.tag==NS+'path':self.assertNotRegex(n.attrib['d'],r'[CcQqAaSsTt]')
                for key in ('fill','stroke'):
                    value=n.attrib.get(key,'none')
                    if value!='none':self.assertTrue(is_gray(value),(ident,value))

    def test_wireframes_fuente_generica_grises_y_marcadores(self):
        for ident,scenes in self.scenes.items():
            svg=scenes['wireframe','light']
            self.assertEqual(len(list(svg.iter(NS+'image'))),0,ident)
            for n in svg.iter(NS+'text'):self.assertEqual(n.attrib['font-family'],'Arial, sans-serif')
            for n in svg.iter():
                for key in ('fill','stroke'):
                    value=n.attrib.get(key,'none')
                    if value!='none':self.assertTrue(is_gray(value),(ident,value))

    def test_mockups_inter_paleta_y_logos_existentes_en_dos_temas(self):
        import base64
        canonical={x.lower() for x in g.C.values()}
        for ident,scenes in self.scenes.items():
            a,b=scenes['mockup','light'],scenes['mockup','dark']
            self.assertNotEqual(ET.tostring(a),ET.tostring(b))
            for theme,svg in [('light',a),('dark',b)]:
                for n in svg.iter(NS+'text'):self.assertEqual(n.attrib['font-family'],'Inter')
                images=[n.attrib['href'] for n in svg.iter(NS+'image')]
                for kind in ('enterprise','product'):
                    resource=g.ROOT/(f'assets/images/brand/{kind}-dark.png' if theme=='dark' else f'assets/images/{kind}Logo.jpeg')
                    mime='image/png' if theme=='dark' else 'image/jpeg'
                    self.assertIn(f'data:{mime};base64,'+base64.b64encode(resource.read_bytes()).decode(),images)
                for n in svg.iter():
                    for key in ('fill','stroke'):
                        value=n.attrib.get(key,'none')
                        if value!='none':self.assertIn(value.lower(),canonical,(ident,value))

def is_gray(hex_value):
    return bool(re.fullmatch(r'#[0-9a-fA-F]{6}',hex_value)) and hex_value[1:3].lower()==hex_value[3:5].lower()==hex_value[5:7].lower()

if __name__=='__main__':unittest.main()
