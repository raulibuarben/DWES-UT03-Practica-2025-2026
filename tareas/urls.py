from django.urls import path

from tareas.views import CrearTareaGrupalView, CrearTareaIndividualView, RegistroUsuarioView, detalle_tarea

urlpatterns = [
    path('<uuid:pk>/', detalle_tarea.as_view(), name = 'detalle_tarea'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('crear_tarea_individual/', CrearTareaIndividualView.as_view(), name='crear_tarea_individual'),
    path('crear_tarea_grupal/', CrearTareaGrupalView.as_view(), name='crear_tarea_grupal'),
]

