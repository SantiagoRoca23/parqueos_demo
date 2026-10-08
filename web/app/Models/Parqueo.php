<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Parqueo extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'nombre',
        'tipo',
        'direccion',
        'zona',
        'latitud',
        'longitud',
        'cupos_totales',
        'cupos_disponibles',
        'precio_hora',
        'descripcion',
        'activo',
    ];

    protected function casts(): array
    {
        return [
            'activo' => 'boolean',
            'precio_hora' => 'decimal:2',
            'latitud' => 'decimal:7',
            'longitud' => 'decimal:7',
        ];
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function scopeActivos($query)
    {
        return $query->where('activo', true);
    }
}
