"""Tarea 03: modelo semántico compartido por HTML y la sincronización de Figma.

No importa capturas en Figma. Las vistas previas se derivan de textos, vectores
y contenedores; los originales raster y los veinte prototipos no se modifican.
"""
from pathlib import Path
from html import escape
import json
import generar as g

ROOT = g.ROOT
OUT = g.HERE / 'identidad/guia'
MODEL_PATH = OUT / 'modelo.json'
FRAME_NAMES = [
    '01. Identidad Gráfica', '02. Paleta de Colores', '03. Tipografía',
    '04. Iconografía de Navegación', '05. Iconografía de Acciones y Estados',
    '06. Aplicación de Estilos',
]
# Q tipográfica: anillo y cola descendente. No es la lupa editorial histórica.
# Geometría original de esta extensión; se conserva el logotipo heredado aparte.
SYMBOL = 'M50 12a34 34 0 1 0 0 68 34 34 0 1 0 0-68 M62 66l24 22'
EXTRA_ICONS = {
    'menu': 'M4 6h16 M4 12h16 M4 18h16',
    'buscar': 'M16 16l6 6 M18 10a8 8 0 1 0-16 0 8 8 0 1 0 16 0',
    'perfil': 'M16 7a4 4 0 1 0-8 0 4 4 0 1 0 8 0 M4 21v-2a8 8 0 0 1 16 0v2',
    'eliminar': 'M3 6h18 M9 6V3h6v3 M5 6l1 15h12l1-15 M10 10v7 M14 10v7',
    'guardar': 'M3 3h14l4 4v14H3Z M7 3v6h10V3 M7 21v-8h10v8',
    'compartir': 'M8 11l8-5 M8 13l8 5 M8 12a3 3 0 1 0-6 0 3 3 0 1 0 6 0 M22 4a3 3 0 1 0-6 0 3 3 0 1 0 6 0 M22 20a3 3 0 1 0-6 0 3 3 0 1 0 6 0',
    'cancelar': 'M5 5l14 14 M19 5L5 19',
    'informacion': 'M12 11v7 M12 6v1 M22 12a10 10 0 1 0-20 0 10 10 0 1 0 20 0',
}
NAV = [
    ('hoy','Inicio / Hoy','Abrir el día de negocio actual.'),
    ('menu','Menú','Mostrar opciones de navegación.'),
    ('buscar','Buscar','Encontrar hábitos propios.'),
    ('perfil','Perfil','Consultar la cuenta propia.'),
    ('volver','Regresar','Volver sin confirmar cambios.'),
    ('ajustes','Configuración','Preferencias y consentimiento.'),
    ('habitos','Hábitos','Catálogo personal y archivo.'),
    ('analisis','Análisis','Resultados de periodos cerrados.'),
    ('calendario','Calendario','Consultar fechas de la agenda.'),
    ('historial','Historial','Revisar registros confirmados.'),
    ('privacidad','Privacidad','Revisar finalidades autorizadas.'),
    ('dispositivo','Dispositivos','Consultar vinculaciones autorizadas.'),
]
ACTIONS = [
    ('crear','Agregar','Crear un hábito.'), ('editar','Editar','Cambiar su programación.'),
    ('eliminar','Eliminar','Solicitar eliminación con confirmación; no equivale a archivar.'),
    ('guardar','Guardar','Solicitar persistencia; esperar confirmación del servidor.'),
    ('descargar','Descargar','Obtener una exportación propia autorizada.'),
    ('compartir','Compartir','Acción prevista; requiere definir destinatario y consentimiento.'),
    ('confirmado','Confirmar','Aceptar una operación explícita.'),
    ('cancelar','Cancelar','Salir sin aplicar cambios.'),
    ('archivar','Archivar','Retirar de activos conservando historial.'),
    ('sincronizar','Sincronizar','Reintentar con la misma clave idempotente.'),
    ('recordatorio','Recordatorio','Configurar un aviso de la agenda.'),
    ('salir','Salir','Cerrar la sesión centralizada.'),
]
STATES = [
    ('confirmado','Éxito','Operación confirmada','emerald'),
    ('aviso','Advertencia','Revisar antes de continuar','amber'),
    ('cancelar','Error','No se guardó · Reintentar','crimson'),
    ('informacion','Información','Consulta el detalle','cyan'),
    ('pendiente','Pendiente','Esperando confirmación','amber'),
]

def text(value, style='body', color='obsidian'):
    return dict(type='text', text=value, style=style, color=color)

def box(children, direction='vertical', width=None, background=None, padding=0, gap=16, name='Grupo', **kw):
    return dict(type='box', children=children, direction=direction, width=width,
                background=background, padding=padding, gap=gap, name=name, **kw)

def icon(key, color='laserBlue', size=32):
    return dict(type='icon', key=key, color=color, size=size)

def brand(variant, symbol_only=False):
    return dict(type='brand', variant=variant, symbolOnly=symbol_only)

def frame(index, description, children):
    return box([text('QUANTIFY CORE / NEXUS CORE · TAREA 03', 'label','steel'),
                text(FRAME_NAMES[index], 'display'), text(description,'body','steel'), *children],
               width=1440, background='white', padding=48, gap=32, name=FRAME_NAMES[index], artboard=True)

def icon_cards(entries):
    cards=[]
    for i in range(0,len(entries),3):
        row=[]
        for key,label,meaning in entries[i:i+3]:
            row.append(box([box([icon(key), text(label,'heading')], 'horizontal', gap=16),
                            text(meaning), box([icon(key,'laserBlue'),
                            box([icon(key,'skyLaser')],background='midnight',padding=12)],'horizontal'),
                            text(f'qc/icon/{key} · 24 × 24 · trazo 1.8','caption','steel')],
                           width=432,background='mist',padding=24,name=f'Icono / {label}'))
        cards.append(box(row,'horizontal',gap=24))
    return cards

def model():
    identity=json.loads((g.HERE/'fuente/identidad.json').read_text(encoding='utf-8'))
    brand_rows=[]
    for variant,title,bg in [('principal','Principal a color','mist'),('monocromatica','Monocromática','mist'),
                             ('oscura','Sobre fondo oscuro','midnight'),('clara','Sobre fondo claro','white')]:
        ink='white' if variant=='oscura' else 'obsidian'
        brand_rows.append(box([text(title,'subtitle',ink),
                               box([brand(variant),brand(variant,True)],'horizontal',gap=32)],
                              background=bg,padding=32,name=f'Aplicación / {title}'))
    frames=[frame(0,'Una extensión de identidad para completar imagotipo e isotipo sin sobrescribir los logos heredados.',[
        text('Identidad y público','subtitle'),
        text('Quantify Core acompaña a personas que registran hábitos y consultan avances con evidencia. Nexus Core identifica a la empresa. La identidad comunica confianza, claridad, continuidad y autonomía; evita promesas clínicas y presión por productividad.'),
        *brand_rows,
        text('Composición y proporciones','subtitle'),
        text('Isotipo Q: retícula 100 × 100, anillo de radio 34, trazo 12 y cola descendente. Imagotipo: símbolo de 72 × 72, separación de 24 y denominación Quantify Core en Inter 700. Símbolo y nombre pueden utilizarse juntos o por separado: es un imagotipo, no un isologo indivisible.'),
        text('Uso y restricciones','subtitle'),
        text('Área libre: al menos 1/4 del alto del símbolo. Mínimos: isotipo 24 × 24; imagotipo 240 × 72. Para favicon de 16 px usar solo la Q y comprobar la lectura. Principal: Laser Blue y Obsidian; oscuro: Sky Laser y blanco; monocromática: una sola tinta Obsidian, o blanco en negativo. No deformar, rotar, añadir sombras, alterar la cola ni colocar sobre fotos sin superficie de protección.'),
        text('Esta Q tipográfica pertenece al producto y usa anillo grueso y cola descendente. La antigua Q editorial de trazo ligero permanece como marca de agua documental y no se utiliza como icono de búsqueda. Los JPEG de empresa y producto permanecen íntegros como antecedentes.'),
    ])]
    colors=[]
    for key,name,psychology,reason in identity['colors']:
        col=g.C[key];rgb=', '.join(str(int(col[i:i+2],16)) for i in (1,3,5))
        colors.append(box([box([],width=96,background=key,padding=32,name='Muestra'),
                           box([text(name,'subtitle'),text(f'{col} · RGB {rgb}','label'),
                                text('Intención de marca: '+psychology),text(reason)])],
                          'horizontal',background='mist',padding=24,gap=24,name=f'Color / {name}'))
    frames.append(frame(1,'Trece colores canónicos: valores sRGB, función e intención de marca. La psicología expresa intención, no efectos universales.',[
        *colors,text('Contraste y asignación por tema','subtitle'),
        text('Claro: Pure Mist / blanco / Obsidian / Steel. Oscuro: Obsidian / Midnight / blanco / Cool Gray. Acción: Laser Blue con blanco. Blanco sobre Laser Blue: 6.28:1; Cool Gray sobre Midnight: 5.70:1. Sky Laser sobre Midnight: 4.25:1 para iconos y gráficos; no texto pequeño. Los cuatro colores de estado se acompañan de forma y texto Obsidian. No usar blanco pequeño sobre Crimson, Amber, Emerald o Cyan.'),
        text('Objetivo de diseño: texto normal ≥ 4.5:1, texto grande y gráficos significativos ≥ 3:1. Bordes decorativos no sustituyen los bordes de controles. La guía no acredita conformidad de una aplicación implementada.'),
    ]))
    type_rows=[]
    for key,spec in g.TOKENS['typography'].items():
        type_rows.append(box([text(spec['use'],key),text(f"qc/type/{key} · {spec['family']} · {spec['weight']} · {spec['size']} px / {spec['lineHeight']} px",'caption','steel')],
                             background='mist',padding=24,name=f'Tipo / {key}'))
    frames.append(frame(2,'Inter: una familia para una interfaz legible, compatible y coherente.',[
        text('Inter Variable · Rasmus Andersson · SIL Open Font License','subtitle'),
        text('Fuente WOFF2 local para web; empaquetar TTF/OTF en Flutter. La licencia está en docs/GUI/assets/inter-license.txt. Los logotipos heredados conservan su dibujo. Mantener pesos, tamaños e interlineados entre temas; reacomodar contenido antes de reducir texto.'),
        *type_rows,
        text('Muestras de caracteres','subtitle'),
        text('ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\nÁÉÍÓÚÜÑ áéíóúüñ\n0123456789 · 10 / 20 minutos · 26/10/2026\n¡Hola! ¿Cómo vas? @ # $ % & * + − = / ( ) [ ] { } : ; , . « » “ ”','subtitle'),
        text('Jerarquía por función','subtitle'),
        text('Los títulos presentan la tarea; subtítulos agrupan contenido; encabezados identifican tarjetas; el cuerpo explica; etiquetas identifican campos; botones nombran acciones; ayuda explica condiciones. No usar solo mayúsculas en párrafos ni peso ligero para información esencial. Alinear cifras tabulares en tablas. La pantalla del frame 06 usa estos estilos.'),
    ]))
    rules=[text('Sistema lineal · retícula 24 × 24 · trazo 1.8 · extremos y uniones redondos. Los tamaños 24 y 32 escalan proporcionalmente. Objetivo táctil: 48 × 48; mantener la geometría sin deformar.','body'),
           text('Claro: Laser Blue activo y Steel neutro. Oscuro: Sky Laser activo y Cool Gray neutro. Nombre visible junto al icono; controles sin texto requieren nombre accesible. El foco usa Deep Cobalt en claro y Sky Laser en oscuro.','body')]
    frames.append(frame(3,'Navegación y acceso a los módulos personales; no concede permisos ni implementa servicios.',[
        *rules,*icon_cards(NAV),text('Procedencia y reutilización','subtitle'),
        text('Trazos originales del catálogo del repositorio y su extensión Tarea 03; sin recursos de iconos de terceros. La distribución conserva los términos del repositorio: no se inventa una licencia externa. Cada símbolo se prepara como qc/icon/<función> y se utiliza mediante instancias; el nombre accesible depende del control.'),
    ]))
    states=[]
    for key,label,meaning,color in STATES:
        states.append(box([icon(key,'obsidian'),text(label+' · '+meaning,'heading')],
                          'horizontal',background=color,padding=24,name=f'Estado / {label}'))
    frames.append(frame(4,'Las acciones expresan intención; los estados informan el resultado confirmado.',[
        *rules,*icon_cards(ACTIONS),text('Retroalimentación en ambos temas','subtitle'),*states,
        text('Error usa cruz; advertencia usa triángulo; información usa círculo con i; éxito usa verificación; pendiente usa reloj. Las etiquetas conservan el significado sin depender del color. Confirmar una intención no equivale a una respuesta exitosa del servidor.'),
        text('Decoración','subtitle'),box([icon('lectura'),icon('movimiento'),icon('descanso'),text('Lectura, movimiento y descanso contextualizan hábitos. No son controles sin una acción explícita.')],'horizontal',background='mist',padding=24),
        text('Los iconos decorativos se ocultan a lectores de pantalla. No sustituir eliminar por archivar: archivar conserva historial. Compartir es una acción prevista, sin promesa de servicio ni divulgación automática.'),
    ]))
    examples=[]
    for theme in ('light','dark'):
        p=g.TOKENS['themes'][theme]
        def button(label):
            return box([icon('crear','white',24),text(label,'button','white')],'horizontal',
                       background=p['action'],padding=16,name='qc/button/primary',component='button/'+theme)
        cards=[]
        for title,value in [('Leer con calma','10 / 20 minutos'),('Caminar','30 / 30 minutos')]:
            cards.append(box([text(title,'heading',p['text']),text(value,'body',p['muted']),
                              box([icon('confirmado','obsidian',24),text('Confirmado','label','obsidian')],
                                  'horizontal',background='emerald',padding=8,name='qc/badge/success',component='badge/'+theme)],
                             background=p['surface'],padding=24,name='qc/card/habit',component='habit/'+theme+'/'+title))
        examples.append(box([text('CLARO' if theme=='light' else 'OSCURO','label',p['muted']),
            brand('clara' if theme=='light' else 'oscura'),
            text('Tu rutina de hoy','title',p['text']),text('26 oct 2026 · America/Mexico_City','caption',p['muted']),
            text('Día abierto · 1 de 2 metas completas','heading',p['text']),*cards,button('Crear hábito'),
            box([icon('hoy',p['icon'],24),text('Hoy','label',p['text']),icon('habitos',p['iconMuted'],24),text('Hábitos','label',p['muted'])],
                'horizontal',background=p['surface'],padding=16,name='Navegación')],
            width=660,background=p['canvas'],padding=32,gap=24,name=f'Pantalla Hoy / {theme}'))
    frames.append(frame(5,'Pantalla propuesta del primer flujo RF-03 / RF-04. Datos sintéticos; sin cuentas reales ni servicios conectados.',[
        box(examples,'horizontal',gap=24),text('Aplicación de la guía','subtitle'),
        text('La Q identifica el producto; Inter organiza títulos, encabezados, párrafos, etiquetas, botones y ayuda. Laser Blue señala la acción. El badge combina verificación, palabra y color. Ambos temas conservan contenido, jerarquía y significado. Los controles se diseñan con área mínima 48 × 48.'),
        text('Anotación funcional: registrar avance envía un valor acumulado absoluto, conserva idempotencia y espera confirmación. El día abierto se separa de métricas cerradas. Los datos de estas tarjetas no certifican guardado real.'),
        text('Revisión: comprobar legibilidad, zoom, nombres accesibles, foco, correspondencia símbolo/acción y contraste en la implementación. En Figma los textos, vectores y componentes deben seguir editables; los PNG del repositorio son solo vistas previas.'),
    ]))
    icons={**g.ICONS,**EXTRA_ICONS}
    return dict(version=1,section='Guía de Estilos',fileKey='L6ePtwcmyBeiC2xI1iDGM3',
                tokens=g.TOKENS,icons=icons,symbol=SYMBOL,frames=frames,
                variants=['principal','monocromatica','oscura','clara'])

def svg_icon(path,color,size=32,view=24,stroke=1.8):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {view} {view}" aria-hidden="true"><path d="{path}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def render(node,data):
    colors=data['tokens']['colors']
    if node['type']=='text':
        return f'<div class="text type-{node["style"]}" style="color:{colors[node["color"]]}">{escape(node["text"])}</div>'
    if node['type']=='icon':return svg_icon(data['icons'][node['key']],colors[node['color']],node['size'])
    if node['type']=='brand':
        dark=node['variant']=='oscura';mono=node['variant']=='monocromatica'
        ink=colors['white' if dark else 'obsidian'];blue=ink if mono else colors['skyLaser' if dark else 'laserBlue']
        symbol=svg_icon(data['symbol'],blue,72,100,12)
        word='' if node['symbolOnly'] else f'<span class="wordmark" style="color:{ink}">Quantify<br>Core</span>'
        return '<div class="brand-sample">'+symbol+word+'</div>'
    styles=[f'gap:{node["gap"]}px',f'padding:{node["padding"]}px',f'flex-direction:{"row" if node["direction"]=="horizontal" else "column"}']
    if node.get('width'):styles.extend([f'width:{node["width"]}px','flex:none'])
    if node.get('background'):styles.append('background:'+colors[node['background']])
    attrs=' data-artboard="true"' if node.get('artboard') else ''
    return f'<section class="box" style="{";".join(styles)}" aria-label="{escape(node["name"])}"{attrs}>'+''.join(render(n,data) for n in node['children'])+'</section>'

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    data=model();MODEL_PATH.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    css=''.join('.type-'+k+'{font-size:'+str(s['size'])+'px;line-height:'+str(s['lineHeight'])+'px;font-weight:'+str(s['weight'])+'}' for k,s in g.TOKENS['typography'].items())
    html='''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guía de Estilos · Quantify Core · Tarea 03</title><style>
@font-face{font-family:Inter;src:url(../../assets/inter.woff2);font-weight:100 900}*{box-sizing:border-box}body{margin:0;background:#F4F7FD;font-family:Inter,sans-serif;color:#0B0F17}.box{display:flex;align-items:stretch;min-width:0;flex:1;border-radius:16px}.box>.box{min-width:0}.text{white-space:pre-wrap;overflow-wrap:break-word;flex:none}.box>.text{flex-shrink:0}.box[style*="flex-direction:row"]>.text{flex:1;min-width:0}svg{flex:none;align-self:center}.brand-sample{display:flex;gap:24px;align-items:center;flex:none;min-height:72px}.wordmark{font-size:28px;font-weight:700;line-height:32px}.box[data-artboard]{margin:40px auto;border-radius:0}.notice{max-width:1440px;margin:24px auto;padding:24px;font-size:16px;line-height:24px}nav a{margin-right:24px;color:inherit}''' + css + '</style><div class="notice"><h1>Guía de Estilos · Tarea 03</h1><p>Vista documental. La entrega editable debe verificarse en Figma; este HTML no acredita su publicación.</p><nav><a href="../README.md">Documentación</a><a href="https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/">Archivo del proyecto en Figma</a></nav></div><main>'
    html+=''.join(render(f,data) for f in data['frames'])+'</main></html>'
    html=html.replace('iLvbL5uaWxAPwuX58xN4yq',data['fileKey'])
    html=html.replace('Vista documental. La entrega editable debe verificarse en Figma; este HTML no acredita su publicación.',
                      'Vista documental de los seis frames. El archivo de Figma contiene la guía editable y los prototipos; comprobar el permiso de visualización del nuevo enlace antes de entregar.')
    (OUT/'index.html').write_text(html,encoding='utf-8')
    gallery=g.HERE/'index.html'
    page=gallery.read_text(encoding='utf-8')
    start=page.index('<div class="identity-grid">')+len('<div class="identity-grid">')
    end=page.index('</div></section>',start)
    cards=[]
    for i,f in enumerate(data['frames'],1):
        name=escape(f['name']);description=escape(f['children'][2]['text'],quote=True)
        src=f'identidad/guia/0{i}.png'
        cards.append(f'<button class="image-card" data-image="{src}" data-title="{name}" data-description="{description}"><img src="{src}" alt="{name}: lámina completa de Tarea 03" width="1440"><span><b>{name}</b><small>Guía de Estilos · Tarea 03</small></span></button>')
    page=page[:start]+'\n'+'\n'.join(cards)+'\n'+page[end:]
    page=page.replace('Cuatro lienzos. Un solo sistema.','Seis frames. Una guía de estilos.')
    page=page.replace('Los cuatro lienzos están disponibles','Los seis frames están disponibles')
    page=page.replace('QUANCORE-26-2026-10-29','QUANCORE-26-2026-10-30')
    page=page.replace('SISTEMA VISUAL · 29/10/2026','SISTEMA VISUAL · 30/10/2026')
    page=page.replace('Diseño de interfaz · 29 octubre 2026','Diseño de interfaz · 30 octubre 2026')
    page=page.replace('https://github.com/angelJesus13/Quantify-Core/blob/hotfix/QUANCORE-26-cuatro-lienzos/docs/GUI/','')
    marker='<div class="identity-grid">'
    old_note='<p><a href="identidad/guia/index.html">Ver los seis frames de la Guía de Estilos →</a> · La aplicación de esta corrección al archivo editable de Figma está pendiente.</p>'
    note='<p><a href="identidad/guia/index.html">Ver los seis frames de la Guía de Estilos →</a> · <a href="https://www.figma.com/design/L6ePtwcmyBeiC2xI1iDGM3?node-id=2-59">Abrir el archivo editable del proyecto en Figma →</a></p>'
    page=page.replace(old_note,note)
    if note not in page:page=page.replace(marker,note+marker,1)
    gallery.write_text(page,encoding='utf-8')
    print(f'Guía preparada: {len(data["frames"])} frames; {len(data["icons"])} iconos; {len(g.TOKENS["typography"])} estilos.')

if __name__=='__main__':build()
