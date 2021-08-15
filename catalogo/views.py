from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ReclamoForm, ClienteForm
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

def reclamo(request):
    datos= request.POST
    email=datos["email"]
    reclamo= datos["reclamo"]
    print(datos, email, reclamo)
    
    return render(request, 'catalogo/contacto.html', {"mensaje":"Datos recibidos", "email": email})

def reclamo2(request):
    if request.method == "POST":
        form= ReclamoForm(data= request.POST)
        email= form["email"]
        reclamo= form["reclamo"]
        return render(request, 'catalogo/reclamoejemplo.html', {"respuesta":"OK"})
    else:
        form = ReclamoForm()
        return render(request, 'catalogo/reclamoejemplo.html', {"form":form})


def clientes2(request):
    if request.method == "POST":
        form= ClienteForm(data= request.POST)
        if form.is_valid():
            cliente= form.save(commit=False)#esta en memoria

            cliente.save()#guarda en base de datos
        return redirect('/clientes')
    else:
        form= ClienteForm()
        return render(request, 'catalogo/crearcliente.html', {"form":form})

