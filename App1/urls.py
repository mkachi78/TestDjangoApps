from django.urls import path
from App1.views import inicio, cursos, profesores, estudiantes

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos,name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('estudiantes', estudiantes)
]