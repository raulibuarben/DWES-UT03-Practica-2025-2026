import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

# Create your models here.
# Modelo base para Tarea
class Tarea(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('validada', 'Validada')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Identificador único")
    titulo = models.CharField(max_length=150, help_text="Nombre o tíutlo de la tarea")
    descripcion = models.TextField(help_text="Descripción detallada")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación")
    fecha_recordatorio = models.DateTimeField(help_text="Fecha recordatorio")

    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas_creadas')
    estado = models.CharField(max_length=15, choices=ESTADOS, default='pendiente')

    requiere_validacion = models.BooleanField(default=False, help_text='¿Es evaluable la tarea?')
    profesor = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE, related_name='tareas_evaluables')

    def __str__(self):
        return self.titulo
    
#Modelo para las tarea individual con herencia de Tarea
class TareaIndividual(Tarea):
    alumno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tareas_individuales')

    
#Modelo para las tareas grupales con herencia de Tarea
class TareaGrupal(Tarea):
    alumnos = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tareas_grupales')


#Modelo para los usuarios (Profesor/Alumno)
class Usuario(AbstractUser):
    alumno = 'AL'
    profesor = 'PR'

    ROLES = [
        (alumno, 'Alumno'),
        (profesor, 'Profesor'),
    ]

    rol = models.CharField(max_length=8, choices=ROLES, default=alumno)

    def is_alumno(self):
        return self.rol == self.alumno

    def is_profesor(self):
        return self.rol == self.profesor 