from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from App1.forms import CursoForm
from App1.models import Curso


def inicio(request):
    return render(request, 'index.html')


def curso_leer(request):
    cursos=Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'App1/curso/leer.html', contexto)


def curso_crear(request):

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso_data.save()

            return redirect('App1CursoLeer')
        else:
            return redirect('App1Inicio')

    contexto = {
        'my_form': CursoForm()
    }

    return render(request, 'App1/curso/crear.html', contexto)


def curso_editar(request, camada):

    curso = Curso.objects.get(camada=camada)
    my_form = CursoForm(initial={'nombre': curso.nombre, 'camada': curso.camada})

    contexto = {
        'my_form': my_form
    }

    return render(request, 'App1/curso/crear.html', contexto)


def curso_eliminar(request, camada):

    curso = Curso.objects.get(camada=camada)
    curso.delete()

    return redirect('App1CursoLeer')

def curso_busqueda(request):

    return render(request, 'App1/curso/buscar.html')

def curso_buscar(request):

    if request.GET['camada']:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada=request.GET['camada']
        cursos=Curso.objects.filter(camada__icontains=camada)

        return render(request, "App1/curso/res_busqueda_camada.html", {'cursos': cursos, 'camada': camada})

    respuesta="No enviaste datos"
    return HttpResponse(respuesta)

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


