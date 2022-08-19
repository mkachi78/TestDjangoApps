from django import forms

class CursoForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Profesor(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
