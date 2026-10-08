# Casos de uso e historias de usuario (Web · Demo)

## Roles

| Rol | Descripción |
|-----|-------------|
| Conductor | Busca parqueos disponibles en Santa Cruz |
| Oferente | Publica un parqueo (patio, lote, mall) |
| Administrador | Supervisa el catálogo |

## Caso de uso CU-01 — Consultar parqueos disponibles

- **Actor:** Conductor  
- **Canal:** Web  
- **Precondición:** ninguna (listado público)  
- **Flujo básico:**
  1. Entra al panel web.
  2. Ve el listado de parqueos activos.
  3. Filtra por zona o tipo (opcional).
  4. Abre el detalle (cupos, precio, dirección).
- **Postcondición:** el conductor conoce opciones de parqueo.

## Caso de uso CU-02 — Registrar un parqueo

- **Actor:** Oferente / Admin  
- **Canal:** Web  
- **Precondición:** sesión iniciada  
- **Flujo básico:**
  1. Inicia sesión.
  2. Elige «Nuevo parqueo».
  3. Completa nombre, tipo, zona, cupos, precio.
  4. Guarda.
- **Alterno:** datos inválidos → se muestran errores de validación.  
- **Postcondición:** el parqueo queda publicado en el catálogo.

---

## Historias de usuario (INVEST)

### HU-01 · Web · Prioridad alta · EDT 3.2 · Issue #3

> Como **conductor** quiero **ver un listado de parqueos disponibles** para **decidir dónde estacionar en Santa Cruz**.

**Criterios de aceptación**

- [ ] Dado que hay parqueos activos, cuando abro el listado, entonces veo nombre, zona, tipo, cupos y precio.
- [ ] Dado un filtro por tipo, cuando lo aplico, entonces solo veo parqueos de ese tipo.
- [ ] Dado un parqueo, cuando abro su detalle, entonces veo dirección y descripción.

**Rama:** `santiago/feature/3-listado-parqueos`

### HU-02 · Web · Prioridad alta · EDT 3.3 · Issue #3

> Como **oferente** quiero **registrar mi parqueo (patio/mall/centro)** para **ofrecer cupos a conductores**.

**Criterios de aceptación**

- [ ] Dado que inicié sesión, cuando completo el formulario válido, entonces el parqueo aparece en el listado.
- [ ] Dado un campo obligatorio vacío, cuando envío, entonces veo un mensaje de error.
- [ ] Dado cupos_disponibles > cupos_totales, cuando envío, entonces la validación lo rechaza.

**Rama:** `santiago/feature/3-listado-parqueos`

---

## Definición de «Listo» (DoD)

No se programa una historia sin:

1. Caso de uso / HU con criterios de aceptación  
2. Estimación PERT y fechas en Planner  
3. Rama nombrada con issue + nombre del driver  
4. PR hacia `develop` con evidencia de prueba  
5. Aprobación del compañero (prueba cruzada)
