# Keycloak para QUANTIFY CORE

Guía local de **QUANCORE-17**, vinculada a [RF-01](../requerimientos/catalogo.md) y a las [reglas de seguridad](../seguridad/README.md). Versión del laboratorio: **Keycloak 26.8.1**, Docker, `start-dev`, dirección `http://localhost:8080`, realm `quantify`.

**Alcance:** configuración del proveedor de identidad y documentación de pruebas de laboratorio. El export auditado existe en [infrastructure/keycloak](../../infrastructure/keycloak/README.md). Las [capturas y pruebas](pruebas.md) acreditan únicamente lo indicado para cada evidencia. El login OAuth completo de React/Flutter y la validación de tokens en NestJS siguen pendientes; las cuentas del portal de Keycloak no son una implementación de las aplicaciones del producto. La decisión web SPA/BFF D-02 continúa abierta.

### Capturas del laboratorio de Keycloak

Capturas originales que el usuario compartió en el chat. Muestran sesiones históricas del portal de cuentas y simulaciones de roles; no acreditan integración OAuth completa de web, móvil y backend. [Ver las diez capturas y su contexto](../evidencias/keycloak/README.md).

**Portal de cuentas: usuario.prueba.** Sesión autenticada con el username visible.

![Portal de cuentas de Keycloak con usuario.prueba autenticado](../evidencias/keycloak/07-portal-user.png)

**Portal de cuentas: Admin Prueba.** Sesión autenticada con ese nombre; esta captura no muestra el username.

![Portal de cuentas de Keycloak con nombre Admin Prueba](../evidencias/keycloak/06-portal-admin.png)

**Evaluación móvil: usuario.prueba.** La salida simulada de `quantify-mobile` incluye `user` en `realm_access.roles`.

![Evaluate de quantify-mobile para usuario.prueba con rol user](../evidencias/keycloak/03-mobile-user-evaluate.png)

**Evaluación móvil: admin.prueba.** La salida simulada incluye `admin`. Otra captura histórica muestra asignación de `admin` y `user`: la diferencia queda pendiente de aclaración. Los resultados de roles del cliente web aún no están entre las capturas recuperadas.

![Evaluate de quantify-mobile para admin.prueba con rol admin](../evidencias/keycloak/02-mobile-admin-evaluate.png)

## Configuración auditada

| Parámetro | quantify-web | quantify-mobile |
|---|---|---|
| Protocolo | OpenID Connect | OpenID Connect |
| Tipo / Client authentication | Público / Off | Público / Off |
| Standard flow | On: Authorization Code | On: Authorization Code |
| PKCE code challenge method | S256 | S256 |
| Direct access grants | Off | Off |
| Implicit flow / Service accounts | Off / Off | Off / Off |
| Root URL | Consultar export; no sustituye redirect URI | No necesario para el callback nativo |
| Valid redirect URIs | `http://localhost:5173/*` | `com.quantify.app:/oauth2redirect` |
| Web origins | `http://localhost:5173` | Vacío; una app nativa no necesita CORS del navegador |
| Default client scope `roles` | Incluido | Incluido |
| Full scope allowed | On en laboratorio | On en laboratorio |

El comodín web reproduce el export recibido, restringido a localhost. Cuando exista una ruta real de callback, sustituirlo por su URI exacta; no inventar hoy un callback implementado. No usar `*` como origen CORS. El callback móvil requiere que Flutter/Android/iOS registren y validen el esquema; guardar la URI en Keycloak no registra ese esquema en el sistema operativo. En dispositivos/emuladores, `localhost` no apunta necesariamente a la PC: definir red, emisor y hostname de forma consistente antes de integrar.

Los roles de realm son `user` y `admin`, ambos no compuestos. El rol `admin` de QUANTIFY CORE no equivale a administrar Keycloak y no concede acceso general a hábitos o biometría privados. La API futura debe comprobar permiso y propiedad. No asignar `realm-admin` a las cuentas de demo.

Los clientes internos de Keycloak también aparecen en el export; no confundirlos con los dos clientes de producto. Por ejemplo, `admin-cli` conserva su configuración interna de direct grants. La comprobación de direct grants deshabilitados se aplica a `quantify-web` y `quantify-mobile`.

## Requisitos y estado del entorno

- Docker Desktop funcionando con contenedores Linux; conexión al registro para descargar la imagen si no existe.
- Puerto local 8080 disponible para una instalación nueva. Node.js para comprobar export y documentación; se verificó con Node 24.14.1 y Docker 29.7.2.
- Credenciales nuevas elegidas localmente y fuera de Git. No usar contraseñas comunes ni escribirlas en comandos, capturas o Jira.
- Ejecutar los ejemplos PowerShell desde la raíz del repositorio. Los comandos de inicio son procedimientos reproducibles; consultar el registro de pruebas para saber cuáles se ejecutaron en esta entrega.

En esta revisión ya existía `quantify-keycloak`, con imagen 26.8.1, comando `start-dev`, puerto `127.0.0.1:8080` y volumen `quantify-keycloak-data` montado en `/opt/keycloak/data`. Se preservó ese entorno. **No ejecutar otro `docker run` con el mismo nombre ni eliminar su volumen.**

## Usar una instalación existente

```powershell
docker ps -a --filter name=quantify-keycloak
# Solo si está detenido:
docker start quantify-keycloak
docker logs --tail 80 quantify-keycloak
```

Abrir la [consola administrativa](http://localhost:8080/admin/) y seleccionar `quantify`, evitando modificar `master` como realm de producto. Comprobar descubrimiento sin credenciales:

```powershell
$oidc = Invoke-RestMethod 'http://localhost:8080/realms/quantify/.well-known/openid-configuration'
$oidc.issuer
$oidc.code_challenge_methods_supported
```

Resultado esperado: emisor `http://localhost:8080/realms/quantify`; soporte de S256. El descubrimiento puede anunciar también `plain`: la restricción S256 se configura en cada cliente y se comprueba en el export. Anunciar S256 no prueba por sí solo su exigencia en una aplicación.

## Crear un laboratorio nuevo e importar

Este procedimiento requiere que no exista el contenedor del mismo nombre ni un realm previo en el volumen seleccionado. Si ya hay datos, usar el entorno existente o elegir otro nombre, puerto y volumen; no borrarlos para reproducir la guía. El ejemplo crea un volumen de desarrollo persistente, no una base productiva.

```powershell
node scripts/check-keycloak.mjs
$realmFile = (Resolve-Path 'infrastructure/keycloak/realm-export.json').Path
$iamBootstrapPassword = Read-Host 'Contraseña nueva para el administrador temporal' -AsSecureString
$env:KC_BOOTSTRAP_ADMIN_PASSWORD = [System.Net.NetworkCredential]::new('', $iamBootstrapPassword).Password
try {
    if ([string]::IsNullOrWhiteSpace($env:KC_BOOTSTRAP_ADMIN_PASSWORD)) { throw 'La contraseña no puede estar vacía' }
    docker run -d --name quantify-keycloak -p 127.0.0.1:8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD -v quantify-keycloak-data:/opt/keycloak/data --mount "type=bind,source=$realmFile,target=/opt/keycloak/data/import/quantify-realm.json,readonly" quay.io/keycloak/keycloak:26.8.1 start-dev --import-realm
    if ($LASTEXITCODE -ne 0) { throw 'Docker no pudo crear el laboratorio; revisar nombre, puerto y logs' }
} finally {
    Remove-Item Env:KC_BOOTSTRAP_ADMIN_PASSWORD -ErrorAction SilentlyContinue
    Remove-Variable iamBootstrapPassword -ErrorAction SilentlyContinue
}
docker logs --tail 80 quantify-keycloak
```

El montaje renombra el archivo a `quantify-realm.json`, conforme a la convención de importación. `--import-realm` omite un realm que ya existe: editar el JSON y reiniciar no lo actualiza. No sobrescribir una instancia en uso; aplicar los cambios explícitamente en consola tras revisión, o probar la importación en un laboratorio aislado. El export no es un respaldo completo de usuarios, sesiones, eventos o base de datos.

`-e KC_BOOTSTRAP_ADMIN_PASSWORD` hereda la variable de esta misma sesión PowerShell. El error `bootstrap-admin-username available only when bootstrap admin password is set` indica que no llegó la contraseña; volver a leerla de forma segura en esa sesión. No reemplazar el texto de la pregunta de `Read-Host` por la contraseña. No publicar `docker inspect` completo: las variables del contenedor pueden revelar el secreto aunque se retire de la terminal.

**Administrador temporal:** Keycloak lo crea en `master` durante el bootstrap inicial. El aviso amarillo en las capturas exige crear un administrador permanente con acceso mínimo y MFA, comprobar su acceso y eliminar manualmente la cuenta temporal. Cambiar una variable de bootstrap no rota la contraseña de una cuenta ya creada. `admin.prueba` es una cuenta de producto en `quantify`, distinta de ese administrador temporal.

## Reproducir la configuración manualmente

Si no se importa el export, crear `quantify` habilitado desde **Manage realms**. En **Clients**, crear cada cliente con los valores de la tabla y guardar también la sección **Advanced → Proof Key for Code Exchange → S256**. Los nombres de secciones pueden variar con la consola; confirmar el atributo `pkce.code.challenge.method` en el export. En **Realm roles**, crear `user` y `admin`.

En cada cliente, verificar **Client scopes**: el scope `roles` debe estar asignado por defecto y su mapper de realm roles debe escribir `realm_access.roles` en el access token. No introducir un secreto para un cliente público ni habilitar password grant para simplificar las pruebas.

## Aprovisionar cuentas de prueba fuera de Git

El export original **no contiene `users`**. Importarlo no crea estas cuentas ni sus contraseñas. Las capturas muestran cuentas existentes en el laboratorio anterior. Para reproducirlas, en **Users → Add user** crear:

| Username | Nombre sintético | Realm role mínimo |
|---|---|---|
| `usuario.prueba` | Usuario Prueba | `user` |
| `admin.prueba` | Admin Prueba | `admin` |

Si el perfil exige correo, usar exclusivamente direcciones sintéticas del laboratorio, sin datos reales. En **Credentials → Set password**, introducir un valor nuevo localmente. Usar contraseña temporal y completar el cambio en la primera sesión; si se desactiva temporalidad para una demo controlada, registrar ese alcance y rotarla al terminar. En **Role mapping → Assign role**, filtrar por realm roles y asignar los de la tabla.

Una captura histórica muestra `admin.prueba` con `admin` y `user`; la simulación móvil posterior muestra `admin` sin `user`. No asumir equivalencia ni herencia: ambos roles son no compuestos. Para este laboratorio basta el rol mínimo `admin`; si el producto necesita ambos, acordarlo y repetir las cuatro evaluaciones. No inventar que esa discrepancia quedó resuelta en el servidor.

Para el login real, abrir una ventana privada en [portal de cuentas](http://localhost:8080/realms/quantify/account/), iniciar sesión con cada cuenta por separado, completar acciones requeridas y comprobar la identidad. Cerrar sesión antes de cambiar de cuenta. Esto demuestra autenticación en el cliente interno Account Console; no demuestra redirección ni canje de código en React/Flutter.

## Operación y diagnóstico

```powershell
docker ps --filter name=quantify-keycloak
docker logs --tail 80 quantify-keycloak
docker logs --follow quantify-keycloak
# Ctrl+C termina el seguimiento de logs, no el servidor.
docker stop quantify-keycloak
docker start quantify-keycloak
```

La parada y el arranque conservan el volumen. No ejecutar `docker volume rm` ni una limpieza con volúmenes para detener el servicio. Revisar y sanear los logs antes de compartirlos. No exportar ni copiar tokens completos.

| Síntoma | Comprobación y acción |
|---|---|
| Puerto ocupado / nombre existente | Revisar `docker ps -a`; usar el contenedor existente o otro laboratorio, sin borrar datos |
| Realm no aparece tras editar JSON | La importación inicial omite realms existentes; comprobar logs y usar configuración explícita o laboratorio limpio |
| `Invalid redirect_uri` | Comparar literalmente la URI solicitada con la lista; no ampliar a `*` |
| Login pide actualizar perfil/contraseña | Completar acciones requeridas de esa cuenta; no desactivar controles globales para evitarlas |
| Falta `realm_access.roles` | Revisar rol de usuario, scope `roles`, mapper y selección de cuenta/cliente en Evaluate |
| Móvil no vuelve a la app | Revisar esquema/callback del sistema operativo y red del dispositivo; integración aún pendiente |

## Siguiente integración y producción

Pendientes: SDK OIDC web/móvil con navegador del sistema cuando corresponda, generación/verificación de PKCE, `state` y `nonce`, callback real, renovación y logout; audiencia de API y validación de firma/JWKS, `iss`, `aud`, vigencia, rol y propiedad en NestJS; pruebas de acceso permitido y denegado. No usar un ID token como bearer de la API.

Antes de producción, resolver D-02 y D-08, fijar versión/digest y mantenimiento de seguridad, ejecutar `start` con configuración productiva, HTTPS y hostname/emisor estables, base externa soportada (por ejemplo PostgreSQL), secretos gestionados fuera de Git, respaldo/restauración comprobados, MFA administrativo, cuentas de mínimo privilegio, límites de sesión, fuerza bruta, registro de eventos sin tokens y monitorización. Reducir redirects a rutas exactas y scopes a lo necesario. `start-dev`, HTTP local y un volumen Docker no equivalen a un despliegue productivo ni a una estrategia de recuperación.

## Referencias oficiales

- [Keycloak en contenedores](https://www.keycloak.org/server/containers): imagen, desarrollo y configuración de ejecución.
- [Importación y exportación](https://www.keycloak.org/server/importExport): nombres de archivo, importación inicial y límites del respaldo.
- [Bootstrap y recuperación de administradores](https://www.keycloak.org/server/bootstrap-admin-recovery): cuenta temporal y eliminación manual.
- [Administración de Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html): clientes OIDC, usuarios, roles y evaluación de scopes.

Las páginas `latest` pueden cambiar; la versión examinada en el export y la imagen del laboratorio es 26.8.1. Consultar [pruebas](pruebas.md) y [cierre de Jira](cierre-quancore-17.md) para conocer resultados y pendientes concretos.
