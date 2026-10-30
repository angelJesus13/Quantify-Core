"""Prepara escenas vectoriales con la fuente de cada etapa desde preview.json.
No escribe en prácticas, aplicaciones ni activos heredados.
"""
from pathlib import Path
import json
from html import escape
import base64, random, colorsys, textwrap

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / 'docs/GUI'
BUILD = HERE / '.build'
SCENES = {}
TOKENS = json.loads((ROOT / 'packages/design-tokens/preview.json').read_text(encoding='utf-8'))
C = TOKENS['colors']
SCREENS = [
    ('acceso','Acceso consciente','RF-01','U01–U05 / U15','Continuar con Keycloak; cancelar regresa a bienvenida. No capturar contraseñas aquí.'),
    ('hoy','Tu rutina, a tu ritmo','RF-03 / RF-04','U06','Abrir hábito o crear uno. El avance del día se separa de las métricas de días cerrados.'),
    ('habito','Diseña tu hábito','RF-03','U07','Validar nombre, meta, unidad, días y zona; cancelar conserva el estado anterior.'),
    ('registro','Cada avance cuenta','RF-04','U08 / U13','Enviar valor acumulado absoluto. Reintentar conserva clave idempotente; conflicto requiere revisión.'),
    ('analisis','Observa tu constancia','RF-05','U10','Consultar solo oportunidades cerradas; ventana, zona, fuente y versión visibles.'),
    ('sugerencias','Ideas con contexto','RF-07','U11','Abstenerse si faltan datos; personalizar no acepta hasta guardar. Sin umbrales inventados.'),
    ('ajustes','Tú decides qué compartir','RF-02','U12','Consentimiento opcional por finalidad; guardar explícitamente. Revocar bloquea usos futuros.'),
    ('administracion','Operación con trazabilidad','RF-09 / RF-10','A02 / A03 / A06','Solo agregados autorizados, motivo y auditoría. Sin enlace a rutinas privadas.')
]
ICONS = {
    'hoy':'M3 10L12 3l9 7v11h-6v-7H9v7H3Z',
    'habitos':'M5 4h14v17H5Z M9 2h6v4H9Z M8 11l2 2 5-5 M8 17h8',
    'analisis':'M4 20V10 M10 20V4 M16 20v-8 M22 20H2',
    'ajustes':'M4 7h16 M4 17h16 M9 4v6 M16 14v6',
    'crear':'M12 4v16 M4 12h16',
    'confirmado':'M4 12l5 5L20 6',
    'pendiente':'M12 8v5l4 2 M12 2a10 10 0 1 0 0 20 10 10 0 1 0 0-20',
    'aviso':'M12 3L2 21h20Z M12 9v5 M12 17v1',
    'volver':'M15 4l-8 8 8 8',
    'privacidad':'M12 2l8 4v6c0 5-8 10-8 10S4 17 4 12V6Z',
    'salir':'M10 3H3v18h7 M8 12h14 M17 7l5 5-5 5',
    'sugerencias':'M12 2l3 7 7 3-7 3-3 7-3-7-7-3 7-3Z'
}

def write(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value,encoding='utf-8',newline='\n')

class Canvas:
    def __init__(self,w,h,title,theme='light',fidelity='mockup'):
        self.w,self.h,self.fidelity,self.theme=w,h,fidelity,theme
        self.p={k:C[v] for k,v in TOKENS['themes'][theme].items()}
        if fidelity!='mockup':
            self.p.update(canvas='#FFFFFF',surface='#FFFFFF',text='#202020',muted='#454545',line='#777777',action='#202020',onAction='#FFFFFF')
        self.s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">Propuesta de diseño Quantify Core. Datos sintéticos. {fidelity}; tema {theme}.</desc>']
        self.rect(0,0,w,h,self.p['canvas'],r=0)
    def rect(self,x,y,w,h,fill=None,r=12,stroke=None):
        fill=fill or self.p['surface']
        style=' stroke-dasharray="6 4"' if self.fidelity=='sketch' else ''
        self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r if self.fidelity != "sketch" else 2}" fill="{fill}" stroke="{stroke or self.p["line"]}" stroke-width="1"{style}/>')
    def text(self,x,y,t,size=16,color=None,weight=400):
        self.s.append(f'<text x="{x}" y="{y}" font-family="Inter" font-size="{size}" fill="{color or self.p["text"]}" font-weight="{weight}">{escape(str(t))}</text>')
    def lines(self,x,y,rows,size=16,color=None,step=24):
        for i,row in enumerate(rows): self.text(x,y+i*step,row,size,color)
    def icon(self,name,x,y,color=None,scale=1):
        self.s.append(f'<path d="{ICONS[name]}" transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color or self.p["text"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')
    def button(self,x,y,w,t,primary=True):
        self.rect(x,y,w,48,self.p['action'] if primary else self.p['surface'],8,self.p['action'] if primary else self.p['line'])
        self.text(x+16,y+30,t,16,self.p['onAction'] if primary else self.p['text'],600)
    def card(self,y,title,sub,badge='',x=24,w=342):
        self.rect(x,y,w,104)
        self.text(x+16,y+29,title,18,weight=600)
        self.text(x+16,y+55,sub,14,self.p['muted'])
        if badge:
            self.icon('confirmado' if 'Confirmado' in badge else 'pendiente',x+16,y+69,scale=.75)
            self.text(x+42,y+85,badge,14)
    def field(self,y,label,value,error=False):
        self.text(24,y,label,14,weight=600)
        self.rect(24,y+12,342,48,r=8)
        self.text(40,y+42,value,16)
        if error:self.text(24,y+80,'Escribe un nombre para continuar.',14)
    def footer(self):
        pass
    def end(self): return ''.join(self.s)+'</svg>'

def screen(key,theme,fidelity):
    title=next(x[1] for x in SCREENS if x[0]==key)
    if fidelity=='sketch': return sketch(key)
    if key=='administracion': return desktop(theme,fidelity,True)
    c=Canvas(390,844,title,theme,fidelity)
    if fidelity=='mockup':
        logos(c,24,10,342,62)
        watermark(c,336,94,.6)
    else:
        c.text(24,38,'Nexus Core',14,weight=600)
        c.text(244,38,'Quantify Core',14,weight=600)
    c.text(24,116,title,24,weight=700)
    if key=='acceso':
        c.lines(24,164,['Pequeños hábitos.','Evidencia que puedes entender.'],20)
        c.rect(24,226,342,176,c.p['surface'])
        if fidelity=='mockup': photo(c,24,226,342,176)
        else:
            for i,h in enumerate([38,70,102,126]): c.rect(58+i*68,370-h,32,h,c.p['action'],5,c.p['action'])
        c.lines(24,446,['Tu sesión se gestiona con Keycloak.','Accede para consultar solo tus datos.'])
        c.button(24,516,342,'Continuar con Keycloak →')
        c.button(24,580,342,'Volver a bienvenida',False)
        c.lines(24,686,['Sesión vencida: vuelve a iniciar sesión.','Sin formularios locales de contraseña.'],14)
    elif key=='hoy':
        c.text(24,150,'Lunes 26 oct · America/Mexico_City',14,c.p['muted'])
        c.rect(24,176,342,110,c.p['action'],16,c.p['action'])
        c.text(42,209,'HOY · DÍA ABIERTO',14,c.p['onAction'])
        c.text(42,249,'1 de 3 metas confirmadas',22,c.p['onAction'],700)
        c.card(310,'Leer con calma','10 / 20 minutos · Diario','Parcial · Confirmado')
        c.card(430,'Caminar','30 / 30 minutos · Lunes','Meta completa · Confirmado')
        c.card(550,'Pausa consciente','Sin registro · 5 minutos · Diario','Todavía sin registro')
        c.button(24,682,342,'+ Crear hábito')
    elif key=='habito':
        c.field(164,'Nombre requerido','Leer con calma')
        c.field(260,'Meta y unidad requeridas','20 minutos')
        c.text(24,364,'Días de la semana requeridos',14,weight=600)
        for i,d in enumerate(['L','M','X','J','V','S','D']):
            c.rect(24+49*i,382,44,48,c.p['action'],8,c.p['action']);c.text(38+49*i,412,d,16,c.p['onAction'])
        c.field(470,'Zona de agenda','America/Mexico_City')
        c.lines(24,578,['Nueva programación desde 26 oct 2026.','Editar conserva la configuración histórica.'],14)
        c.button(24,644,342,'Guardar hábito')
        c.button(24,708,342,'Cancelar creación',False)
    elif key=='registro':
        c.text(24,154,'Leer con calma · 26 oct 2026',16)
        c.card(184,'Meta del día: 20 minutos','Último valor confirmado: 10 minutos','Parcial · Confirmado')
        c.field(332,'Valor acumulado del día (minutos)','15')
        c.lines(24,436,['Se enviarán 15 minutos en total.','Reintentar no añade otros 15 minutos.'],16)
        c.button(24,508,342,'Enviar valor acumulado')
        c.button(24,572,342,'Volver sin cambios',False)
        c.lines(24,682,['Archivar requiere confirmación.','El historial se conserva.'],14)
    elif key=='analisis':
        c.lines(24,154,['19–25 oct 2026 · Días cerrados','Zona: America/Mexico_City'],14)
        c.card(204,'Cumplimiento: 71.4 %','5 de 7 oportunidades cerradas','Fuente: registros confirmados')
        c.rect(24,332,342,206)
        c.text(40,362,'Oportunidades completas / programadas',14,weight=600)
        for i,v in enumerate([1,1,0,1,1,1,0]):
            c.rect(46+i*43,466-v*64,22,max(4,v*64),c.p['action'],2,c.p['action']);c.text(47+i*43,502,['L','M','X','J','V','S','D'][i],14)
        c.lines(24,582,['L: 1/1 · M: 1/1 · X: 0/1 · J: 1/1','V: 1/1 · S: 1/1 · D: 0/1','Racha en este periodo: 0 al cierre.','Regla: RN-P17 · cálculo 26 oct 2026.'],14)
        c.button(24,714,342,'Consultar otro periodo',False)
    elif key=='sugerencias':
        c.text(24,154,'Recomendaciones voluntarias',16)
        c.rect(24,194,342,232)
        c.icon('sugerencias',172,222,c.p['action'],1.8)
        c.text(44,308,'Aún faltan datos',22,weight=700)
        c.lines(44,344,['No hay información suficiente para','una recomendación en este periodo.','Puedes seguir registrando tus hábitos.'],14)
        c.button(24,462,342,'Revisar mis hábitos')
        c.button(24,526,342,'Revisar consentimiento',False)
        c.lines(24,640,['Cuando exista una sugerencia: mostrar','fuentes, periodo, versión y limitaciones.','Personalizar → guardar explícitamente.','Cancelar no acepta la sugerencia.'],14)
    elif key=='ajustes':
        c.field(168,'Zona del perfil','America/Mexico_City')
        c.card(276,'Análisis para sugerencias','Finalidad: personalizar hábitos','Desactivado · Opcional')
        c.card(406,'Fuente biométrica','Sin dispositivo vinculado','No se recopilan señales')
        c.lines(24,558,['Revocar impide nuevos usos y trabajos.','Cada fuente necesita su consentimiento.','Cambiar zona no reclasifica el historial.'],14)
        c.button(24,652,342,'Guardar preferencias')
        c.button(24,716,342,'Cancelar cambios',False)
    if fidelity=='mockup' and key!='acceso': mobile_nav(c,key)
    return c.end()

def desktop(theme,fidelity,admin=False):
    c=Canvas(1440,900,'Administración' if admin else 'Hoy · Escritorio',theme,fidelity)
    c.rect(0,0,248,900,r=0)
    if fidelity=='mockup':
        logos(c,18,20,212,70)
        watermark(c,1330,846,.75)
    else:c.text(30,56,'Quantify Core',24,weight=700)
    c.text(30,104,'OPERACIÓN' if admin else 'MI ESPACIO',12,c.p['muted'])
    items=[('hoy','Resumen' if admin else 'Hoy'),('habitos','Catálogo' if admin else 'Mis hábitos'),('analisis','Auditoría' if admin else 'Análisis'),('ajustes','Configuración')]
    for i,(icon,label) in enumerate(items):
        y=150+i*66
        if i==0:c.rect(16,y-30,216,52,c.p['action'],8,c.p['action'])
        color=c.p['onAction'] if i==0 else c.p['text'];c.icon(icon,30,y-17,color);c.text(70,y,label,16,color,600)
    c.text(30,823,'Datos sintéticos',14,c.p['muted'])
    c.text(288,54,'TU ESPACIO / '+('OPERACIÓN' if admin else 'HÁBITOS'),14,c.p['muted'])
    c.text(288,112,'Operación con trazabilidad' if admin else 'Tu rutina, a tu ritmo',36,weight=700)
    c.text(288,152,'Solo agregados autorizados · Sin acceso a rutinas privadas' if admin else 'Lunes 26 octubre 2026 · America/Mexico_City · Día abierto',16,c.p['muted'])
    c.button(1110,82,282,'Consultar auditoría' if admin else '+ Crear hábito')
    for i,(label,value,sub) in enumerate([('Catálogo','12 plantillas','Ejemplo agregado'),('Estado','Disponible','Sin datos personales'),('Control','Motivo requerido','Operaciones auditadas')] if admin else [('Hoy','1 / 3','Metas confirmadas'),('Último periodo','71.4 %','5 / 7 · 19–25 octubre'),('Sincronización','Al día','Solo datos confirmados')]):
        x=288+i*374;c.rect(x,200,350,146);c.text(x+24,232,label,16,c.p['muted']);c.text(x+24,279,value,28,weight=700);c.text(x+24,316,sub,14,c.p['muted'])
    c.rect(288,378,722,340);c.text(312,420,'Catálogo de plantillas' if admin else 'Programados para hoy',24,weight=700)
    for i,(name,desc) in enumerate([('Pausa consciente','Activa · Versión 2'),('Lectura diaria','Activa · Versión 1'),('Movimiento','Pausada · Versión 3')] if admin else [('Leer con calma','10 / 20 minutos · Parcial confirmado'),('Caminar','30 / 30 minutos · Meta confirmada'),('Pausa consciente','Sin registro · Meta de 5 minutos')]):
        y=452+i*76;c.rect(312,y,674,64,r=8);c.text(330,y+25,name,18,weight=600);c.text(330,y+49,desc,14,c.p['muted']);c.text(847,y+37,'Revisar →' if admin else 'Abrir →',16)
    c.rect(1034,378,378,340)
    if fidelity=='mockup' and not admin:
        photo(c,1034,378,378,126)
        c.text(1058,538,'Haz espacio para avanzar',20,weight=600)
    else:c.text(1058,421,'Antes de confirmar' if admin else 'Una pausa también suma',22,weight=600)
    c.lines(1058,578 if fidelity=='mockup' and not admin else 466,['Indica el motivo del cambio.','Cancelar no modifica la plantilla.','El historial se conserva.','Editar no cambia hábitos creados.'] if admin else ['Pequeños pasos, con intención.','Tu progreso empieza hoy.'],16)
    c.button(1058,648,330,'Revisar cambio' if admin else 'Ver mi progreso',False)
    c.rect(288,750,1124,82);c.icon('privacidad' if admin else 'pendiente',310,774)
    c.lines(352,780,['La API debe comprobar permiso, motivo y revisión antes de aplicar el cambio.','Vista de diseño: no ejecuta operaciones ni consulta cuentas reales.'] if admin else ['Respuesta perdida: aún no pudimos confirmar el guardado.','Reintentar conserva la misma clave; un conflicto requiere revisar la versión.'],16)
    c.footer();return c.end()

def image(c,path,x,y,w,h):
    mime='image/jpeg' if Path(path).suffix in ['.jpg','.jpeg'] else 'image/png'
    data=base64.b64encode(Path(path).read_bytes()).decode()
    clip=f'clip-{len(c.s)}'
    c.s.append(f'<defs><clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/></clipPath></defs><image href="data:{mime};base64,{data}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip})"/>')

def photo(c,x,y,w,h):
    image(c,HERE/'assets/ritual-cotidiano.png',x,y,w,h)


def logos(c,x,y,w,h,dark=None):
    """Co-branding: original enterprise left, original product right.
    The SVG viewport removes outer white margins, never any lettering.
    """
    size=min(w*.44,h*2.4)
    dark=(c.theme=='dark') if dark is None else dark
    for kind,xx in [('enterprise',x),('product',x+w-size)]:
        path=ROOT/f'assets/images/brand/{kind}-dark.png' if dark else ROOT/f'assets/images/{kind}Logo.jpeg'
        data=base64.b64encode(path.read_bytes()).decode()
        view='100 290 1400 650' if kind=='enterprise' else '100 350 1400 520'
        if not dark:c.rect(xx,y,size,h,'#FFFFFF',6,'#FFFFFF')
        mime='image/png' if dark else 'image/jpeg'
        c.s.append(f'<svg x="{xx+4}" y="{y+4}" width="{size-8}" height="{h-8}" viewBox="{view}" preserveAspectRatio="xMidYMid meet"><image href="data:{mime};base64,{data}" width="1600" height="1194"/></svg>')

def watermark(c,x,y,scale,color='#526179'):
    c.s.append(f'<g transform="translate({x} {y}) scale({scale})" opacity=".12"><circle cx="24" cy="24" r="18" fill="none" stroke="{color}" stroke-width="6"/><path d="M34 36l12 12" stroke="{color}" stroke-width="6" stroke-linecap="round"/></g>')

def mobile_nav(c,key):
    c.rect(0,774,390,70,c.p['surface'],0,c.p['line'])
    for i,(icon,label,active) in enumerate([('hoy','Hoy',key=='hoy'),('habitos','Hábitos',key in ['habito','registro']),('analisis','Análisis',key=='analisis'),('ajustes','Perfil',key=='ajustes')]):
        x=36+i*94; ink=c.p['text'] if active else c.p['muted']
        if active:c.rect(x-12,780,48,29,C['laserBlue'],12,C['laserBlue'])
        c.icon(icon,x,782,c.p['onAction'] if active else ink,.9)
        c.text(x-5,827,label,11,ink,600 if active else 400)

def sketch(key):
    desktop_mode=key=='administracion';w,h=(1440,900) if desktop_mode else (390,844)
    c=Canvas(w,h,'Sketch de '+key,'light','sketch')
    c.s=c.s[:1];c.s.append(f'<rect width="{w}" height="{h}" fill="#FFFEFB"/>')
    rng=random.Random(key)
    def rough(x,y,ww,hh):
        for offset in [0,1.7]:
            points=[(x,y),(x+ww,y),(x+ww,y+hh),(x,y+hh),(x,y)]
            d='M'+' L'.join(f'{xx+rng.uniform(-2,2)+offset:.1f} {yy+rng.uniform(-2,2):.1f}' for xx,yy in points)
            c.s.append(f'<path d="{d}" fill="none" stroke="#555861" stroke-width="{1.4 if offset==0 else .55}" stroke-linecap="round"/>')
    def bars(x,y,ww=180,n=2):
        for i in range(n):
            length=ww*(1 if i==0 else .67)
            c.s.append(f'<path d="M{x} {y+i*13}q{length/3:.1f} -3 {length:.1f} 0" fill="none" stroke="#777A82" stroke-width="3" stroke-linecap="round"/>')
    if desktop_mode:
        rough(12,12,1416,876);rough(26,28,210,844)
        for y in [80,170,236,302,368]:bars(50,y,130)
        bars(280,70,420,2)
        for i in range(3):rough(280+i*375,170,340,140);bars(305+i*375,210,140)
        rough(280,350,1080,430)
        for y in [390,470,550,630,710]:bars(305,y,700,2)
    else:
        rough(10,10,370,824);rough(32,30,30,30);bars(80,42,125,1);bars(30,110,260)
        if key=='acceso':
            rough(30,184,330,250)
            c.s.append('<path d="M32 432L170 240 272 380 360 300M30 184l330 250" stroke="#B2B3B8" fill="none"/>')
            bars(36,490,270,3);rough(30,600,330,52);rough(30,682,330,52)
        elif key=='hoy':
            rough(30,162,330,102);bars(54,198,230)
            for y in [300,430,560]:rough(30,y,330,102);rough(48,y+22,36,36);bars(104,y+32,220,3)
            rough(30,700,330,48)
        elif key=='habito':
            for y in [178,296,538]:bars(30,y-18,150,1);rough(30,y,330,58)
            for i in range(7):rough(30+i*47,428,38,42)
            rough(30,678,330,52);bars(130,772,120,1)
        elif key=='registro':
            rough(30,180,330,140);bars(50,216,230,3);rough(30,386,330,72)
            bars(30,500,290,3);rough(30,604,330,52);rough(30,684,330,52)
        elif key=='analisis':
            rough(30,166,330,120);bars(52,202,240,3);rough(30,330,330,270)
            for i,v in enumerate([90,150,110,192,80,160,120]):rough(52+i*42,560-v,20,v)
            bars(30,650,290,4)
        elif key=='sugerencias':
            rough(30,184,330,290);c.s.append('<circle cx="195" cy="276" r="40" stroke="#777A82" fill="none" stroke-width="2"/>');bars(62,368,250,3)
            rough(30,536,330,52);rough(30,620,330,52)
        else:
            rough(30,178,330,70)
            for y in [300,444,588]:rough(30,y,330,106);bars(50,y+30,210,3);rough(300,y+26,40,22)
            rough(30,738,330,52)
    return c.end()

ICONS.update({
 'calendario':'M3 5h18v16H3Z M3 10h18 M7 2v6 M17 2v6 M7 14h2 M13 14h2 M7 18h2',
 'recordatorio':'M5 17h14l-2-3V9a5 5 0 0 0-10 0v5Z M10 21h4 M12 2v2',
 'lectura':'M3 4h7l2 2 2-2h7v16h-7l-2 2-2-2H3Z M12 6v16',
 'movimiento':'M14 4a1 1 0 1 0 0-2 1 1 0 1 0 0 2 M10 8l4-2 3 5 4 1 M3 12l5-4 4 5-4 8 M12 13l5 3 1 5',
 'descanso':'M20 15A9 9 0 0 1 9 3a9 9 0 1 0 11 12Z',
 'historial':'M3 10A9 9 0 1 1 5 19 M3 3v7h7 M12 7v6l4 2',
 'ver':'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z M15 12a3 3 0 1 0-6 0 3 3 0 1 0 6 0',
 'editar':'M4 16L16 4l4 4L8 20H4Z M14 6l4 4',
 'archivar':'M3 3h18v5H3Z M5 8v13h14V8 M9 12h6',
 'descargar':'M12 2v13 M7 10l5 5 5-5 M3 16v5h18v-5',
 'sincronizar':'M3 10A9 9 0 0 1 18 5l3 3 M21 2v6h-6 M21 14A9 9 0 0 1 6 19l-3-3 M3 22v-6h6',
 'dispositivo':'M7 5h10v14H7Z M9 2h6v3 M9 19v3h6v-3 M10 9h4 M10 13h4'
})

def sheets():
    """Cuatro lienzos; el texto compartido con Figma vive en identidad.json."""
    d=json.loads((HERE/'fuente/identidad.json').read_text(encoding='utf-8'))
    def start(n,title,subtitle):
        c=Canvas(1600,6200,title)
        c.rect(0,0,1600,6200,C['white'],0,C['white'])
        logos(c,64,30,1472,96)
        c.text(744,91,f'{n:02d} / 04',22,C['steel'],600)
        c.text(64,214,title,48,weight=700)
        para(c,64,264,subtitle,1472,22,'steel')
        return c,350
    def para(c,x,y,value,w,size=22,key='obsidian',weight=400):
        rows=[]
        for line in value.split('\n'):
            rows.extend(textwrap.wrap(line,max(12,int(w/(size*.55)))) or [''])
        c.lines(x,y,rows,size,C[key],step=round(size*1.5))
        return y+len(rows)*round(size*1.5)
    def finish(c,y,path):
        c.s.append(f'<path d="M64 {y}H1536" stroke="{C["softBorder"]}"/>')
        c.text(64,y+46,'QUANTIFY CORE · SISTEMA VISUAL 04 · CLARO / OSCURO',20,C['steel'],600)
        h=int(y+90)
        svg=c.end().replace('height="6200" viewBox="0 0 1600 6200"',f'height="{h}" viewBox="0 0 1600 {h}"',1)
        SCENES[path]=svg
    def samples(c,y,typography=False):
        for dark,x in [(False,64),(True,816)]:
            ink='white' if dark else 'obsidian';sub='gray' if dark else 'steel'
            c.rect(x,y,720,410,C['midnight'] if dark else C['mist'],16,C['midnight'] if dark else C['mist'])
            c.text(x+24,y+50,'MODO OSCURO' if dark else 'MODO CLARO',24,C[ink],700)
            c.text(x+24,y+112,'Tu rutina, a tu ritmo',32,C[ink],700)
            para(c,x+24,y+160,'La misma familia y jerarquía. Cambian superficie, tinta, iconos y foco.',672,23,sub)
            c.rect(x+24,y+268,672,66,C['laserBlue'],8,C['laserBlue'])
            c.text(x+44,y+309,'Registrar avance',24,C['white'],600)
            c.icon('hoy',x+24,y+354,C['skyLaser'] if dark else C['laserBlue'],1.1)
            c.text(x+68,y+376,'Inter 400 / 500 / 600 / 700' if typography else 'Icono activo y foco visibles',21,C[sub])
        return y+450
    c,y=start(1,'Paleta de colores','La identidad se conserva; cada rol responde a su superficie. Valores, psicología y justificación por color.')
    for key,name,psychology,reason in d['colors']:
        col=C[key];rgb=[int(col[j:j+2],16) for j in (1,3,5)]
        h,l,s=colorsys.rgb_to_hls(*[v/255 for v in rgb]);k=1-max(rgb)/255
        cm=[0,0,0,100] if k==1 else [round((1-v/255-k)/(1-k)*100) for v in rgb]+[round(k*100)]
        reasonrows=textwrap.wrap(reason,82)
        psyrows=textwrap.wrap('Psicología: '+psychology,35)
        height=max(246+len(psyrows)*30,104+len(reasonrows)*33)
        c.rect(64,y,1472,height,C['mist'],12,C['mist'])
        c.rect(88,y+24,72,48,col,8,C['gray'])
        c.text(184,y+58,name,27,weight=700)
        values=f'HEX {col}\nRGB {", ".join(map(str,rgb))}\nHSL {h*360:.1f}° {s*100:.1f}% {l*100:.1f}%\nCMYK {" / ".join(map(str,cm))}%'
        para(c,88,y+111,values,440,20,'steel')
        para(c,88,y+231,'Psicología: '+psychology,440,20,'steel')
        c.text(580,y+54,'POR QUÉ Y CÓMO SE USA',22,C['laserBlue'],700)
        para(c,580,y+104,reason,924,22)
        y+=height+20
    c.text(64,y+32,'QUÉ CAMBIA AL ACTIVAR OSCURO',28,weight=700);y=samples(c,y+66)
    for label,light,dark,note in d['themes']:
        y=para(c,64,y,f'{label}: claro {C[light]} → oscuro {C[dark]}. {note}',1472,22,'steel')+10
    y=para(c,64,y+12,'Los cuatro estados conservan su matiz: badge con tinta Obsidian, forma y palabra. Psicología: intención de marca, no efecto universal. HSL desde sRGB. CMYK matemático sin perfil ICC: requiere prueba de impresión. Soft Border #D8E1F0 es decorativo; no identifica controles.',1472,21,'steel')
    finish(c,y+32,'identidad/imagenes/01-paleta-de-colores.png')
    c,y=start(2,'Tipografía · Inter','Una misma familia y jerarquía para claro y oscuro. Seis criterios explican su elección y aplicación.')
    c.text(64,y+100,'Aa · ÁÉÍÓÚÜÑ · 0123456789',72,C['laserBlue'],650);y+=170
    y=para(c,64,y,'Inter Variable local · Rasmus Andersson · SIL Open Font License\nEscala 40 / 28 / 20 / 16 / 14 · Pesos 400 / 500 / 600 / 700',1472,22,'steel')+30
    y=samples(c,y,True)
    for i in range(0,6,2):
        entries=d['typography'][i:i+2]
        height=max(104+len(textwrap.wrap(reason,54))*33 for _,reason in entries)
        for j,(title,reason) in enumerate(entries):
            x=64+j*752;c.rect(x,y,720,height,C['mist'],12,C['mist'])
            c.text(x+24,y+48,title,27,weight=700)
            para(c,x+24,y+104,reason,672,22)
        y+=height+28
    y=para(c,64,y+12,'No adelgazar ni reducir el texto al activar oscuro. La elección de Inter no modifica las letras dibujadas de los logos. El diseño no acredita clientes React o Flutter implementados: requieren pruebas de dispositivo, reflujo y tecnologías de asistencia.',1472,22,'steel')
    finish(c,y+32,'identidad/imagenes/02-tipografia.png')
    c,y=start(3,'Iconografía · 24 símbolos','Cada símbolo aparece en claro y oscuro, con el mismo trazo, nombre y función. Cambia su tinta activa.')
    y=para(c,64,y,d['iconRules'],1472,22,'steel')+28
    labels=['Inicio / Hoy','Mis hábitos','Análisis','Preferencias','Crear hábito','Confirmado','Pendiente','Aviso / error','Volver','Privacidad','Cerrar sesión','Sugerencias','Calendario','Recordatorio','Lectura','Movimiento','Descanso','Historial','Ver detalle','Editar','Archivar','Descargar','Sincronizar','Dispositivo']
    symbols=['Casa','Lista con verificación','Barras de datos','Deslizadores','Signo más','Marca de verificación','Reloj','Triángulo de alerta','Flecha a la izquierda','Escudo','Puerta con flecha','Destello','Calendario','Campana','Libro abierto','Persona caminando','Luna','Reloj con retorno','Ojo','Lápiz','Caja de archivo','Flecha hacia abajo','Flechas circulares','Reloj inteligente']
    for i,((key,path),label,symbol) in enumerate(zip(ICONS.items(),labels,symbols)):
        x=64+(i%4)*376;yy=y+(i//4)*270
        c.rect(x,yy,344,246,C['mist'],12,C['mist']);c.text(x+16,yy+35,f'{i+1:02d} {label}',22,weight=600);c.text(x+16,yy+69,symbol,17,C['steel'])
        for dark,xx in [(False,x+16),(True,x+180)]:
            c.rect(xx,yy+90,148,136,C['midnight'] if dark else C['white'],8,C['midnight'] if dark else C['white'])
            c.icon(key,xx+16,yy+108,C['skyLaser'] if dark else C['laserBlue'],2)
            c.text(xx+16,yy+204,'Oscuro' if dark else 'Claro',18,C['white'] if dark else C['obsidian'])
    y+=6*270+20;c.text(64,y+30,'ESTADOS EN LOS DOS TEMAS',28,weight=700);y+=65
    for dark,x in [(False,64),(True,816)]:
        c.rect(x,y,720,370,C['midnight'] if dark else C['mist'],16,C['midnight'] if dark else C['mist'])
        for i,(key,label,icon) in enumerate([('emerald','Confirmado','confirmado'),('amber','Pendiente','pendiente'),('crimson','Error · Reintentar','aviso'),('cyan','Métrica / sugerencia','sugerencias')]):
            yy=y+22+i*84;c.rect(x+24,yy,672,66,C[key],8,C[key]);c.icon(icon,x+40,yy+20,C['obsidian']);c.text(x+88,yy+42,label,24,C['obsidian'],600)
    y=para(c,64,y+420,'Retícula 24 × 24 · Trazo 1.8 · Extremos y uniones redondos · Objetivo táctil propuesto: 48. Los controles deben tener nombre accesible. La forma y la etiqueta mantienen el significado del estado; un icono no certifica una función de producto implementada.',1472,22,'steel')
    finish(c,y+32,'identidad/imagenes/03-iconografia.png')
    c,y=start(4,'Logotipo / isologo y marcas de agua','El mismo dibujo en ambos temas. Original claro intacto; derivado oscuro de color sobre transparencia.')
    y=para(c,64,y,d['logoRules'],1472,23,'steel')+30
    for dark in [False,True]:
        c.rect(64,y,1472,520,C['midnight'] if dark else C['mist'],16,C['midnight'] if dark else C['mist'])
        c.text(88,y+50,'MODO OSCURO · FONDO TRANSPARENTE' if dark else 'MODO CLARO · ORIGINALES',28,C['white'] if dark else C['obsidian'],700)
        logos(c,112,y+124,1376,292,dark=dark)
        c.text(112,y+460,'Empresa · Nexus Core',24,C['white'] if dark else C['obsidian'],600)
        c.text(900,y+460,'Producto · Quantify Core',24,C['white'] if dark else C['obsidian'],600)
        y+=550
    y=para(c,64,y,'Logotipo: denominación escrita. Isologo: símbolo y nombre como conjunto. No separar partes de un JPEG ni reconstruir letras. Área libre mínima: 1/4 de la altura visible de cada firma; validar legibilidad al reducir. La convivencia no crea una marca fusionada: la empresa respalda y el producto identifica la experiencia.',1472,23,'steel')+30
    c.text(64,y+30,'MARCA DE AGUA DOCUMENTAL / DOS VARIANTES',28,weight=700);y+=75
    y=para(c,64,y,d['watermarkRules'],1472,23,'steel')+30
    for dark,x in [(False,64),(True,816)]:
        c.rect(x,y,720,370,C['midnight'] if dark else C['mist'],16,C['midnight'] if dark else C['mist'])
        c.text(x+24,y+52,'Documento oscuro' if dark else 'Documento claro',28,C['white'] if dark else C['obsidian'],700)
        watermark(c,x+250,y+104,3,C['white'] if dark else '#526179')
        c.text(x+24,y+331,'Q editorial independiente · 12 %',24,C['white'] if dark else C['obsidian'])
    finish(c,y+420,'identidad/imagenes/04-identidad-isologo.png')


def main():
    import argparse
    from movil import build
    from marcas import generate
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mobile-only',action='store_true',help='Generar solo el catálogo móvil, sin identidad ni escritorio.')
    parser.add_argument('--brand-only',action='store_true',help='Solo aplicaciones afectadas por las variantes oscuras de marca.')
    args=parser.parse_args()
    generate(ROOT)
    mobile,manifest=build(Canvas,C,ICONS,logos,photo,HERE/'prototipos/movil')
    SCENES.update(mobile)
    if not args.mobile_only:sheets()
    if args.brand_only:
        for admin,key in [(False,'hoy-escritorio'),(True,'administracion')]:
            SCENES[f'prototipos/mockups/{key}-dark.png']=desktop('dark','mockup',admin)
        affected={'identidad/imagenes/01-paleta-de-colores.png','identidad/imagenes/04-identidad-isologo.png','prototipos/mockups/hoy-escritorio-dark.png','prototipos/mockups/administracion-dark.png'}
        for name in list(SCENES):
            if '/mockups/dark/' not in name and name not in affected:del SCENES[name]
    # Adaptador CSS documental; todavía no hay clientes de producto consumidores.
    css=[]
    role_names={'icon':'icon-active','iconMuted':'icon-muted','statusInk':'status-ink'}
    for theme,roles in TOKENS['themes'].items():
        selector=':root, [data-qc-theme="light"]' if theme=='light' else '[data-qc-theme="dark"]'
        css.append(selector+' {')
        for role,key in roles.items():
            name=role_names.get(role,''.join('-'+ch.lower() if ch.isupper() else ch for ch in role))
            css.append('  --qc-'+name+': '+C[key]+';')
        css.append('}')
    if not args.mobile_only:write(ROOT/'packages/design-tokens/themes.css','\n'.join(css)+'\n')
    BUILD.mkdir(exist_ok=True)
    (BUILD/'escenas.json').write_text(json.dumps(SCENES,ensure_ascii=False),encoding='utf-8')
    data=[dict(id=s['id'],number=s['number'],title=s['title'],rf=s['rf'],reference=s['ref'],note=s['note'],intent=s['intent'],assets=s['assets'],width=s['width'],height=s['height']) for s in manifest]
    # Únicamente las dos vistas de escritorio ya existentes; no se regeneran.
    data.append(dict(id='administracion',title='Operación con trazabilidad',rf='RF-09 / RF-10',reference='A02 / A03 / A06',note='Referencia de escritorio anterior, fuera de la revisión móvil.',legacyDesktop=True))
    html=(HERE/'index.html').read_text(encoding='utf-8')
    import re
    html=re.sub(r'<script id="screen-data" type="application/json">.*?</script>', '<script id="screen-data" type="application/json">'+json.dumps(data,ensure_ascii=False)+'</script>',html,flags=re.S)
    (HERE/'index.html').write_text(html,encoding='utf-8')
    print(f'{len(SCENES)} escenas listas. Móvil: sketches sin texto, wireframes Arial y mockups Inter.')

if __name__=='__main__':main()
