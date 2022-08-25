from django.urls import path
from App1.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('profesores', profesores, name='Profesores'),
    path('estudiantes', estudiantes),
    #urls curso
    path('curso/', curso_leer, name='App1CursoLeer'),
    path('curso/crear', curso_crear, name='App1CursoCrear'),
    path('curso/eliminar/<int:camada>', curso_eliminar, name='App1CursoEliminar'),
    path('curso/editar/<int:camada>', curso_editar, name='App1CursoEditar'),
    path('curso/curso_busqueda', curso_busqueda, name='App1CursoBusqueda'),
    path('curso/curso_buscar/', curso_buscar)


]