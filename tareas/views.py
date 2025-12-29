from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Tarea, TareaGrupal, TareaIndividual
from django.views.generic.edit import CreateView
from .forms import RegistroUsuarioForm, TareaGrupalForm, TareaIndividualForm
from django.urls import reverse_lazy

# Create your views here.
#Detalle tarea.
class detalle_tarea(DetailView):
    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'


#Vista para el formulario de registro de usuarios

class RegistroUsuarioView(CreateView):
    template_name = 'tareas/registro_usuario.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')

#Vista para crear una tarea individual
class CrearTareaIndividualView(CreateView):
    model = TareaIndividual
    form_class = TareaIndividualForm
    template_name = 'tareas/crear_tarea_individual.html'
    success_url = reverse_lazy('lista_tareas')

#Vista para crear una tarea grupal
class CrearTareaGrupalView(CreateView):
    model = TareaGrupal
    form_class = TareaGrupalForm
    template_name = 'tareas/crear_tarea_grupal.html'
    success_url = reverse_lazy('lista_tareas')