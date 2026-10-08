@extends('layouts.app')

@section('title', $parqueo->nombre)

@section('content')
    <a class="btn btn-secondary" href="{{ route('parqueos.index') }}">← Volver al listado</a>
    <div class="card form-card" style="margin-top:1rem;">
        <span class="badge">{{ $parqueo->tipo }}</span>
        <h1 style="margin-top:0.75rem;">{{ $parqueo->nombre }}</h1>
        <p class="meta"><strong>Zona:</strong> {{ $parqueo->zona }}</p>
        <p class="meta"><strong>Dirección:</strong> {{ $parqueo->direccion }}</p>
        <p class="meta"><strong>Cupos:</strong> {{ $parqueo->cupos_disponibles }} libres de {{ $parqueo->cupos_totales }}</p>
        <p class="meta"><strong>Precio:</strong> Bs {{ number_format($parqueo->precio_hora, 2) }} / hora</p>
        <p class="meta"><strong>Publicado por:</strong> {{ $parqueo->user->name ?? 'N/D' }}</p>
        @if($parqueo->descripcion)
            <p class="meta">{{ $parqueo->descripcion }}</p>
        @endif
    </div>
@endsection
