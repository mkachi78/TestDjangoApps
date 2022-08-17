from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from App1.models import Curso


def inicio(request):
    return render(request, 'index.html')

def cursos(request):

    contexto= {
       "cursos":{
        "curso1": "Nombre1",
        "curso2": "Nombre2",
        "curso3": "Nombre3",
       }
    }
    return render(request, 'App1/cursos.html', contexto)

def profesores(request):
    return render(request,"App1/profesores.html")

def estudiantes(request):
    return redirect("App1Inicio")

def entregables(request):
    return HttpResponse("Vista Entregables")


