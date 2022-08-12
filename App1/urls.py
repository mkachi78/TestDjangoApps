from django.urls import path
from App1.views import inicio, cursos, profesores, estudiantes

urlpatterns = [
    path('', inicio, name='App1Inicio'),
    path('cursos', cursos),
    path('profesores', profesores),
    path('estudiantes', estudiantes)
]