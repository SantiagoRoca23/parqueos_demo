<?php

namespace Database\Seeders;

use App\Models\Parqueo;
use App\Models\User;
use Illuminate\Database\Seeder;

class ParqueoSeeder extends Seeder
{
    public function run(): void
    {
        $oferente = User::query()->where('email', 'oferente@parqueos.test')->first();
        $admin = User::query()->where('email', 'admin@parqueos.test')->first();

        if (! $oferente || ! $admin) {
            return;
        }

        $datos = [
            [
                'user_id' => $oferente->id,
                'nombre' => 'Patio Av. Banzer',
                'tipo' => 'patio',
                'direccion' => 'Av. Banzer 3er anillo',
                'zona' => 'Equipetrol',
                'cupos_totales' => 6,
                'cupos_disponibles' => 2,
                'precio_hora' => 5.00,
                'descripcion' => 'Parqueo en patio residencial con vigilancia informal.',
            ],
            [
                'user_id' => $admin->id,
                'nombre' => 'Ventura Mall',
                'tipo' => 'mall',
                'direccion' => 'Av. San Martín',
                'zona' => 'Equipetrol',
                'cupos_totales' => 400,
                'cupos_disponibles' => 85,
                'precio_hora' => 8.00,
                'descripcion' => 'Estacionamiento de centro comercial.',
            ],
            [
                'user_id' => $admin->id,
                'nombre' => 'Cine Center',
                'tipo' => 'mall',
                'direccion' => 'Av. Monseñor Rivero',
                'zona' => 'Centro',
                'cupos_totales' => 220,
                'cupos_disponibles' => 40,
                'precio_hora' => 7.50,
                'descripcion' => 'Parqueo cubierto cercano a cines y locales.',
            ],
            [
                'user_id' => $oferente->id,
                'nombre' => 'Parqueo Calle Bolívar',
                'tipo' => 'centro',
                'direccion' => 'Calle Bolívar esq. España',
                'zona' => 'Centro',
                'cupos_totales' => 30,
                'cupos_disponibles' => 8,
                'precio_hora' => 6.00,
                'descripcion' => 'Lote del centro urbano, ideal para trámites.',
            ],
        ];

        foreach ($datos as $item) {
            Parqueo::query()->updateOrCreate(
                [
                    'nombre' => $item['nombre'],
                    'direccion' => $item['direccion'],
                ],
                $item + ['activo' => true]
            );
        }
    }
}
