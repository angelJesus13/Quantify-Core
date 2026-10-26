# Quantify Core · Galería y sistema visual

**Versión 02 · 26 de octubre de 2026 · [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26)**

## Revisar las imágenes

### [Abrir la galería en GitHub Pages →](https://angeljesus13.github.io/Quantify-Core/docs/GUI/)

La galería muestra las cinco láminas completas de identidad y las pantallas de diseño como imágenes. Cada miniatura se puede abrir, ampliar y descargar en PNG. Las flechas recorren las imágenes; Escape cierra el visor y devuelve el foco. Los filtros separan sketches, wireframes, mockups, temas y formato. [Abrir el archivo local](index.html).

Esta es la **única documentación completa de la entrega visual**. Los índices de `docs/diseno` y del mapa documental enlazan aquí. Se retiraron las tablas de enlaces SVG, el manual duplicado, los manifiestos duplicados, los informes separados y los iconos exportados uno por uno. Las fuentes de autoría permanecen para poder actualizar las imágenes sin redibujar cada una manualmente.

## 1. Paleta de colores

[![Paleta de colores de Quantify Core: trece tonos con nombre, HEX, RGB y aplicación](imagenes/01-paleta-de-colores.png)](imagenes/01-paleta-de-colores.png)

La identidad conserva **Laser Blue `#275BC0`** como marca y acción principal. La imagen desarrolla las trece familias de la [paleta canónica](../../packages/design-tokens/README.md), con valores HEX/RGB y propósito: marca, neutros y estados. La separación de roles sostiene jerarquía y legibilidad; no se atribuyen efectos psicológicos universales al color.

Tema claro: fondo Pure Mist, tarjetas blancas, texto Obsidian y secundario Steel. Tema oscuro: fondo Obsidian, tarjetas Midnight, texto blanco y secundario Cool Gray. El borde suave derivado `#D8E1F0` separa tarjetas decorativas; no sirve como único contorno de un control interactivo. Campos y controles de wireframe usan borde con contraste. En la implementación, distinguir el borde decorativo del borde requerido para identificar un control.

Blanco sobre Laser Blue alcanza **6.28:1**; Cool Gray sobre Midnight **5.70:1**. Cool Gray sobre blanco y blanco sobre Sky Laser no se usan para texto pequeño. Emerald, Amber, Crimson y Cyan son acentos acompañados de palabras y formas. Un dato pendiente no se comunica como confirmado por su color.

La fuente de valores y geometría es [preview.json](../../packages/design-tokens/preview.json). El nombre histórico del archivo no implica que Inter siga sin elegir: la familia de esta entrega queda definida por la solicitud del proyecto. Todavía no se distribuye un paquete de componentes React/Flutter.

## 2. Tipografía definida: Inter

[![Tipografía Inter con muestras de español, números, pesos y jerarquías de interfaz](imagenes/02-tipografia.png)](imagenes/02-tipografia.png)

**Inter es la familia para títulos, párrafos, formularios, botones, etiquetas, gráficos y galería.** Los logos oficiales conservan su dibujo original. Se incluye el mismo archivo [Inter Variable WOFF2](assets/inter.woff2) y se renderizan los PNG con él. No se mezclan Segoe UI y Arial ni se depende de Google Fonts al abrir la página. `sans-serif` queda únicamente como recuperación de emergencia si el archivo no puede cargarse, no como otra elección de diseño.

Inter ofrece una construcción legible para interfaz, soporte de los caracteres del español y pesos variables sin cambiar de familia. Escala base: 40 presentación, 28 pantalla, 20 sección, 16 cuerpo y 14 ayuda; pesos habituales 400/500/600/700. El logotipo raster heredado conserva su dibujo original: no se pretende identificar o sustituir la fuente con la que fue creado.

Fuente: [proyecto oficial rsms/inter](https://github.com/rsms/inter), autoría Rasmus Andersson; [licencia SIL Open Font License incluida](assets/inter-license.txt). Archivo fijado al commit `353b61b9f4430d5f420d56605a6e7993e0941470`, sin modificaciones. SHA-256 WOFF2: `693b77d4f32ee9b8bfc995589b5fad5e99adf2832738661f5402f9978429a8e3`.

## 3. Iconografía en una sola lámina

[![Catálogo de 24 iconos coherentes de Quantify Core](imagenes/03-iconografia.png)](imagenes/03-iconografia.png)

La imagen reúne los **24 iconos**: Hoy, hábitos, análisis, preferencias, crear, confirmado, pendiente, aviso, volver, privacidad, salir, sugerencias, calendario, recordatorio, lectura, movimiento, descanso, historial, ver, editar, archivar, descargar, sincronizar y dispositivo.

Todos comparten retícula 24 × 24, trazo 1.8, extremos/uniones redondos y ausencia de relleno. Se dibujan desde un catálogo único en [la fuente](fuente/generar.py), utilizado también por los mockups. No se instala otra familia ni se mezclan emojis como iconos de navegación. Las acciones conservan etiqueta; los estados combinan forma y texto. Objetivo de interacción del diseño: 48 unidades, por resolver y comprobar al implementar cada plataforma.

Los trazos son originales de esta entrega y siguen las condiciones de distribución del repositorio; no se les atribuye una licencia externa inexistente. Para controles de producto, un icono decorativo se oculta al lector y un control sin texto necesita nombre accesible.

## 4. Uso de imágenes

[![Fotografía de ambiente y reglas de encuadre, color, contexto y accesibilidad](imagenes/04-uso-de-imagenes.png)](imagenes/04-uso-de-imagenes.png)

La fotografía representa un ritual cotidiano de lectura e hidratación: luz natural, objetos sencillos, paleta neutra y cuaderno azul. Se usa en bienvenida, apoyo del dashboard y cabecera de la galería. Los formularios priorizan la tarea; no se añade una foto a cada tarjeta por decoración.

El encuadre conserva proporciones mediante recorte de ventana, sin deformar la imagen; deja espacio útil y evita superponer texto sobre zonas de poco contraste. Una imagen informativa lleva descripción contextual; la decorativa no repite lo que ya dice el texto. Las gráficas conservan alternativa textual, periodo y unidad. No se usan fotos de personas, capturas de datos privados ni imágenes de marcas ajenas.

[ritual-cotidiano.png](assets/ritual-cotidiano.png) fue creado para esta entrega mediante generación de imágenes de OpenAI el 26/10/2026. Es una imagen editorial sintética, no evidencia de un usuario ni de mediciones de salud. Las fotografías del ejemplo aportado por el usuario solo inspiran la organización del manual; no se copian Spotify, sus recursos ni sus fuentes.

## 5. Identidad / isologo

[![Identidad de Quantify Core: firma, variantes, área libre y original preservado](imagenes/05-identidad-isologo.png)](imagenes/05-identidad-isologo.png)

Las cabeceras presentan **Nexus Core (empresarial) a la izquierda** y **Quantify Core (producto) a la derecha**. Se utilizan los JPEG originales, con su color y proporciones. Sobre oscuro permanecen en una placa blanca. La lámina explica su convivencia sin convertirlos en una sola marca ni recolorear sus letras.

El símbolo Q parecido a una lupa, utilizado en la primera revisión, es únicamente una **marca de agua editorial de la documentación visual**. Es independiente de ambas marcas oficiales y no las sustituye ni representa una tercera identidad empresarial. Aparece de forma tenue como sello de la maqueta; no funciona como botón, icono de búsqueda o logotipo del producto. Los wireframes mantienen referencias de marca en grises; los sketches continúan sin texto ni logos.

No estirar, recortar letras, añadir sombras ni invertir automáticamente los JPEG. Se pueden retirar visualmente márgenes blancos exteriores para presentar el contenido, conservando todas las letras y símbolos. La tipografía Inter rige los textos de la interfaz; las marcas raster conservan su dibujo propio.

Los archivos [quantifyLogo.jpeg](../../assets/images/quantifyLogo.jpeg), [productLogo.jpeg](../../assets/images/productLogo.jpeg) y [enterpriseLogo.jpeg](../../assets/images/enterpriseLogo.jpeg) permanecen intactos. La autoría/licencia del material heredado conserva el estado del [inventario original](../../assets/images/README.md). No se reemplazan activos de prácticas ni de `main`.

## Prototipos: tres fidelidades reales

**Sketches:** trazos irregulares y formas para explorar composición. **No contienen letras ni texto visible**, ni marca, fotografía, cifras o contenido de pantalla. Los nombres y las referencias se muestran en la galería, fuera de la imagen.

**Wireframes:** estructura en grises con bloques, campos y etiquetas funcionales. Permiten evaluar jerarquía, navegación y distribución sin fotografía ni identidad gráfica.

**Mockups:** diseños estáticos con Inter, logos oficiales empresarial/producto, colores claros/oscuros, iconos y fotografías donde aportan contexto. Son guía visual de interfaz; los botones dibujados no ejecutan acciones de negocio.

Hay **34 PNG de pantallas**: ocho sketches, ocho wireframes, dieciséis mockups claros/oscuros y dos variantes de Hoy en escritorio. Los móviles usan lienzo 390 × 844; administración y Hoy de escritorio, 1440 × 900. La galería es adaptable; una imagen estática no demuestra reflujo ni texto grande dentro de una aplicación futura.

[![Mockup de Hoy en escritorio con identidad e imagen de producto](prototipos/mockups/hoy-escritorio-light.png)](prototipos/mockups/hoy-escritorio-light.png)

### Cobertura funcional y trazabilidad

- **Acceso:** RF-01, referencia U01–U05/U15. Continuar con Keycloak, cancelar a bienvenida y resolver sesión vencida. Sin contraseña local ni autenticación paralela.
- **Hoy:** RF-03/04, U06. Hábitos programados y valor confirmado por día; vacío ofrece crear hábito. Los pendientes se separan de los confirmados.
- **Crear hábito:** RF-03, U07. Nombre, meta, unidad, días y zona; validación conserva borrador. Cancelar creación vuelve a Hoy; cancelar edición vuelve al detalle.
- **Registrar avance:** RF-04, U08/U13. Valor acumulado absoluto por fecha de negocio. Reintentar conserva la clave idempotente; un conflicto requiere revisar la versión. Archivar conserva el historial.
- **Análisis:** RF-05, U10. Ventana cerrada, unidad, zona, fuente, regla y alternativa textual. Sin oportunidades se muestra «sin datos», no fracaso.
- **Sugerencias:** RF-07, U11. Abstención explicada cuando faltan datos o consentimiento. Personalizar no acepta hasta guardar; cancelar no consume la recomendación.
- **Preferencias:** RF-02, U12. Finalidad voluntaria por uso y fuente; guardar explícitamente. Revocar bloquea usos futuros. Cambiar zona no reclasifica el historial.
- **Administración:** RF-09/10, A02/A03/A06. Agregados autorizados, motivo y auditoría; sin acceso a rutinas privadas por el simple rol de administrador.

Estados a implementar por recorrido: carga, vacío, validación, error de servicio, sesión vencida, permiso insuficiente y conflicto. Pendiente de sincronización es una variante condicionada a soporte offline aprobado; hasta entonces guardar exige conexión. El catálogo de estados sigue en las [reglas canónicas](../requerimientos/reglas-negocio.md), [recorridos](../diseno/recorridos.md) y [sistema de diseño](../diseno/sistema-diseno.md), no en fichas universales que sustituyan una pantalla real.

Análisis usa datos sintéticos del 19–25/10/2026: un hábito diario, completas L=1, M=1, X=0, J=1, V=1, S=1, D=0. Cumplimiento 5/7 = 71.4 %, racha al cierre 0 **en ese periodo**, zona America/Mexico_City, regla RN-P17, cálculo ilustrativo 26/10. El 26/10 es día abierto y aparece separado en Hoy. No se inventan biometría ni puntuaciones de IA.

La cobertura no equivale a las 24 pantallas históricas completas. Recordatorios/avisos, vinculación Wear OS, exportación/eliminación personal y formularios administrativos detallados requieren ampliación. RF-01 a RF-05 enlazan el [contrato propuesto](../../packages/contracts/README.md); RF-06 a RF-10 requieren contratos adicionales. Las láminas no añaden endpoints ni certifican backend, permisos o sincronización.

## Organización y mantenimiento

```text
docs/GUI/
  README.md             Documentación completa de esta entrega
  index.html            Galería pública y visor
  imagenes/             Las cinco láminas completas (PNG)
  prototipos/           Sketches, wireframes y mockups (PNG)
  assets/               Fuente Inter, licencia, foto, estilos e interacción
  fuente/               Dos archivos para regenerar las imágenes
```

Cada PNG corresponde a una lámina o variante de pantalla; no se mantiene una segunda copia SVG exportada ni 24 iconos sueltos. La fuente vectorial vive en el generador y sus temporales quedan ignorados en `.build/`. Los PNG preservan exactamente la tipografía elegida al revisarlos en otro equipo.

Para consultar localmente con la fuente web exacta, servir la raíz con `python -m http.server 8765`, y visitar `http://localhost:8765/docs/GUI/`. No hace falta instalar dependencias para consultar la galería. Para regenerar: Python 3 ejecuta `python docs/GUI/fuente/generar.py`; el entorno de autoría con Node/Playwright y Chrome ejecuta `node docs/GUI/fuente/render.cjs`. El exportador comprueba carga de Inter y texto dentro de los lienzos. Los paths del navegador se pueden configurar mediante `QC_CHROME`; Playwright debe estar disponible en el entorno. No se instala como dependencia del producto.

Los cambios visuales compartidos se hacen primero en tokens o en el catálogo de la fuente, se regeneran las imágenes y se revisan ambos temas. React y Flutter deberán incorporar la misma familia y semántica al implementar componentes; esta entrega no modifica clientes de producto todavía inexistentes en esta base.

## Publicación y control de ramas

La rama de trabajo sigue siendo `feature/QUANCORE-26-documentacion-prototipos`, creada desde `develop` en `55604085492983ecebcea81d0ad4d0fef04d99a9`. Se conservan los commits anteriores y se añaden commits separados de identidad, galería/consolidación y publicación.

GitHub Pages utilizaba `main` con raíz `/`. Para publicar sin integrar cambios a `main`, la rama **`gh-pages`** conserva una instantánea del contenido del portal ya publicado y añade la nueva galería. Es una rama de artefactos de publicación, no una fusión del código. El ajuste de Pages apunta a `gh-pages`/`/`; las rutas previas del portal y de la Práctica 07 se conservan. Para actualizar, exportar nuevamente el portal vigente más los recursos GUI revisados; no publicar `.git`, `.build`, credenciales ni archivos de trabajo.

`main` y `develop` no reciben commits, no se crea PR y no se hace merge. La Práctica 07 conserva su contexto y árbol original `9a87a160df81b88c4f5a925f71970d969e36e60d`. Una publicación de imágenes no da por terminada la implementación de QUANCORE-26.

## Verificación y límites

Las comprobaciones de esta revisión incluyen los cinco PNG de identidad, 34 PNG de pantallas, carga de Inter local, filtros, visor, ampliación, descarga, navegación por flechas, cierre con Escape y retorno del foco, ausencia de desbordamiento de página en anchos compactos/amplios, sintaxis y enlaces. Las pruebas existentes de Práctica 07 se ejecutan sin modificarla.

No se declara conformidad WCAG global. La galería utiliza controles HTML con nombre y foco visible; los PNG no son controles accesibles de aplicación. La implementación deberá probar lector de pantalla, teclado, zoom, reflujo y tamaños táctiles de cada componente. No se comprobaron clientes nativos, autenticación, API o hardware real mediante estas imágenes.

Para verificar integridad desde la raíz:

```sh
node --check docs/GUI/assets/galeria.js
node --test --test-timeout=10000 docs/practica-07/tests/prototipo.test.cjs
git diff --check
git diff 55604085492983ecebcea81d0ad4d0fef04d99a9 -- docs/practica-07
git rev-parse HEAD:docs/practica-07
```

El diff de Práctica 07 debe estar vacío y su árbol coincidir con el indicado. Los resultados finales de publicación y revisión se añaden al cierre de esta sección.
