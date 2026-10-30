"""Veinte intenciones móviles; una misma estructura atraviesa tres fidelidades.

Los sketches dibujan únicamente cuadros y líneas. Los wireframes concretan la
estructura con Arial y grises; los mockups aplican los activos canónicos.
"""
import json
import random
import re
import textwrap
from html import escape


def b(kind, height, title='', text='', **extra):
    return dict(kind=kind, height=height, title=title, text=text, **extra)


CATALOG = [
    dict(id='bienvenida', title='Cada avance cuenta', rf='RF-01', ref='U01', intent='Presentar el producto y conducir al acceso centralizado.', note='La bienvenida no solicita credenciales ni concede una sesión.', blocks=[
        b('photo',150), b('copy',74,'Hábitos con intención','Registra tu rutina y comprende tu progreso, a tu ritmo.'), b('benefit',78,'Un espacio para tus hábitos','Organiza, registra y revisa lo que importa.',icon='habitos'), b('button',48,'Empezar',target='acceso'), b('secondary',44,'Conocer mi privacidad',target='consentimiento')]),
    dict(id='acceso', title='Accede a tu espacio', rf='RF-01', ref='U02–U05 / U15', intent='Iniciar el flujo de identidad con Keycloak y regresar al cliente.', note='No hay formulario local de contraseña, registro ni recuperación paralelos; se delegan al proveedor.', blocks=[
        b('empty',148,'Una cuenta, un solo acceso','Continúa con el servicio de identidad para entrar a tu espacio.',icon='privacidad'), b('notice',72,'Tú controlas tus datos','Tus hábitos y preferencias pertenecen a tu cuenta.'), b('button',48,'Continuar con Keycloak',target='hoy'), b('secondary',44,'Volver a bienvenida',target='bienvenida')]),
    dict(id='hoy', title='Tu rutina de hoy', rf='RF-03 / RF-04', ref='U06', intent='Consultar lo programado para el día abierto y abrir un hábito.', note='Ejemplo del 26/10/2026, America/Mexico_City. Separar día abierto y periodo cerrado.', blocks=[
        b('summary',80,'1 de 3 metas completas','Hoy · 26 octubre · Día abierto'), b('habit',80,'Leer con calma','10 / 20 minutos · Parcial confirmado',icon='lectura',target='detalle'), b('habit',80,'Caminar','30 / 30 minutos · Meta completa',icon='movimiento',target='detalle'), b('habit',80,'Pausa consciente','Sin registro · Meta de 5 minutos',icon='descanso',target='detalle'), b('button',48,'Crear hábito',target='habito')]),
    dict(id='habitos', title='Mis hábitos', rf='RF-03', ref='U06 / U08', intent='Encontrar hábitos propios y distinguir los activos de los archivados.', note='La búsqueda y el filtro son controles propuestos, sin consulta a cuentas reales.', blocks=[
        b('field',64,'Buscar por nombre','Leer, caminar, descansar…'), b('tabs',46,options=['Activos','Archivados']), b('habit',76,'Leer con calma','Diario · 20 minutos',icon='lectura',target='detalle'), b('habit',76,'Caminar','Lunes y jueves · 30 minutos',icon='movimiento',target='detalle'), b('habit',76,'Pausa consciente','Diario · 5 minutos',icon='descanso',target='detalle'), b('button',48,'Crear un hábito',target='habito')]),
    dict(id='habito', title='Crear hábito', rf='RF-03', ref='U07', intent='Definir nombre, meta, unidad, días y zona de un hábito nuevo.', note='Guardar requiere validación y confirmación del servidor; cancelar vuelve a Hoy sin crear.', blocks=[
        b('field',64,'Nombre','Leer con calma'), b('field',64,'Meta y unidad','20 minutos'), b('days',66,'Días programados'), b('field',64,'Zona de agenda','America/Mexico_City'), b('notice',82,'Tu programación','Se aplicará a nuevos periodos; el historial se conserva.'), b('button',48,'Guardar hábito',target='detalle'), b('secondary',40,'Cancelar creación',target='hoy')]),
    dict(id='detalle', title='Leer con calma', rf='RF-03 / RF-04', ref='U08', intent='Consultar la meta y el avance confirmado de un hábito antes de actuar.', note='No recalcular registros pasados con una nueva meta. Archivar conserva el historial y requiere confirmación.', blocks=[
        b('habit',92,'Lectura diaria','20 minutos · Todos los días',icon='lectura'), b('summary',84,'10 de 20 minutos','Parcial confirmado · 26 octubre'), b('button',48,'Registrar avance',target='registro'), b('row',62,'Historial de lectura','Consultar registros anteriores',target='historial'), b('row',62,'Recordatorio','Elegir horario y días',target='recordatorio'), b('secondary',44,'Editar programación',target='editar')]),
    dict(id='editar', title='Editar programación', rf='RF-03', ref='U07 / U08', intent='Revisar cambios de meta y frecuencia conservando la configuración histórica.', note='Una versión obsoleta requiere revisar el conflicto. Cancelar edición regresa a Detalle.', blocks=[
        b('notice',110,'Tu historial queda intacto','La nueva programación aplica hacia adelante, desde su fecha de vigencia.'), b('field',64,'Nombre del hábito','Leer con calma'), b('field',64,'Nueva meta','25 minutos'), b('days',66,'Días de la nueva versión'), b('button',48,'Revisar y guardar cambios',target='detalle'), b('secondary',44,'Cancelar edición',target='detalle')]),
    dict(id='registro', title='Registrar avance', rf='RF-04', ref='U08', intent='Enviar el valor acumulado absoluto para la fecha de negocio del hábito.', note='Enviar 15 dos veces no suma 30. Reintentar tras respuesta perdida conserva idempotencia; un conflicto requiere revisión.', blocks=[
        b('habit',84,'Leer con calma','26 octubre · Meta de 20 minutos',icon='lectura'), b('field',72,'Minutos acumulados del día','15'), b('notice',110,'Se guardarán 15 en total','Este valor sustituye el acumulado de hoy; no se sumará como otro registro.'), b('button',48,'Confirmar valor acumulado',target='detalle'), b('secondary',44,'Volver sin cambios',target='detalle')]),
    dict(id='historial', title='Historial de lectura', rf='RF-04 / RF-05', ref='U08 / U10', intent='Revisar fechas, cantidades y estado confirmado de un hábito.', note='Los registros son ejemplos sintéticos; no se inventan señales biométricas.', blocks=[
        b('field',64,'Periodo de consulta','19–25 octubre 2026'), b('summary',78,'5 de 7 metas completas','Solo oportunidades cerradas'), b('row',72,'Domingo 25 · Sin completar','0 / 20 minutos · Día cerrado'), b('row',72,'Sábado 24 · Meta completa','20 / 20 minutos · Confirmado'), b('row',72,'Viernes 23 · Meta completa','20 / 20 minutos · Confirmado'), b('secondary',44,'Ver análisis del periodo',target='analisis')]),
    dict(id='recordatorio', title='Tu recordatorio', rf='RF-06', ref='U09', intent='Configurar un recordatorio dentro de los días programados del hábito.', note='No seleccionar días ajenos a la agenda. Comprobar permisos del canal y zona; no se promete entrega operativa.', blocks=[
        b('field',64,'Hábito','Leer con calma'), b('field',64,'Hora de tu zona','20:00 · America/Mexico_City'), b('days',66,'Días del recordatorio'), b('notice',110,'Permiso para avisarte','Revisa las notificaciones del dispositivo. Puedes desactivar este recordatorio cuando quieras.'), b('button',48,'Guardar recordatorio',target='detalle'), b('secondary',40,'Cancelar',target='detalle')]),
    dict(id='avisos', title='Tus avisos', rf='RF-06', ref='U14', intent='Revisar recordatorios y abrir el hábito al que pertenece cada aviso.', note='Avisos de ejemplo; las preferencias, horario y permiso deben respetarse en producto.', blocks=[
        b('tabs',46,options=['Todos','Sin leer']), b('benefit',104,'Un momento para leer','Leer con calma · Hoy, 20:00\nAbre tu hábito cuando estés listo.',icon='recordatorio',target='detalle'), b('benefit',104,'Tu horario está guardado','Puedes cambiarlo desde el recordatorio de tu hábito.',icon='calendario',target='recordatorio'), b('secondary',44,'Revisar mis recordatorios',target='recordatorio')]),
    dict(id='analisis', title='Observa tu constancia', rf='RF-05', ref='U10', intent='Interpretar cumplimiento de un periodo cerrado, con fecha, fuente y unidad.', note='19–25/10/2026: 1,1,0,1,1,1,0; 5/7=71.4 %. Racha de ese periodo: 0 al cierre; RN-P17.', blocks=[
        b('summary',80,'Cumplimiento: 71.4 %','5 de 7 oportunidades · 19–25 octubre'), b('chart',170,'Metas completas por día'), b('notice',78,'Solo días cerrados','Datos de registros confirmados. La racha al cierre de este periodo es 0.'), b('row',62,'Hábito consultado','Leer con calma · minutos',target='historial'), b('secondary',44,'Cambiar periodo',target='periodo')]),
    dict(id='periodo', title='Elige un periodo', rf='RF-05', ref='U10', intent='Elegir una ventana de análisis sin mezclar días abiertos y cerrados.', note='Validar inicio≤fin y zona de negocio. No reinterpretar el historial al cambiar zona del perfil.', blocks=[
        b('field',64,'Desde','19 octubre 2026'), b('field',64,'Hasta','25 octubre 2026'), b('field',64,'Hábito','Leer con calma'), b('notice',110,'Una comparación consistente','La ventana utiliza America/Mexico_City y oportunidades ya cerradas.'), b('button',48,'Aplicar periodo',target='analisis'), b('secondary',44,'Cancelar selección',target='analisis')]),
    dict(id='sugerencias', title='Ideas para tu rutina', rf='RF-07', ref='U11', intent='Explicar la ausencia de una recomendación cuando no hay datos suficientes.', note='Abstenerse sin inventar IA ni umbrales. El diseño de personalización es una vista condicional separada.', blocks=[
        b('empty',164,'Aún faltan datos','Sigue registrando tus hábitos. Cuando haya información suficiente podrás revisar sugerencias.',icon='sugerencias'), b('notice',82,'Las ideas son voluntarias','Tú decides si revisarlas y adaptarlas a tu rutina.'), b('button',48,'Revisar mis hábitos',target='habitos'), b('secondary',44,'Revisar consentimiento',target='consentimiento')]),
    dict(id='personalizar', title='Personaliza una idea', rf='RF-07 / RF-03', ref='U11 → U07', intent='Adaptar una sugerencia disponible antes de guardarla y aceptarla.', note='Vista condicional de una idea de ejemplo, no resultado de un modelo. Guardar confirma aceptación; cancelar no la acepta.', blocks=[
        b('benefit',96,'Una pausa entre tareas','Idea de ejemplo · Puedes cambiarla antes de decidir.',icon='descanso'), b('field',64,'Nombre de tu versión','Pausa consciente'), b('field',64,'Meta y unidad','5 minutos'), b('days',66,'Días que te funcionan'), b('button',48,'Guardar y aceptar',target='detalle'), b('secondary',44,'Cancelar sin aceptar',target='sugerencias')]),
    dict(id='ajustes', title='Perfil y preferencias', rf='RF-02', ref='U12', intent='Ajustar datos del perfil, zona preferida y apariencia con guardado explícito.', note='Cambiar zona no reclasifica fechas históricas. Los controles de tema son diseño, no un cliente implementado.', blocks=[
        b('field',64,'Nombre para mostrar','Mi espacio'), b('field',64,'Zona preferida','America/Mexico_City'), b('tabs',58,'Apariencia',options=['Claro','Oscuro']), b('row',68,'Privacidad y consentimiento','Revisar finalidades y permisos',target='consentimiento'), b('button',48,'Guardar preferencias',target='hoy'), b('secondary',44,'Cancelar cambios',target='hoy')]),
    dict(id='consentimiento', title='Tú decides qué compartir', rf='RF-02 / RF-08', ref='U12', intent='Revisar finalidades y dar o retirar consentimiento por uso y fuente.', note='Revocar bloquea nuevos usos y trabajos. No inferir permiso de biometría por aceptar sugerencias.', blocks=[
        b('toggle',100,'Sugerencias personalizadas','Opcional · Usar mis hábitos para propuestas.',enabled=False), b('toggle',100,'Señales del dispositivo','Opcional · Requiere fuente vinculada y permiso.',enabled=False), b('notice',82,'Puedes cambiar de decisión','Retirar un permiso detiene nuevos usos de esa finalidad.'), b('button',48,'Guardar mi decisión',target='ajustes'), b('secondary',44,'Gestionar mis datos',target='datos')]),
    dict(id='dispositivos', title='Tus dispositivos', rf='RF-08', ref='Recorrido Wear OS', intent='Consultar fuentes vinculadas y comenzar la asociación de una fuente compatible.', note='No inventar telemetría ni mediciones. La vinculación requiere capacidades y consentimiento explícitos.', blocks=[
        b('empty',156,'Aún no hay dispositivos','Vincula una fuente compatible solo si deseas compartir sus señales.',icon='dispositivo'), b('benefit',94,'Permisos por fuente','Puedes revisar y retirar cada finalidad por separado.',icon='privacidad',target='consentimiento'), b('button',48,'Vincular dispositivo',target='vincular'), b('secondary',44,'Volver a preferencias',target='ajustes')]),
    dict(id='vincular', title='Vincula una fuente', rf='RF-08 / RF-02', ref='Recorrido Wear OS', intent='Revisar compatibilidad y permisos antes de confirmar una asociación.', note='No fija OTP, QR, Bluetooth ni protocolo aún pendiente. Confirmación de diseño; no conecta hardware.', blocks=[
        b('steps',62,options=['Fuente','Permisos','Confirmar']), b('benefit',104,'Dispositivo de ejemplo','Wear OS · Compatibilidad por comprobar.',icon='dispositivo'), b('toggle',108,'Permitir esta finalidad','Revisa las señales y su uso antes de autorizar.',enabled=False), b('button',48,'Revisar asociación',target='dispositivos'), b('secondary',44,'Cancelar vinculación',target='dispositivos')]),
    dict(id='datos', title='Tus datos personales', rf='RF-02 / RF-10', ref='Solicitud personal', intent='Solicitar una copia o iniciar una solicitud de eliminación de datos propios.', note='Revisar alcance y política; la eliminación requiere confirmación específica posterior. Ninguna imagen ejecuta solicitudes.', blocks=[
        b('benefit',106,'Una copia para ti','Reúne tus registros y preferencias. Podrás consultar el estado de tu solicitud.',icon='descargar'), b('button',48,'Solicitar una copia',target='datos'), b('notice',122,'Eliminar tus datos','Antes de confirmar, revisa qué se elimina, qué se conserva por política y las consecuencias.'), b('secondary',48,'Revisar solicitud de eliminación',target='datos'), b('row',64,'Tu privacidad','Volver a finalidades y permisos',target='consentimiento')]),
]


def geometry(spec):
    """Mismos bloques y posiciones para sketch, wireframe y ambos temas."""
    y=150
    result=[]
    for index,block in enumerate(spec['blocks']):
        height=max(block['height'],114) if block['kind']=='notice' else block['height']
        result.append(dict(id=f"{spec['id']}-{index+1:02d}",x=24,y=y,w=342,h=height,**block))
        y+=height+12
    if y>770:raise ValueError(f"{spec['id']}: contenido invade navegación ({y})")
    return result


def render(spec, fidelity, theme, Canvas, colors, icons, logos, photo):
    c=Canvas(390,844,spec['title'],theme,fidelity)
    p=c.p;mock=fidelity=='mockup';sketch=fidelity=='sketch'
    if not mock:p.update(icon='#202020',iconMuted='#454545',controlBorder='#777777',statusInk='#202020')
    rng=random.Random(spec['id'])
    c.s[0]=c.s[0].replace('role="img"',f'data-screen="{spec["id"]}" data-fidelity="{fidelity}" role="img"')
    def rough(x,y,w,h):
        pts=[(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)]
        for off in (0,1.1):
            points=' '.join(f'{xx+rng.uniform(-1,1)+off:.1f},{yy+rng.uniform(-1,1):.1f}' for xx,yy in pts)
            c.s.append(f'<polyline points="{points}" stroke="#666666" stroke-width="{1.1 if not off else .45}" fill="none"/>')
    def bar(x,y,w,n=1):
        for i in range(n):
            ww=w*(1 if i==0 else .72)
            c.s.append(f'<path d="M{x} {y+12*i} L{x+ww} {y+12*i}" fill="none" stroke="#777777" stroke-width="2"/>')
    def txt(x,y,value,size=16,key='text',weight=400,w=310):
        lines=[]
        for line in value.split('\n'):lines.extend(textwrap.wrap(line,max(10,int(w/(size*.52)))) or [''])
        c.lines(x,y,lines,size,p.get(key,key),step=round(size*1.4)) if weight==400 else [c.text(x,y+i*round(size*1.4),line,size,p.get(key,key),weight) for i,line in enumerate(lines)]
    def placeholder(x,y,w,h):
        c.rect(x,y,w,h,p['surface'],0,p['line'])
        c.s.append(f'<path d="M{x} {y}L{x+w} {y+h}M{x+w} {y}L{x} {y+h}" stroke="{p["line"]}" fill="none"/>')
    if sketch:
        rough(24,20,128,48);rough(238,20,128,48);bar(24,110,264,2)
    else:
        if mock:logos(c,24,14,342,58)
        else:placeholder(24,20,128,46);placeholder(238,20,128,46)
        txt(24,117,spec['title'],24,weight=700,w=342)
    for item in geometry(spec):
        x,y,w,h=item['x'],item['y'],item['w'],item['h'];kind=item['kind']
        c.s.append(f'<g data-block="{item["id"]}" data-kind="{kind}" data-box="{x},{y},{w},{h}">')
        if sketch:
            if kind in ('copy','notice'):rough(x,y,w,h);bar(x+14,y+22,w-60,2 if h<80 else 3)
            elif kind=='photo':rough(x,y,w,h);c.s.append(f'<path d="M{x} {y}L{x+w} {y+h}M{x+w} {y}L{x} {y+h}" stroke="#888888" fill="none"/>')
            elif kind in ('tabs','days','steps'):
                count=7 if kind=='days' else len(item.get('options',[]));cw=(w-(count-1)*6)/count
                for i in range(count):rough(x+i*(cw+6),y+18,cw,h-20)
                if item['title']:bar(x,y+5,150)
            elif kind=='chart':
                rough(x,y,w,h);bar(x+16,y+22,210)
                for i,v in enumerate([1,1,0,1,1,1,0]):rough(x+22+i*43,y+h-26-v*80,20,max(2,v*80))
            else:
                rough(x,y,w,h)
                if kind=='field':bar(x+12,y+16,100);rough(x+10,y+24,w-20,h-32);bar(x+22,y+44,170)
                elif kind in ('button','secondary'):bar(x+36,y+h/2,w-90)
                elif kind=='empty':rough(x+w/2-20,y+14,40,40);bar(x+28,y+80,w-56,3)
                elif kind=='toggle':bar(x+12,y+24,w-90,2);rough(x+w-60,y+14,44,24)
                elif kind in ('habit','benefit'):rough(x+14,y+18,30,30);bar(x+58,y+28,w-86,2)
                else:bar(x+14,y+26,w-46,2)
        elif kind=='photo':
            if mock:photo(c,x,y,w,h)
            else:placeholder(x,y,w,h)
        elif kind in ('button','secondary'):
            primary=kind=='button';c.rect(x,y,w,h,p['action'] if primary else p['surface'],8 if mock else 0,p['action'] if primary else p['line'])
            txt(x+14,y+h/2+6,item['title'],16,'onAction' if primary else 'text',600,w-28)
        elif kind=='field':
            txt(x,y+14,item['title'],14,weight=600);c.rect(x,y+23,w,h-24,p['surface'],8 if mock else 0,p.get('controlBorder',p['line']))
            txt(x+12,y+49,item['text'],15,w=w-24)
        elif kind in ('days','tabs','steps'):
            if item['title']:txt(x,y+14,item['title'],14,weight=600)
            opts=['L','M','X','J','V','S','D'] if kind=='days' else item['options'];top=22 if item['title'] else 0
            cw=(w-(len(opts)-1)*6)/len(opts)
            for i,label in enumerate(opts):
                selected=kind=='days' or i==0;fill=p['action'] if selected else p['surface'];ink=p['onAction'] if selected else p['text']
                c.rect(x+i*(cw+6),y+top,cw,h-top,fill,6 if mock else 0,p['line']);txt(x+i*(cw+6)+10,y+top+(h-top)/2+5,label,14,ink,w=cw-16)
        elif kind=='chart':
            c.rect(x,y,w,h,p['surface'],12 if mock else 0,p['line']);txt(x+14,y+24,item['title'],15,weight=600)
            for i,v in enumerate([1,1,0,1,1,1,0]):
                hh=max(3,v*84);xx=x+24+i*43;c.rect(xx,y+h-32-hh,20,hh,p['action'],2 if mock else 0,p['action']);txt(xx,y+h-12,['L','M','X','J','V','S','D'][i],12,w=24)
        elif kind=='empty':
            c.rect(x,y,w,h,p['surface'],12 if mock else 0,p['line'])
            if mock:c.icon(item['icon'],x+w/2-18,y+14,p.get('icon',p['action']),1.5)
            else:placeholder(x+w/2-18,y+14,36,36)
            txt(x+16,y+76,item['title'],20,weight=600,w=w-32);txt(x+16,y+104,item['text'],14,'muted',w=w-32)
        elif kind=='summary':
            c.rect(x,y,w,h,p['action'],12 if mock else 0,p['action']);txt(x+16,y+31,item['title'],22,'onAction',700,w-32);txt(x+16,y+59,item['text'],13,'onAction',w=w-32)
        elif kind=='toggle':
            c.rect(x,y,w,h,p['surface'],12 if mock else 0,p['line']);txt(x+14,y+28,item['title'],16,weight=600,w=w-84)
            c.rect(x+w-58,y+14,42,24,p['muted'],12 if mock else 0,p['muted']);c.rect(x+w-55,y+17,18,18,p['surface'],9 if mock else 0,p['surface']);txt(x+14,y+61,item['text'],14,'muted',w=w-28)
        else:
            if kind!='copy':c.rect(x,y,w,h,p['surface'],12 if mock else 0,p['line'])
            icon=kind in ('habit','benefit');pad=56 if icon else 14
            if icon:
                if mock:c.icon(item['icon'],x+15,y+20,p.get('icon',p['action']),1)
                else:placeholder(x+14,y+16,28,28)
            txt(x+pad,y+27,item['title'],16 if icon else 17,weight=600,w=w-pad-14)
            txt(x+pad,y+51,item['text'],13 if icon else 14,'muted',w=w-pad-14)
        c.s.append('</g>')
    # Navegación: estructura estable; nada de iconos ni texto en los sketches.
    nav=[('hoy','Hoy'),('habitos','Hábitos'),('analisis','Análisis'),('ajustes','Perfil')]
    if sketch:
        rough(0,774,390,70)
        for i in range(4):rough(24+i*94,788,44,28);bar(26+i*94,832,40)
    else:
        c.rect(0,774,390,70,p['surface'],0,p['line'])
        for i,(icon,label) in enumerate(nav):
            xx=32+i*94
            if mock:c.icon(icon,xx,788,p.get('icon',p['text']),1)
            else:placeholder(xx,788,24,24)
            txt(xx-6,832,label,11,w=80)
    svg=c.end()
    if fidelity=='wireframe':svg=svg.replace('font-family="Inter"','font-family="Arial, sans-serif"')
    return svg


AUDIT_TEXT='## Acceso, registro de cuenta y recuperación\n\nAuditoría del catálogo y de los PNG existentes (29/10/2026):\n\n| Flujo | Qué existe en estas veinte pantallas |\n|---|---|\n| Bienvenida | **01 Bienvenida**: presenta el producto y conduce a Acceso. |\n| Login / acceso | **02 Acceso**: entrada al proveedor con «Continuar con Keycloak». No muestra campos de usuario o contraseña ni el formulario del proveedor. |\n| Registro de cuenta | **No hay una pantalla de creación de cuenta** en el catálogo móvil ni entre sus PNG. |\n| Forgot password / recuperación | **No hay una pantalla de recuperación de contraseña** en el catálogo móvil ni entre sus PNG. |\n| Registrar avance | **08 Registrar avance**: check-in de un hábito; no es registro de cuenta. |\n\nLa autenticación se delega a Keycloak. Faltan aquí las representaciones del formulario de login del proveedor, creación de cuenta y recuperación; la pantalla de acceso no acredita que esos flujos estén diseñados o implementados. Esta revisión documental conserva las veinte pantallas y no añade formularios nuevos.'

SHARED_NOTES="## Condiciones por pantalla\n\n01. **Cada avance cuenta:** La bienvenida no solicita credenciales ni concede una sesión.\n02. **Accede a tu espacio:** No hay formulario local de contraseña, registro ni recuperación paralelos; se delegan al proveedor.\n03. **Tu rutina de hoy:** Ejemplo del 26/10/2026, America/Mexico_City. Separar día abierto y periodo cerrado.\n04. **Mis hábitos:** La búsqueda y el filtro son controles propuestos, sin consulta a cuentas reales.\n05. **Crear hábito:** Guardar requiere validación y confirmación del servidor; cancelar vuelve a Hoy sin crear.\n06. **Leer con calma:** No recalcular registros pasados con una nueva meta. Archivar conserva el historial y requiere confirmación.\n07. **Editar programación:** Una versión obsoleta requiere revisar el conflicto. Cancelar edición regresa a Detalle.\n08. **Registrar avance:** Enviar 15 dos veces no suma 30. Reintentar tras respuesta perdida conserva idempotencia; un conflicto requiere revisión.\n09. **Historial de lectura:** Los registros son ejemplos sintéticos; no se inventan señales biométricas.\n10. **Tu recordatorio:** No seleccionar días ajenos a la agenda. Comprobar permisos del canal y zona; no se promete entrega operativa.\n11. **Tus avisos:** Avisos de ejemplo; las preferencias, horario y permiso deben respetarse en producto.\n12. **Observa tu constancia:** 19–25/10/2026: 1,1,0,1,1,1,0; 5/7=71.4 %. Racha de ese periodo: 0 al cierre; RN-P17.\n13. **Elige un periodo:** Validar inicio≤fin y zona de negocio. No reinterpretar el historial al cambiar zona del perfil.\n14. **Ideas para tu rutina:** Abstenerse sin inventar IA ni umbrales. El diseño de personalización es una vista condicional separada.\n15. **Personaliza una idea:** Vista condicional de una idea de ejemplo, no resultado de un modelo. Guardar confirma aceptación; cancelar no la acepta.\n16. **Perfil y preferencias:** Cambiar zona no reclasifica fechas históricas. Los controles de tema son diseño, no un cliente implementado.\n17. **Tú decides qué compartir:** Revocar bloquea nuevos usos y trabajos. No inferir permiso de biometría por aceptar sugerencias.\n18. **Tus dispositivos:** No inventar telemetría ni mediciones. La vinculación requiere capacidades y consentimiento explícitos.\n19. **Vincula una fuente:** No fija OTP, QR, Bluetooth ni protocolo aún pendiente. Confirmación de diseño; no conecta hardware.\n20. **Tus datos personales:** Revisar alcance y política; la eliminación requiere confirmación específica posterior. Ninguna imagen ejecuta solicitudes.\n\n## Alcance y límites\n\nLas referencias RF y notas describen intención y restricciones, no capacidades implementadas. Los ejemplos son sintéticos: análisis del 19–25/10/2026 (5/7 = 71.4 %, racha al cierre 0) y día abierto 26/10, America/Mexico_City, RN-P17. Acceso delega credenciales a Keycloak; permisos, persistencia, errores, conflictos, accesibilidad y soporte offline requieren implementación y pruebas propias.\n\nLas seis referencias anteriores de escritorio permanecen fuera del conteo móvil. Solo sus dos mockups oscuros recibieron los derivados de color de los logos el 29/10/2026. No se añaden pantallas PWA ni funciones de producto. Los veinte mockups móviles oscuros cambiaron únicamente en la cabecera de marca; los demás píxeles, sketches, wireframes y mockups claros se conservaron.\n\n## Fuente, regeneración y verificación\n\nSe sigue la distinción de Carlos Salgado en [Mosaic/UOC, «Sketchs, mockups, wireframes y prototipos»](https://mosaic.uoc.edu/2015/09/15/proceso-de-desarrollo-de-un-proyecto-digital/). La solicitud precisa sketches sin anotaciones y veinte pantallas; no se copian los ejemplos del artículo.\n\nEl catálogo de [movil.py](../../fuente/movil.py) genera geometría, manifiesto, índice y los tres README de etapas; mantenerlo como fuente para conservar esta separación al regenerar. Los PNG no tienen copias SVG exportadas. La [identidad](../../identidad/README.md) define los recursos compartidos.\n\nDesde la raíz del repositorio, en el entorno de autoría Python/Pillow y Node/Playwright con Chrome:\n\n```powershell\npython docs/GUI/fuente/generar.py --mobile-only\n$env:QC_MOBILE_ONLY='1'\nnode docs/GUI/fuente/render.cjs\npython -m unittest discover -s docs/GUI/tests -p 'test_*.py' -v\n```\n\nNo definir `QC_IDENTITY_ONLY=1` en esa exportación. `QC_CHROME` permite configurar Chrome. El exportador comprueba Inter local y texto dentro del lienzo y de cada bloque.\n\nValidación del catálogo (28–29/10/2026): veinte conjuntos y ochenta archivos; correspondencia de bloques y destinos; sketches sin texto/imágenes/color, wireframes Arial y grises, mockups Inter y marcas en ambos temas. Se comprobaron el visor, los temas, la navegación por imágenes y su carga local. Esta evidencia de diseño no certifica una aplicación funcional ni accesibilidad global.\n"


def write_readme(manifest, output):
    """Índice común y tres README visuales: sketch, wireframe y mockup."""
    areas=[('Inicio y acceso',1,2),('Hábitos y registros',3,9),('Recordatorios y avisos',10,11),('Análisis y sugerencias',12,15),('Perfil, privacidad y dispositivos',16,20)]
    names={'bienvenida':'Bienvenida','acceso':'Acceso','hoy':'Hoy','detalle':'Detalle de hábito','historial':'Historial de hábito','analisis':'Análisis','periodo':'Elegir periodo','sugerencias':'Sugerencias','personalizar':'Personalizar sugerencia','ajustes':'Perfil y preferencias','consentimiento':'Consentimiento','dispositivos':'Dispositivos','vincular':'Vincular una fuente','datos':'Datos personales'}
    stages=[('sketches','Sketch','Sketches','20 PNG. Solo cuadros y líneas en blanco/gris; sin texto, logos, fotos, color ni temas. El número y el nombre se identifican fuera del dibujo.'),('wireframes','Wireframe','Wireframes','20 PNG. Misma estructura e intención del sketch, con grises, Arial y marcadores de imagen/logo; sin identidad visual final.'),('mockups','Mockup','Mockups','20 pantallas, 40 PNG: cada pantalla presenta claro y oscuro juntos. Inter, paleta, iconos y marcas existentes aplicados a la misma estructura.')]
    def label(item):return names.get(item['id'],item['title'])
    def heading(item,stage):return f'{stage} {item["number"]:02d} {label(item)}'
    def anchor(title):return re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
    readme="""# Móvil · Índice y correspondencia

Las veinte pantallas se desarrollan en tres etapas: **20 sketches, 20 wireframes y 40 PNG de mockups** (claro/oscuro). Todos miden 390 × 844. Los temas no son pantallas adicionales. Este índice no incrusta imágenes: cada etapa tiene su propio README visual.

[Índice GUI](../../README.md) · [Identidad visual](../../identidad/README.md) · [Galería](../../index.html#prototipos) · [Catálogo con geometría](catalogo.json)

| Etapa | Dónde revisar sus imágenes |
|---|---|
| Sketches · 20 PNG | [README de sketches](sketches/README.md) |
| Wireframes · 20 PNG | [README de wireframes](wireframes/README.md) |
| Mockups · 40 PNG | [README de mockups · Claro y oscuro juntos](mockups/README.md) |

## Matriz por áreas funcionales

La misma numeración e ID conserva la correspondencia. Cada enlace abre la pantalla dentro del README de su etapa.

| Nº | Área | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro/oscuro |
|---|---|---|---|---|---|---|
"""
    for item in manifest:
        area=next(title for title,first,last in areas if first<=item['number']<=last)
        links=[f'[Ver]({folder}/README.md#{anchor(heading(item,stage))})' for folder,stage,_,_ in stages]
        readme+=f'| {item["number"]:02d} | {area} | **{label(item)}** — {item["intent"]} | {item["rf"]} | '+' | '.join(links)+' |\n'
    readme+='\n'+AUDIT_TEXT+'\n\n'+SHARED_NOTES
    (output/'README.md').write_text(readme,encoding='utf-8')
    for folder,stage,title,criterion in stages:
        document=f'# Móvil · {title}\n\n{criterion} Todas las imágenes miden 390 × 844 y son documentación estática.\n\n[Índice y matriz móvil](../README.md) · [Condiciones por pantalla](../README.md#condiciones-por-pantalla) · [Identidad visual](../../../identidad/README.md) · [Galería](../../../index.html#prototipos)\n\n'
        document+='\n'.join(f'- [{area} · {first:02d}–{last:02d}](#{anchor(area)})' for area,first,last in areas)+'\n'
        for area,first,last in areas:
            document+=f'\n## {area}\n'
            for item in manifest:
                if not first<=item['number']<=last:continue
                caption=heading(item,stage)
                document+=f'\n### {caption}\n\nID: `{item["id"]}`.\n\n'
                if folder=='mockups':
                    light=item['assets']['mockup:light'].removeprefix('prototipos/movil/mockups/')
                    dark=item['assets']['mockup:dark'].removeprefix('prototipos/movil/mockups/')
                    document+=f'| Claro | Oscuro |\n|---|---|\n| ![{caption} claro]({light}) | ![{caption} oscuro]({dark}) |\n'
                else:
                    key='sketch:none' if folder=='sketches' else 'wireframe:none'
                    rel=item['assets'][key].removeprefix(f'prototipos/movil/{folder}/')
                    document+=f'![{caption}]({rel})\n'
        destination=output/folder;destination.mkdir(exist_ok=True)
        (destination/'README.md').write_text(document,encoding='utf-8')


def build(Canvas, colors, icons, logos, photo, output):
    scenes={};manifest=[]
    for n,spec in enumerate(CATALOG,1):
        assets={}
        for fidelity in ('sketch','wireframe','mockup'):
            for theme in (('light','dark') if fidelity=='mockup' else ('none',)):
                folder={'sketch':'sketches','wireframe':'wireframes','mockup':'mockups'}[fidelity]
                suffix=f'/{theme}' if fidelity=='mockup' else ''
                filename=f'prototipos/movil/{folder}{suffix}/{spec["id"]}.png'
                scenes[filename]=render(spec,fidelity,theme if theme!='none' else 'light',Canvas,colors,icons,logos,photo)
                assets[f'{fidelity}:{theme}']=filename
        manifest.append({k:v for k,v in spec.items() if k!='blocks'}|dict(number=n,assets=assets,blocks=geometry(spec),width=390,height=844))
    output.mkdir(parents=True,exist_ok=True)
    (output/'catalogo.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_readme(manifest,output)
    return scenes,manifest
