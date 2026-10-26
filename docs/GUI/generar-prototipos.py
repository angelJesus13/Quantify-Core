"""Genera recursos de revisión SVG/CSS desde preview.json. Python 3, sin paquetes.
No escribe en prácticas, aplicaciones ni activos heredados.
"""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / 'docs/GUI'
DESIGN = ROOT / 'docs/diseno/recursos'
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
        self.w,self.h,self.fidelity=w,h,fidelity
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
        self.s.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" fill="{color or self.p["text"]}" font-weight="{weight}">{escape(str(t))}</text>')
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
        self.text(24,self.h-18,'PROPUESTA · Datos sintéticos · 26 oct 2026',12,self.p['muted'])
    def end(self): return ''.join(self.s)+'</svg>'

def screen(key,theme,fidelity):
    title=next(x[1] for x in SCREENS if x[0]==key)
    if key=='administracion': return desktop(theme,fidelity,True)
    c=Canvas(390,844,title,theme,fidelity)
    c.text(24,36,'QUANTIFY CORE',16,weight=700)
    c.text(24,68,f'{fidelity.upper()} / MÓVIL',12,c.p['muted'])
    c.text(24,116,title,24,weight=700)
    if fidelity=='sketch':
        c.lines(24,151,['Intención: '+{'acceso':'entrar sin fricción','hoy':'priorizar el siguiente avance','habito':'definir una meta clara','registro':'entender qué se enviará','analisis':'leer el periodo correcto','sugerencias':'explicar la abstención','ajustes':'elegir cada finalidad'}[key]],14)
        blocks={
          'acceso':[('Promesa de producto','Hábitos y evidencia comprensible'),('Identidad centralizada','Continuar con Keycloak'),('Salida segura','Cancelar y volver a bienvenida')],
          'hoy':[('Resumen del día abierto','Metas confirmadas por separado'),('Lista de hábitos programados','Nombre, unidad, valor y estado'),('Siguiente acción','Abrir detalle o crear hábito')],
          'habito':[('Definición del hábito','Nombre, meta y unidad'),('Agenda semanal','Días y zona de agenda'),('Cierre del borrador','Guardar válido o cancelar')],
          'registro':[('Contexto del registro','Meta histórica y fecha de negocio'),('Valor acumulado absoluto','Último confirmado y nuevo valor'),('Resultado verificable','Confirmado, pendiente o conflicto')],
          'analisis':[('Ventana cerrada','Periodo y zona de cálculo'),('Métrica con alternativa textual','Completas / programadas'),('Procedencia y siguiente consulta','Fuente, regla y otro periodo')],
          'sugerencias':[('Finalidad voluntaria','Consentimiento y elegibilidad'),('Abstención explicada','Datos insuficientes sin inventarlos'),('Opciones del usuario','Revisar hábitos o consentimiento')],
          'ajustes':[('Preferencias de cuenta','Zona del perfil sin mover historia'),('Finalidades separadas','Análisis y cada fuente biométrica'),('Decisión explícita','Guardar, revocar o cancelar')]
        }[key]
        for y,(t,s) in zip([192,324,456],blocks):
            c.card(y,t,s,'Bloque de composición')
        c.button(24,612,342,'Acción principal →')
        c.lines(24,704,['Referencia histórica: '+next(x[3] for x in SCREENS if x[0]==key),'Redibujo conceptual; no copia la paleta','ni las reglas de la Práctica 07.'],14)
    elif key=='acceso':
        c.lines(24,164,['Pequeños hábitos.','Evidencia que puedes entender.'],20)
        c.rect(24,226,342,176,c.p['surface'])
        for i,h in enumerate([38,70,102,126]): c.rect(58+i*68,370-h,32,h,c.p['action'],5,c.p['action'])
        c.text(42,390,'Registrar · comprender · ajustar',14)
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
    c.footer()
    return c.end()

def desktop(theme,fidelity,admin=False):
    c=Canvas(1440,900,'Administración' if admin else 'Hoy · Escritorio',theme,fidelity)
    c.rect(0,0,248,900,r=0)
    c.text(30,56,'QUANTIFY',26,weight=700);c.text(30,83,'CORE / '+('OPERACIÓN' if admin else 'PERSONAL'),14,c.p['muted'])
    items=[('hoy','Resumen' if admin else 'Hoy'),('habitos','Catálogo' if admin else 'Mis hábitos'),('analisis','Auditoría' if admin else 'Análisis'),('ajustes','Configuración')]
    for i,(icon,label) in enumerate(items):
        y=150+i*66
        if i==0:c.rect(16,y-30,216,52,c.p['action'],8,c.p['action'])
        color=c.p['onAction'] if i==0 else c.p['text'];c.icon(icon,30,y-17,color);c.text(70,y,label,16,color,600)
    c.text(30,823,'Datos sintéticos',14,c.p['muted'])
    c.text(288,54,'ESTUDIO DE INTERFAZ / '+fidelity.upper(),14,c.p['muted'])
    c.text(288,112,'Operación con trazabilidad' if admin else 'Tu rutina, a tu ritmo',36,weight=700)
    c.text(288,152,'Solo agregados autorizados · Sin acceso a rutinas privadas' if admin else 'Lunes 26 octubre 2026 · America/Mexico_City · Día abierto',16,c.p['muted'])
    c.button(1110,82,282,'Consultar auditoría' if admin else '+ Crear hábito')
    for i,(label,value,sub) in enumerate([('Catálogo','12 plantillas','Ejemplo agregado'),('Estado','Disponible','Sin datos personales'),('Control','Motivo requerido','Operaciones auditadas')] if admin else [('Hoy','1 / 3','Metas confirmadas'),('Último periodo','71.4 %','5 / 7 · 19–25 octubre'),('Sincronización','Al día','Solo datos confirmados')]):
        x=288+i*374;c.rect(x,200,350,146);c.text(x+24,232,label,16,c.p['muted']);c.text(x+24,279,value,28,weight=700);c.text(x+24,316,sub,14,c.p['muted'])
    c.rect(288,378,722,340);c.text(312,420,'Catálogo de plantillas' if admin else 'Programados para hoy',24,weight=700)
    for i,(name,desc) in enumerate([('Pausa consciente','Activa · Versión 2'),('Lectura diaria','Activa · Versión 1'),('Movimiento','Pausada · Versión 3')] if admin else [('Leer con calma','10 / 20 minutos · Parcial confirmado'),('Caminar','30 / 30 minutos · Meta confirmada'),('Pausa consciente','Sin registro · Meta de 5 minutos')]):
        y=452+i*76;c.rect(312,y,674,64,r=8);c.text(330,y+25,name,18,weight=600);c.text(330,y+49,desc,14,c.p['muted']);c.text(847,y+37,'Revisar →' if admin else 'Abrir →',16)
    c.rect(1034,378,378,340);c.text(1058,421,'Antes de confirmar' if admin else 'Una pausa también suma',22,weight=600)
    c.lines(1058,466,['Indica el motivo del cambio.','Cancelar no modifica la plantilla.','El historial se conserva.','Editar no cambia hábitos creados.'] if admin else ['Elige un hábito y registra','su valor acumulado del día.','Hoy se muestra por separado','de tus métricas de días cerrados.'],16)
    c.button(1058,620,330,'Revisar cambio' if admin else 'Ver mi progreso',False)
    c.rect(288,750,1124,82);c.icon('privacidad' if admin else 'pendiente',310,774)
    c.lines(352,780,['La API debe comprobar permiso, motivo y revisión antes de aplicar el cambio.','Vista de diseño: no ejecuta operaciones ni consulta cuentas reales.'] if admin else ['Respuesta perdida: aún no pudimos confirmar el guardado.','Reintentar conserva la misma clave; un conflicto requiere revisar la versión.'],16)
    c.footer();return c.end()

def board(title,subtitle):
    c=Canvas(1200,900,title);c.text(48,58,'QUANTIFY CORE / MANUAL VISUAL',14,c.p['action'],700)
    c.text(48,122,title,40,weight=700);c.text(48,162,subtitle,18,c.p['muted']);return c

def assets():
    c=board('01 / Paleta y tipografía','Color de identidad existente · Escalas de interfaz propuestas')
    names=list(C.items())
    for i,(name,col) in enumerate(names):
        x=48+(i%7)*160;y=210+(i//7)*140
        c.rect(x,y,136,72,col,8,col);c.text(x,y+98,name,15,weight=600);c.text(x,y+120,col,14)
    c.text(48,552,'Segoe UI / Arial / sans-serif',36,weight=700)
    c.text(48,598,'Aa Bb Cc Ññ · Hábitos, acción y constancia',28)
    c.text(48,642,'ABCDEFGHIJKLMNOPQRSTUVWXYZ · 0123456789 · ¿Qué sigue?',20)
    c.lines(48,700,['40 / Presentación   28 / Pantalla   20 / Sección   16 / Cuerpo   14 / Ayuda','Pesos 400, 600 y 700 · Texto base 16 · Sin descarga de fuentes','Laser Blue + blanco: 6.28:1 · Cool Gray se reserva al tema oscuro.'],18)
    c.footer();write(DESIGN/'paleta-tipografia.svg',c.end())
    c=board('02 / Iconografía y componentes','Trazos originales de propuesta · Retícula 24 × 24 · Trazo 1.8 · Contenedor táctil 48')
    for i,name in enumerate(ICONS):
        x=48+(i%6)*188;y=220+(i//6)*130
        c.rect(x,y,160,102);c.icon(name,x+16,y+16,c.p['action'],1.5);c.text(x+12,y+83,name,15)
    c.button(48,532,310,'Guardar hábito');c.button(390,532,310,'Cancelar',False)
    c.card(622,'Leer con calma','10 / 20 minutos · Parcial','Confirmado',48,500)
    c.lines(600,650,['✓ Confirmado','◷ Pendiente de sincronizar','! Error: revisar el dato'],18)
    c.lines(48,786,['Iconos siempre con etiqueta en acciones; decorativos ocultos a lectores.','El color acompaña al texto del estado. No se incorporó una biblioteca externa.'],16)
    c.footer();write(DESIGN/'iconografia.svg',c.end())
    c=board('03 / Identidad e imagen','Original preservado · Nuevas aplicaciones sujetas a revisión de marca')
    c.rect(48,210,520,270,'#FFFFFF')
    # Original raster embedded to make the exported sheet self contained.
    import base64
    logo=base64.b64encode((ROOT/'assets/images/quantifyLogo.jpeg').read_bytes()).decode()
    c.s.append(f'<image x="88" y="226" width="440" height="220" href="data:image/jpeg;base64,{logo}"/>')
    c.text(72,464,'Marca heredada · Sin recolorear ni deformar',16)
    c.rect(600,210,552,270,C['obsidian'])
    c.s.append(f'<circle cx="690" cy="315" r="38" fill="none" stroke="{C["skyLaser"]}" stroke-width="12"/><path d="M709 338l23 23" stroke="{C["skyLaser"]}" stroke-width="12"/>')
    c.text(762,315,'QUANTIFY',32,C['white'],700);c.text(762,350,'CORE',24,C['white'],600)
    c.text(624,442,'Isologo Q + nombre / propuesta para fondo oscuro',16,C['white'])
    c.lines(48,550,['Área libre propuesta: 1 altura de Q alrededor de la marca.','Mínimo propuesto: 160 px para la marca completa; símbolo 24 px.','Usar el original sobre una placa blanca también en tema oscuro.','No alterar proporciones, recortar letras, añadir sombras ni usarlo como icono de acción.'],18)
    for i,h in enumerate([35,56,82,108]): c.rect(76+i*72,816-h,40,h,C['laserBlue'],8,C['laserBlue'])
    c.lines(460,730,['Imagen de producto: ilustración geométrica original.','No representa mediciones reales ni evidencia biométrica.','Sin fotografías de personas ni imágenes externas añadidas.'],18)
    c.footer();write(DESIGN/'identidad-imagen.svg',c.end())
    # Reusable proposal mark and illustration, independent from the historic logo.
    write(DESIGN/'isologo-propuesto.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="120" viewBox="0 0 480 120" role="img" aria-label="Propuesta de isologo Quantify Core"><rect width="480" height="120" rx="16" fill="{C["obsidian"]}"/><circle cx="60" cy="54" r="28" fill="none" stroke="{C["skyLaser"]}" stroke-width="9"/><path d="M78 76l19 19" stroke="{C["skyLaser"]}" stroke-width="9"/><text x="126" y="57" fill="white" font-family="Segoe UI,Arial,sans-serif" font-size="36" font-weight="700">QUANTIFY</text><text x="126" y="89" fill="white" font-family="Segoe UI,Arial,sans-serif" font-size="24">CORE</text></svg>')
    write(DESIGN/'constancia.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="240" viewBox="0 0 480 240" role="img" aria-label="Ilustración conceptual de constancia, sin datos reales"><rect width="480" height="240" rx="24" fill="{C["mist"]}"/>'+''.join(f'<rect x="{65+i*92}" y="{200-h}" width="48" height="{h}" rx="10" fill="{C["laserBlue"]}"/>' for i,h in enumerate([48,85,120,160]))+'</svg>')
    for name,path in ICONS.items():
        write(DESIGN/f'iconos/{name}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="img" aria-label="{name}"><path d="{path}" fill="none" stroke="{C["laserBlue"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def main():
    manifest=[]
    for key,title,rf,ref,note in SCREENS:
        item=dict(id=key,title=title,rf=rf,reference=ref,note=note,variants={})
        for fidelity in ['sketch','wireframe','mockup']:
            for theme in (['light','dark'] if fidelity=='mockup' else ['light']):
                folder={'sketch':'sketches','wireframe':'wireframes','mockup':'mockups'}[fidelity]
                filename=f'{folder}/{key}-{theme}.svg'
                write(HERE/filename,screen(key,theme,fidelity))
                item['variants'][f'{fidelity}-{theme}']=filename
        manifest.append(item)
    for theme in ['light','dark']:write(HERE/f'mockups/hoy-escritorio-{theme}.svg',desktop(theme,'mockup'))
    write(HERE/'pantallas.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    write(HERE/'pantallas.js','window.QC_SCREENS = '+json.dumps(manifest,ensure_ascii=False,indent=2)+';\n')
    css='/* Generado por docs/GUI/generar-prototipos.py desde preview.json; solo revisión. */\n'
    for theme,mapping in TOKENS['themes'].items():
        css+=f':root[data-theme="{theme}"]'+'{'+''.join(f'--{k}:{C[v]};' for k,v in mapping.items())+'}\n'
    write(HERE/'tokens-preview.css',css)
    assets()
    print('34 pantallas SVG, 17 recursos de diseño, manifiestos y CSS generados.')

if __name__=='__main__':main()
