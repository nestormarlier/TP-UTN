from django.shortcuts import render

# Create your views here.


def parteDiario(request):
    data = {
        'nombre_pagina': 'Mi primer pagina'
    }
    return render(request, 'inicio.html', data)
