# Imágenes y recursos gráficos

Esta carpeta conserva recursos visuales compartidos del repositorio. Los recursos existentes documentan la identidad; no acreditan una biblioteca de iconos ni un sistema de ilustraciones de producto terminado.

## Inventario actual

| Archivo | Uso documentado | Texto alternativo orientativo |
|---|---|---|
| [quantifyLogo.jpeg](quantifyLogo.jpeg) | Cabecera del proyecto | “Logotipo de Quantify Core” |
| [productLogo.jpeg](productLogo.jpeg) | Identidad del producto | “Logotipo del producto Quantify Core” |
| [enterpriseLogo.jpeg](enterpriseLogo.jpeg) | Identidad empresarial del equipo | “Logotipo empresarial del equipo Quantify” |
| [organigrama-quantify-core.png](organigrama-quantify-core.png) | Organigrama del README principal con la paleta V2.0, sin logotipo | “Jerarquía del equipo: jefatura, backend, frontend, base de datos y documentación” |

La autoría, licencia o autorización de distribución de los recursos heredados debe documentarse cuando se confirme; no atribuir una licencia por su presencia en el repositorio. Conservar sus nombres actuales mientras existan referencias. Una eventual deduplicación requiere comprobar referencias y acordar un archivo canónico.

El organigrama PNG se generó el 19 de octubre de 2026 con la herramienta de edición de imágenes a partir del `ORGANIGRAMA.jpg` heredado. Es una visualización derivada; los nombres y cargos del equipo se mantienen como texto en el [README principal](../../README.md). La autorización sobre los retratos sigue vinculada al archivo de origen.

## Incorporar un recurso

1. Elegir nombre descriptivo en minúsculas y guiones para archivos nuevos, incluyendo pantalla/variante si hace falta; no renombrar los heredados sin migrar enlaces.
2. Registrar autor/fuente, licencia o autorización, propósito y fecha. Para un recurso generado, registrar procedencia y revisión de uso sin incluir datos personales del prompt.
3. Usar SVG sanitizado para iconos/diagramas cuando corresponda, PNG para capturas con detalle y JPEG/WebP para fotografía. El formato debe servir al contenido y a los clientes destino.
4. Mantener proporciones, calidad suficiente y peso razonable. Fijar dimensiones de presentación para evitar saltos; no estirar logos.
5. Añadir texto alternativo por contexto; una imagen puramente decorativa no repite el texto adyacente. Un gráfico necesita también descripción o tabla, no solo “gráfico”.
6. Revisar contraste y legibilidad en los fondos de destino. Las variantes de logo o marca deben aprobarse; no recolorear los originales automáticamente.
7. Actualizar este inventario y comprobar todos los enlaces locales del documento que lo use.

## Capturas y diagramas

Las capturas deben identificar sketch/producto, rol, pantalla, ambiente y commit o versión. Usar datos sintéticos sin correos personales, tokens, biometría ni rutinas reales. Un recorte no debe ocultar estados relevantes de carga, error o sincronización cuando sean parte de la evidencia.

Preferir Mermaid para diagramas mantenidos con la documentación; conserva texto editable y se visualiza directamente en GitHub. Si se exporta una imagen, conservar también su fuente y fecha de actualización. La [Práctica 07](../../docs/practica-07/README.md) mantiene sus propios recursos académicos y evidencia.

La paleta de producto y los contrastes están en [tokens de diseño](../../packages/design-tokens/README.md); las normas de interfaz, en el [sistema de diseño](../../docs/diseno/sistema-diseno.md).

## Derivados oscuros autorizados · 29/10/2026

| Original claro, conservado | Variante oscura transparente |
|---|---|
| [enterpriseLogo.jpeg](enterpriseLogo.jpeg) | [brand/enterprise-dark.png](brand/enterprise-dark.png) |
| [productLogo.jpeg](productLogo.jpeg) | [brand/product-dark.png](brand/product-dark.png) |

Autorización expresa del propietario: adaptar únicamente colores/fondo, conservando exactamente formas, símbolos, composición y textos. Se reutilizan Sky Laser y Optical White de la paleta; no se crea un azul nuevo ni se aplica una inversión complementaria. Los originales JPEG no se sobrescriben. Los archivos tienen la misma resolución y coordenadas; su cobertura alfa deriva del mismo raster, sin redibujar, recortar o remuestrear. Se reemplaza la antigua aplicación de placa blanca en oscuro.

[Manifiesto con hashes y método](brand/variants.json) · [Fuente reproducible](../../docs/GUI/fuente/marcas.py) · [Reglas y estado Figma](../../docs/GUI/README.md#variantes-de-marca--corrección-del-29102026). El selector [brand/theme.js](brand/theme.js) solo cambia el recurso del logo al cambiar el tema de una página; no altera el resto de su interfaz.

La referencia antigua de Práctica 05 usa [product-legacy-dark.png](brand/product-legacy-dark.png), derivado de la misma marca en [su recorte cuadrado histórico](../../docs/quantifyLogo.jpeg), conservando sus 640 × 640 y su encuadre. No es otro logotipo.
