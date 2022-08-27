from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
from App1.forms import CursoForm
from App1.models import Curso, Profesor


def inicio(request):
    return render(request, 'index.html')


class ProfesorList(ListView):

    model = Profesor
    template_name = "App1/profesor/list.html"


class ProfesorDetalle(DetailView):

    model = Profesor
    template_name = "App1/profesor/Detalle.html"



class ProfesorCreacion(CreateView):

    model = Profesor
    success_url = "/App1/profesor/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorUpdate(UpdateView):

    model = Profesor
    success_url = "/App1/profesor/list"
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorDelete(DeleteView):

    model = Profesor
    success_url = "/App1/profesor/list"


def profesores(request):

    return render(request, "App1/profesores.html")


def curso_leer(request):

    if request.method == 'POST':
        camada = request.POST['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        title = "Los cursos encontrados son: "
    else:
        cursos = Curso.objects.all()
        title = "Todos los cursos: "

    contexto = {
        'cursos': cursos,
        'title': title
    }
    return render(request, 'App1/curso/leer.html', contexto)

@login_required
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

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "App1/curso/res_busqueda_camada.html", {'cursos': cursos, 'camada': camada})

    respuesta = "No enviaste datos"
    return HttpResponse(respuesta)


def estudiantes(request):
    return redirect("App1Inicio")


def entregables(request):
    return HttpResponse("Vista Entregables")


