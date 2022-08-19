from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from App1.forms import CursoForm
from App1.models import Curso


def inicio(request):
    return render(request, 'index.html')


def cursos(request):

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            curso = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso.save()

    cursos=Curso.objects.all()

    contexto = {
        'cursos': cursos,
        'my_form': CursoForm()
    }

    return render(request, 'App1/cursos.html', contexto)


def profesores(request):

    return render(request,"App1/profesores.html")

def estudiantes(request):
    return redirect("App1Inicio")

def entregables(request):
    return HttpResponse("Vista Entregables")


