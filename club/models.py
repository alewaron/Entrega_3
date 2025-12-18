from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    anio_nacimiento_desde = models.IntegerField()
    anio_nacimiento_hasta = models.IntegerField()
    profesor = models.CharField(max_length=100)
    dias_horarios = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} ({self.profesor}) (Desde: {self.anio_nacimiento_desde} Hasta: {self.anio_nacimiento_hasta})"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    responsable = models.CharField(max_length=100)
    dni_responsable = models.IntegerField()
    contacto_responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class SolicitudInscripcion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud: {self.jugador.apellido} - {self.categoria.nombre}"