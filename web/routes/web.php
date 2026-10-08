<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\ParqueoController;
use Illuminate\Support\Facades\Route;

Route::get('/', fn () => redirect()->route('parqueos.index'));

Route::get('/parqueos', [ParqueoController::class, 'index'])->name('parqueos.index');
Route::get('/parqueos/{parqueo}', [ParqueoController::class, 'show'])->name('parqueos.show');

Route::middleware('guest')->group(function () {
    Route::get('/login', [AuthController::class, 'showLogin'])->name('login');
    Route::post('/login', [AuthController::class, 'login']);
});

Route::post('/logout', [AuthController::class, 'logout'])->middleware('auth')->name('logout');

Route::middleware('auth')->group(function () {
    Route::get('/parqueos-crear/nuevo', [ParqueoController::class, 'create'])->name('parqueos.create');
    Route::post('/parqueos', [ParqueoController::class, 'store'])->name('parqueos.store');
});
