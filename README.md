# Parqueos Demo — Gestión de Parqueos con IoT

Demo académica del **Proyecto de Sistemas III** (Universidad del Valle — Santa Cruz de la Sierra).

Plataforma web/móvil para publicar, consultar y gestionar estacionamientos formales e informales de la ciudad (patios, centro, malls), con visión de integración IoT.

> Repositorio de práctica del equipo. El repositorio oficial del docente se integrará cuando se habilite el acceso.

## Pareja

| Rol | Integrante | Producto |
|-----|------------|----------|
| Estudiante 1 · Móvil | Bruno Ferrufino Mercado | `movil/` |
| Estudiante 2 · Web | Santiago Roca Martínez | `web/` |

## Estructura del repositorio

```
parqueos_demo/
├── movil/          # App móvil (Bruno) — pendiente
├── web/            # App web Laravel MVC + API (Santiago)
├── docs/           # EDT, PERT/CPM, Planner, arquitectura, HU
├── .github/        # Plantillas de issue y PR
├── .gitignore
└── README.md
```

## Stack (Stack A del curso)

| Capa | Tecnología |
|------|------------|
| Web | Laravel (MVC + Blade) + API REST |
| Móvil | Flutter (consume la API de `web/`) |
| Base de datos | **SQL relacional** (MySQL/MariaDB en XAMPP para demo local; PostgreSQL alineado al stack del curso en producción) |
| Arquitectura | Cliente–servidor; la app móvil **nunca** accede directo a la BD |

Detalle: [`docs/arquitectura.md`](docs/arquitectura.md)

## Flujo Git (reglas del curso)

1. **No se programa en `main` ni en `develop`.**
2. `main` = producción (solo PR desde `develop` o `hotfix`).
3. `develop` = integración de la iteración.
4. Cada historia vive en su rama: `santiago/feature/<n>-<slug>` o `bruno/feature/<n>-<slug>`.
5. Pull Request hacia `develop` con `Closes #<issue>` y **1 aprobación del compañero**.

## Cómo levantar la web (demo)

```bash
cd web
composer install
copy .env.example .env   # Windows
php artisan key:generate
# Configurar DB en .env (MySQL XAMPP)
php artisan migrate --seed
php artisan serve
```

Abrir: <http://127.0.0.1:8000>

Credenciales demo (seeder):

- Admin: `admin@parqueos.test` / `password`
- Conductor: `conductor@parqueos.test` / `password`

## Documentación de planificación

| Documento | Ruta |
|-----------|------|
| EDT (WBS) | [`docs/EDT.md`](docs/EDT.md) |
| PERT / CPM | [`docs/PERT-CPM.md`](docs/PERT-CPM.md) |
| Planner (Kanban) | [`docs/PLANNER.md`](docs/PLANNER.md) |
| Historias / casos de uso | [`docs/historias-usuario.md`](docs/historias-usuario.md) |
| Arquitectura y BD | [`docs/arquitectura.md`](docs/arquitectura.md) |

## Funcionalidad demo actual (web)

**Listado y registro de parqueos** — consultar parqueos publicados en Santa Cruz y registrar nuevos espacios (patio, centro, mall).

- Issue de referencia: `#3`
- Rama: `santiago/feature/3-listado-parqueos`
- EDT: `3.2`

## Entrega del proyecto

Fecha objetivo de finalización: **fin de noviembre 2026**.
