from django import forms
from .models import Jugador, Categoria 
from django.core.exceptions import ValidationError

class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre de la Categoría")
    anio_nacimiento_desde = forms.IntegerField(label="Año desde")
    anio_nacimiento_hasta = forms.IntegerField(label="Año hasta")
    profesor = forms.CharField(max_length=100, label="Profesor a cargo")
    dias_horarios = forms.CharField(max_length=150, label="Días y Horarios")

class JugadorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.IntegerField(label="DNI del Jugador")
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )
    responsable = forms.CharField(max_length=100, label="Nombre del Padre/Madre")
    dni_responsable = forms.IntegerField(label="DNI del Responsable")
    contacto_responsable = forms.CharField(max_length=100, label="Teléfono de contacto")


class SolicitudForm(forms.Form):
    jugador = forms.ModelChoiceField(queryset=Jugador.objects.all(), label="Seleccionar Jugador")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Seleccionar Categoría")

    def clean(self):
        cleaned_data = super().clean()
        jugador = cleaned_data.get("jugador")
        categoria = cleaned_data.get("categoria")

        if jugador and categoria:
            anio_nacimiento = jugador.fecha_nacimiento.year
            
            # Verificación lógica
            if not (categoria.anio_nacimiento_desde <= anio_nacimiento <= categoria.anio_nacimiento_hasta):
                raise ValidationError(
                    f"Error: El jugador nació en {anio_nacimiento}, pero esta categoría solo acepta nacidos entre {categoria.anio_nacimiento_desde} y {categoria.anio_nacimiento_hasta}."
                )