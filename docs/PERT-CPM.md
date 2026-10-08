# PERT / CPM — Estimación y ruta crítica

**Proyecto:** Gestión de Parqueos con IoT (Demo)  
**Unidad:** días hábiles  
**Inicio planificado:** 8 oct 2026  
**Fin objetivo:** 28 nov 2026 (~37 días hábiles / 8 semanas)

## Fórmulas PERT

\[
TE = \frac{O + 4M + P}{6} \qquad \sigma = \frac{P - O}{6}
\]

- **O** = optimista · **M** = más probable · **P** = pesimista  
- **TE** = tiempo esperado · **σ** = desviación estándar

## Tabla PERT

| Act. | EDT | Paquete de trabajo | Pred. | O | M | P | TE | σ |
|------|-----|--------------------|-------|---|---|---|----|---|
| A | 2.1 | Requisitos e historias de usuario | — | 1 | 2 | 3 | **2** | 0,33 |
| B | 2.2 | Diseño de la base de datos SQL | A | 1 | 3 | 5 | **3** | 0,67 |
| C | 2.3 | Diseño de interfaz web (mockups) | A | 1 | 2 | 4 | **2** | 0,50 |
| D | 3.1 | Autenticación y roles (Laravel) | B | 2 | 4 | 6 | **4** | 0,67 |
| E | 3.2 | Catálogo / listado de parqueos (web) | B, C | 3 | 5 | 9 | **5** | 1,00 |
| F | 3.3 | Registro de parqueos por oferente | D, E | 2 | 4 | 7 | **4** | 0,83 |
| G | 3.4 | Reserva web de espacios | F | 3 | 5 | 8 | **5** | 0,83 |
| H | 3.5 | Listado móvil (Flutter → API) | E | 3 | 5 | 10 | **6** | 1,17 |
| I | 4.2 | Manual de usuario y README | C | 1 | 2 | 4 | **2** | 0,50 |
| J | 4.1 | Pruebas integrales (prueba cruzada) | G, H | 2 | 3 | 5 | **3** | 0,50 |
| K | 5.1 | Puesta en producción / release | J, I | 1 | 2 | 4 | **2** | 0,50 |

> Actividades de planificación (1.1, 1.2) se consideran previas/paralelas a A (días 0–2) y no forman parte del camino crítico de desarrollo.

## Red CPM (cálculo forward / backward)

| Act. | TE | IT | FT | IL | FL | Holgura | Crítica |
|------|----|----|----|----|----|---------|---------|
| A | 2 | 0 | 2 | 0 | 2 | **0** | Sí |
| B | 3 | 2 | 5 | 2 | 5 | **0** | Sí |
| C | 2 | 2 | 4 | 3 | 5 | 1 | No |
| D | 4 | 5 | 9 | 6 | 10 | 1 | No |
| E | 5 | 5 | 10 | 5 | 10 | **0** | Sí |
| F | 4 | 10 | 14 | 10 | 14 | **0** | Sí |
| G | 5 | 14 | 19 | 14 | 19 | **0** | Sí |
| H | 6 | 10 | 16 | 13 | 19 | 3 | No |
| I | 2 | 4 | 6 | 20 | 22 | 16 | No |
| J | 3 | 19 | 22 | 19 | 22 | **0** | Sí |
| K | 2 | 22 | 24 | 22 | 24 | **0** | Sí |

**Duración del proyecto (ruta crítica):** 24 días hábiles  
**Ruta crítica:** **A → B → E → F → G → J → K**

Si alguna actividad crítica se atrasa, se atrasa la entrega del 28 de noviembre.

## Calendario orientativo (desde 8 oct 2026)

| Iteración | Días | Fechas aprox. | Actividades |
|-----------|------|---------------|-------------|
| Iteración 0 | 0–2 | 8–10 oct | EDT, Planner, Issues (#1) |
| Iteración 1 | 0–5 | 8–15 oct | A, B, C — requisitos, BD, mockups |
| Iteración 2 | 5–10 | 15–22 oct | E (listado web · **demo**), inicio D |
| Iteración 3 | 10–14 | 22–29 oct | F registro oferente, avance H móvil |
| Iteración 4 | 14–19 | 29 oct – 6 nov | G reserva web |
| Iteración 5 | 19–22 | 6–12 nov | J pruebas cruzadas |
| Iteración 6 | 22–24 | 12–17 nov | K release |
| Buffer | — | 17–28 nov | Ajustes, defensa IoT (3.7), defensa |

## Diagrama de red (simplificado)

```
     ┌──► C (UI web) ──────────────┐
     │                             ▼
A ───┼──► B (BD) ──► E (Listado) ──► F (Registro) ──► G (Reserva) ──► J ──► K
     │              │        ▲                         ▲
     │              │        └── D (Auth) ─────────────┘
     │              └──► H (Móvil listado) ─────────────┘
     └──► I (Manual) ──────────────────────────────────┘
```

## Lectura para Planner

Las fechas de **inicio** y **vencimiento** de cada tarea en Microsoft Planner salen de **IT** y **FT**.  
Cada lunes se planifican primero las tareas en **ruta crítica** (rojo).
