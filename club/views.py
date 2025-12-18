from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriaForm, JugadorForm, SolicitudForm
from .models import Categoria, Jugador, SolicitudInscripcion

def home(request):
    categorias = Categoria.objects.all()
    return render(request, "club/index.html", {"categorias": categorias})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            categoria = Categoria(
                nombre=info['nombre'], 
                anio_nacimiento_desde=info['anio_nacimiento_desde'],
                anio_nacimiento_hasta=info['anio_nacimiento_hasta'],
                profesor=info['profesor'],
                dias_horarios=info['dias_horarios']
            )
            categoria.save()
            return redirect("inicio")
    else:
        form = CategoriaForm()
    
    return render(request, "club/categoria_form.html", {"form": form})

def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jugador = Jugador(
                nombre=info['nombre'],
                apellido=info['apellido'],
                dni=info['dni'],
                fecha_nacimiento=info['fecha_nacimiento'],
                responsable=info['responsable'],
                dni_responsable=info['dni_responsable'],
                contacto_responsable=info['contacto_responsable']
            )
            jugador.save()
            return redirect("inicio")
    else:
        form = JugadorForm()
    return render(request, "club/jugador_form.html", {"form": form})

def crear_solicitud(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            solicitud = SolicitudInscripcion(
                jugador=info['jugador'],
                categoria=info['categoria']
            )
            solicitud.save()
            return redirect("inicio")
    else:
        form = SolicitudForm()
    return render(request, "club/solicitud_form.html", {"form": form})

def buscar_jugador(request):
    jugadores = Jugador.objects.all()
    inscripciones = SolicitudInscripcion.objects.all()
    ids_inscriptos = inscripciones.values_list('jugador_id', flat=True)

    return render(request, "club/buscar_jugador.html", {
        "jugadores": jugadores, 
        "ids_inscriptos": ids_inscriptos,
        "inscripciones": inscripciones
    })

def resultado_busqueda(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        jugadores = Jugador.objects.filter(apellido__icontains=apellido)
        
        return render(request, "club/resultado_busqueda.html", {"jugadores": jugadores, "termino": apellido})
    else:
        return redirect("buscar_jugador")

def eliminar_inscripcion(request, inscripcion_id):
    
    inscripcion = get_object_or_404(SolicitudInscripcion, id=inscripcion_id)
    
    if request.method == "POST":
        inscripcion.delete()
        return redirect("buscar_jugador") 
    
    return redirect("buscar_jugador")