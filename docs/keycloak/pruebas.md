# Pruebas y límites de la evidencia

Revisión del **25 de octubre de 2026** para QUANCORE-17. [Guía](README.md) · [Capturas originales recuperadas](../evidencias/keycloak/README.md) · [Checklist de aceptación](cierre-quancore-17.md).

## Qué se comprobó en esta entrega

Entorno: Windows/PowerShell, Node.js 24.14.1, Docker cliente/servidor 29.7.2 e imagen `quay.io/keycloak/keycloak:26.8.1`.

| ID | Comprobación realmente ejecutada | Resultado y límite |
|---|---|---|
| V-01 | `git status`, ramas, remotos y `git fetch origin` | Inicio en `main`, único cambio local: export sin seguimiento. `origin/develop` actualizado en `076d0ad`. Rama feature creada desde esa base; main sin cambios |
| V-02 | Auditoría recursiva del export original y `node scripts/check-keycloak.mjs` | JSON válido; realm habilitado, roles `user`/`admin`, ambos clientes públicos, Code + S256, direct grants/implicit/service accounts deshabilitados, redirects y mapper correctos. Sin campos de secretos ni patrones de claves/JWT detectados |
| V-03 | `docker ps` e inspección selectiva de comando y montajes, sin mostrar variables | Servidor existente `quantify-keycloak`, imagen 26.8.1, `start-dev`, loopback 8080, volumen `quantify-keycloak-data` |
| V-04 | Descubrimiento OIDC del servidor existente | Respuesta satisfactoria; issuer `http://localhost:8080/realms/quantify`, endpoints OIDC y S256 anunciados. No implica comprobar el estado de todos sus clientes |
| V-05 | Importación en contenedor temporal nuevo sin credenciales, puerto loopback 18080, sin el volumen existente | Logs: `Realm 'quantify' imported`, `Import finished successfully`, Keycloak 26.8.1 iniciado; discovery respondió con issuer en 18080. Contenedor temporal detenido y eliminado por `--rm` al finalizar |

V-05 usa el mismo JSON versionado montado como `/opt/keycloak/data/import/quantify-realm.json`. No se importó sobre el entorno del usuario ni se cambiaron sus cuentas. La aceptación del JSON por Keycloak no prueba el login de los clientes de producto.

La auditoría revisó campos sensibles y patrones de PEM/JWT/valores codificados, y la estructura de proveedores de claves. El export incluye configuración de generadores de claves, no material privado exportado. Dos campos `authenticatorConfig.*.config.credentials` contienen el identificador de tipo `webauthn-passwordless`, no credenciales de usuarios; el validador permite exclusivamente esos identificadores conocidos en esa ubicación. No se eliminó información funcional a ciegas. Una revisión estática no puede demostrar ausencia absoluta de secretos arbitrarios; revisar también todo diff antes de publicar. El original permanece fuera del índice en `.git/quancore-17-private/realm-export.original.json`.

## Evidencia histórica recuperada

Las capturas provienen de la conversación «Configurar Keycloak en Jira», no de nuevas sesiones de login realizadas por este agente. Se copiaron sin editar y sus hashes están en el índice de evidencias. Solo se incluyen nombres y correo sintéticos de las cuentas de laboratorio; no hay contraseñas, claves ni JWT compactos visibles. Los fragmentos de claims corresponden a la salida simulada de **Evaluate**.

| Caso | Evidencia disponible | Qué demuestra |
|---|---|---|
| Usuario en portal real | K-07 | Portal `realms/quantify/account`, username `usuario.prueba` y nombre Usuario Prueba visibles: sesión autenticada histórica de Account Console |
| Administrador en portal real | K-06 | Portal de cuentas con nombre Admin Prueba y Account Console en uso; compatible con la cuenta `admin.prueba`, pero esa captura no muestra el username |
| Asignación de roles | K-08, K-09, K-10 | `user` y `admin` disponibles; K-08 muestra asignación guardada de ambos roles a `admin.prueba` en ese momento |
| Evaluación web | K-04, K-05 | URL del cliente que corresponde al ID de `quantify-web` en el export; Evaluate con `usuario.prueba` y mapper `realm roles`. No se ve el resultado JSON con roles para web |
| Evaluación móvil de usuario | K-03 | `azp: quantify-mobile`, selección `usuario.prueba`, `realm_access.roles` incluye `user`, sin `admin` en el arreglo visible |
| Evaluación móvil de administrador | K-02 | `azp: quantify-mobile`, selección `admin.prueba`, `realm_access.roles` incluye `admin`, sin `user` en el arreglo visible |

**Discrepancia abierta:** K-08 muestra `admin` y `user` asignados, mientras K-02 muestra solo `admin` entre los roles de producto. Pueden corresponder a estados distintos; no se dispone de una secuencia completa que explique el cambio. No se afirma una sincronización actual ni se modifica el servidor para ocultar la diferencia.

## Repetir login y evaluación de los dos clientes

Primero aprovisionar las cuentas conforme a la guía; no hay contraseñas en el export. Estos pasos son un **procedimiento pendiente de repetición completa**, no resultados nuevos de esta entrega.

1. En ventana privada, abrir `http://localhost:8080/realms/quantify/account/`, autenticar `usuario.prueba`, verificar username y cerrar sesión. Repetir con `admin.prueba`, verificando también username. No incluir contraseñas o cookies en capturas.
2. En consola administrativa → realm `quantify` → **Clients → quantify-web → Client scopes → Evaluate**, elegir scope `openid` y usuario `usuario.prueba`.
3. Abrir **Generated access token**. Revisar el JSON de claims, `azp` y `realm_access.roles`. No copiar el JWT completo. Repetir con `admin.prueba`.
4. Repetir los dos casos para `quantify-mobile`.
5. Registrar la cuenta y rol realmente asignados, fecha y resultado; si no coincide, revisar **Role mapping**, scope `roles`, mapper y roles efectivos. Nunca marcar un resultado esperado como observado.

| Cliente | Cuenta | Resultado esperado de roles de producto | Evidencia actual |
|---|---|---|---|
| `quantify-web` | `usuario.prueba` | Incluye `user`; no `admin` | Pendiente captura del resultado |
| `quantify-web` | `admin.prueba` | Incluye `admin`; registrar si tiene además `user` | Pendiente captura del resultado |
| `quantify-mobile` | `usuario.prueba` | Incluye `user`; no `admin` | Histórico observado K-03 |
| `quantify-mobile` | `admin.prueba` | Incluye `admin`; registrar si tiene además `user` | Histórico observado K-02; discrepancia K-08 abierta |

Otros roles como `offline_access`, `uma_authorization` y `default-roles-quantify` no son permisos de negocio `user`/`admin`. No usar el orden del arreglo como criterio. Los fragmentos JSON aportados en el chat corroboran los nombres de roles, pero por sí solos no identifican cliente/cuenta.

**Evaluate es una simulación de mappers y scope mappings.** No ejecuta el callback del producto, no prueba el canje real de código con `code_verifier`, la firma/validación de un bearer por NestJS ni la autorización de recursos. El login real del portal usa un cliente interno distinto. Juntas, esas pruebas siguen sin acreditar la integración OAuth de web, móvil y backend.

## Evidencias que faltan

Colocar las capturas originales faltantes en `docs/evidencias/keycloak/` y actualizar su índice después de revisar que no expongan secretos. Faltan los dos resultados de roles para `quantify-web`, la identificación explícita de `admin.prueba` dentro del portal, y la repetición documentada que aclare la discrepancia de roles. Para evidenciar ajustes de consola pueden agregarse capturas de PKCE/direct grants de ambos clientes; hoy su comprobación proviene del JSON auditado. No se crearon imágenes de sustitución ni enlaces a archivos inexistentes.

## Criterios para la integración posterior

- Login, callback, logout y renovación reales en cada aplicación; canje con S256 y rechazo sin/verifier incorrecto, `state` inválido o redirect no autorizado.
- API con access token: acceso autorizado y rechazo de firma inválida, issuer/audiencia incorrectos, token vencido y rol insuficiente. La configuración de audiencia de API todavía debe definirse.
- Propiedad de recursos, suspensión/revocación y aislamiento de privilegios de administración; no basta mostrar/ocultar una pantalla.
- Registro de entorno y evidencia saneada para cada caso. Evitar datos personales y tokens reutilizables.

Consultar la [definición de terminado y checklist de Jira](cierre-quancore-17.md); esta documentación no marca automáticamente todos esos casos como aprobados.
