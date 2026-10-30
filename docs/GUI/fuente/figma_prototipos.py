"""Prepara las 80 vistas previas existentes como vectores, textos y activos separados.

Los PNG de pantallas nunca se importan. XML conserva geometría del catálogo;
Figma recibe textos nativos y únicamente logos/fotografía como imágenes.
"""
import json
import xml.etree.ElementTree as ET
import generar as g
import movil

NS='{http://www.w3.org/2000/svg}'
STAGES=[('sketch','light'),('wireframe','light'),('mockup','light'),('mockup','dark')]

def build_scenes():
    data={}
    for fidelity,theme in STAGES:
        screens=[]
        for number,spec in enumerate(movil.CATALOG,1):
            source=ET.fromstring(movil.render(spec,fidelity,theme,g.Canvas,g.C,g.ICONS,g.logos,g.photo))
            texts=[];images=[]
            for parent in list(source.iter()):
                if parent is not source and parent.tag==NS+'svg':
                    continue  # Sus imágenes ya se consumieron con el viewport del logo.
                for child in list(parent):
                    kind=child.tag.removeprefix(NS)
                    if kind=='text':
                        a=child.attrib
                        texts.append([float(a['x']),float(a['y']),child.text or '',float(a.get('font-size',16)),int(a.get('font-weight',400)),a.get('fill','#0B0F17')])
                        parent.remove(child)
                    elif kind=='svg':
                        # Solo los dos logos se encapsulan en viewports SVG anidados.
                        a=child.attrib;image=child.find(NS+'image')
                        if image is not None:
                            x,y,w,h=[float(a.get(k,0)) for k in ('x','y','width','height')]
                            vx,vy,vw,vh=map(float,a['viewBox'].split())
                            scale=min(w/vw,h/vh)
                            key=('enterprise' if len(images)==0 else 'product')+('-dark' if theme=='dark' else '')
                            images.append([key,x,y,w,h,1600*scale,1194*scale,(w-vw*scale)/2-vx*scale,(h-vh*scale)/2-vy*scale])
                            parent.remove(child)
                    elif kind=='image':
                        a=child.attrib
                        images.append(['photo',*[float(a.get(k,0)) for k in ('x','y','width','height')]])
                        parent.remove(child)
                    elif kind in ('title','desc','defs'):
                        parent.remove(child)
            ET.register_namespace('',NS[1:-1])
            vector=ET.tostring(source,encoding='unicode')
            targets=[[b['x'],b['y'],b['w'],b['h'],b['target']] for b in movil.geometry(spec) if b.get('target')]
            screens.append(dict(id=spec['id'],number=number,title=spec['title'],rf=spec['rf'],note=spec['note'],
                                vector=vector,texts=texts,images=images,targets=targets))
        data[fidelity+'/'+theme]=screens
    return data

def prepare():
    data=build_scenes()
    g.BUILD.mkdir(exist_ok=True)
    (g.BUILD/'figma-prototipos.json').write_text(json.dumps(data,ensure_ascii=True),encoding='utf-8')
    print({key:len(json.dumps(items,ensure_ascii=False)) for key,items in data.items()})

if __name__=='__main__':prepare()
