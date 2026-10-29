# Quantify Core · GUI

Índice de la documentación visual de [QUANCORE-26](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-26). Revisión: 29 de octubre de 2026.

## Estado de la entrega

| Elemento | Estado | Dónde revisarlo |
|---|---|---|
| Paleta de colores | Nombre, HEX, RGB, HSL, CMYK, psicología y justificación; claro y oscuro | [README de identidad · Paleta](identidad/README.md#paleta-de-colores) |
| Tipografía | Inter; seis criterios justificados | [README de identidad · Tipografía](identidad/README.md#tipografía) |
| Iconografía | 24 símbolos identificados, en claro y oscuro | [README de identidad · Iconografía](identidad/README.md#iconografía) |
| Logotipo, firma empresarial y marcas de agua | Originales claros y derivados oscuros; usos diferenciados | [README de identidad · Marcas](identidad/README.md#marcas-oficiales) |
| Móvil: sketches, wireframes, mockups y matriz | 20 pantallas correspondientes; 80 PNG | [README móvil · Matriz por áreas](prototipos/movil/README.md#matriz-por-áreas-funcionales) |
| Galería pública | Publicación desde `gh-pages` | [Abrir galería](https://angeljesus13.github.io/Quantify-Core/docs/GUI/) |
| Archivo editable | — | [Figma](https://www.figma.com/design/iLvbL5uaWxAPwuX58xN4yq/Quantify-Core-%C2%B7-Sistema-visual-y-prototipos--QUANCORE-26-?node-id=0-1&t=vNJ6E9RRwxvSXkNs-1) |
| Implementación en producto | Pendiente | Ver [Verificación y límites](#verificación-y-límites) |

## Revisión y mantenimiento

La [identidad](identidad/README.md) reúne las láminas, justificaciones, fuentes y estado pendiente de Figma. El [README móvil](prototipos/movil/README.md) contiene etapas, áreas funcionales, correspondencias, condiciones y regeneración. La [galería local](index.html) permite ampliar y descargar imágenes; puede abrirse sirviendo la raíz del repositorio con `python -m http.server 8765` y visitando `http://localhost:8765/docs/GUI/`.

Pages publica desde la raíz de `gh-pages`. La galería y sus recursos se sincronizan desde la hotfix autorizada y se comprueban en la URL pública; publicar la documentación no integra la hotfix en `main` ni cambia el estado del producto.

## Verificación y límites

La revisión valida generación de los cuatro lienzos, Inter, límites de texto, galería y enlaces. Los PNG y el visor documentan el diseño; no autentican, guardan hábitos ni conectan hardware.

No se declara conformidad WCAG global. La galería utiliza controles HTML con nombre y foco visible; los PNG no son controles accesibles de aplicación. La implementación deberá probar lector de pantalla, teclado, zoom, reflujo y tamaños táctiles de cada componente. No se comprobaron clientes nativos, autenticación, API o hardware real mediante estas imágenes.
