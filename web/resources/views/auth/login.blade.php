@extends('layouts.app')

@section('title', 'Iniciar sesión')

@section('content')
    <h1>Iniciar sesión</h1>
    <p class="muted">Usa las cuentas demo del seeder para probar el registro de parqueos.</p>

    <form class="card form-card" method="POST" action="{{ route('login') }}">
        @csrf
        <label for="email">Correo</label>
        <input id="email" type="email" name="email" value="{{ old('email', 'oferente@parqueos.test') }}" required>

        <label for="password">Contraseña</label>
        <input id="password" type="password" name="password" value="password" required>

        <label style="display:flex; align-items:center; gap:0.4rem; font-weight:500;">
            <input type="checkbox" name="remember" value="1" style="width:auto; margin:0;"> Recordarme
        </label>

        <button class="btn" type="submit">Entrar</button>
    </form>

    <div class="card form-card" style="margin-top:1rem;">
        <p class="meta"><strong>Cuentas demo</strong></p>
        <p class="meta muted">admin@parqueos.test / password</p>
        <p class="meta muted">oferente@parqueos.test / password</p>
        <p class="meta muted">conductor@parqueos.test / password</p>
    </div>
@endsection
