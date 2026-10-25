# Keycloak para QUANTIFY CORE — QUANCORE-17

Configuración local de identidad, relacionada con RF-01. El archivo `realm-export.json` procede del export local Keycloak 26.8.1 auditado; no incluye cuentas, contraseñas, claves de firma ni tokens. Los usuarios de prueba se aprovisionan fuera de Git. Los clientes `quantify-web` y `quantify-mobile` son públicos y usan Authorization Code + PKCE S256.

Comprobación estática desde la raíz:

```powershell
node scripts/check-keycloak.mjs
```

El export no implementa clientes web/Flutter ni protección de API. La configuración HTTP, el callback web con comodín limitado a localhost y `fullScopeAllowed` son exclusivos del laboratorio y requieren revisión antes de producción. Los clientes internos de Keycloak conservan sus valores de origen: por ejemplo `admin-cli` tiene direct grants; la prohibición comprobada corresponde a los dos clientes QUANTIFY.

El original se preservó localmente en `.git/quancore-17-private/realm-export.original.json`, fuera del índice. No publicar ese respaldo ni añadir exports nuevos sin auditarlos.

Consulta la [guía de configuración y operación](../../docs/keycloak/README.md) para iniciar el laboratorio, crear cuentas sin guardar sus contraseñas y revisar los pendientes de integración.
