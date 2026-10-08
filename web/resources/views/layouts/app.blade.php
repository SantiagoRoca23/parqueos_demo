<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>@yield('title', 'Parqueos SCZ') — Demo IoT</title>
    <style>
        :root {
            --bg: #f4f6f8;
            --card: #ffffff;
            --ink: #1f2933;
            --muted: #52606d;
            --line: #d9e2ec;
            --brand: #0b6e4f;
            --brand-dark: #084c37;
            --accent: #f0b429;
            --danger: #ba1b1b;
        }
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: "Segoe UI", Tahoma, sans-serif;
            background:
                radial-gradient(circle at top right, rgba(11, 110, 79, 0.08), transparent 40%),
                linear-gradient(180deg, #eef2f5 0%, var(--bg) 100%);
            color: var(--ink);
            min-height: 100vh;
        }
        header {
            background: var(--brand);
            color: #fff;
            padding: 1rem 1.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        header a { color: #fff; text-decoration: none; font-weight: 600; }
        nav { display: flex; gap: 0.85rem; align-items: center; flex-wrap: wrap; }
        nav a, nav span { font-size: 0.95rem; opacity: 0.95; }
        main { max-width: 1100px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
        h1, h2 { margin: 0 0 0.75rem; }
        .muted { color: var(--muted); }
        .flash {
            background: #e3f9e5;
            border: 1px solid #b8e0b8;
            color: #0b6e4f;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .errors {
            background: #ffe3e3;
            border: 1px solid #f5c1c1;
            color: var(--danger);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .toolbar {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin: 1rem 0 1.25rem;
            align-items: end;
        }
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 1rem;
        }
        .card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
        }
        .badge {
            display: inline-block;
            padding: 0.15rem 0.55rem;
            border-radius: 999px;
            background: #e0fcf4;
            color: var(--brand-dark);
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
        }
        .btn {
            display: inline-block;
            background: var(--brand);
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            text-decoration: none;
            cursor: pointer;
            font-weight: 600;
        }
        .btn:hover { background: var(--brand-dark); }
        .btn-secondary {
            background: #fff;
            color: var(--brand-dark);
            border: 1px solid var(--line);
        }
        label { display: block; font-size: 0.9rem; margin-bottom: 0.25rem; font-weight: 600; }
        input, select, textarea {
            width: 100%;
            padding: 0.6rem 0.7rem;
            border: 1px solid var(--line);
            border-radius: 8px;
            margin-bottom: 0.85rem;
            font: inherit;
            background: #fff;
        }
        .form-card { max-width: 640px; }
        .meta { font-size: 0.92rem; line-height: 1.45; }
        footer {
            text-align: center;
            color: var(--muted);
            font-size: 0.85rem;
            padding: 1rem;
        }
    </style>
</head>
<body>
<header>
    <a href="{{ route('parqueos.index') }}">Parqueos SCZ · Demo IoT</a>
    <nav>
        <a href="{{ route('parqueos.index') }}">Listado</a>
        @auth
            @if(auth()->user()->esOferente())
                <a href="{{ route('parqueos.create') }}">Nuevo parqueo</a>
            @endif
            <span>{{ auth()->user()->name }} ({{ auth()->user()->role }})</span>
            <form action="{{ route('logout') }}" method="POST" style="display:inline;">
                @csrf
                <button class="btn btn-secondary" type="submit">Salir</button>
            </form>
        @else
            <a href="{{ route('login') }}">Iniciar sesión</a>
        @endauth
    </nav>
</header>
<main>
    @if(session('success'))
        <div class="flash">{{ session('success') }}</div>
    @endif
    @if($errors->any())
        <div class="errors">
            <ul style="margin:0; padding-left:1.1rem;">
                @foreach($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif
    @yield('content')
</main>
<footer>
    Proyecto de Sistemas III · Santiago Roca Martínez (web) · Demo académica
</footer>
</body>
</html>
