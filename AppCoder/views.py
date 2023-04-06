from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    
    nombre_curso = "Programación"
    comision_curso = 123456

    curso = Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f" Curso creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

    
