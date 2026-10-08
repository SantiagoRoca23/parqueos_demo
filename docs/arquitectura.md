# Arquitectura y base de datos

**Proyecto:** Gestión de Parqueos con IoT  
**Stack del curso:** Stack A — Laravel (web/API) + Flutter (móvil)  
**Patrón web:** MVC (Model–View–Controller) en Laravel

## 1. Visión de arquitectura

```
┌─────────────────┐     HTTPS/JSON      ┌──────────────────────────┐
│  movil/         │ ──────────────────► │  web/  (Laravel)         │
│  Flutter        │ ◄────────────────── │  - Panel Blade (MVC)     │
│  (Bruno)        │                     │  - API REST              │
└─────────────────┘                     │  - Auth / Roles          │
                                        └────────────┬─────────────┘
                                                     │ Eloquent ORM
                                                     ▼
                                        ┌──────────────────────────┐
                                        │  Base de datos SQL       │
                                        │  MySQL (demo XAMPP)      │
                                        │  PostgreSQL (prod curso) │
                                        └──────────────────────────┘
```

Reglas del curso:

- Un solo stack por pareja.
- La app móvil **nunca** se conecta directo a la BD; solo consume la API de `web/`.
- Carpetas por producto (`web/`, `movil/`), no por capa.

## 2. Tipo de base de datos: SQL (relacional)

Se elige **SQL relacional** (no NoSQL ni híbrida en esta etapa) porque:

| Motivo | Detalle |
|--------|---------|
| Datos estructurados | Usuarios, parqueos, cupos, reservas y roles tienen relaciones claras |
| Integridad | Foreign keys evitan reservas huérfanas o parqueos sin dueño |
| Stack del curso | Laravel + migraciones + PostgreSQL/MySQL |
| Consultas | Filtros por zona, tipo (patio/mall/centro), precio y disponibilidad |

### ¿Y el IoT?

Los sensores de ocupación (estilo Disney Springs) generan telemetría de alta frecuencia.  
**En una versión futura** se puede adoptar un enfoque **híbrido**:

- **SQL:** catálogo, usuarios, reservas, pagos.  
- **Time-series / NoSQL (opcional):** lecturas de sensores, histórico de ocupación.

Para el demo actual **no se implementa IoT físico**; el campo `cupos_disponibles` simula la ocupación y deja el gancho para sensores.

## 3. Modelo de datos (demo)

### `users`
| Campo | Tipo | Notas |
|-------|------|-------|
| id | bigint PK | |
| name | string | |
| email | string unique | |
| password | string | hashed |
| role | enum | `admin`, `oferente`, `conductor` |
| timestamps | | |

### `parqueos`
| Campo | Tipo | Notas |
|-------|------|-------|
| id | bigint PK | |
| user_id | FK → users | Dueño / oferente |
| nombre | string | Ej. "Patio Av. Banzer" |
| tipo | enum | `patio`, `centro`, `mall`, `otro` |
| direccion | string | |
| zona | string | Ej. Equipetrol, Centro |
| latitud / longitud | decimal nullable | Para mapa futuro |
| cupos_totales | int | |
| cupos_disponibles | int | Simula IoT / estado |
| precio_hora | decimal | BOB |
| descripcion | text nullable | |
| activo | boolean | |
| timestamps | | |

### Relaciones
- Un **usuario** (oferente) tiene muchos **parqueos**.
- Un **parqueo** pertenece a un **usuario**.
- Futuro: `reservas` (parqueo_id, user_id, inicio, fin, estado).

## 4. Capas MVC en `web/`

| Capa | Responsabilidad | Ejemplo |
|------|-----------------|---------|
| Model | Persistencia Eloquent | `App\Models\Parqueo` |
| View | Blade (UI panel) | `resources/views/parqueos/*` |
| Controller | Orquestación HTTP | `ParqueoController` |
| Routes | Entrada web | `routes/web.php` |
| Migrations / Seeders | Esquema y datos demo | `database/` |

## 5. Seguridad básica

- Contraseñas hasheadas (bcrypt).
- Middleware `auth` para crear/editar parqueos.
- Validación de formularios en Form Request / Controller.
- `.env` fuera de Git (secretos y credenciales DB).

## 6. Despliegue local (XAMPP)

1. Crear BD `parqueos_demo` en phpMyAdmin / MySQL.  
2. Configurar `web/.env` (`DB_DATABASE`, `DB_USERNAME`, `DB_PASSWORD`).  
3. `php artisan migrate --seed`  
4. `php artisan serve`
