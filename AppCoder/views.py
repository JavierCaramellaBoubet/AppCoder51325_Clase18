from django.shortcuts import render
from .models import Curso, Profesor
from .forms import ProfesorForm
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    
    nombre_curso = "Programación"
    comision_curso = 123456

    curso = Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f" Curso creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)


def cursos(request):
    return render(request, 'AppCoder/cursos.html')    

def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
        else:
            pass    

    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all()
    #profesores = Profesor.objects.filter(nombre__icontains = "J").all()  # CREAMOS UN FILTRO PARA BUSCAR POR LETRA
    context = {"profesores": profesores, "form": form}
    return render(request, 'AppCoder/profesores.html', context)

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def inicio(request):
    return HttpResponse('Bienvenido a la Página Principal') 

def inicioApp(request):
    return render(request, 'AppCoder/inicio.html')


    
    
