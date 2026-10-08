# Planner — Tablero Kanban del equipo

**Plan:** Parqueos IoT · Pareja Santiago & Bruno  
**Columnas (depósitos):** Backlog · Iteración · En progreso · En revisión (PR) · Hecho  
**Etiquetas:** `Ruta crítica` · `Web` · `Móvil` · `Fase EDT` · `Docs`

> Este documento es la fuente de verdad para crear/replicar el tablero en **Microsoft Planner** (Teams / Microsoft 365) y conectarlo con Issues de GitHub.

## Cómo nombrar cada tarea

```
[EDT] #<issue> Título corto
```

Ejemplo: `[3.2] #3 Listado de parqueos web`

- **Código EDT** → conecta con el plan y el CPM  
- **#issue** → conecta con GitHub (rama, commits, PR)  
- **Checklist** → copia los criterios de aceptación del issue  

## Asignación

Toda tarea se asigna a **ambos** integrantes.  
El **driver** del código es quien aparece en el nombre de la rama (`santiago/...` o `bruno/...`).

---

## Tablero actual (demo)

### Backlog

| Tarea | Etiquetas | IT–FT | Driver |
|-------|-----------|-------|--------|
| [3.4] #4 Reserva web de espacios | Web, Fase 3 | 14–19 | Santiago |
| [3.5] #5 Listado móvil vía API | Móvil, Fase 3 | 10–16 | Bruno |
| [3.7] #6 Ocupación IoT (futuro) | Web, IoT | buffer | Ambos |

### Iteración (actual · Iteración 2)

| Tarea | Etiquetas | IT–FT | Driver |
|-------|-----------|-------|--------|
| [3.2] #3 Listado y registro de parqueos | **Ruta crítica**, Web, Fase 3 | 5–10 | Santiago |
| [3.1] #7 Autenticación Laravel | Web, Fase 3 | 5–9 | Santiago |

### En progreso

| Tarea | Issue | Rama | Checklist |
|-------|-------|------|-----------|
| [3.2] #3 Listado y registro de parqueos | #3 | `santiago/feature/3-listado-parqueos` | Ver HU-01 / HU-02 |

### En revisión (PR)

_(vacío al inicio del demo — mover aquí al abrir el PR hacia `develop`)_

### Hecho

| Tarea | Evidencia |
|-------|-----------|
| [1.1] #1 Plan EDT y CPM | `docs/EDT.md`, `docs/PERT-CPM.md` |
| [1.2] #1 Tablero Planner documentado | `docs/PLANNER.md` |
| [2.1]/2.2] #2 Requisitos y diseño BD | `docs/historias-usuario.md`, `docs/arquitectura.md` |

---

## Flujo Planner ↔ GitHub

1. Se crea el **Issue** en GitHub → título con verbo + etiquetas `web`/`movil`.  
2. Se crea la tarea en Planner: `[EDT] #n Título` y se adjunta el enlace del issue.  
3. `git switch -c santiago/feature/n-slug` → mover a **En progreso**.  
4. Se abre el **Pull Request** hacia `develop` → **En revisión (PR)**.  
5. Merge con `Closes #n` + aprobación del compañero → **Hecho**.  
6. Release semanal → revisar vista Gráficos con el docente.

## Integración opcional (Power Automate)

- Disparador GitHub: *When an issue is assigned to me*  
- Acción Planner: *Create a task* con título `[EDT] #número Título`

## Vista semanal (lo crítico primero)

Cada lunes priorizar en rojo:

1. A → B → E → F → G → J → K (ruta crítica del CPM)  
2. Luego tareas con holgura (C, D, H, I)
