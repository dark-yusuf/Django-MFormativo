from django.shortcuts import render
from .models import Cliente
# Create your views here.

def index(request):
    return render(request, 'catalogo/index.html')


def recibir(request):
    print(request.GET["data"])
    numero=request.GET["data"]
    return render(request, 'catalogo/index.html',{"numero":numero})

def sumar(request, numero1, numero2):
    print(numero1, numero2)
    resultado= numero1+numero2
    return render(request, 'catalogo/index.html', {"numero": resultado})

def contacto(request):
    return render(request, 'catalogo/contacto.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'catalogo/clientes.html', {"data":cliente})
