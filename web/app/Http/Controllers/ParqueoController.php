<?php

namespace App\Http\Controllers;

use App\Models\Parqueo;
use Illuminate\Contracts\View\View as ViewContract;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class ParqueoController extends Controller
{
    public function index(Request $request): View
    {
        $query = Parqueo::with('user')->activos()->latest();

        if ($request->filled('tipo')) {
            $query->where('tipo', $request->string('tipo'));
        }

        if ($request->filled('zona')) {
            $query->where('zona', 'like', '%'.$request->string('zona').'%');
        }

        $parqueos = $query->paginate(9)->withQueryString();

        return view('parqueos.index', compact('parqueos'));
    }

    public function show(Parqueo $parqueo): View
    {
        $parqueo->load('user');

        return view('parqueos.show', compact('parqueo'));
    }

    public function create(Request $request): ViewContract|RedirectResponse
    {
        if (! $request->user()->esOferente()) {
            return redirect()
                ->route('parqueos.index')
                ->withErrors(['auth' => 'Solo oferentes o administradores pueden registrar parqueos.']);
        }

        return view('parqueos.create');
    }

    public function store(Request $request): RedirectResponse
    {
        if (! $request->user()->esOferente()) {
            return redirect()
                ->route('parqueos.index')
                ->withErrors(['auth' => 'Solo oferentes o administradores pueden registrar parqueos.']);
        }

        $data = $request->validate([
            'nombre' => ['required', 'string', 'max:120'],
            'tipo' => ['required', 'in:patio,centro,mall,otro'],
            'direccion' => ['required', 'string', 'max:255'],
            'zona' => ['required', 'string', 'max:100'],
            'cupos_totales' => ['required', 'integer', 'min:1', 'max:5000'],
            'cupos_disponibles' => ['required', 'integer', 'min:0'],
            'precio_hora' => ['required', 'numeric', 'min:0'],
            'descripcion' => ['nullable', 'string', 'max:1000'],
        ]);

        if ($data['cupos_disponibles'] > $data['cupos_totales']) {
            return back()
                ->withErrors(['cupos_disponibles' => 'Los cupos disponibles no pueden superar los cupos totales.'])
                ->withInput();
        }

        $data['user_id'] = $request->user()->id;
        $data['activo'] = true;

        Parqueo::create($data);

        return redirect()
            ->route('parqueos.index')
            ->with('success', 'Parqueo registrado correctamente.');
    }
}
