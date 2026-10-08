# EDT — Estructura de Desglose del Trabajo

**Proyecto:** Gestión de Parqueos con IoT (Demo)  
**Pareja:** Santiago Roca Martínez (Web) · Bruno Ferrufino Mercado (Móvil)  
**Horizonte:** 8 oct 2026 → 28 nov 2026  
**Regla del 100 %:** la EDT incluye todo el trabajo del demo y nada más.  
**Paquete ≤ 1 semana:** si no cabe en una iteración, se divide.

## 1.0 Gestión de Parqueos con IoT

### 1 Gestión y planificación
| Código | Paquete de trabajo | Responsable |
|--------|--------------------|-------------|
| 1.1 | Plan: EDT y CPM | Ambos |
| 1.2 | Tablero Planner + Issues GitHub | Ambos |

### 2 Análisis y diseño
| Código | Paquete de trabajo | Responsable |
|--------|--------------------|-------------|
| 2.1 | Requisitos, casos de uso e historias de usuario | Ambos |
| 2.2 | Diseño de base de datos (SQL) | Ambos (lidera Web) |
| 2.3 | Diseño de interfaz web (mockups) | Santiago |
| 2.4 | Diseño de interfaz móvil (mockups) | Bruno |

### 3 Desarrollo
| Código | Paquete de trabajo | Canal | Responsable |
|--------|--------------------|-------|-------------|
| 3.1 | Autenticación y roles (API + panel web) | Web / API | Santiago |
| 3.2 | **Catálogo / listado de parqueos** | Web | Santiago |
| 3.3 | Registro de parqueos por oferente | Web | Santiago |
| 3.4 | Reserva web de espacios | Web | Santiago |
| 3.5 | Consumo API: listado en app móvil | Móvil | Bruno |
| 3.6 | Consumo API: reserva en app móvil | Móvil | Bruno |
| 3.7 | Integración IoT (ocupación / sensores) — alcance futuro | Web + IoT | Ambos |

### 4 Pruebas y documentación
| Código | Paquete de trabajo | Responsable |
|--------|--------------------|-------------|
| 4.1 | Pruebas integrales (web ↔ API ↔ móvil) | Ambos (prueba cruzada) |
| 4.2 | Manual de usuario y README | Ambos |

### 5 Despliegue
| Código | Paquete de trabajo | Responsable |
|--------|--------------------|-------------|
| 5.1 | Puesta en producción / release | Ambos |

## Trazabilidad demo (iteración actual)

| EDT | Issue | Historia | Rama | Producto |
|-----|-------|----------|------|----------|
| 1.1 / 1.2 | #1 | Planificación EDT-PERT-Planner | `santiago/docs/1-planificacion` | docs |
| 2.1 / 2.2 | #2 | Diseño BD y requisitos web | `santiago/docs/2-diseno` | docs |
| **3.2 / 3.3** | **#3** | **Listado y registro de parqueos (web)** | `santiago/feature/3-listado-parqueos` | web |

## Diagrama jerárquico

```
1.0 Gestión de Parqueos con IoT
├── 1 Gestión
│   ├── 1.1 Plan EDT y CPM
│   └── 1.2 Tablero Planner
├── 2 Análisis y diseño
│   ├── 2.1 Requisitos e HU
│   ├── 2.2 Base de datos
│   ├── 2.3 Interfaz web
│   └── 2.4 Interfaz móvil
├── 3 Desarrollo
│   ├── 3.1 Autenticación
│   ├── 3.2 Catálogo parqueos (WEB · DEMO)
│   ├── 3.3 Registro oferente
│   ├── 3.4 Reserva web
│   ├── 3.5 Listado móvil
│   ├── 3.6 Reserva móvil
│   └── 3.7 IoT ocupación (futuro)
├── 4 Pruebas y docs
│   ├── 4.1 Pruebas
│   └── 4.2 Manual
└── 5 Despliegue
    └── 5.1 Producción
```
