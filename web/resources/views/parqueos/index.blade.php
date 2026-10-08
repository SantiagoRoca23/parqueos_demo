@extends('layouts.app')

@section('title', 'Listado de parqueos')

@section('content')
    <h1>Parqueos en Santa Cruz</h1>
    <p class="muted">Consulta patios, parqueos del centro y estacionamientos de malls. Issue #3 · EDT 3.2</p>

    <form class="toolbar" method="GET" action="{{ route('parqueos.index') }}">
        <div>
            <label for="tipo">Tipo</label>
            <select name="tipo" id="tipo">
                <option value="">Todos</option>
                @foreach(['patio','centro','mall','otro'] as $tipo)
                    <option value="{{ $tipo }}" @selected(request('tipo') === $tipo)>{{ ucfirst($tipo) }}</option>
                @endforeach
            </select>
        </div>
        <div>
            <label for="zona">Zona</label>
            <input type="text" name="zona" id="zona" value="{{ request('zona') }}" placeholder="Ej. Centro, Equipetrol">
        </div>
        <button class="btn" type="submit">Filtrar</button>
        <a class="btn btn-secondary" href="{{ route('parqueos.index') }}">Limpiar</a>
    </form>

    <div class="card-grid">
        @forelse($parqueos as $parqueo)
            <article class="card">
                <span class="badge">{{ $parqueo->tipo }}</span>
                <h2 style="margin-top:0.6rem; font-size:1.15rem;">{{ $parqueo->nombre }}</h2>
                <p class="meta muted">{{ $parqueo->zona }} · {{ $parqueo->direccion }}</p>
                <p class="meta">
                    <strong>{{ $parqueo->cupos_disponibles }}</strong> / {{ $parqueo->cupos_totales }} cupos libres<br>
                    Bs {{ number_format($parqueo->precio_hora, 2) }} / hora
                </p>
                <a class="btn btn-secondary" href="{{ route('parqueos.show', $parqueo) }}">Ver detalle</a>
            </article>
        @empty
            <p class="muted">No hay parqueos con esos filtros.</p>
        @endforelse
    </div>

    <div style="margin-top:1.25rem;">
        {{ $parqueos->links() }}
    </div>
@endsection
