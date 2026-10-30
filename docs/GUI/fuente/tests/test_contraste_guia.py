"""Contrastes realmente utilizados por la guía y sus dos pantallas de ejemplo."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[4]
TOKENS = json.loads((ROOT/'packages/design-tokens/preview.json').read_text(encoding='utf-8'))

def luminance(hex_value):
    c=[int(hex_value[i:i+2],16)/255 for i in (1,3,5)]
    linear=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
    return sum(a*b for a,b in zip(linear,[.2126,.7152,.0722]))

def contrast(a,b):
    x,y=sorted([luminance(a),luminance(b)])
    return (y+.05)/(x+.05)

class GuideContrast(unittest.TestCase):
    def test_textos_y_controles_en_ambos_temas(self):
        colors=TOKENS['colors']
        for theme,p in TOKENS['themes'].items():
            for surface in ('surface','canvas'):
                for ink in ('text','muted'):
                    self.assertGreaterEqual(contrast(colors[p[ink]],colors[p[surface]]),4.5,(theme,ink,surface))
                for ink in ('icon','controlBorder','focus'):
                    self.assertGreaterEqual(contrast(colors[p[ink]],colors[p[surface]]),3,(theme,ink,surface))
            self.assertGreaterEqual(contrast(colors[p['onAction']],colors[p['action']]),4.5,theme)

    def test_estados_legibles_sin_texto_blanco_sobre_acento(self):
        c=TOKENS['colors']
        for color in ('emerald','amber','crimson','cyan'):
            self.assertGreaterEqual(contrast(c['obsidian'],c[color]),4.5,color)

if __name__=='__main__':unittest.main()
