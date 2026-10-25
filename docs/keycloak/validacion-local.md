# Registro de validación local — QUANCORE-17

Fecha de revisión: **25 de octubre de 2026**. Entorno: Windows y PowerShell, Node.js **24.14.1**, Docker cliente/servidor **29.7.2**, Keycloak **26.8.1**. Este registro contiene resultados observados; no incluye secretos, JWT ni logs completos. [Interpretación de las pruebas](pruebas.md).

## Comprobaciones realizadas

| Comprobación | Resultado observado |
|---|---|
| `git fetch origin`, estado y ramas | Correcto; inicio en `main` con `realm-export.json` sin seguimiento y sin otros cambios locales |
| Base de trabajo | `origin/develop` y `develop` en `076d0ad`; feature creada desde esa base |
| Referencia `main` | Se conserva en `7a4266f`, sin commits ni fusiones sobre ella |
| Preservación del export | Copia original en `.git/quancore-17-private/realm-export.original.json`, fuera del índice; comparación JSON profunda idéntica al archivo incorporado, con formato normalizado |
| Auditoría del export | Sin usuarios, contraseñas, secretos de cliente, material criptográfico privado ni tokens detectados. Los dos campos de tipo de autenticador `credentials` contienen `webauthn-passwordless`, no credenciales |
| `node scripts/check-keycloak.mjs` | Correcto: JSON, versión, realm, roles, clientes públicos, S256, grants deshabilitados, redirects y mapper |
| Controles negativos con copias sintéticas temporales | Rechazó los seis casos: secreto de cliente, credenciales de usuario, clave privada, JWT compacto, PKCE plain y direct grants activados; copias eliminadas después |
| Identificación de cliente web | ID del export coincide con la URL visible en K-04/K-05; esas capturas muestran mappers, no resultados de roles web |
| Integridad de evidencias | Diez archivos PNG sin editar; SHA-256 verificados contra su índice |
| Servidor existente | `quantify-keycloak` siguió activo; loopback 8080, imagen 26.8.1, comando `start-dev`, volumen `quantify-keycloak-data` preservado |
| Descubrimiento existente | Respondió issuer `http://localhost:8080/realms/quantify` y soporte S256; no se usaron credenciales |
| Importación aislada | Contenedor `quantify-keycloak-quancore17-check`, puerto loopback 18080, sin montar el volumen existente y sin bootstrap de administrador. Logs de importación satisfactoria y arranque 26.8.1 |
| Descubrimiento aislado | Respondió issuer `http://localhost:18080/realms/quantify` y soporte S256 |
| Limpieza del ensayo | Contenedor temporal detenido y eliminado por `--rm`; no permaneció en `docker ps -a`; servidor original activo |

El ensayo aislado se inició con este comando real (desde PowerShell, usando la ruta absoluta del repositorio para el bind):

```powershell
docker run -d --rm --name quantify-keycloak-quancore17-check -p 127.0.0.1:18080:8080 --mount 'type=bind,source=C:\Users\telle\OneDrive\Escritorio\Quantify-Core\infrastructure\keycloak\realm-export.json,target=/opt/keycloak/data/import/quantify-realm.json,readonly' quay.io/keycloak/keycloak:26.8.1 start-dev --import-realm
```

Después se consultó `http://localhost:18080/realms/quantify/.well-known/openid-configuration`, se filtraron los logs de importación/arranque y se ejecutó `docker stop quantify-keycloak-quancore17-check`. No se crearon cuentas ni se intentó autenticar las aplicaciones en ese contenedor.

## Validación documental de la entrega

Desde la raíz del repositorio:

```powershell
node scripts/check-keycloak.mjs
node scripts/check-docs.mjs
git diff --check origin/develop...HEAD
```

Resultado final documentado tras ejecutar las comprobaciones: **77 archivos Markdown, 530 enlaces locales, 53 bloques Mermaid; rutas, capitalización, bloques y referencias comprobados**. El control existente de OpenAPI también informó JSON válido, 5 rutas y 22 referencias distintas; eso no acredita endpoints implementados. Diff sin errores de espacios. La revisión inicial detectó el enlace a este registro aún no creado; se completó el archivo y se repitió la validación.

## Límites y pendientes

No se repitieron logins reales con contraseñas en esta sesión; la evidencia de portal y Evaluate es histórica. No se ejecutaron login/callback/canje OAuth de React/Flutter, validación/autoridad de tokens en NestJS, logout/renovación ni pruebas productivas. No se retiró el administrador temporal del entorno original ni se resolvió la diferencia de roles de admin. No se subieron ramas, crearon PR ni fusionaron cambios. El estado remoto de Jira se consultó sin modificarlo.

La ausencia de patrones sensibles detectados no garantiza que toda cadena arbitraria sea inocua; se exige revisión del contenido y de futuras capturas antes de publicar. La aceptación completa se mantiene en el [checklist de QUANCORE-17](cierre-quancore-17.md).
