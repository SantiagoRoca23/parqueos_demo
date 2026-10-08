@extends('layouts.app')

@section('title', 'Registrar parqueo')

@section('content')
    <h1>Registrar parqueo</h1>
    <p class="muted">HU-02 · EDT 3.3 · Issue #3 — publica un patio, lote o mall.</p>

    <form class="card form-card" method="POST" action="{{ route('parqueos.store') }}">
        @csrf
        <label for="nombre">Nombre</label>
        <input id="nombre" name="nombre" value="{{ old('nombre') }}" required>

        <label for="tipo">Tipo</label>
        <select id="tipo" name="tipo" required>
            @foreach(['patio','centro','mall','otro'] as $tipo)
                <option value="{{ $tipo }}" @selected(old('tipo') === $tipo)>{{ ucfirst($tipo) }}</option>
            @endforeach
        </select>

        <label for="direccion">Dirección</label>
        <input id="direccion" name="direccion" value="{{ old('direccion') }}" required>

        <label for="zona">Zona</label>
        <input id="zona" name="zona" value="{{ old('zona') }}" required>

        <label for="cupos_totales">Cupos totales</label>
        <input id="cupos_totales" type="number" min="1" name="cupos_totales" value="{{ old('cupos_totales', 1) }}" required>

        <label for="cupos_disponibles">Cupos disponibles</label>
        <input id="cupos_disponibles" type="number" min="0" name="cupos_disponibles" value="{{ old('cupos_disponibles', 1) }}" required>

        <label for="precio_hora">Precio por hora (Bs)</label>
        <input id="precio_hora" type="number" step="0.01" min="0" name="precio_hora" value="{{ old('precio_hora', 5) }}" required>

        <label for="descripcion">Descripción</label>
        <textarea id="descripcion" name="descripcion" rows="3">{{ old('descripcion') }}</textarea>

        <button class="btn" type="submit">Guardar parqueo</button>
    </form>
@endsection
