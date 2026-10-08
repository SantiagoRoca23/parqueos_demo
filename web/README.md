# Web — Gestión de Parqueos con IoT

**Responsable:** Santiago Roca Martínez  
**Stack:** Laravel 11 · MVC (Blade) · SQLite (demo) / MySQL·PostgreSQL (prod)  
**Funcionalidad demo:** Listado y registro de parqueos (Issue `#3`, EDT `3.2` / `3.3`)

## Requisitos

- PHP 8.2+
- Composer
- Extensiones: pdo_sqlite (demo) o pdo_mysql

## Instalación

```bash
cd web
composer install
copy .env.example .env
php artisan key:generate
php artisan migrate --seed
php artisan serve
```

Abrir <http://127.0.0.1:8000>

## Cuentas demo

| Rol | Email | Password |
|-----|-------|----------|
| Admin | admin@parqueos.test | password |
| Oferente | oferente@parqueos.test | password |
| Conductor | conductor@parqueos.test | password |

## Rutas principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/parqueos` | Listado + filtros |
| GET | `/parqueos/{id}` | Detalle |
| GET | `/parqueos-crear/nuevo` | Formulario (auth oferente/admin) |
| POST | `/parqueos` | Guardar parqueo |
| GET/POST | `/login` | Autenticación |

## Rama de esta funcionalidad

`santiago/feature/3-listado-parqueos` → PR hacia `develop` (no a `main`).
