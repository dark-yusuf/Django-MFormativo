from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'catalogo/index.html')

def contacto(request):
    return render(request, 'catalogo/contacto.html')
