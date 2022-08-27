from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from UserAdmin.forms import UserRegisterForm


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')
                return redirect('Inicio')
            else:
                messages.info(request, 'inicio de sesion fallido!')
                return redirect('UserLogin')
        else:
            messages.info(request, 'inicio de sesion fallido!')
            return redirect('UserLogin')

    contexto = {
        'form': AuthenticationForm(),
        'user_cmd': 'Ingreso de usuario'
    }
    return render(request, 'UserAdmin/login.html', contexto)


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
            return redirect('Inicio')

        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
            return redirect('UserRegister')

    contexto = {
        'form': UserRegisterForm(),
        'user_cmd': 'Registro de Usuario'
    }

    return render(request, 'UserAdmin/login.html', contexto)
