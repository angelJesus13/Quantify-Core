# Móvil · Correspondencia de veinte pantallas

20 sketches + 20 wireframes + 20 mockups con variante clara y oscura: **80 PNG**, todos a 390 × 844. Los temas no son pantallas adicionales. La intención y las posiciones de bloques se conservan entre etapas. Son imágenes estáticas de diseño; el visor no ejecuta operaciones de negocio.

[Índice GUI](../../README.md) · [Identidad visual](../../identidad/README.md) · [Galería](../../index.html#prototipos) · [Catálogo con geometría](catalogo.json) · [Fuente](../../fuente/movil.py)

**Ver imágenes:** [Sketches](#sketches) · [Wireframes](#wireframes) · [Mockups claros](#mockups-claros) · [Mockups oscuros](#mockups-oscuros). La matriz sirve de índice; cada enlace lleva a la imagen incrustada de esa pantalla.

## Acceso, registro de cuenta y recuperación

Auditoría del catálogo y de los PNG existentes (29/10/2026):

| Flujo | Qué existe en estas veinte pantallas |
|---|---|
| Bienvenida | **01 Bienvenida**: presenta el producto y conduce a Acceso. |
| Login / acceso | **02 Acceso**: entrada al proveedor con «Continuar con Keycloak». No muestra campos de usuario o contraseña ni el formulario del proveedor. |
| Registro de cuenta | **No hay una pantalla de creación de cuenta** en el catálogo móvil ni entre sus PNG. |
| Forgot password / recuperación | **No hay una pantalla de recuperación de contraseña** en el catálogo móvil ni entre sus PNG. |
| Registrar avance | **08 Registrar avance**: check-in de un hábito; no es registro de cuenta. |

La autenticación se delega a Keycloak. Faltan aquí las representaciones del formulario de login del proveedor, creación de cuenta y recuperación; la pantalla de acceso no acredita que esos flujos estén diseñados o implementados. Esta revisión documental conserva las veinte pantallas y no añade formularios nuevos.

## Etapas

| Etapa | Pantallas | PNG | Criterio |
|---|---:|---:|---|
| Sketch | 20 | 20 | Cuadros y líneas en blanco/gris; sin texto, logos, fotos, color ni temas. Número y nombre fuera del dibujo. |
| Wireframe | 20 | 20 | Misma estructura, grises, Arial y marcadores de imagen/logo. |
| Mockup | 20 | 40 | Misma función y organización con Inter, paleta, iconos y marcas existentes; claro y oscuro. |

Se sigue la distinción de Carlos Salgado en [Mosaic/UOC, «Sketchs, mockups, wireframes y prototipos»](https://mosaic.uoc.edu/2015/09/15/proceso-de-desarrollo-de-un-proyecto-digital/). La solicitud de esta entrega precisa sketches sin anotaciones y veinte pantallas; no se copian los ejemplos del artículo.

## Matriz por áreas funcionales

- [Inicio y acceso · 01–02](#inicio-y-acceso)
- [Hábitos y registros · 03–09](#hábitos-y-registros)
- [Recordatorios y avisos · 10–11](#recordatorios-y-avisos)
- [Análisis y sugerencias · 12–15](#análisis-y-sugerencias)
- [Perfil, privacidad y dispositivos · 16–20](#perfil-privacidad-y-dispositivos)

Cada fila identifica una pantalla y sus cuatro recursos correspondientes. Las etapas se indican en las columnas; los títulos de Detalle e Historial conservan el hábito de lectura usado como ejemplo.

### Inicio y acceso

| Nº | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro | Mockup oscuro |
|---|---|---|---|---|---|---|
| 01 | **Bienvenida** · Cada avance cuenta — Presentar el producto y conducir al acceso centralizado. | RF-01 | [Ver](#sketch-01-bienvenida) | [Ver](#wireframe-01-bienvenida) | [Ver](#mockup-claro-01-bienvenida) | [Ver](#mockup-oscuro-01-bienvenida) |
| 02 | **Acceso** · Accede a tu espacio — Iniciar el flujo de identidad con Keycloak y regresar al cliente. | RF-01 | [Ver](#sketch-02-acceso) | [Ver](#wireframe-02-acceso) | [Ver](#mockup-claro-02-acceso) | [Ver](#mockup-oscuro-02-acceso) |

### Hábitos y registros

| Nº | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro | Mockup oscuro |
|---|---|---|---|---|---|---|
| 03 | **Hoy** · Tu rutina de hoy — Consultar lo programado para el día abierto y abrir un hábito. | RF-03 / RF-04 | [Ver](#sketch-03-hoy) | [Ver](#wireframe-03-hoy) | [Ver](#mockup-claro-03-hoy) | [Ver](#mockup-oscuro-03-hoy) |
| 04 | **Mis hábitos** — Encontrar hábitos propios y distinguir los activos de los archivados. | RF-03 | [Ver](#sketch-04-mis-hábitos) | [Ver](#wireframe-04-mis-hábitos) | [Ver](#mockup-claro-04-mis-hábitos) | [Ver](#mockup-oscuro-04-mis-hábitos) |
| 05 | **Crear hábito** — Definir nombre, meta, unidad, días y zona de un hábito nuevo. | RF-03 | [Ver](#sketch-05-crear-hábito) | [Ver](#wireframe-05-crear-hábito) | [Ver](#mockup-claro-05-crear-hábito) | [Ver](#mockup-oscuro-05-crear-hábito) |
| 06 | **Detalle de hábito** · Leer con calma — Consultar la meta y el avance confirmado de un hábito antes de actuar. | RF-03 / RF-04 | [Ver](#sketch-06-detalle-de-hábito) | [Ver](#wireframe-06-detalle-de-hábito) | [Ver](#mockup-claro-06-detalle-de-hábito) | [Ver](#mockup-oscuro-06-detalle-de-hábito) |
| 07 | **Editar programación** — Revisar cambios de meta y frecuencia conservando la configuración histórica. | RF-03 | [Ver](#sketch-07-editar-programación) | [Ver](#wireframe-07-editar-programación) | [Ver](#mockup-claro-07-editar-programación) | [Ver](#mockup-oscuro-07-editar-programación) |
| 08 | **Registrar avance** — Enviar el valor acumulado absoluto para la fecha de negocio del hábito. | RF-04 | [Ver](#sketch-08-registrar-avance) | [Ver](#wireframe-08-registrar-avance) | [Ver](#mockup-claro-08-registrar-avance) | [Ver](#mockup-oscuro-08-registrar-avance) |
| 09 | **Historial de hábito** · Historial de lectura — Revisar fechas, cantidades y estado confirmado de un hábito. | RF-04 / RF-05 | [Ver](#sketch-09-historial-de-hábito) | [Ver](#wireframe-09-historial-de-hábito) | [Ver](#mockup-claro-09-historial-de-hábito) | [Ver](#mockup-oscuro-09-historial-de-hábito) |

### Recordatorios y avisos

| Nº | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro | Mockup oscuro |
|---|---|---|---|---|---|---|
| 10 | **Tu recordatorio** — Configurar un recordatorio dentro de los días programados del hábito. | RF-06 | [Ver](#sketch-10-tu-recordatorio) | [Ver](#wireframe-10-tu-recordatorio) | [Ver](#mockup-claro-10-tu-recordatorio) | [Ver](#mockup-oscuro-10-tu-recordatorio) |
| 11 | **Tus avisos** — Revisar recordatorios y abrir el hábito al que pertenece cada aviso. | RF-06 | [Ver](#sketch-11-tus-avisos) | [Ver](#wireframe-11-tus-avisos) | [Ver](#mockup-claro-11-tus-avisos) | [Ver](#mockup-oscuro-11-tus-avisos) |

### Análisis y sugerencias

| Nº | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro | Mockup oscuro |
|---|---|---|---|---|---|---|
| 12 | **Análisis** · Observa tu constancia — Interpretar cumplimiento de un periodo cerrado, con fecha, fuente y unidad. | RF-05 | [Ver](#sketch-12-análisis) | [Ver](#wireframe-12-análisis) | [Ver](#mockup-claro-12-análisis) | [Ver](#mockup-oscuro-12-análisis) |
| 13 | **Elegir periodo** · Elige un periodo — Elegir una ventana de análisis sin mezclar días abiertos y cerrados. | RF-05 | [Ver](#sketch-13-elegir-periodo) | [Ver](#wireframe-13-elegir-periodo) | [Ver](#mockup-claro-13-elegir-periodo) | [Ver](#mockup-oscuro-13-elegir-periodo) |
| 14 | **Sugerencias** · Ideas para tu rutina — Explicar la ausencia de una recomendación cuando no hay datos suficientes. | RF-07 | [Ver](#sketch-14-sugerencias) | [Ver](#wireframe-14-sugerencias) | [Ver](#mockup-claro-14-sugerencias) | [Ver](#mockup-oscuro-14-sugerencias) |
| 15 | **Personalizar sugerencia** · Personaliza una idea — Adaptar una sugerencia disponible antes de guardarla y aceptarla. | RF-07 / RF-03 | [Ver](#sketch-15-personalizar-sugerencia) | [Ver](#wireframe-15-personalizar-sugerencia) | [Ver](#mockup-claro-15-personalizar-sugerencia) | [Ver](#mockup-oscuro-15-personalizar-sugerencia) |

### Perfil, privacidad y dispositivos

| Nº | Pantalla e intención | Requisito | Sketch | Wireframe | Mockup claro | Mockup oscuro |
|---|---|---|---|---|---|---|
| 16 | **Perfil y preferencias** — Ajustar datos del perfil, zona preferida y apariencia con guardado explícito. | RF-02 | [Ver](#sketch-16-perfil-y-preferencias) | [Ver](#wireframe-16-perfil-y-preferencias) | [Ver](#mockup-claro-16-perfil-y-preferencias) | [Ver](#mockup-oscuro-16-perfil-y-preferencias) |
| 17 | **Consentimiento** · Tú decides qué compartir — Revisar finalidades y dar o retirar consentimiento por uso y fuente. | RF-02 / RF-08 | [Ver](#sketch-17-consentimiento) | [Ver](#wireframe-17-consentimiento) | [Ver](#mockup-claro-17-consentimiento) | [Ver](#mockup-oscuro-17-consentimiento) |
| 18 | **Dispositivos** · Tus dispositivos — Consultar fuentes vinculadas y comenzar la asociación de una fuente compatible. | RF-08 | [Ver](#sketch-18-dispositivos) | [Ver](#wireframe-18-dispositivos) | [Ver](#mockup-claro-18-dispositivos) | [Ver](#mockup-oscuro-18-dispositivos) |
| 19 | **Vincular una fuente** · Vincula una fuente — Revisar compatibilidad y permisos antes de confirmar una asociación. | RF-08 / RF-02 | [Ver](#sketch-19-vincular-una-fuente) | [Ver](#wireframe-19-vincular-una-fuente) | [Ver](#mockup-claro-19-vincular-una-fuente) | [Ver](#mockup-oscuro-19-vincular-una-fuente) |
| 20 | **Datos personales** · Tus datos personales — Solicitar una copia o iniciar una solicitud de eliminación de datos propios. | RF-02 / RF-10 | [Ver](#sketch-20-datos-personales) | [Ver](#wireframe-20-datos-personales) | [Ver](#mockup-claro-20-datos-personales) | [Ver](#mockup-oscuro-20-datos-personales) |

## Sketches

[Volver a la matriz](#matriz-por-áreas-funcionales). Las imágenes conservan su número e ID entre etapas.

### Sketch · Inicio y acceso

#### Sketch 01 Bienvenida

ID: `bienvenida`.

![Sketch 01 Bienvenida](sketches/bienvenida.png)

#### Sketch 02 Acceso

ID: `acceso`.

![Sketch 02 Acceso](sketches/acceso.png)

### Sketch · Hábitos y registros

#### Sketch 03 Hoy

ID: `hoy`.

![Sketch 03 Hoy](sketches/hoy.png)

#### Sketch 04 Mis hábitos

ID: `habitos`.

![Sketch 04 Mis hábitos](sketches/habitos.png)

#### Sketch 05 Crear hábito

ID: `habito`.

![Sketch 05 Crear hábito](sketches/habito.png)

#### Sketch 06 Detalle de hábito

ID: `detalle`.

![Sketch 06 Detalle de hábito](sketches/detalle.png)

#### Sketch 07 Editar programación

ID: `editar`.

![Sketch 07 Editar programación](sketches/editar.png)

#### Sketch 08 Registrar avance

ID: `registro`.

![Sketch 08 Registrar avance](sketches/registro.png)

#### Sketch 09 Historial de hábito

ID: `historial`.

![Sketch 09 Historial de hábito](sketches/historial.png)

### Sketch · Recordatorios y avisos

#### Sketch 10 Tu recordatorio

ID: `recordatorio`.

![Sketch 10 Tu recordatorio](sketches/recordatorio.png)

#### Sketch 11 Tus avisos

ID: `avisos`.

![Sketch 11 Tus avisos](sketches/avisos.png)

### Sketch · Análisis y sugerencias

#### Sketch 12 Análisis

ID: `analisis`.

![Sketch 12 Análisis](sketches/analisis.png)

#### Sketch 13 Elegir periodo

ID: `periodo`.

![Sketch 13 Elegir periodo](sketches/periodo.png)

#### Sketch 14 Sugerencias

ID: `sugerencias`.

![Sketch 14 Sugerencias](sketches/sugerencias.png)

#### Sketch 15 Personalizar sugerencia

ID: `personalizar`.

![Sketch 15 Personalizar sugerencia](sketches/personalizar.png)

### Sketch · Perfil, privacidad y dispositivos

#### Sketch 16 Perfil y preferencias

ID: `ajustes`.

![Sketch 16 Perfil y preferencias](sketches/ajustes.png)

#### Sketch 17 Consentimiento

ID: `consentimiento`.

![Sketch 17 Consentimiento](sketches/consentimiento.png)

#### Sketch 18 Dispositivos

ID: `dispositivos`.

![Sketch 18 Dispositivos](sketches/dispositivos.png)

#### Sketch 19 Vincular una fuente

ID: `vincular`.

![Sketch 19 Vincular una fuente](sketches/vincular.png)

#### Sketch 20 Datos personales

ID: `datos`.

![Sketch 20 Datos personales](sketches/datos.png)

## Wireframes

[Volver a la matriz](#matriz-por-áreas-funcionales). Las imágenes conservan su número e ID entre etapas.

### Wireframe · Inicio y acceso

#### Wireframe 01 Bienvenida

ID: `bienvenida`.

![Wireframe 01 Bienvenida](wireframes/bienvenida.png)

#### Wireframe 02 Acceso

ID: `acceso`.

![Wireframe 02 Acceso](wireframes/acceso.png)

### Wireframe · Hábitos y registros

#### Wireframe 03 Hoy

ID: `hoy`.

![Wireframe 03 Hoy](wireframes/hoy.png)

#### Wireframe 04 Mis hábitos

ID: `habitos`.

![Wireframe 04 Mis hábitos](wireframes/habitos.png)

#### Wireframe 05 Crear hábito

ID: `habito`.

![Wireframe 05 Crear hábito](wireframes/habito.png)

#### Wireframe 06 Detalle de hábito

ID: `detalle`.

![Wireframe 06 Detalle de hábito](wireframes/detalle.png)

#### Wireframe 07 Editar programación

ID: `editar`.

![Wireframe 07 Editar programación](wireframes/editar.png)

#### Wireframe 08 Registrar avance

ID: `registro`.

![Wireframe 08 Registrar avance](wireframes/registro.png)

#### Wireframe 09 Historial de hábito

ID: `historial`.

![Wireframe 09 Historial de hábito](wireframes/historial.png)

### Wireframe · Recordatorios y avisos

#### Wireframe 10 Tu recordatorio

ID: `recordatorio`.

![Wireframe 10 Tu recordatorio](wireframes/recordatorio.png)

#### Wireframe 11 Tus avisos

ID: `avisos`.

![Wireframe 11 Tus avisos](wireframes/avisos.png)

### Wireframe · Análisis y sugerencias

#### Wireframe 12 Análisis

ID: `analisis`.

![Wireframe 12 Análisis](wireframes/analisis.png)

#### Wireframe 13 Elegir periodo

ID: `periodo`.

![Wireframe 13 Elegir periodo](wireframes/periodo.png)

#### Wireframe 14 Sugerencias

ID: `sugerencias`.

![Wireframe 14 Sugerencias](wireframes/sugerencias.png)

#### Wireframe 15 Personalizar sugerencia

ID: `personalizar`.

![Wireframe 15 Personalizar sugerencia](wireframes/personalizar.png)

### Wireframe · Perfil, privacidad y dispositivos

#### Wireframe 16 Perfil y preferencias

ID: `ajustes`.

![Wireframe 16 Perfil y preferencias](wireframes/ajustes.png)

#### Wireframe 17 Consentimiento

ID: `consentimiento`.

![Wireframe 17 Consentimiento](wireframes/consentimiento.png)

#### Wireframe 18 Dispositivos

ID: `dispositivos`.

![Wireframe 18 Dispositivos](wireframes/dispositivos.png)

#### Wireframe 19 Vincular una fuente

ID: `vincular`.

![Wireframe 19 Vincular una fuente](wireframes/vincular.png)

#### Wireframe 20 Datos personales

ID: `datos`.

![Wireframe 20 Datos personales](wireframes/datos.png)

## Mockups claros

[Volver a la matriz](#matriz-por-áreas-funcionales). Las imágenes conservan su número e ID entre etapas.

### Mockup claro · Inicio y acceso

#### Mockup claro 01 Bienvenida

ID: `bienvenida`.

![Mockup claro 01 Bienvenida](mockups/light/bienvenida.png)

#### Mockup claro 02 Acceso

ID: `acceso`.

![Mockup claro 02 Acceso](mockups/light/acceso.png)

### Mockup claro · Hábitos y registros

#### Mockup claro 03 Hoy

ID: `hoy`.

![Mockup claro 03 Hoy](mockups/light/hoy.png)

#### Mockup claro 04 Mis hábitos

ID: `habitos`.

![Mockup claro 04 Mis hábitos](mockups/light/habitos.png)

#### Mockup claro 05 Crear hábito

ID: `habito`.

![Mockup claro 05 Crear hábito](mockups/light/habito.png)

#### Mockup claro 06 Detalle de hábito

ID: `detalle`.

![Mockup claro 06 Detalle de hábito](mockups/light/detalle.png)

#### Mockup claro 07 Editar programación

ID: `editar`.

![Mockup claro 07 Editar programación](mockups/light/editar.png)

#### Mockup claro 08 Registrar avance

ID: `registro`.

![Mockup claro 08 Registrar avance](mockups/light/registro.png)

#### Mockup claro 09 Historial de hábito

ID: `historial`.

![Mockup claro 09 Historial de hábito](mockups/light/historial.png)

### Mockup claro · Recordatorios y avisos

#### Mockup claro 10 Tu recordatorio

ID: `recordatorio`.

![Mockup claro 10 Tu recordatorio](mockups/light/recordatorio.png)

#### Mockup claro 11 Tus avisos

ID: `avisos`.

![Mockup claro 11 Tus avisos](mockups/light/avisos.png)

### Mockup claro · Análisis y sugerencias

#### Mockup claro 12 Análisis

ID: `analisis`.

![Mockup claro 12 Análisis](mockups/light/analisis.png)

#### Mockup claro 13 Elegir periodo

ID: `periodo`.

![Mockup claro 13 Elegir periodo](mockups/light/periodo.png)

#### Mockup claro 14 Sugerencias

ID: `sugerencias`.

![Mockup claro 14 Sugerencias](mockups/light/sugerencias.png)

#### Mockup claro 15 Personalizar sugerencia

ID: `personalizar`.

![Mockup claro 15 Personalizar sugerencia](mockups/light/personalizar.png)

### Mockup claro · Perfil, privacidad y dispositivos

#### Mockup claro 16 Perfil y preferencias

ID: `ajustes`.

![Mockup claro 16 Perfil y preferencias](mockups/light/ajustes.png)

#### Mockup claro 17 Consentimiento

ID: `consentimiento`.

![Mockup claro 17 Consentimiento](mockups/light/consentimiento.png)

#### Mockup claro 18 Dispositivos

ID: `dispositivos`.

![Mockup claro 18 Dispositivos](mockups/light/dispositivos.png)

#### Mockup claro 19 Vincular una fuente

ID: `vincular`.

![Mockup claro 19 Vincular una fuente](mockups/light/vincular.png)

#### Mockup claro 20 Datos personales

ID: `datos`.

![Mockup claro 20 Datos personales](mockups/light/datos.png)

## Mockups oscuros

[Volver a la matriz](#matriz-por-áreas-funcionales). Las imágenes conservan su número e ID entre etapas.

### Mockup oscuro · Inicio y acceso

#### Mockup oscuro 01 Bienvenida

ID: `bienvenida`.

![Mockup oscuro 01 Bienvenida](mockups/dark/bienvenida.png)

#### Mockup oscuro 02 Acceso

ID: `acceso`.

![Mockup oscuro 02 Acceso](mockups/dark/acceso.png)

### Mockup oscuro · Hábitos y registros

#### Mockup oscuro 03 Hoy

ID: `hoy`.

![Mockup oscuro 03 Hoy](mockups/dark/hoy.png)

#### Mockup oscuro 04 Mis hábitos

ID: `habitos`.

![Mockup oscuro 04 Mis hábitos](mockups/dark/habitos.png)

#### Mockup oscuro 05 Crear hábito

ID: `habito`.

![Mockup oscuro 05 Crear hábito](mockups/dark/habito.png)

#### Mockup oscuro 06 Detalle de hábito

ID: `detalle`.

![Mockup oscuro 06 Detalle de hábito](mockups/dark/detalle.png)

#### Mockup oscuro 07 Editar programación

ID: `editar`.

![Mockup oscuro 07 Editar programación](mockups/dark/editar.png)

#### Mockup oscuro 08 Registrar avance

ID: `registro`.

![Mockup oscuro 08 Registrar avance](mockups/dark/registro.png)

#### Mockup oscuro 09 Historial de hábito

ID: `historial`.

![Mockup oscuro 09 Historial de hábito](mockups/dark/historial.png)

### Mockup oscuro · Recordatorios y avisos

#### Mockup oscuro 10 Tu recordatorio

ID: `recordatorio`.

![Mockup oscuro 10 Tu recordatorio](mockups/dark/recordatorio.png)

#### Mockup oscuro 11 Tus avisos

ID: `avisos`.

![Mockup oscuro 11 Tus avisos](mockups/dark/avisos.png)

### Mockup oscuro · Análisis y sugerencias

#### Mockup oscuro 12 Análisis

ID: `analisis`.

![Mockup oscuro 12 Análisis](mockups/dark/analisis.png)

#### Mockup oscuro 13 Elegir periodo

ID: `periodo`.

![Mockup oscuro 13 Elegir periodo](mockups/dark/periodo.png)

#### Mockup oscuro 14 Sugerencias

ID: `sugerencias`.

![Mockup oscuro 14 Sugerencias](mockups/dark/sugerencias.png)

#### Mockup oscuro 15 Personalizar sugerencia

ID: `personalizar`.

![Mockup oscuro 15 Personalizar sugerencia](mockups/dark/personalizar.png)

### Mockup oscuro · Perfil, privacidad y dispositivos

#### Mockup oscuro 16 Perfil y preferencias

ID: `ajustes`.

![Mockup oscuro 16 Perfil y preferencias](mockups/dark/ajustes.png)

#### Mockup oscuro 17 Consentimiento

ID: `consentimiento`.

![Mockup oscuro 17 Consentimiento](mockups/dark/consentimiento.png)

#### Mockup oscuro 18 Dispositivos

ID: `dispositivos`.

![Mockup oscuro 18 Dispositivos](mockups/dark/dispositivos.png)

#### Mockup oscuro 19 Vincular una fuente

ID: `vincular`.

![Mockup oscuro 19 Vincular una fuente](mockups/dark/vincular.png)

#### Mockup oscuro 20 Datos personales

ID: `datos`.

![Mockup oscuro 20 Datos personales](mockups/dark/datos.png)

## Condiciones por pantalla

01. **Cada avance cuenta:** La bienvenida no solicita credenciales ni concede una sesión.
02. **Accede a tu espacio:** No hay formulario local de contraseña, registro ni recuperación paralelos; se delegan al proveedor.
03. **Tu rutina de hoy:** Ejemplo del 26/10/2026, America/Mexico_City. Separar día abierto y periodo cerrado.
04. **Mis hábitos:** La búsqueda y el filtro son controles propuestos, sin consulta a cuentas reales.
05. **Crear hábito:** Guardar requiere validación y confirmación del servidor; cancelar vuelve a Hoy sin crear.
06. **Leer con calma:** No recalcular registros pasados con una nueva meta. Archivar conserva el historial y requiere confirmación.
07. **Editar programación:** Una versión obsoleta requiere revisar el conflicto. Cancelar edición regresa a Detalle.
08. **Registrar avance:** Enviar 15 dos veces no suma 30. Reintentar tras respuesta perdida conserva idempotencia; un conflicto requiere revisión.
09. **Historial de lectura:** Los registros son ejemplos sintéticos; no se inventan señales biométricas.
10. **Tu recordatorio:** No seleccionar días ajenos a la agenda. Comprobar permisos del canal y zona; no se promete entrega operativa.
11. **Tus avisos:** Avisos de ejemplo; las preferencias, horario y permiso deben respetarse en producto.
12. **Observa tu constancia:** 19–25/10/2026: 1,1,0,1,1,1,0; 5/7=71.4 %. Racha de ese periodo: 0 al cierre; RN-P17.
13. **Elige un periodo:** Validar inicio≤fin y zona de negocio. No reinterpretar el historial al cambiar zona del perfil.
14. **Ideas para tu rutina:** Abstenerse sin inventar IA ni umbrales. El diseño de personalización es una vista condicional separada.
15. **Personaliza una idea:** Vista condicional de una idea de ejemplo, no resultado de un modelo. Guardar confirma aceptación; cancelar no la acepta.
16. **Perfil y preferencias:** Cambiar zona no reclasifica fechas históricas. Los controles de tema son diseño, no un cliente implementado.
17. **Tú decides qué compartir:** Revocar bloquea nuevos usos y trabajos. No inferir permiso de biometría por aceptar sugerencias.
18. **Tus dispositivos:** No inventar telemetría ni mediciones. La vinculación requiere capacidades y consentimiento explícitos.
19. **Vincula una fuente:** No fija OTP, QR, Bluetooth ni protocolo aún pendiente. Confirmación de diseño; no conecta hardware.
20. **Tus datos personales:** Revisar alcance y política; la eliminación requiere confirmación específica posterior. Ninguna imagen ejecuta solicitudes.

## Alcance y límites

Las referencias RF y notas describen intención y restricciones, no capacidades implementadas. Los ejemplos son sintéticos: análisis del 19–25/10/2026 (5/7 = 71.4 %, racha al cierre 0) y día abierto 26/10, America/Mexico_City, RN-P17. Acceso delega credenciales a Keycloak; permisos, persistencia, errores, conflictos, accesibilidad y soporte offline requieren implementación y pruebas propias.

Las seis referencias anteriores de escritorio permanecen fuera del conteo móvil. Solo sus dos mockups oscuros recibieron los derivados de color de los logos el 29/10/2026. No se añaden pantallas PWA ni funciones de producto. Los veinte mockups móviles oscuros cambiaron únicamente en la cabecera de marca; los demás píxeles, sketches, wireframes y mockups claros se conservaron.

## Fuente, regeneración y verificación

El catálogo de [movil.py](../../fuente/movil.py) genera geometría, manifiesto y este README; mantenerlo como fuente para no perder la agrupación al regenerar. Los PNG no tienen copias SVG exportadas. La [identidad](../../identidad/README.md) define los recursos compartidos.

Desde la raíz del repositorio, en el entorno de autoría Python/Pillow y Node/Playwright con Chrome:

```powershell
python docs/GUI/fuente/generar.py --mobile-only
$env:QC_MOBILE_ONLY='1'
node docs/GUI/fuente/render.cjs
python -m unittest discover -s docs/GUI/tests -p 'test_*.py' -v
```

No definir `QC_IDENTITY_ONLY=1` en esa exportación. `QC_CHROME` permite configurar Chrome. El exportador comprueba Inter local y texto dentro del lienzo y de cada bloque.

Validación del catálogo (28–29/10/2026): veinte conjuntos y ochenta archivos; correspondencia de bloques y destinos; sketches sin texto/imágenes/color, wireframes Arial y grises, mockups Inter y marcas en ambos temas. Se comprobaron el visor, los temas, la navegación por imágenes y su carga local. Esta evidencia de diseño no certifica una aplicación funcional ni accesibilidad global.
