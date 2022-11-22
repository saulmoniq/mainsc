from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manejo-de-camaras', views.manejoCamaras, name="manejoCamaras"),
    path('manejo-de-tiempos', views.manejoTiempos, name="manejoTiempos"),
]