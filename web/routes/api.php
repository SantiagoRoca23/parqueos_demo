<?php

use App\Models\Parqueo;
use Illuminate\Support\Facades\Route;

Route::get('/parqueos', function () {
    return Parqueo::query()
        ->activos()
        ->latest()
        ->get([
            'id',
            'nombre',
            'tipo',
            'direccion',
            'zona',
            'cupos_totales',
            'cupos_disponibles',
            'precio_hora',
            'descripcion',
        ]);
});
