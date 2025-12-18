from django.contrib import admin
from .models import Categoria, Jugador, SolicitudInscripcion

admin.site.register(Categoria)
admin.site.register(Jugador)
admin.site.register(SolicitudInscripcion)