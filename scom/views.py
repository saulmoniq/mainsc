from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def manejoCamaras(request):
    return render(request, 'manejo-camaras.html')

def manejoTiempos(request):
    return render(request, 'manejo-de-tiempos.html')