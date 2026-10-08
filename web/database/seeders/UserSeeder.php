<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    public function run(): void
    {
        User::query()->updateOrCreate(
            ['email' => 'admin@parqueos.test'],
            [
                'name' => 'Admin Demo',
                'password' => Hash::make('password'),
                'role' => 'admin',
            ]
        );

        User::query()->updateOrCreate(
            ['email' => 'oferente@parqueos.test'],
            [
                'name' => 'Oferente Demo',
                'password' => Hash::make('password'),
                'role' => 'oferente',
            ]
        );

        User::query()->updateOrCreate(
            ['email' => 'conductor@parqueos.test'],
            [
                'name' => 'Conductor Demo',
                'password' => Hash::make('password'),
                'role' => 'conductor',
            ]
        );
    }
}
