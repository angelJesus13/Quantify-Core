# Evidencias visuales de Keycloak

Diez capturas originales recuperadas de la conversación «Configurar Keycloak en Jira» (ID `6ade700b-10e8-83e8-b923-5d981025e46b`). Se copiaron sin editar después de inspección visual. Los nombres originales contienen `20261025`; no se interpreta la hora del archivo como hora local validada.

Son evidencia histórica aportada por el usuario. No son capturas nuevas de este agente ni prueban integración final de React, Flutter o NestJS. Los resultados Evaluate son simulaciones de claims, sin JWT compacto visible. Los nombres y correo visibles corresponden a cuentas sintéticas del laboratorio.

[Interpretación, pruebas y faltantes](../../keycloak/pruebas.md) · [Configuración](../../keycloak/README.md)

| ID | Archivo | Original | SHA-256 |
|---|---|---|---|
| K-01 | [01-repo-inicial.png](01-repo-inicial.png) | image(20261025-221606).png | `04bfdeb2f1aed800544917bcf4130f84861aea13d8dbdeb2198e94d65237cb49` |
| K-02 | [02-mobile-admin-evaluate.png](02-mobile-admin-evaluate.png) | image(20261025-221245).png | `426f06605fc7304c4c0f540f186fe2a773be0edd2786e57b5d451e50f651b5b3` |
| K-03 | [03-mobile-user-evaluate.png](03-mobile-user-evaluate.png) | image(20261025-221238).png | `f93bb68c3f4cb2d314b1ca3f714458623e0d42629c234299b3acf85e7c1b370d` |
| K-04 | [04-web-mappers.png](04-web-mappers.png) | image(20261025-220947).png | `545669230d26cbd0bbafa2b981cb20ed03b955353d06bb524c4a92285fac64ab` |
| K-05 | [05-web-evaluate.png](05-web-evaluate.png) | image(20261025-220846).png | `d936552f7b5fbca24695240bc589a819b4ecadaa75b43989adb3a523865686de` |
| K-06 | [06-portal-admin.png](06-portal-admin.png) | image(20261025-220703).png | `006a1ff277cc30c1ab605616f00ad83729623d8a78f54af539498f617618dea1` |
| K-07 | [07-portal-user.png](07-portal-user.png) | image(20261025-220631).png | `25f0b6537a734cf6a71b2fad12cdcdef36c0eed12953dd2deee346d2b28929cc` |
| K-08 | [08-admin-roles-guardados.png](08-admin-roles-guardados.png) | image(20261025-220453).png | `67428ec5ff98e049e42ecf8b98621286d956799317c4ec53732518759f986f53` |
| K-09 | [09-asignar-admin.png](09-asignar-admin.png) | image(20261025-220413).png | `806557600ac4c0f20e3d194cfc1b450a2f66d37bf1b6cdba22c8192db73c01a5` |
| K-10 | [10-asignar-user.png](10-asignar-user.png) | image(20261025-220234).png | `cf72063425420b5014129e5c7e7c4468ae61690713b0f0e12eac19b52c0238de` |

## K-01

Export sin seguimiento en main; captura histórica, no estado final de la entrega.

![Export sin seguimiento en main; captura histórica, no estado final de la entrega.](01-repo-inicial.png)

## K-02

Evaluate móvil: admin.prueba, azp quantify-mobile y rol admin. Aviso de administrador temporal visible.

![Evaluate móvil: admin.prueba, azp quantify-mobile y rol admin. Aviso de administrador temporal visible.](02-mobile-admin-evaluate.png)

## K-03

Evaluate móvil: usuario.prueba, azp quantify-mobile y rol user.

![Evaluate móvil: usuario.prueba, azp quantify-mobile y rol user.](03-mobile-user-evaluate.png)

## K-04

Mappers efectivos del cliente web; incluye realm roles. No muestra roles resultantes del usuario.

![Mappers efectivos del cliente web; incluye realm roles. No muestra roles resultantes del usuario.](04-web-mappers.png)

## K-05

Evaluate del cliente web con usuario.prueba. No muestra el resultado JSON de roles.

![Evaluate del cliente web con usuario.prueba. No muestra el resultado JSON de roles.](05-web-evaluate.png)

## K-06

Portal de cuentas autenticado con nombre Admin Prueba. No muestra username.

![Portal de cuentas autenticado con nombre Admin Prueba. No muestra username.](06-portal-admin.png)

## K-07

Portal de cuentas autenticado con usuario.prueba y perfil sintético.

![Portal de cuentas autenticado con usuario.prueba y perfil sintético.](07-portal-user.png)

## K-08

Asignación guardada: admin.prueba tiene admin y user en ese momento.

![Asignación guardada: admin.prueba tiene admin y user en ese momento.](08-admin-roles-guardados.png)

## K-09

Selección del rol admin para admin.prueba; selección sola no demuestra guardado.

![Selección del rol admin para admin.prueba; selección sola no demuestra guardado.](09-asignar-admin.png)

## K-10

Selección del rol user para usuario.prueba; selección sola no demuestra guardado.

![Selección del rol user para usuario.prueba; selección sola no demuestra guardado.](10-asignar-user.png)

## Incorporar evidencias faltantes

Pedir al usuario que coloque aquí los resultados web de ambas cuentas, username del administrador autenticado y repetición que resuelva la diferencia de roles. Revisar y retirar contraseñas, cookies, claves o tokens reutilizables antes de añadir imágenes. Si requieren saneamiento, conservar el original fuera de Git e identificar explícitamente la copia saneada; no alterar un resultado para aparentar éxito. Actualizar este índice y la tabla de pruebas con lo realmente visible.
