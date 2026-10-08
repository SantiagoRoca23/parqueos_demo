# -*- coding: utf-8 -*-
"""Genera documentos Word a partir de la documentación del proyecto."""

from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT_DIR = Path(__file__).resolve().parent / "word"
OUT_DIR.mkdir(exist_ok=True)


def set_run_font(run, size=11, bold=False, italic=False, name="Arial Narrow"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)


def add_heading(doc, text, level=1):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT if level > 1 else WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12 if level == 1 else 8)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    run = p.add_run(text)
    sizes = {1: 14, 2: 12, 3: 11}
    set_run_font(run, size=sizes.get(level, 11), bold=True)
    return p


def add_para(doc, text, bold=False, italic=False, center=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    # soporte simple **negrita**
    parts = text.split("**")
    for i, part in enumerate(parts):
        if not part:
            continue
        run = p.add_run(part)
        set_run_font(run, bold=bold or (i % 2 == 1), italic=italic)
    return p


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    p.clear()
    parts = text.split("**")
    for i, part in enumerate(parts):
        if not part:
            continue
        run = p.add_run(part)
        set_run_font(run, bold=(i % 2 == 1))
    return p


def shade_header_cells(row):
    for cell in row.cells:
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:fill"), "D9E2EC")
        shd.set(qn("w:val"), "clear")
        tcPr.append(shd)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    hdr = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(h)
        set_run_font(run, size=9, bold=True)
    shade_header_cells(hdr)
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            set_run_font(run, size=9)
    doc.add_paragraph()
    return table


def add_code(doc, text):
    for line in text.strip("\n").splitlines():
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(line if line else " ")
        set_run_font(run, size=9, name="Consolas")
    doc.add_paragraph()


def new_doc():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
    style = doc.styles["Normal"]
    style.font.name = "Arial Narrow"
    style.font.size = Pt(11)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial Narrow")
    return doc


def portada(doc, titulo):
    add_para(doc, "UNIVERSIDAD DEL VALLE", bold=True, center=True)
    add_para(doc, "Proyecto de Sistemas III", center=True)
    add_para(doc, "Gestión de Parqueos con IoT — Demo", center=True)
    doc.add_paragraph()
    add_heading(doc, titulo, 1)
    add_para(doc, "Autores: Santiago Roca Martínez · Bruno Ferrufino Mercado", center=True)
    add_para(doc, "Santa Cruz de la Sierra, Bolivia — Octubre 2026", center=True)
    doc.add_paragraph()


def build_edt(doc):
    portada(doc, "EDT — Estructura de Desglose del Trabajo")
    add_para(doc, "**Proyecto:** Gestión de Parqueos con IoT (Demo)")
    add_para(doc, "**Pareja:** Santiago Roca Martínez (Web) · Bruno Ferrufino Mercado (Móvil)")
    add_para(doc, "**Horizonte:** 8 oct 2026 → 28 nov 2026")
    add_para(doc, "**Regla del 100 %:** la EDT incluye todo el trabajo del demo y nada más.")
    add_para(doc, "**Paquete ≤ 1 semana:** si no cabe en una iteración, se divide.")

    add_heading(doc, "1.0 Gestión de Parqueos con IoT", 2)
    add_heading(doc, "1 Gestión y planificación", 3)
    add_table(doc, ["Código", "Paquete de trabajo", "Responsable"], [
        ["1.1", "Plan: EDT y CPM", "Ambos"],
        ["1.2", "Tablero Planner + Issues GitHub", "Ambos"],
    ])
    add_heading(doc, "2 Análisis y diseño", 3)
    add_table(doc, ["Código", "Paquete de trabajo", "Responsable"], [
        ["2.1", "Requisitos, casos de uso e historias de usuario", "Ambos"],
        ["2.2", "Diseño de base de datos (SQL)", "Ambos (lidera Web)"],
        ["2.3", "Diseño de interfaz web (mockups)", "Santiago"],
        ["2.4", "Diseño de interfaz móvil (mockups)", "Bruno"],
    ])
    add_heading(doc, "3 Desarrollo", 3)
    add_table(doc, ["Código", "Paquete de trabajo", "Canal", "Responsable"], [
        ["3.1", "Autenticación y roles (API + panel web)", "Web / API", "Santiago"],
        ["3.2", "Catálogo / listado de parqueos", "Web", "Santiago"],
        ["3.3", "Registro de parqueos por oferente", "Web", "Santiago"],
        ["3.4", "Reserva web de espacios", "Web", "Santiago"],
        ["3.5", "Consumo API: listado en app móvil", "Móvil", "Bruno"],
        ["3.6", "Consumo API: reserva en app móvil", "Móvil", "Bruno"],
        ["3.7", "Integración IoT (ocupación / sensores) — futuro", "Web + IoT", "Ambos"],
    ])
    add_heading(doc, "4 Pruebas y documentación", 3)
    add_table(doc, ["Código", "Paquete de trabajo", "Responsable"], [
        ["4.1", "Pruebas integrales (web ↔ API ↔ móvil)", "Ambos (prueba cruzada)"],
        ["4.2", "Manual de usuario y README", "Ambos"],
    ])
    add_heading(doc, "5 Despliegue", 3)
    add_table(doc, ["Código", "Paquete de trabajo", "Responsable"], [
        ["5.1", "Puesta en producción / release", "Ambos"],
    ])

    add_heading(doc, "Trazabilidad demo (iteración actual)", 2)
    add_table(doc, ["EDT", "Issue", "Historia", "Rama", "Producto"], [
        ["1.1 / 1.2", "#1", "Planificación EDT-PERT-Planner", "santiago/docs/1-planificacion", "docs"],
        ["2.1 / 2.2", "#2", "Diseño BD y requisitos web", "santiago/docs/2-diseno", "docs"],
        ["3.2 / 3.3", "#3", "Listado y registro de parqueos (web)", "santiago/feature/3-listado-parqueos", "web"],
    ])

    add_heading(doc, "Diagrama jerárquico", 2)
    add_code(doc, """1.0 Gestión de Parqueos con IoT
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
    └── 5.1 Producción""")


def build_pert(doc):
    portada(doc, "PERT / CPM — Estimación y ruta crítica")
    add_para(doc, "**Proyecto:** Gestión de Parqueos con IoT (Demo)")
    add_para(doc, "**Unidad:** días hábiles")
    add_para(doc, "**Inicio planificado:** 8 oct 2026")
    add_para(doc, "**Fin objetivo:** 28 nov 2026 (~37 días hábiles / 8 semanas)")

    add_heading(doc, "Fórmulas PERT", 2)
    add_para(doc, "TE = (O + 4M + P) ÷ 6")
    add_para(doc, "σ = (P − O) ÷ 6")
    add_bullet(doc, "**O** = optimista · **M** = más probable · **P** = pesimista")
    add_bullet(doc, "**TE** = tiempo esperado · **σ** = desviación estándar")

    add_heading(doc, "Tabla PERT", 2)
    add_table(doc, ["Act.", "EDT", "Paquete de trabajo", "Pred.", "O", "M", "P", "TE", "σ"], [
        ["A", "2.1", "Requisitos e historias de usuario", "—", "1", "2", "3", "2", "0,33"],
        ["B", "2.2", "Diseño de la base de datos SQL", "A", "1", "3", "5", "3", "0,67"],
        ["C", "2.3", "Diseño de interfaz web (mockups)", "A", "1", "2", "4", "2", "0,50"],
        ["D", "3.1", "Autenticación y roles (Laravel)", "B", "2", "4", "6", "4", "0,67"],
        ["E", "3.2", "Catálogo / listado de parqueos (web)", "B, C", "3", "5", "9", "5", "1,00"],
        ["F", "3.3", "Registro de parqueos por oferente", "D, E", "2", "4", "7", "4", "0,83"],
        ["G", "3.4", "Reserva web de espacios", "F", "3", "5", "8", "5", "0,83"],
        ["H", "3.5", "Listado móvil (Flutter → API)", "E", "3", "5", "10", "6", "1,17"],
        ["I", "4.2", "Manual de usuario y README", "C", "1", "2", "4", "2", "0,50"],
        ["J", "4.1", "Pruebas integrales (prueba cruzada)", "G, H", "2", "3", "5", "3", "0,50"],
        ["K", "5.1", "Puesta en producción / release", "J, I", "1", "2", "4", "2", "0,50"],
    ])
    add_para(doc, "Actividades de planificación (1.1, 1.2) se consideran previas/paralelas a A (días 0–2) y no forman parte del camino crítico de desarrollo.", italic=True)

    add_heading(doc, "Red CPM (cálculo forward / backward)", 2)
    add_table(doc, ["Act.", "TE", "IT", "FT", "IL", "FL", "Holgura", "Crítica"], [
        ["A", "2", "0", "2", "0", "2", "0", "Sí"],
        ["B", "3", "2", "5", "2", "5", "0", "Sí"],
        ["C", "2", "2", "4", "3", "5", "1", "No"],
        ["D", "4", "5", "9", "6", "10", "1", "No"],
        ["E", "5", "5", "10", "5", "10", "0", "Sí"],
        ["F", "4", "10", "14", "10", "14", "0", "Sí"],
        ["G", "5", "14", "19", "14", "19", "0", "Sí"],
        ["H", "6", "10", "16", "13", "19", "3", "No"],
        ["I", "2", "4", "6", "20", "22", "16", "No"],
        ["J", "3", "19", "22", "19", "22", "0", "Sí"],
        ["K", "2", "22", "24", "22", "24", "0", "Sí"],
    ])
    add_para(doc, "**Duración del proyecto (ruta crítica):** 24 días hábiles")
    add_para(doc, "**Ruta crítica:** A → B → E → F → G → J → K")
    add_para(doc, "Si alguna actividad crítica se atrasa, se atrasa la entrega del 28 de noviembre.")

    add_heading(doc, "Calendario orientativo (desde 8 oct 2026)", 2)
    add_table(doc, ["Iteración", "Días", "Fechas aprox.", "Actividades"], [
        ["Iteración 0", "0–2", "8–10 oct", "EDT, Planner, Issues (#1)"],
        ["Iteración 1", "0–5", "8–15 oct", "A, B, C — requisitos, BD, mockups"],
        ["Iteración 2", "5–10", "15–22 oct", "E (listado web · demo), inicio D"],
        ["Iteración 3", "10–14", "22–29 oct", "F registro oferente, avance H móvil"],
        ["Iteración 4", "14–19", "29 oct – 6 nov", "G reserva web"],
        ["Iteración 5", "19–22", "6–12 nov", "J pruebas cruzadas"],
        ["Iteración 6", "22–24", "12–17 nov", "K release"],
        ["Buffer", "—", "17–28 nov", "Ajustes, espacio IoT (3.7), defensa"],
    ])

    add_heading(doc, "Diagrama de red (simplificado)", 2)
    add_code(doc, """     ┌──► C (UI web) ──────────────┐
     │                             ▼
A ───┼──► B (BD) ──► E (Listado) ──► F (Registro) ──► G (Reserva) ──► J ──► K
     │              │        ▲                         ▲
     │              │        └── D (Auth) ─────────────┘
     │              └──► H (Móvil listado) ─────────────┘
     └──► I (Manual) ──────────────────────────────────┘""")

    add_heading(doc, "Lectura para Planner", 2)
    add_para(doc, "Las fechas de **inicio** y **vencimiento** de cada tarea en Microsoft Planner salen de **IT** y **FT**.")
    add_para(doc, "Cada lunes se planifican primero las tareas en **ruta crítica** (rojo).")


def build_planner(doc):
    portada(doc, "Planner — Tablero Kanban del equipo")
    add_para(doc, "**Plan:** Parqueos IoT · Pareja Santiago & Bruno")
    add_para(doc, "**Columnas (depósitos):** Backlog · Iteración · En progreso · En revisión (PR) · Hecho")
    add_para(doc, "**Etiquetas:** Ruta crítica · Web · Móvil · Fase EDT · Docs")
    add_para(doc, "Este documento es la fuente de verdad para crear/replicar el tablero en Microsoft Planner (Teams / Microsoft 365) y conectarlo con Issues de GitHub.", italic=True)

    add_heading(doc, "Cómo nombrar cada tarea", 2)
    add_code(doc, "[EDT] #<issue> Título corto")
    add_para(doc, "Ejemplo: [3.2] #3 Listado de parqueos web")
    add_bullet(doc, "**Código EDT** → conecta con el plan y el CPM")
    add_bullet(doc, "**#issue** → conecta con GitHub (rama, commits, PR)")
    add_bullet(doc, "**Checklist** → copia los criterios de aceptación del issue")

    add_heading(doc, "Asignación", 2)
    add_para(doc, "Toda tarea se asigna a **ambos** integrantes.")
    add_para(doc, "El **driver** del código es quien aparece en el nombre de la rama (santiago/... o bruno/...).")

    add_heading(doc, "Tablero actual (demo)", 2)
    add_heading(doc, "Backlog", 3)
    add_table(doc, ["Tarea", "Etiquetas", "IT–FT", "Driver"], [
        ["[3.4] #4 Reserva web de espacios", "Web, Fase 3", "14–19", "Santiago"],
        ["[3.5] #5 Listado móvil vía API", "Móvil, Fase 3", "10–16", "Bruno"],
        ["[3.7] #6 Ocupación IoT (futuro)", "Web, IoT", "buffer", "Ambos"],
    ])
    add_heading(doc, "Iteración (actual · Iteración 2)", 3)
    add_table(doc, ["Tarea", "Etiquetas", "IT–FT", "Driver"], [
        ["[3.2] #3 Listado y registro de parqueos", "Ruta crítica, Web, Fase 3", "5–10", "Santiago"],
        ["[3.1] #7 Autenticación Laravel", "Web, Fase 3", "5–9", "Santiago"],
    ])
    add_heading(doc, "En progreso", 3)
    add_table(doc, ["Tarea", "Issue", "Rama", "Checklist"], [
        ["[3.2] #3 Listado y registro de parqueos", "#3", "santiago/feature/3-listado-parqueos", "Ver HU-01 / HU-02"],
    ])
    add_heading(doc, "En revisión (PR)", 3)
    add_para(doc, "Vacío al inicio del demo — mover aquí al abrir el PR hacia develop.", italic=True)
    add_heading(doc, "Hecho", 3)
    add_table(doc, ["Tarea", "Evidencia"], [
        ["[1.1] #1 Plan EDT y CPM", "docs/EDT.md, docs/PERT-CPM.md"],
        ["[1.2] #1 Tablero Planner documentado", "docs/PLANNER.md"],
        ["[2.1 / 2.2] #2 Requisitos y diseño BD", "docs/historias-usuario.md, docs/arquitectura.md"],
    ])

    add_heading(doc, "Flujo Planner ↔ GitHub", 2)
    add_bullet(doc, "Se crea el **Issue** en GitHub → título con verbo + etiquetas web/movil.")
    add_bullet(doc, "Se crea la tarea en Planner: [EDT] #n Título y se adjunta el enlace del issue.")
    add_bullet(doc, "git switch -c santiago/feature/n-slug → mover a En progreso.")
    add_bullet(doc, "Se abre el Pull Request hacia develop → En revisión (PR).")
    add_bullet(doc, "Merge con Closes #n + aprobación del compañero → Hecho.")
    add_bullet(doc, "Release semanal → revisar vista Gráficos con el docente.")

    add_heading(doc, "Vista semanal (lo crítico primero)", 2)
    add_para(doc, "Cada lunes priorizar en rojo:")
    add_bullet(doc, "A → B → E → F → G → J → K (ruta crítica del CPM)")
    add_bullet(doc, "Luego tareas con holgura (C, D, H, I)")


def build_arquitectura(doc):
    portada(doc, "Arquitectura y base de datos")
    add_para(doc, "**Proyecto:** Gestión de Parqueos con IoT")
    add_para(doc, "**Stack del curso:** Stack A — Laravel (web/API) + Flutter (móvil)")
    add_para(doc, "**Patrón web:** MVC (Model–View–Controller) en Laravel")

    add_heading(doc, "1. Visión de arquitectura", 2)
    add_code(doc, """┌─────────────────┐     HTTPS/JSON      ┌──────────────────────────┐
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
                                        └──────────────────────────┘""")
    add_para(doc, "Reglas del curso:")
    add_bullet(doc, "Un solo stack por pareja.")
    add_bullet(doc, "La app móvil **nunca** se conecta directo a la BD; solo consume la API de web/.")
    add_bullet(doc, "Carpetas por producto (web/, movil/), no por capa.")

    add_heading(doc, "2. Tipo de base de datos: SQL (relacional)", 2)
    add_para(doc, "Se elige **SQL relacional** (no NoSQL ni híbrida en esta etapa) porque:")
    add_table(doc, ["Motivo", "Detalle"], [
        ["Datos estructurados", "Usuarios, parqueos, cupos, reservas y roles tienen relaciones claras"],
        ["Integridad", "Foreign keys evitan reservas huérfanas o parqueos sin dueño"],
        ["Stack del curso", "Laravel + migraciones + PostgreSQL/MySQL"],
        ["Consultas", "Filtros por zona, tipo (patio/mall/centro), precio y disponibilidad"],
    ])
    add_heading(doc, "¿Y el IoT?", 3)
    add_para(doc, "Los sensores de ocupación generan telemetría de alta frecuencia. En una versión futura se puede adoptar un enfoque **híbrido**:")
    add_bullet(doc, "**SQL:** catálogo, usuarios, reservas, pagos.")
    add_bullet(doc, "**Time-series / NoSQL (opcional):** lecturas de sensores, histórico de ocupación.")
    add_para(doc, "Para el demo actual no se implementa IoT físico; el campo cupos_disponibles simula la ocupación.")

    add_heading(doc, "3. Modelo de datos (demo)", 2)
    add_heading(doc, "Tabla users", 3)
    add_table(doc, ["Campo", "Tipo", "Notas"], [
        ["id", "bigint PK", ""],
        ["name", "string", ""],
        ["email", "string unique", ""],
        ["password", "string", "hashed"],
        ["role", "enum", "admin, oferente, conductor"],
        ["timestamps", "", ""],
    ])
    add_heading(doc, "Tabla parqueos", 3)
    add_table(doc, ["Campo", "Tipo", "Notas"], [
        ["id", "bigint PK", ""],
        ["user_id", "FK → users", "Dueño / oferente"],
        ["nombre", "string", 'Ej. "Patio Av. Banzer"'],
        ["tipo", "enum", "patio, centro, mall, otro"],
        ["direccion", "string", ""],
        ["zona", "string", "Ej. Equipetrol, Centro"],
        ["latitud / longitud", "decimal nullable", "Para mapa futuro"],
        ["cupos_totales", "int", ""],
        ["cupos_disponibles", "int", "Simula IoT / estado"],
        ["precio_hora", "decimal", "BOB"],
        ["descripcion", "text nullable", ""],
        ["activo", "boolean", ""],
        ["timestamps", "", ""],
    ])
    add_heading(doc, "Relaciones", 3)
    add_bullet(doc, "Un usuario (oferente) tiene muchos parqueos.")
    add_bullet(doc, "Un parqueo pertenece a un usuario.")
    add_bullet(doc, "Futuro: reservas (parqueo_id, user_id, inicio, fin, estado).")

    add_heading(doc, "4. Capas MVC en web/", 2)
    add_table(doc, ["Capa", "Responsabilidad", "Ejemplo"], [
        ["Model", "Persistencia Eloquent", "App\\Models\\Parqueo"],
        ["View", "Blade (UI panel)", "resources/views/parqueos/*"],
        ["Controller", "Orquestación HTTP", "ParqueoController"],
        ["Routes", "Entrada web", "routes/web.php"],
        ["Migrations / Seeders", "Esquema y datos demo", "database/"],
    ])

    add_heading(doc, "5. Seguridad básica", 2)
    add_bullet(doc, "Contraseñas hasheadas (bcrypt).")
    add_bullet(doc, "Middleware auth para crear/editar parqueos.")
    add_bullet(doc, "Validación de formularios en Controller.")
    add_bullet(doc, ".env fuera de Git (secretos y credenciales DB).")

    add_heading(doc, "6. Despliegue local (XAMPP)", 2)
    add_bullet(doc, "Crear BD parqueos_demo en phpMyAdmin / MySQL.")
    add_bullet(doc, "Configurar web/.env (DB_DATABASE, DB_USERNAME, DB_PASSWORD).")
    add_bullet(doc, "php artisan migrate --seed")
    add_bullet(doc, "php artisan serve")


def build_historias(doc):
    portada(doc, "Casos de uso e historias de usuario (Web · Demo)")
    add_heading(doc, "Roles", 2)
    add_table(doc, ["Rol", "Descripción"], [
        ["Conductor", "Busca parqueos disponibles en Santa Cruz"],
        ["Oferente", "Publica un parqueo (patio, lote, mall)"],
        ["Administrador", "Supervisa el catálogo"],
    ])

    add_heading(doc, "Caso de uso CU-01 — Consultar parqueos disponibles", 2)
    add_bullet(doc, "**Actor:** Conductor")
    add_bullet(doc, "**Canal:** Web")
    add_bullet(doc, "**Precondición:** ninguna (listado público)")
    add_para(doc, "**Flujo básico:**")
    add_bullet(doc, "Entra al panel web.")
    add_bullet(doc, "Ve el listado de parqueos activos.")
    add_bullet(doc, "Filtra por zona o tipo (opcional).")
    add_bullet(doc, "Abre el detalle (cupos, precio, dirección).")
    add_bullet(doc, "**Postcondición:** el conductor conoce opciones de parqueo.")

    add_heading(doc, "Caso de uso CU-02 — Registrar un parqueo", 2)
    add_bullet(doc, "**Actor:** Oferente / Admin")
    add_bullet(doc, "**Canal:** Web")
    add_bullet(doc, "**Precondición:** sesión iniciada")
    add_para(doc, "**Flujo básico:**")
    add_bullet(doc, "Inicia sesión.")
    add_bullet(doc, "Elige «Nuevo parqueo».")
    add_bullet(doc, "Completa nombre, tipo, zona, cupos, precio.")
    add_bullet(doc, "Guarda.")
    add_bullet(doc, "**Alterno:** datos inválidos → se muestran errores de validación.")
    add_bullet(doc, "**Postcondición:** el parqueo queda publicado en el catálogo.")

    add_heading(doc, "Historias de usuario (INVEST)", 2)
    add_heading(doc, "HU-01 · Web · Prioridad alta · EDT 3.2 · Issue #3", 3)
    add_para(doc, "Como conductor quiero ver un listado de parqueos disponibles para decidir dónde estacionar en Santa Cruz.", italic=True)
    add_para(doc, "**Criterios de aceptación**")
    add_bullet(doc, "Dado que hay parqueos activos, cuando abro el listado, entonces veo nombre, zona, tipo, cupos y precio.")
    add_bullet(doc, "Dado un filtro por tipo, cuando lo aplico, entonces solo veo parqueos de ese tipo.")
    add_bullet(doc, "Dado un parqueo, cuando abro su detalle, entonces veo dirección y descripción.")
    add_para(doc, "**Rama:** santiago/feature/3-listado-parqueos")

    add_heading(doc, "HU-02 · Web · Prioridad alta · EDT 3.3 · Issue #3", 3)
    add_para(doc, "Como oferente quiero registrar mi parqueo (patio/mall/centro) para ofrecer cupos a conductores.", italic=True)
    add_para(doc, "**Criterios de aceptación**")
    add_bullet(doc, "Dado que inicié sesión, cuando completo el formulario válido, entonces el parqueo aparece en el listado.")
    add_bullet(doc, "Dado un campo obligatorio vacío, cuando envío, entonces veo un mensaje de error.")
    add_bullet(doc, "Dado cupos_disponibles > cupos_totales, cuando envío, entonces la validación lo rechaza.")
    add_para(doc, "**Rama:** santiago/feature/3-listado-parqueos")

    add_heading(doc, "Definición de «Listo» (DoD)", 2)
    add_para(doc, "No se programa una historia sin:")
    add_bullet(doc, "Caso de uso / HU con criterios de aceptación")
    add_bullet(doc, "Estimación PERT y fechas en Planner")
    add_bullet(doc, "Rama nombrada con issue + nombre del driver")
    add_bullet(doc, "PR hacia develop con evidencia de prueba")
    add_bullet(doc, "Aprobación del compañero (prueba cruzada)")


def build_flujo(doc):
    portada(doc, "Flujo Git / GitHub del equipo")
    add_para(doc, "Basado en las diapositivas Git y GitHub — Trabajo colaborativo en parejas con XP.", italic=True)

    add_heading(doc, "Ramas protegidas", 2)
    add_table(doc, ["Rama", "Uso"], [
        ["main", "Producción. Nadie programa aquí. Solo PR desde develop o hotfix."],
        ["develop", "Integración de la iteración. Se llega solo por Pull Request."],
    ])

    add_heading(doc, "Convención de ramas (con nombre del driver)", 2)
    add_code(doc, """santiago/docs/<n>-<slug>          # documentación de Santiago
santiago/feature/<n>-<slug>       # historias web de Santiago
bruno/feature/<n>-<slug>          # historias móvil de Bruno
fix/<n>-<slug>                   # bugs
hotfix/<n>-<slug>                 # urgencias desde main""")
    add_para(doc, "Ejemplos reales de este demo:")
    add_bullet(doc, "santiago/docs/1-planificacion")
    add_bullet(doc, "santiago/feature/3-listado-parqueos")

    add_heading(doc, "Commits", 2)
    add_code(doc, """docs: EDT PERT Planner (#1)
feat(web): listado y registro de parqueos (#3)""")

    add_heading(doc, "Issues de referencia (crear en GitHub)", 2)
    add_heading(doc, "Issue #1 — Documentar planificación EDT / PERT / Planner", 3)
    add_bullet(doc, "Labels: docs")
    add_bullet(doc, "Rama: santiago/docs/1-planificacion")
    add_heading(doc, "Issue #2 — Diseñar BD y requisitos web", 3)
    add_bullet(doc, "Labels: docs, web")
    add_bullet(doc, "Rama: santiago/docs/2-diseno")
    add_heading(doc, "Issue #3 — Implementar listado y registro de parqueos web", 3)
    add_bullet(doc, "Labels: web, feat")
    add_bullet(doc, "Rama: santiago/feature/3-listado-parqueos")
    add_bullet(doc, "Closes en el PR: Closes #3")

    add_heading(doc, "Ciclo diario", 2)
    add_code(doc, """git switch develop
git pull origin develop
git switch -c santiago/feature/3-listado-parqueos
# ... código ...
git add .
git commit -m "feat(web): listado de parqueos (#3)"
git push -u origin santiago/feature/3-listado-parqueos
# Abrir PR → develop · Bruno prueba y aprueba · Squash and merge""")

    add_heading(doc, "Prueba cruzada", 2)
    add_bullet(doc, "Bruno prueba los PR de web/ y aprueba el merge.")
    add_bullet(doc, "Santiago prueba los PR de movil/ y aprueba el merge.")
    add_bullet(doc, "Nadie fusiona su propio código sin la prueba del compañero.")


def main():
    builders = [
        ("01_EDT.docx", build_edt),
        ("02_PERT_CPM.docx", build_pert),
        ("03_PLANNER.docx", build_planner),
        ("04_Arquitectura_y_BD.docx", build_arquitectura),
        ("05_Historias_de_Usuario.docx", build_historias),
        ("06_Flujo_GitHub.docx", build_flujo),
    ]

    # Individuales
    for filename, builder in builders:
        doc = new_doc()
        builder(doc)
        path = OUT_DIR / filename
        doc.save(path)
        print("OK", path)

    # Documento único con todo
    full = new_doc()
    portada(full, "Documentación completa del proyecto")
    add_para(full, "Este archivo reúne EDT, PERT/CPM, Planner, Arquitectura, Historias de usuario y Flujo Git/GitHub.", center=True)
    full.add_page_break()

    sections = [
        build_edt,
        build_pert,
        build_planner,
        build_arquitectura,
        build_historias,
        build_flujo,
    ]
    for i, builder in enumerate(sections):
        # evitar portadas duplicadas en el combinado: construir en docs temporales
        temp = new_doc()
        builder(temp)
        # copiar body elements (excepto sectPr final)
        for element in temp.element.body:
            if element.tag.endswith("sectPr"):
                continue
            full.element.body.append(element)
        if i < len(sections) - 1:
            full.add_page_break()

    combined = OUT_DIR / "00_Documentacion_Completa_Parqueos_IoT.docx"
    full.save(combined)
    print("OK", combined)


if __name__ == "__main__":
    main()
