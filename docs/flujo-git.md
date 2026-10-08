# Flujo Git / GitHub del equipo

Basado en las diapositivas *Git y GitHub — Trabajo colaborativo en parejas con XP*.

## Ramas protegidas

| Rama | Uso |
|------|-----|
| `main` | Producción. **Nadie programa aquí.** Solo PR desde `develop` o `hotfix`. |
| `develop` | Integración de la iteración. Se llega solo por Pull Request. |

## Convención de ramas (con nombre del driver)

```
santiago/docs/<n>-<slug>          # documentación de Santiago
santiago/feature/<n>-<slug>       # historias web de Santiago
bruno/feature/<n>-<slug>          # historias móvil de Bruno
fix/<n>-<slug>                   # bugs
hotfix/<n>-<slug>                 # urgencias desde main
```

Ejemplos reales de este demo:

- `santiago/docs/1-planificacion`
- `santiago/feature/3-listado-parqueos`

## Commits

```
docs: EDT PERT Planner (#1)
feat(web): listado y registro de parqueos (#3)
```

## Issues de referencia (crear en GitHub)

### Issue #1 — Documentar planificación EDT / PERT / Planner
- Labels: `docs`
- Rama: `santiago/docs/1-planificacion`

### Issue #2 — Diseñar BD y requisitos web
- Labels: `docs`, `web`
- Rama: `santiago/docs/2-diseno` (contenido en `docs/arquitectura.md` e `historias-usuario.md`)

### Issue #3 — Implementar listado y registro de parqueos web
- Labels: `web`, `feat`
- Rama: `santiago/feature/3-listado-parqueos`
- Closes en el PR: `Closes #3`

## Ciclo diario

```bash
git switch develop
git pull origin develop
git switch -c santiago/feature/3-listado-parqueos
# ... código ...
git add .
git commit -m "feat(web): listado de parqueos (#3)"
git push -u origin santiago/feature/3-listado-parqueos
# Abrir PR → develop · Bruno prueba y aprueba · Squash and merge
```

## Prueba cruzada

- Bruno prueba los PR de `web/` y aprueba el merge.
- Santiago prueba los PR de `movil/` y aprueba el merge.
- Nadie fusiona su propio código sin la prueba del compañero.
