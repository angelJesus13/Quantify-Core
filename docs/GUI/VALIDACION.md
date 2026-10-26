# Validación del estudio visual

**Fecha:** 26/10/2026. **Alcance:** documentación y prototipos de revisión, no interfaz de producto. [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26) permanece abierto.

## Base e integridad

- Repositorio comprobado: `angelJesus13/Quantify-Core`; clon limpio antes de editar.
- Base exclusiva: `develop` en `55604085492983ecebcea81d0ad4d0fef04d99a9`.
- Rama: `feature/QUANCORE-26-documentacion-prototipos`, usando el prefijo `feature/` del Git Flow del repositorio.
- `main` inspeccionada por lectura remota en `7a4266f0e656e16c22fa8256dd735686708e14ca`. La comparación remota `main...develop` indicaba 8 commits por delante y 1 por detrás; no se incorporaron commits de `main`.
- Árbol Git de `docs/practica-07` en la base: `9a87a160df81b88c4f5a925f71970d969e36e60d`. Ningún archivo de esa carpeta fue modificado, movido o copiado a esta entrega. El árbol final debe coincidir con ese identificador.
- Logos heredados preservados; el nuevo isologo tiene nombre y estado de propuesta.

## Comprobaciones ejecutadas

| Comprobación | Resultado |
|---|---|
| Sintaxis de `galeria.js` y manifiesto `pantallas.js` con `node --check` | Correcta |
| Pruebas existentes de la Práctica 07 | 21/21 aprobadas, sin editar su código |
| Galería por archivo local, en Chrome sin interfaz | 144 combinaciones: 8 pantallas × 3 fidelidades × 2 temas × 3 anchos |
| Anchos de galería | 320, 390 y 1440 px; imágenes cargadas y sin desbordamiento horizontal de página |
| Estados de revisión | Ocho fichas alternativas y retorno a vista base comprobados |
| Navegación de revisión | Hoy → Crear hábito comprobada; no guarda datos |
| SVG en navegador | 39 láminas/recursos principales inspeccionados por cajas de texto dentro del lienzo |
| Manual visual | Imágenes cargadas y sin desbordamiento horizontal a 320, 390 y 1440 px |
| Errores JavaScript observados | Ninguno en la revisión automatizada |
| Recursos vectoriales | XML analizable, sin scripts, eventos embebidos ni recursos externos; solo el logo heredado incrustado como imagen local |
| Regeneración | Salidas idénticas al regenerar desde tokens y fuente versionada |
| Enlaces locales | Existencia de destinos comprobada en GUI, diseño, mapa documental y README de tokens |

Resultados numéricos, contrastes y árbol de base: [verificacion.json](verificacion.json). La galería permite abrir por archivo gracias al manifiesto JS generado del mismo inventario JSON; no requiere servidor, llamadas de API ni recursos de red.

En sketches/wireframes los dos valores del selector de tema usan la misma lámina gris; no se contabilizan como diseños adicionales. Son **34 SVG de pantalla** y **17 recursos de diseño** (3 láminas, 2 activos de propuesta/ilustración, 12 iconos).

## Contraste

Se midieron con luminancia relativa sRGB los roles de texto sobre fondo/tarjeta, secundario sobre fondo/tarjeta y texto de acción sobre botón en ambos temas; todos alcanzan 4.5:1. Borde de control sobre superficie y foco sobre fondo/tarjeta alcanzan 3:1. El reporte conserva los valores exactos redondeados y el umbral aplicado.

Esto comprueba pares sólidos seleccionados, no conformidad WCAG global. No se usan textos pequeños Cool Gray sobre blanco ni blancos sobre Sky Laser. Los acentos semánticos no se presentan como pares universalmente accesibles.

## Inspección visual y límites

Se revisaron las capturas de la galería, el mockup de Hoy en escritorio y la lámina de paleta/tipografía para comprobar jerarquía, legibilidad, separación de bloques y convivencia de controles de revisión. La exportación PNG de recursos SVG se realizó mediante rasterización local; la captura de la galería corresponde al navegador.

Una lámina SVG se escala como imagen: no acredita reflujo de una aplicación, lector de pantalla, texto ampliado ni teclado dentro de los controles dibujados. El visor usa controles HTML y foco visible; todavía requiere revisión manual con lector de pantalla y usuarios. No se probaron Flutter, dispositivos físicos, API, autenticación, entrega de avisos ni sincronización offline. Las fichas de estados son anotaciones textuales y no sustituyen pantallas funcionales ni pruebas de integración.

La cobertura no abarca todos los sketches históricos. RF-08 y derechos personales de RF-10 necesitan diseño adicional; los contratos RF-06 a RF-10 siguen pendientes. El isologo, tipografía y geometría siguen propuestos. No se declara aprobación de marca, publicación en Pages ni implementación de clientes.

## Reproducir

Desde la raíz, con Python 3 y Node.js disponibles:

```sh
python docs/GUI/generar-prototipos.py
node --check docs/GUI/galeria.js
node --check docs/GUI/pantallas.js
node --test --test-timeout=10000 docs/practica-07/tests/prototipo.test.cjs
git diff --check
git diff 55604085492983ecebcea81d0ad4d0fef04d99a9 -- docs/practica-07
git rev-parse HEAD:docs/practica-07
```

El diff de Práctica 07 debe estar vacío y el árbol coincidir con el indicado arriba. La matriz automatizada de navegador se ejecutó con herramientas del entorno de autoría; no se añade Playwright como dependencia del proyecto ni se inventa un comando de CI. Para revisión manual abrir [index.html](index.html), alternar pantallas/niveles/temas/estados y seguir los recorridos.

## Entrega por commits

1. Fuente de tokens de revisión, generador y recursos de identidad.
2. Galería, sketches, wireframes, mockups y manual visual.
3. Integración de los índices documentales y evidencia de validación.

Todos pertenecen a la rama de trabajo. No se crea PR, no se hace merge y no se modifica `main` ni `develop`.
