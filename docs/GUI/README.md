# Quantify Core · Galería y sistema visual

**Versión 05 · Revisión móvil · 28 de octubre de 2026 · [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26)**

## Contenido

1. [Revisar las imágenes](#revisar-las-imágenes)
2. [Sistema visual](#1-paleta-de-colores)
3. [Prototipos](#prototipos-tres-fidelidades-reales)
4. [Organización y mantenimiento](#organización-y-mantenimiento)
5. [Publicación y control de ramas](#publicación-y-control-de-ramas)
6. [Verificación y límites](#verificación-y-límites)

## Estado de la entrega

| Elemento | Estado | Dónde revisarlo |
|---|---|---|
| Paleta, tipografía, iconografía, logotipo/isologo y marcas de agua | Cuatro lienzos PNG en hotfix | [imagenes/](imagenes/) |
| Móvil: 20 pantallas en cada etapa | 20 sketches + 20 wireframes + 40 variantes de mockup (80 PNG) | [Matriz móvil](prototipos/movil/README.md) |
| Galería pública | Versión anterior; esta hotfix no se publica en Pages | [Abrir galería](https://angeljesus13.github.io/Quantify-Core/docs/GUI/) |
| Archivo editable | Cuatro lienzos editables actualizados; claro y oscuro | [Figma](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/Quantify-Core-%C2%B7-Sistema-visual-y-prototipos--QUANCORE-26-?node-id=0-1&t=vNJ6E9RRwxvSXkNs-1) |
| Implementación en producto | Pendiente | Ver [Verificación y límites](#verificación-y-límites) |

## Revisar las imágenes

### [Abrir la galería en GitHub Pages →](https://angeljesus13.github.io/Quantify-Core/docs/GUI/)

**Estado de esta revisión:** cuatro lienzos en la rama `hotfix/QUANCORE-26-cuatro-lienzos`; GitHub Pages conserva la versión anterior. [Abrir la galería local](index.html). Cada lienzo puede ampliarse y descargarse; los prototipos conservan sus filtros y visor.

Figma se actualizó el 28/10/2026 después de obtener acceso. La primera página contiene exactamente cuatro lienzos: [paleta](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/?node-id=17-2), [tipografía](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/?node-id=17-146), [iconografía](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/?node-id=17-187) y [logotipo/isologo y marcas de agua](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/?node-id=17-508). Son textos, vectores e instancias editables; las marcas usan sus originales raster o derivados de color documentados. Se conservaron los 24 maestros de iconos y las otras dos páginas.

Las justificaciones ampliadas de colores y seis criterios tipográficos viven en [identidad.json](fuente/identidad.json), compartido como contenido con Figma. Cada lienzo muestra las aplicaciones de ambos temas. Los PNG se regeneran desde la fuente local y comparten contenido y roles; no se presentan como exportaciones idénticas de Figma.

Esta es la **única documentación completa de la entrega visual**. Los índices de `docs/diseno` y del mapa documental enlazan aquí. Se retiraron las tablas de enlaces SVG, el manual duplicado, los manifiestos duplicados, los informes separados y los iconos exportados uno por uno. Las fuentes de autoría permanecen para poder actualizar las imágenes sin redibujar cada una manualmente.

## 1. Paleta de colores

[![Paleta de colores de Quantify Core: trece tonos con nombre, HEX, RGB, HSL, CMYK, psicología y justificación](imagenes/01-paleta-de-colores.png)](imagenes/01-paleta-de-colores.png)

La identidad conserva **Laser Blue `#275BC0`** como marca y acción principal. La imagen desarrolla las trece familias de la [paleta canónica](../../packages/design-tokens/README.md), con valores HEX/RGB/HSL/CMYK, psicología y justificación por color: marca, neutros y estados. HSL se deriva de sRGB; CMYK usa conversión matemática sin perfil ICC y requiere prueba de impresión. La separación de roles sostiene jerarquía y legibilidad; no se atribuyen efectos psicológicos universales al color.

Tema claro: fondo Pure Mist, tarjetas blancas, texto Obsidian y secundario Steel. Tema oscuro: fondo Obsidian, tarjetas Midnight, texto blanco y secundario Cool Gray. El borde suave derivado `#D8E1F0` separa tarjetas decorativas; no sirve como único contorno de un control interactivo. Campos y controles de wireframe usan borde con contraste. En la implementación, distinguir el borde decorativo del borde requerido para identificar un control.

Blanco sobre Laser Blue alcanza **6.28:1**; Cool Gray sobre Midnight **5.70:1**. Cool Gray sobre blanco y blanco sobre Sky Laser no se usan para texto pequeño. Emerald, Amber, Crimson y Cyan son acentos acompañados de palabras y formas. Un dato pendiente no se comunica como confirmado por su color.

La fuente de valores y geometría es [preview.json](../../packages/design-tokens/preview.json). El nombre histórico del archivo no implica que Inter siga sin elegir: la familia de esta entrega queda definida por la solicitud del proyecto. Todavía no se distribuye un paquete de componentes React/Flutter.

### Justificación completa por color

**Laser Blue.** Psicología de marca: Confianza, continuidad y precisión. Se usa como ancla reconocible del producto y para la acción principal: permite localizar qué hacer sin convertir toda la pantalla en un acento. Su profundidad sostiene texto blanco legible y da continuidad entre web, móvil y documentos. En oscuro conserva el valor de marca; los iconos aislados cambian a Sky Laser para distinguirse de la superficie.

**Sky Laser.** Psicología de marca: Apertura, energía y exploración. Su mayor luminosidad hace visibles selección, foco e iconos activos sobre Midnight Navy. Mantiene parentesco con Laser Blue sin introducir otra marca para el tema oscuro. En claro no se usa con texto blanco pequeño ni como única señal sobre blanco; se reserva como acento y se combina con una etiqueta o contorno legible. También es el azul de las variantes oscuras de empresa y producto: ilumina sus trazos sin convertir el azul en su complementario ni modificar sus formas.

**Deep Cobalt.** Psicología de marca: Solidez, concentración y estabilidad. Es la variante profunda de la familia azul para foco y acciones presionadas sobre claro. Refuerza una interacción sin recurrir a negro ni cambiar de matiz, de modo que el estado sigue perteneciendo a la marca. Sobre oscuro pierde separación: el foco se muestra en Sky Laser y no se hereda este valor automáticamente.

**Obsidian Slate.** Psicología de marca: Sobriedad y profundidad visual. Estructura el fondo oscuro y el texto principal sobre claro, por lo que articula ambos temas sin añadir un negro ajeno a la paleta. También sirve de tinta en badges semánticos luminosos. Su función es separar niveles y priorizar contenido; no se usa como texto sobre Midnight Navy, donde se necesita Optical White.

**Midnight Navy.** Psicología de marca: Calma, continuidad y contención. Eleva tarjetas y paneles respecto del fondo Obsidian sin recurrir a grandes áreas blancas en modo oscuro. La diferencia de luminancia organiza la profundidad, mientras texto blanco y secundarios Cool Gray mantienen la lectura. No se confía solo en esa diferencia para identificar un campo: los controles reciben un borde visible adicional.

**Steel Border.** Psicología de marca: Orden, estructura y neutralidad. Proporciona texto secundario e iconos neutros legibles sobre blanco y un contorno reconocible para controles claros. Su tono azulado mantiene coherencia con la marca sin competir con la acción principal. En modo oscuro se sustituye en esos roles por Cool Gray, porque el mismo tono profundo se perdería contra las superficies oscuras.

**Cool Gray.** Psicología de marca: Discreción y equilibrio. Se elige como segundo nivel de lectura en oscuro: diferencia metadatos de títulos sin volverlos invisibles sobre Midnight Navy. También delimita controles oscuros cuando el borde identifica la interacción. En claro se sustituye por Steel Border para texto e iconos informativos; su apariencia suave sobre blanco no aporta el contraste necesario.

**Pure Mist.** Psicología de marca: Ligereza y espacio visual. Ofrece un fondo claro ligeramente azulado que separa las tarjetas blancas sin rodearlas de bloques intensos. La cercanía con la familia de marca mantiene unidad y deja protagonismo a datos y acciones. Al activar oscuro, el rol fondo pasa a Obsidian; Pure Mist no se invierte ni se conserva como gran superficie luminosa.

**Optical White.** Psicología de marca: Claridad y amplitud. Se emplea en superficies claras y como tinta principal sobre oscuro, además de texto sobre botones Laser Blue. Su rol cambia con el tema, pero el valor permanece estable. En los derivados oscuros de las marcas, las letras y trazos neutros pasan a Optical White sobre transparencia. Los originales claros permanecen intactos: ya no se coloca un rectángulo blanco detrás de la marca oscura.

**Emerald.** Psicología de marca: Progreso y confirmación. Relaciona una acción completada con avance verificable, sin usar el verde para prometer bienestar o resultados clínicos. Se conserva en ambos temas como acento o fondo de badge con tinta Obsidian y una marca de verificación. No se pone como texto pequeño sobre blanco ni se confunde un registro pendiente con uno confirmado.

**Amber.** Psicología de marca: Atención y cautela. Distingue espera, pendiente o una decisión que necesita revisión sin comunicar un fallo definitivo. El mismo matiz en ambos temas evita reaprender el significado del estado. Se muestra en un badge con tinta Obsidian, reloj y etiqueta: un punto amarillo por sí solo no explica qué falta ni cuándo puede continuar la persona.

**Crimson.** Psicología de marca: Urgencia y recuperación. Se reserva a error o interrupción para que lo excepcional conserve peso visual. Siempre se acompaña de una explicación y una vía de recuperación, evitando presentarlo como juicio sobre la persona o sus hábitos. En ambos temas puede funcionar como fondo de badge con tinta Obsidian; no como texto blanco pequeño o rojo aislado sobre blanco.

**Electric Cyan.** Psicología de marca: Exploración y precisión informativa. Separa métricas y sugerencias del azul reservado a la acción principal. Así la persona distingue información de una invitación a actuar. Conserva su valor en claro y oscuro como acento o badge con tinta Obsidian y etiqueta descriptiva. El color no certifica inteligencia, exactitud de un modelo ni validez médica de una recomendación.

### Aplicación de claro y oscuro

Los valores primitivos no se invierten: cambian sus asignaciones por rol. [preview.json](../../packages/design-tokens/preview.json) es la fuente; [themes.css](../../packages/design-tokens/themes.css) exporta los roles para revisión y futuros consumidores. El tema normal es claro; `data-qc-theme="dark"` selecciona oscuro en un consumidor que use esas variables. La galería conserva su diseño editorial claro y muestra los dos temas dentro de cada lienzo; no se declara implementado un selector de tema del producto.

| Rol | Claro | Oscuro | Criterio |
|---|---|---|---|
| Fondo del lienzo | `#F4F7FD` | `#0B0F17` | Cambia para ajustar la superficie general; conserva la jerarquía. |
| Tarjeta | `#FFFFFF` | `#161F2E` | Cambia para elevar contenido sin deslumbrar en oscuro. |
| Texto principal | `#0B0F17` | `#FFFFFF` | Cambia la tinta para mantener legibilidad. |
| Texto / icono secundario | `#283548` | `#8A99AD` | Cambia la luminosidad; conserva su menor jerarquía. |
| Icono activo / navegación | `#275BC0` | `#4A7DE8` | Cambia de azul por separación contra la superficie. |
| Foco visible | `#183D87` | `#4A7DE8` | Cambia para distinguir el control con teclado. |
| Acción principal | `#275BC0` | `#275BC0` | No cambia: mantiene reconocimiento y texto blanco. |
| Confirmación | `#10B981` | `#10B981` | Conserva su matiz; badge con tinta Obsidian, forma y etiqueta. |
| Pendiente | `#F59E0B` | `#F59E0B` | Conserva su matiz; badge con tinta Obsidian, forma y etiqueta. |
| Error | `#EF4444` | `#EF4444` | Conserva su matiz; badge con tinta Obsidian, forma y etiqueta. |
| Métrica / sugerencia | `#0EA5E9` | `#0EA5E9` | Conserva su matiz; badge con tinta Obsidian, forma y etiqueta. |

Los badges semánticos usan tinta Obsidian sobre Emerald, Amber, Crimson y Cyan en ambos temas. No trasladar esos tonos a texto pequeño sobre blanco. Las etiquetas, formas y explicación conservan el significado aunque no se distinga el color.

## 2. Tipografía definida: Inter

[![Tipografía Inter con muestras de español, números, pesos y jerarquías de interfaz](imagenes/02-tipografia.png)](imagenes/02-tipografia.png)

**Inter es la familia para títulos, párrafos, formularios, botones, etiquetas, gráficos de la interfaz final y la galería.** Los logos oficiales conservan su dibujo original. Se incluye el mismo archivo [Inter Variable WOFF2](assets/inter.woff2) y se renderizan los mockups con él, sin depender de Google Fonts. Los wireframes son la excepción metodológica: usan Arial genérica, sin representar la tipografía final. Los sketches no tienen texto. `sans-serif` en la galería queda únicamente como recuperación si Inter no puede cargarse.

Inter ofrece una construcción legible para interfaz, soporte de los caracteres del español y pesos variables sin cambiar de familia. Escala base: 40 presentación, 28 pantalla, 20 sección, 16 cuerpo y 14 ayuda; pesos habituales 400/500/600/700. El logotipo raster heredado conserva su dibujo original: no se pretende identificar o sustituir la fuente con la que fue creado.

Los seis criterios del lienzo se desarrollan así:

**Identidad de marca.** Inter acompaña una identidad basada en evidencia, hábitos y claridad: su dibujo sobrio permite que el contenido tenga protagonismo y que la personalidad se apoye en el azul, la composición y el tono de voz. Se usa en la interfaz y documentación para reconocer el mismo producto. Los logos conservan su dibujo original; no se recompone su nombre con Inter.

**Legibilidad.** Las formas abiertas, la cobertura del español y una jerarquía consistente ayudan a distinguir etiquetas, cifras y párrafos en una interfaz de consulta frecuente. El cuerpo parte de 16 y la ayuda de 14; el contenido no se comprime para hacerlo caber. En oscuro cambia la tinta, no se adelgaza la fuente. Deben comprobarse zoom, lector, interlineado y reflujo en producto.

**Estética moderna.** La construcción sin ornamentos y los pesos graduados permiten una presentación actual centrada en datos, sin necesitar una familia decorativa para cada sección. El carácter moderno proviene de una jerarquía contenida, aire y alineaciones coherentes. Ambos temas conservan tamaños y pesos para que activar oscuro cambie la iluminación visual sin transformar la personalidad ni el orden de lectura.

**Consistencia visual.** Una sola familia en navegación, formularios, tablas, métricas y documentos evita diferencias accidentales entre plataformas. La escala 40/28/20/16/14 y los pesos 400/500/600/700 asignan funciones repetibles, no elecciones arbitrarias por pantalla. Claro y oscuro mantienen esa estructura; únicamente cambian las tintas y superficies asociadas a sus roles. Cada cliente deberá usar los mismos nombres y criterios.

**Flexibilidad tipográfica.** Los pesos variables permiten pasar de párrafos tranquilos a títulos y etiquetas firmes sin mezclar tipografías. Los números de métricas pueden usar cifras tabulares al alinear columnas; los encabezados no requieren ese tratamiento. Se elige peso por función y no por tema. Si una cadena crece, el contenedor debe reacomodarse antes de reducir tamaño o eliminar contenido.

**Compatibilidad tecnológica.** El archivo WOFF2 local mantiene la familia disponible en la galería sin consultar servicios de fuentes al abrirla. Los PNG fijan su aspecto para revisión, mientras Figma conserva texto editable. React deberá cargar ese recurso y Flutter empaquetar una versión TTF/OTF compatible; ese cliente aún requiere validación propia. Deben conservarse licencia, cobertura, fallback y pruebas en dispositivos reales.

Fuente: [proyecto oficial rsms/inter](https://github.com/rsms/inter), autoría Rasmus Andersson; [licencia SIL Open Font License incluida](assets/inter-license.txt). Archivo fijado al commit `353b61b9f4430d5f420d56605a6e7993e0941470`, sin modificaciones. SHA-256 WOFF2: `693b77d4f32ee9b8bfc995589b5fad5e99adf2832738661f5402f9978429a8e3`.

## 3. Iconografía en una sola lámina

[![Catálogo de 24 iconos coherentes de Quantify Core](imagenes/03-iconografia.png)](imagenes/03-iconografia.png)

Cada icono identifica su función y el símbolo que lo representa (casa, escudo, reloj, etc.), con muestras en claro y oscuro. El mismo trazo y significado se conservan al cambiar de tema. Navegación activa: Laser Blue sobre blanco y Sky Laser sobre Midnight. Iconos neutros: Steel en claro y Cool Gray en oscuro. Estados: badge Emerald, Amber, Crimson o Cyan con tinta Obsidian, forma y etiqueta. No usar el color como única información. La imagen reúne los **24 iconos**: Hoy, hábitos, análisis, preferencias, crear, confirmado, pendiente, aviso, volver, privacidad, salir, sugerencias, calendario, recordatorio, lectura, movimiento, descanso, historial, ver, editar, archivar, descargar, sincronizar y dispositivo.

Todos comparten retícula 24 × 24, trazo 1.8, extremos/uniones redondos y ausencia de relleno. Se dibujan desde un catálogo único en [la fuente](fuente/generar.py), utilizado también por los mockups. No se instala otra familia ni se mezclan emojis como iconos de navegación. Las acciones conservan etiqueta; los estados combinan forma y texto. Objetivo de interacción del diseño: 48 unidades, por resolver y comprobar al implementar cada plataforma.

Los trazos son originales de esta entrega y siguen las condiciones de distribución del repositorio; no se les atribuye una licencia externa inexistente. Para controles de producto, un icono decorativo se oculta al lector y un control sin texto necesita nombre accesible.

### Uso de imágenes (reglas documentales, sin quinto lienzo)

La fotografía representa un ritual cotidiano de lectura e hidratación: luz natural, objetos sencillos, paleta neutra y cuaderno azul. Se usa en bienvenida, apoyo del dashboard y cabecera de la galería. Los formularios priorizan la tarea; no se añade una foto a cada tarjeta por decoración.

El encuadre conserva proporciones mediante recorte de ventana, sin deformar la imagen; deja espacio útil y evita superponer texto sobre zonas de poco contraste. Una imagen informativa lleva descripción contextual; la decorativa no repite lo que ya dice el texto. Las gráficas conservan alternativa textual, periodo y unidad. No se usan fotos de personas, capturas de datos privados ni imágenes de marcas ajenas.

[ritual-cotidiano.png](assets/ritual-cotidiano.png) fue creado para esta entrega mediante generación de imágenes de OpenAI el 26/10/2026. Es una imagen editorial sintética, no evidencia de un usuario ni de mediciones de salud. Las fotografías del ejemplo aportado por el usuario solo inspiran la organización del manual; no se copian Spotify, sus recursos ni sus fuentes.

## 4. Logotipo / isologo y marcas de agua

[![Identidad de Quantify Core: firma, variantes, área libre y original preservado](imagenes/04-identidad-isologo.png)](imagenes/04-identidad-isologo.png)

Las cabeceras presentan **Nexus Core (empresarial) a la izquierda** y **Quantify Core (producto) a la derecha**. En claro se utilizan los JPEG originales sin cambios. En oscuro se utilizan sus derivados PNG transparentes, con Sky Laser y Optical White, sin placa blanca. Las dos marcas conservan sus formas y proporciones; no se fusionan ni se redibujan.

El símbolo Q parecido a una lupa, utilizado en la primera revisión, es únicamente una **marca de agua editorial de la documentación visual**. Es independiente de ambas marcas oficiales y no las sustituye ni representa una tercera identidad empresarial. Aparece de forma tenue como sello de la maqueta; no funciona como botón, icono de búsqueda o logotipo del producto. Los wireframes mantienen referencias de marca en grises; los sketches continúan sin texto ni logos.

Logotipo designa la denominación escrita; isologo, el conjunto de símbolo y nombre. Los JPEG se presentan íntegros sin inventar una versión separable. Área libre propuesta: al menos un cuarto de la altura visible de cada firma; comprobar legibilidad al reducirla. Marca de agua editorial Q: dos variantes al 12 % (gris sobre claro y blanco sobre oscuro), en portada o pie libre de texto y controles, independiente de los logos oficiales. La afinidad geométrica y los neutros mantienen coherencia sin confundir empresa, producto y documentación.

No estirar, recortar letras, añadir sombras ni invertir automáticamente los JPEG. La adaptación de color/fondo autorizada el 29/10/2026 se aplica a archivos derivados y no sobrescribe originales. Se pueden retirar visualmente márgenes blancos exteriores para presentar el contenido, conservando todas las letras y símbolos. La tipografía Inter rige los textos de la interfaz; las marcas raster conservan su dibujo propio.

Los archivos [quantifyLogo.jpeg](../../assets/images/quantifyLogo.jpeg), [productLogo.jpeg](../../assets/images/productLogo.jpeg) y [enterpriseLogo.jpeg](../../assets/images/enterpriseLogo.jpeg) permanecen intactos. La autoría/licencia del material heredado conserva el estado del [inventario original](../../assets/images/README.md). Se actualizan únicamente las referencias o aplicaciones afectadas de esos mismos logos; no se modifican prácticas funcionales ni `main`.

## Prototipos: tres fidelidades reales

Esta revisión se concentra **solo en móvil**: veinte pantallas distintas, identificadas del 01 al 20, desarrolladas en tres etapas con correspondencia uno a uno. Cada mockup tiene variante clara y oscura; los temas no cuentan como pantallas diferentes. [Matriz con todos los PNG y la intención de cada pantalla](prototipos/movil/README.md) · [Catálogo y geometría](prototipos/movil/catalogo.json).

| Etapa móvil | Pantallas distintas | PNG | Criterio |
|---|---:|---:|---|
| Sketch | 20 | 20 | Solo cuadros y líneas de boceto en blanco/gris. Sin texto, colores, logos, fotos ni variantes de tema. |
| Wireframe | 20 | 20 | Misma estructura, grises, Arial y marcadores de imagen/logo. Sin iconografía o marca final. |
| Mockup | 20 | 40 | Mismas funciones y organización con Inter, paleta, iconos, imágenes y logos existentes; claro y oscuro. |

Las cuatro variantes de cada pantalla usan **los mismos identificadores y posiciones de bloques**, generados desde un catálogo único en [movil.py](fuente/movil.py). Los controles, jerarquía, espacios de imagen y navegación se reconocen de una etapa a la siguiente. El sketch es un boceto geométrico independiente, no un mockup convertido a grises. Las etiquetas de revisión, numeración, requisitos y nombres se muestran fuera del sketch.

Se sigue la distinción metodológica de Carlos Salgado en [Mosaic/UOC, «Sketchs, mockups, wireframes y prototipos»](https://mosaic.uoc.edu/2015/09/15/proceso-de-desarrollo-de-un-proyecto-digital/): explorar primero el boceto, ordenar contenido y navegación en el wireframe, y desarrollar después la apariencia visual. La persona solicitante precisa que los sketches no llevan anotaciones, aunque el artículo las admite. El mínimo de veinte es un requisito de esta entrega. No se copian sus ejemplos ni se adoptan sus herramientas históricas.

### Inventario y alcance funcional

01 Bienvenida · 02 Acceso · 03 Hoy · 04 Mis hábitos · 05 Crear hábito · 06 Detalle · 07 Editar programación · 08 Registrar avance · 09 Historial · 10 Recordatorio · 11 Avisos · 12 Análisis · 13 Elegir periodo · 14 Sugerencias · 15 Personalizar una idea · 16 Perfil · 17 Consentimiento · 18 Dispositivos · 19 Vincular una fuente · 20 Datos personales.

Cada pantalla tiene una intención distinta, referencias RF y notas de alcance en la matriz. El acceso delega credenciales a Keycloak. Crear y editar conservan sus diferencias; cancelar no guarda. El registro expresa el acumulado absoluto del día, no una suma por reintento. Las sugerencias se abstienen sin datos; personalizar es una vista condicional ilustrativa y no un resultado de IA. Dispositivos no inventa mediciones ni fija un protocolo de vinculación pendiente. Datos personales inicia solicitudes; una eliminación requiere revisión y confirmación posteriores, no se ejecuta desde esta imagen.

Los ejemplos de análisis conservan 19–25/10/2026: 1,1,0,1,1,1,0; 5/7 = 71.4 %, racha al cierre 0 en ese periodo, America/Mexico_City y RN-P17. El 26/10 se muestra separado como día abierto. Son datos sintéticos, sin cuentas ni biometría reales.

### Límites de esta revisión

Los PNG son representaciones estáticas a **390 × 844**, no una app ni un prototipo de negocio navegable. El visor de la galería abre imágenes y cambia la etapa; no guarda hábitos, autentica, solicita permisos ni conecta hardware. Los enlaces de destino del catálogo documentan la intención y no se presentan como operaciones implementadas. Los requisitos de carga, error, conflicto, accesibilidad y soporte offline siguen requiriendo implementación y pruebas propias; no se declara cobertura de todos sus estados por tener veinte pantallas.

Las seis imágenes anteriores de escritorio (administración y Hoy) permanecen como referencia histórica sin cambios. **No se amplía PWA/web, no se rediseñan logos y no se edita Figma en esta entrega móvil.** Los cuatro lienzos de identidad y los activos existentes quedan conservados. Los 28 PNG móviles anteriores se sustituyen por el catálogo móvil coherente; su historial sigue disponible en Git.

## Organización y mantenimiento

```text
docs/GUI/
  README.md             Documentación completa de esta entrega
  index.html            Galería pública y visor
  imagenes/             Los cuatro lienzos completos (PNG)
  prototipos/movil/     Catálogo, matriz y 80 PNG móviles
  prototipos/           Seis referencias anteriores de escritorio
  assets/               Fuente Inter, licencia, foto, estilos e interacción
  fuente/               Generador, catálogo móvil, exportador y contenido de identidad
  tests/                Regresiones de cantidad, fidelidad y correspondencia móvil
```

Cada PNG corresponde a una lámina o variante de pantalla; no se mantiene una segunda copia SVG exportada ni 24 iconos sueltos. La fuente vectorial vive en el generador y sus temporales quedan ignorados en `.build/`. Los PNG preservan la fuente de su etapa: Arial para wireframes e Inter para mockups; los sketches no contienen texto.

Para consultar localmente con la fuente web exacta, servir la raíz con `python -m http.server 8765`, y visitar `http://localhost:8765/docs/GUI/`. No hace falta instalar dependencias para consultar la galería. Para regenerar: Python 3 ejecuta `python docs/GUI/fuente/generar.py`; el entorno de autoría con Node/Playwright y Chrome ejecuta `node docs/GUI/fuente/render.cjs`. El exportador comprueba carga de Inter y texto dentro de los lienzos. Para exportar solo los cuatro lienzos sin tocar las pantallas, definir `QC_IDENTITY_ONLY=1` antes de ejecutar el exportador. La altura se adapta a las justificaciones; se mantiene el ancho de 1600 px. Los paths del navegador se pueden configurar mediante `QC_CHROME`; Playwright debe estar disponible en el entorno. No se instala como dependencia del producto.

Para regenerar únicamente móvil, sin modificar identidad ni escritorio:

```powershell
python docs/GUI/fuente/generar.py --mobile-only
$env:QC_MOBILE_ONLY='1'
node docs/GUI/fuente/render.cjs
python -m unittest discover -s docs/GUI/tests -p 'test_*.py' -v
```

No definir `QC_IDENTITY_ONLY=1` en esa exportación. El exportador verifica Inter local y límites de texto tanto del lienzo como de cada bloque; la prueba de fidelidades comprueba que los wireframes especifiquen Arial y que sketches/wireframes solo usen grises.

Los cambios visuales compartidos se hacen primero en tokens, identidad.json o el catálogo de la fuente, se regeneran las imágenes y se revisan ambos temas. React y Flutter deberán incorporar la misma familia y semántica al implementar componentes; esta entrega no modifica clientes de producto todavía inexistentes en esta base.

## Variantes de marca · Corrección del 29/10/2026

La instrucción de conservar una placa blanca en oscuro queda **superada**. Se mantienen los originales claros byte por byte y se generan [empresa oscura](../../assets/images/brand/enterprise-dark.png) y [producto oscuro](../../assets/images/brand/product-dark.png) con transparencia. [Manifiesto de procedencia](../../assets/images/brand/variants.json) · [Generador reproducible](fuente/marcas.py).

Se reutilizan **Sky Laser `#4A7DE8`** y **Optical White `#FFFFFF`**; no se añade un color nuevo. Sky Laser tiene contraste 4.25:1 sobre Midnight y 4.92:1 sobre Obsidian; se aplica a las marcas, no se autoriza como texto pequeño general. Los eslóganes y letras neutras se muestran en blanco. La medida de contraste se refiere al color sólido: los bordes suavizados de un raster tienen cobertura parcial.

La derivación mantiene los 1600 × 1194 píxeles y sus coordenadas; no recorta, escala, vectoriza, dilata trazos ni escribe letras nuevas. Extrae cobertura de tinta del mate casi blanco y reasigna colores. Se conservan símbolos, nombres, composición y eslóganes. El generador registra hashes de los originales y derivados y usa roles de [preview.json](../../packages/design-tokens/preview.json).

Las aplicaciones oscuras actualizadas son los veinte mockups móviles, las dos referencias de escritorio que ya contenían estos logos, la lámina de marcas y la explicación de paleta, y las referencias HTML/Markdown a los mismos originales. La geometría y el resto de píxeles de los mockups móviles permanecen iguales fuera de la cabecera. Sketches, wireframes y mockups claros no se regeneran. No se añaden pantallas PWA.

Para regenerar los únicos PNG afectados:

```powershell
python docs/GUI/fuente/generar.py --brand-only
node docs/GUI/fuente/render.cjs
```

El generador de variantes usa Pillow en el entorno de autoría, como los recursos gráficos; no es una dependencia de producto. Esta corrección conserva los cuatro lienzos de identidad y los veinte conjuntos móviles.

**Figma: actualización parcial verificada por el servicio de carga.** Se reemplazaron las dos imágenes oscuras del lienzo de marcas (`17:528` y `17:531`) por estos PNG. La operación oficial para retirar los fondos de sus contenedores y corregir los textos fue rechazada por el límite Starter. La interfaz de Windows se detuvo al no poder verificar la URL; después el usuario pausó expresamente Figma y asumió su revisión. No se hacen más intentos de edición o recuperación. No se afirma que esos contenedores, reglas ni las otras páginas hayan quedado corregidos en Figma; quedan pendientes de una vía de edición disponible.

### Verificación de variantes (29/10/2026)

- Ocho pruebas aprobadas: integridad de originales, transparencia/cobertura, generación determinista y cinco regresiones del catálogo móvil.
- Navegador local: cuatro páginas con marcas comprobadas en claro y oscuro (ocho combinaciones); galería con cuatro lienzos y veinte mockups por tema, sin imágenes rotas.
- Los veinte mockups móviles oscuros solo cambian en la cabecera de marca: los píxeles fuera de los primeros 80 px son idénticos a `4447a9d`. Las dos referencias oscuras de escritorio conservan los píxeles fuera de su área de marca (248 × 100). No se modifican los PNG claros, sketches ni wireframes.
- Se regeneraron 24 PNG afectados con medición de texto. Enlaces/documentación: 73 Markdown, 618 enlaces locales y 51 bloques Mermaid válidos; sintaxis del selector de marcas y diff comprobados.

## Publicación y control de ramas

Base: `origin/develop`, commit `dc127ea`, obtenido el 28/10/2026. La copia anterior conserva su `develop` divergente (`ba7bc96`, un commit local y cinco remotos distintos); se creó una copia independiente para conservar ese historial sin reset, rebase ni merge. En la nueva copia, `develop` coincide con remoto y la hotfix parte de él.

Por instrucción expresa del usuario, `hotfix/QUANCORE-26-cuatro-lienzos` parte de `develop`, excepción al origen `main` del flujo general. La rama permanece abierta. No se modifica `main`, no se fusiona ni se publica en `gh-pages`. La Práctica 07 y los logos originales quedan fuera del cambio.

## Verificación y límites

La revisión local de esta hotfix valida generación de los cuatro lienzos, Inter, límites de texto, galería local y enlaces. Las comprobaciones del 26/10 descritas abajo son evidencia histórica y no acreditan publicación de esta versión.

No se declara conformidad WCAG global. La galería utiliza controles HTML con nombre y foco visible; los PNG no son controles accesibles de aplicación. La implementación deberá probar lector de pantalla, teclado, zoom, reflujo y tamaños táctiles de cada componente. No se comprobaron clientes nativos, autenticación, API o hardware real mediante estas imágenes.

Para verificar integridad desde la raíz:

```sh
node --check docs/GUI/assets/galeria.js
node --test --test-timeout=10000 docs/practica-07/tests/prototipo.test.cjs
git diff --check
git diff 55604085492983ecebcea81d0ad4d0fef04d99a9 -- docs/practica-07
git rev-parse HEAD:docs/practica-07
```

El diff de Práctica 07 debe estar vacío y su árbol coincidir con el indicado.

### Resultados de la revisión móvil (28/10/2026)

- **20/20/20 pantallas distintas:** 20 sketches, 20 wireframes y 20 mockups con dos temas, **80 PNG a 390 × 844**. No se cuentan los temas ni las seis imágenes anteriores de escritorio como pantallas móviles extra.
- **Cinco pruebas de regresión aprobadas:** inventario y archivos, correspondencia de bloques y destinos, sketches sin texto/imágenes/color, wireframes Arial/grises/marcadores y mockups Inter/paleta/logos existentes. Comando reproducible: `python -m unittest discover -s docs/GUI/tests -p 'test_*.py' -v`.
- **Exportación:** los 80 lienzos pasan la medición real de texto dentro del lienzo y dentro de cada bloque. Se corrigió el alto de avisos antes de cerrar la revisión. Los 40 PNG de sketches/wireframes se comprobaron también píxel a píxel: R = G = B.
- **Galería:** 16 combinaciones de etapa/tema/ancho (320, 390, 768 y 1440 px), 80 PNG móviles distintos cargados y 92 comprobaciones del visor, ampliación, flechas, descarga enlazada, Escape y retorno del foco. Sin imágenes rotas, desbordamiento horizontal ni errores JavaScript/HTTP. Tema oculto en sketches/wireframes.
- **Revisión visual:** hojas de las veinte pantallas en cada etapa/tema y una comparación ampliada de Hoy, con las cuatro variantes alineadas. La numeración y el nombre quedan fuera del sketch.
- **Documentación:** 73 Markdown, 602 enlaces locales y 51 bloques Mermaid comprobados, más sintaxis del visor y OpenAPI válidos.
- **Alcance:** sin cambios en las seis referencias de escritorio, logos originales, cuatro lienzos de identidad, tokens, Figma ni Práctica 07. No se crea PR, no se fusiona y no se despliega; Pages conserva la versión anterior.

### Resultados previos de identidad (28/10/2026)

- Cuatro PNG de identidad a 1600 px de ancho y altura ajustada al contenido; Inter cargada y texto dentro del lienzo.
- Galería local: 320, 390, 768 y 1440 px; 16 revisiones del visor (cuatro lienzos por ancho), ampliación, flechas, Escape, retorno del foco y enlace de descarga. Sin desbordamiento horizontal, imágenes rotas ni errores de página o HTTP.
- Documentación: 72 Markdown, 520 enlaces locales y 51 bloques Mermaid válidos; OpenAPI válido.
- Práctica 07: 21/21 pruebas existentes; sin cambios en su árbol ni en los logos o los 34 prototipos.
- Contrastes calculados: blanco/Laser Blue 6.28:1; Sky Laser/Midnight 4.25:1 para iconos (no texto normal pequeño); tinta Obsidian sobre estados entre 5.10:1 y 8.93:1. No se declara conformidad global del producto.
- Figma: cuatro lienzos editables; 24 maestros preservados, 48 instancias de muestra y cuatro colocaciones de los dos logos oficiales. Texto Inter y autoajuste comprobados estructuralmente, sin desbordamientos. La iconografía se revisó visualmente. El plan Starter agotó las llamadas al pedir las otras tres capturas: su revisión visual remota queda pendiente; la estructura sí se verificó. GitHub Pages conserva la versión anterior.

### Evidencia histórica de la versión 02 (26/10/2026)

- **39 imágenes exportadas:** cinco láminas de identidad a 1600 × 2000 y 34 pantallas. Se comprobó la fuente Inter antes de exportar y las cajas de texto dentro del lienzo. Los ocho sketches no contienen elementos de texto visible.
- **16 configuraciones del visor**, entre fidelidades/temas a 320, 390, 768 y 1440 px, con 208 cargas de miniaturas comprobadas. Las vistas de escritorio se revisaron también a esos cuatro anchos. Sin desbordamiento horizontal de página ni errores JavaScript o peticiones fallidas por HTTP local.
- **Visor:** las cinco láminas abren a resolución original; se comprobaron descarga PNG, ampliación, flechas, Escape y restauración de foco.
- **Tipografía:** Inter local cargada y familia calculada coherente en títulos, párrafos, controles y enlaces de la galería. Los logos oficiales son imágenes independientes de la fuente de interfaz.
- **Documentación:** `node scripts/check-docs.mjs` aprobó 72 Markdown, 514 enlaces locales y 51 bloques Mermaid, además de la comprobación básica OpenAPI existente. La revisión específica de los seis documentos/entrada afectados comprobó 126 enlaces locales sin destinos rotos.
- **Práctica 07:** 21/21 pruebas existentes aprobadas; diff vacío y árbol conservado. Los tres logos heredados mantienen sus bytes originales.
- **Publicación:** GitHub informó despliegue `built` desde `gh-pages`. La revisión pública repitió las 16 configuraciones y las 208 cargas de miniaturas sin errores. Se comprobaron HTTP 200 y coincidencia SHA-256 de 42 recursos: 39 imágenes, Inter y los dos logos oficiales. El portal principal y los cuatro recursos principales de Práctica 07 coinciden byte por byte con sus blobs Git; los 13 archivos de la práctica conservan el árbol original. No se creó PR ni se hizo merge.

La galería se verificó tanto por HTTP local como en el sitio público de GitHub Pages el 26/10/2026. Esta revisión de imágenes y controles del visor no certifica accesibilidad global ni implementación funcional de una aplicación de producto.
