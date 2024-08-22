from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
def inicio(request):
    return render(request,'paginas/inicio.html')
# Create your views here.
def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros=Libro.objects.all()
    return render(request,'libros/index.html',{'libros':libros})
def crear(request):
    formulario=LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid(): 
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html',{'formulario':formulario})
def editar(request):
    return render(request,'libros/editar.html')
def  eliminar(request,id):
    libros=Libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')
