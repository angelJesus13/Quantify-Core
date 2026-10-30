"""Evita que el traslado editable confunda logos recortados con fotografías."""
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import figma_prototipos as fp

class EditableTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.scenes=fp.build_scenes()

    def test_logos_una_vez_por_mockup_y_sin_imagenes_de_ui(self):
        for stage,screens in self.scenes.items():
            for screen in screens:
                with self.subTest(stage=stage,screen=screen['id']):
                    vector=ET.fromstring(screen['vector'])
                    self.assertFalse(list(vector.iter(fp.NS+'image')))
                    self.assertFalse(list(vector.iter(fp.NS+'text')))
                    if stage.startswith('mockup'):
                        suffix='-dark' if stage.endswith('dark') else ''
                        self.assertEqual([x[0] for x in screen['images'][:2]],['enterprise'+suffix,'product'+suffix])
                        self.assertEqual(len(screen['images']),3 if screen['id']=='bienvenida' else 2)
                        for _,x,y,w,h,*_ in screen['images']:
                            self.assertGreaterEqual(x,0);self.assertGreaterEqual(y,0)
                            self.assertLessEqual(x+w,390);self.assertLessEqual(y+h,844)
                    else:self.assertFalse(screen['images'])

    def test_texto_editable_y_sketch_sin_rotulos_internos(self):
        for stage,screens in self.scenes.items():
            for screen in screens:
                if stage.startswith('sketch'):self.assertFalse(screen['texts'])
                else:
                    content='\n'.join(t[2] for t in screen['texts'])
                    self.assertIn(screen['title'],content)
                    self.assertIn('Hoy',content)

if __name__=='__main__':unittest.main()
