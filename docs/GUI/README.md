# Quantify Core · GUI

Índice de la documentación visual de [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26). Revisión: 30 de octubre de 2026.

## Estado de la entrega

| Elemento | Estado | Dónde revisarlo |
|---|---|---|
| Tarea 03 · Guía de Estilos | Seis frames editables sincronizados y revisados en el archivo propio Education | [Requisitos y evidencia](identidad/README.md#tarea-03--guía-de-estilos) · [Vista de los seis frames](identidad/guia/index.html) |
| Identidad visual anterior | Cuatro lienzos de referencia conservados; claro y oscuro | [README único de identidad visual](identidad/README.md) |
| Móvil · Sketches | 20 bocetos correspondientes | [README de sketches](prototipos/movil/sketches/README.md) |
| Móvil · Wireframes | 20 estructuras correspondientes | [README de wireframes](prototipos/movil/wireframes/README.md) |
| Móvil · Mockups | 20 pantallas; claro y oscuro juntos (40 PNG) | [README de mockups](prototipos/movil/mockups/README.md) |
| Matriz móvil | Correspondencia y condiciones de las veinte pantallas | [Índice y matriz móvil](prototipos/movil/README.md#matriz-por-áreas-funcionales) |
| Galería pública | Publicación desde `gh-pages` | [Abrir galería](https://angeljesus13.github.io/Quantify-Core/docs/GUI/) |
| Archivo editable propio | Guía, 20 sketches, 20 wireframes y 40 mockups; acceso público del nuevo enlace pendiente de comprobar | [Figma · Proyecto Integrador](https://www.figma.com/design/L6ePtwcmyBeiC2xI1iDGM3?node-id=2-59) |
| Implementación en producto | Pendiente | Ver [Verificación y límites](#verificación-y-límites) |

## Revisión y mantenimiento

La [identidad](identidad/README.md) reúne la matriz de las quince actividades, seis frames de Tarea 03, antecedentes, justificaciones y evidencia de Figma. El [índice móvil](prototipos/movil/README.md) reúne correspondencias, condiciones y regeneración; las imágenes se revisan en los tres README de etapa. La [galería local](index.html) permite ampliar y descargar imágenes; puede abrirse sirviendo la raíz del repositorio con `python -m http.server 8765` y visitando `http://localhost:8765/docs/GUI/`.

Pages publica desde la raíz de `gh-pages`. La galería y sus recursos se sincronizan desde la hotfix autorizada y se comprueban en la URL pública; publicar la documentación no integra la hotfix en `main` ni cambia el estado del producto.

## Carpetas

- `identidad/`: README único y sus cuatro láminas en `identidad/imagenes/`.
- `prototipos/`: diseños y README de cada etapa móvil; referencias de escritorio.
- `assets/`: estilos, visor, fuente Inter, licencia y fotografía compartidos por la galería.
- `fuente/`: contenido y generadores; sus pruebas están en `fuente/tests/`.

## Verificación y límites

La revisión valida generación de los cuatro lienzos, Inter, límites de texto, galería y enlaces. Los PNG y el visor documentan el diseño; no autentican, guardan hábitos ni conectan hardware.

No se declara conformidad WCAG global. La galería utiliza controles HTML con nombre y foco visible; los PNG no son controles accesibles de aplicación. La implementación deberá probar lector de pantalla, teclado, zoom, reflujo y tamaños táctiles de cada componente. No se comprobaron clientes nativos, autenticación, API o hardware real mediante estas imágenes.
