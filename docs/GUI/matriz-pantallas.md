# Inventario de prototipos y estados

**Propuesta 0.1 · 26/10/2026 · [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26).** [Abrir galería](index.html). Los SVG son láminas de diseño, no aplicaciones operativas.

## Tres niveles de detalle

1. **Sketch:** redibujo conceptual, bloques e intención específica. Referencia los IDs históricos sin copiar ni mover archivos de la Práctica 07.
2. **Wireframe:** composición en grises con contenido y controles; permite revisar jerarquía antes del color.
3. **Mockup:** misma composición con identidad Laser Blue; temas claro y oscuro. Las decisiones nuevas siguen propuestas.

| Vista / RF | Sketch | Wireframe | Mockup claro | Mockup oscuro | Referencia histórica |
|---|---|---|---|---|---|
| Acceso · RF-01 | [SVG](sketches/acceso-light.svg) | [SVG](wireframes/acceso-light.svg) | [SVG](mockups/acceso-light.svg) | [SVG](mockups/acceso-dark.svg) | U01–U05/U15; credenciales solo Keycloak |
| Hoy · RF-03/04 | [SVG](sketches/hoy-light.svg) | [SVG](wireframes/hoy-light.svg) | [SVG](mockups/hoy-light.svg) | [SVG](mockups/hoy-dark.svg) | U06 |
| Crear hábito · RF-03 | [SVG](sketches/habito-light.svg) | [SVG](wireframes/habito-light.svg) | [SVG](mockups/habito-light.svg) | [SVG](mockups/habito-dark.svg) | U07 |
| Registro · RF-04 | [SVG](sketches/registro-light.svg) | [SVG](wireframes/registro-light.svg) | [SVG](mockups/registro-light.svg) | [SVG](mockups/registro-dark.svg) | U08/U13 |
| Análisis · RF-05 | [SVG](sketches/analisis-light.svg) | [SVG](wireframes/analisis-light.svg) | [SVG](mockups/analisis-light.svg) | [SVG](mockups/analisis-dark.svg) | U10 |
| Sugerencias · RF-07 | [SVG](sketches/sugerencias-light.svg) | [SVG](wireframes/sugerencias-light.svg) | [SVG](mockups/sugerencias-light.svg) | [SVG](mockups/sugerencias-dark.svg) | U11 |
| Preferencias · RF-02 | [SVG](sketches/ajustes-light.svg) | [SVG](wireframes/ajustes-light.svg) | [SVG](mockups/ajustes-light.svg) | [SVG](mockups/ajustes-dark.svg) | U12 |
| Administración · RF-09/10 | [SVG](sketches/administracion-light.svg) | [SVG](wireframes/administracion-light.svg) | [SVG](mockups/administracion-light.svg) | [SVG](mockups/administracion-dark.svg) | A02/A03/A06 |

Hoy también tiene composición de escritorio [clara](mockups/hoy-escritorio-light.svg) y [oscura](mockups/hoy-escritorio-dark.svg). Administración está diseñada para escritorio. El resto usa lienzo 390 × 844. No se afirma cobertura completa de las 24 pantallas históricas: recordatorios/avisos, vinculación Wear OS, exportación/eliminación personal y formularios administrativos completos requieren ampliar esta revisión.

## Recorridos de revisión

Acceso → Hoy → Crear hábito → Registro → Análisis. Desde Hoy se puede revisar Sugerencias y Ajustes. Los botones de «Continuar el recorrido» del visor cambian láminas; no ejecutan los controles dibujados. Administración se selecciona como contexto separado, sin transición que simule concesión de privilegios.

| Pantalla | Alternativas y comportamiento a implementar | Trazabilidad |
|---|---|---|
| Acceso | Cancelación a bienvenida; error/vencimiento retorna a Keycloak; sin contraseñas locales | AC-01.1/01.2, RN-P01 |
| Hoy | Carga, vacío con «Crear hábito», fallo con reintento, pendientes aparte de confirmados | AC-03.1, AC-04.2, RN-P16 |
| Crear hábito | Nombre/meta/unidad/días/zona; validación conserva borrador; cancelar creación vuelve a Hoy; edición vuelve al detalle | AC-03.1/03.2/03.4, RN-P04/06/12 |
| Registro | Confirmado solo tras respuesta; valor absoluto; respuesta perdida reintenta la misma clave; conflicto obliga revisar versión | AC-04.1–04.4, RN-P11/14/15 |
| Análisis | Carga, sin oportunidades, parcial, error y recálculo pendiente; tabla equivalente | AC-05.1–05.4, RN-P17/18 |
| Sugerencias | Sin consentimiento o datos: abstención; disponible: fundamento/fuentes/periodo/versión; personalizar no acepta hasta guardar | AC-07.1–07.5, RN-P19/20/21 |
| Ajustes | Decisión explícita, permiso SO separado, error conserva borrador; revocar bloquea futuro uso; zona no mueve historial | AC-02.1–02.4, RN-P02/08 |
| Administración | Carga, vacío, 403, confirmación con motivo, cancelación y conflicto; sin inspección de rutinas privadas | AC-09.1/09.4, AC-10.1/10.4, RN-P23/24 |

El selector de estados muestra fichas textuales independientes de las láminas, con explicación y retorno a vista base. No modifica los datos de los SVG ni simula llamadas de servicio. La validación ejemplifica el formulario de hábito; la ficha no implica que todas las pantallas tengan los mismos campos. Offline es una variante futura y condicionada: hasta implementar la cola y sus controles, guardar exige conexión.

## Datos sintéticos de Análisis

Periodo cerrado 19–25/10/2026, America/Mexico_City. Un hábito diario con una oportunidad cada día; completas L=1, M=1, X=0, J=1, V=1, S=1, D=0. Resultado: 5/7 = 71.4 %, racha al cierre = 0 **en ese periodo**. Fuente: registros confirmados; regla RN-P17; cálculo ilustrativo 26/10. El 26/10 es día abierto y se muestra aparte en Hoy. No se generan cifras de recomendaciones ni biometría.

## Arquitectura y límites

RF-01 a RF-05 enlazan el [contrato propuesto](../../packages/contracts/README.md); RF-06 a RF-10 todavía necesitan contratos detallados. Las fichas no añaden endpoints, reglas de calendario ni permisos. Consultar [reglas canónicas](../requerimientos/reglas-negocio.md) y [recorridos](../diseno/recorridos.md).

Las fuentes son [pantallas.json](pantallas.json), [generador](generar-prototipos.py) y [tokens preview](../../packages/design-tokens/preview.json). El manifiesto JS se genera del mismo inventario para abrir por archivo sin servidor. No se usa almacenamiento local, cuentas, backend ni recursos de red.
