from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'paginas/inicio.html')
# Create your views here.
def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    return render(request,'libros/index.html')
def crear(request):
    return render(request,'libros/crear.html')
