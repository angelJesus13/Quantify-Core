# QUANCORE-17 — aceptación y preparación del PR

[Tarea en Jira](https://utxicotepec-team-q5ufett6.atlassian.net/browse/QUANCORE-17): **Configurar Keycloak, realm, cliente web/móvil y roles**. Relación con [RF-01](../requerimientos/catalogo.md). Consulta realizada el 25 de octubre de 2026: Jira figura como **Listo**. Esta entrega no cambió su estado ni publicó comentarios.

El criterio de aceptación de Jira dice: «Realm y clientes configurados, roles de usuario/admin y cuentas de prueba». Su definición de terminado también exige implementación y pruebas verificadas, integración en rama principal y evidencia/documentación suficiente para demo académica. El estado de Jira no acredita por sí mismo esos resultados. Esta rama prepara configuración y documentación revisables; **no certifica cierre completo de la definición de terminado**.

## Matriz de aceptación

Los identificadores IAM-xx organizan esta revisión; no son criterios oficiales nuevos de Jira.

| ID | Criterio y comprobación | Estado real de esta entrega | Referencia |
|---|---|---|---|
| IAM-01 | Realm `quantify` habilitado en Keycloak 26.8.1 | Verificado en JSON, discovery del servidor existente e importación aislada | [V-02 a V-05](pruebas.md) |
| IAM-02 | Clientes públicos web/móvil con Authorization Code + PKCE S256; sin direct grants | Verificado estáticamente en export importable; no se probó aún el canje OAuth de las apps | [Configuración y valores](README.md) |
| IAM-03 | Roles de realm `user` y `admin` | Verificados en JSON y capturas históricas | [K-08 a K-10](../evidencias/keycloak/README.md) |
| IAM-04 | Cuentas `usuario.prueba` y `admin.prueba` | Existencia histórica documentada en consola; export sin usuarios, reprovisión manual necesaria. Diferencia entre asignación y simulación de admin pendiente de aclarar | [Cuentas y límites](README.md) |
| IAM-05 | Autenticación real en portal de cuentas | Histórico: username de usuario visible; nombre Admin Prueba visible. No se repitió login ni se capturó username de admin en este trabajo | [K-06/K-07](../evidencias/keycloak/README.md) |
| IAM-06 | Evaluación de `realm_access.roles` para ambos clientes y cuentas | Móvil: dos simulaciones históricas disponibles. Web: mapper visible; faltan dos resultados de claims | [Matriz de cuatro casos](pruebas.md) |
| IAM-07 | Documentación y evidencia para demo | Guía, export auditado, diez imágenes originales, índice con hashes y procedimientos disponibles; pendientes explícitos | [Guía](README.md), [evidencias](../evidencias/keycloak/README.md) |
| IAM-08 | Seguridad y reproducibilidad de repositorio | Sin secretos detectados en export; original conservado fuera del índice; no se guardaron contraseñas de prueba. Importación aislada satisfactoria | [Validación local](validacion-local.md) |
| IAM-09 | Integración conforme al flujo del equipo | Pendiente PR feature → develop; posterior release → main según revisión. No se hizo push ni merge | [Git Flow](../guias/git-flow.md) |
| IAM-10 | OAuth completo web/móvil y autorización de backend | Pendiente implementación y pruebas; fuera de lo acreditado por esta configuración de IAM | [Integración posterior](pruebas.md) |

La configuración de laboratorio no cierra D-02 (sesión/arquitectura web) ni D-08 (operación). El comodín local web, scopes amplios, cuenta admin temporal y `start-dev` requieren revisión según la guía. Los volúmenes de desarrollo no equivalen a un despliegue productivo.

## Checklist antes de solicitar cierre técnico

- [x] Preservar el único archivo local no confirmado y no alterar `main`.
- [x] Actualizar referencias y crear `feature/QUANCORE-17-keycloak-iam` desde `origin/develop` (`076d0ad`).
- [x] Incorporar export auditado sin cuentas/secretos y comprobar importación con la imagen 26.8.1.
- [x] Documentar configuración, roles, cuentas, arranque/parada/logs y recomendaciones de producción.
- [x] Conservar capturas reales y separar simulación, sesión de portal e integración pendiente.
- [ ] Colocar en `docs/evidencias/keycloak/` los resultados originales de roles de web para las dos cuentas y username de admin dentro del portal, tras revisar secretos.
- [ ] Repetir las cuatro evaluaciones y resolver/documentar la diferencia de roles de `admin.prueba`.
- [ ] Crear administrador permanente seguro, comprobar su acceso y retirar el administrador temporal del laboratorio cuando corresponda; no afirmar que ya se hizo.
- [ ] Revisar el PR y autorizar su publicación; integrar en `develop` y seguir el proceso de release hacia `main` si se exige para cierre.
- [ ] Completar los criterios de integración de producto cuando esa implementación forme parte de una entrega; no atribuirlos a estas capturas.

## Commits y flujo

Se separó trabajo real en cuatro commits: configuración/auditoría, guía, pruebas/evidencias e índices/checklist. Se usaron fechas reales de Git; no se fabricó actividad ni se modificó identidad de autor. Los SHA se consultan con:

```powershell
git log --oneline origin/develop..feature/QUANCORE-17-keycloak-iam
git diff --stat origin/develop...feature/QUANCORE-17-keycloak-iam
```

`main` se dejó en su referencia inicial `7a4266f`; `develop` quedó sincronizado con `origin/develop`, `076d0ad`. No se fusionó `main` sobre la feature: el flujo es rama publicada `main`, línea de integración `develop`, trabajo feature creado desde develop.

Antes de publicar, ejecutar desde la raíz:

```powershell
git status --short --branch
node scripts/check-keycloak.mjs
node scripts/check-docs.mjs
git diff --check origin/develop...HEAD
```

No incluir el respaldo de `.git/quancore-17-private/`, exports nuevos ni credenciales. Si `develop` avanza antes de abrir el PR, revisar su diferencia y actualizar la rama de forma que preserve su trabajo e historial; no forzar una rama compartida.

**Solo cuando el usuario autorice subir al remoto**, publicar:

```powershell
git push -u origin feature/QUANCORE-17-keycloak-iam
```

Después abrir un PR con base **develop** y compare **feature/QUANCORE-17-keycloak-iam**, preferentemente borrador mientras falten evidencias de la matriz. No dirigir este PR a `main`. No se creó un PR remoto en esta entrega.

## Texto propuesto para el PR

Título: `chore(iam): configurar Keycloak local y documentar QUANCORE-17`

**Cambio y propósito:** incorporar el realm local `quantify` auditado, con clientes públicos web/móvil, Code + PKCE S256 y roles `user`/`admin`. Centralizar instalación, operación y evidencia para reproducir el laboratorio sin versionar credenciales.

**Alcance:** QUANCORE-17 / RF-01; infraestructura Keycloak, validación estática y documentación en español. Las cuentas se aprovisionan manualmente. La decisión SPA/BFF y la integración React/Flutter/NestJS siguen pendientes.

**Validación:** export validado; importación correcta en contenedor temporal Keycloak 26.8.1 y discovery del realm. Consultar el registro de validación local para enlaces, controles negativos y Git. Diez capturas históricas inspeccionadas y conservadas sin editar. Falta completar resultados web y aclarar diferencia de roles de admin.

**Compatibilidad y operación:** HTTP y volumen locales para desarrollo; no desplegar `start-dev` en producción. El import inicial no sobrescribe realms existentes ni crea las cuentas ausentes del export. La cuenta administrativa temporal debe retirarse después de establecer acceso permanente seguro. Sin modificaciones al contrato de API ni implementación de permisos de negocio.
