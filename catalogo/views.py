from catalogo.backend import MyBackend
from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ReclamoForm, ClienteForm, UsuariosForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

myBackend=MyBackend()
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

def crearUsuario(request):
    #dinamico
    if request.method=="POST":
        form = UsuariosForm(data= request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            clave=form.cleaned_data["password"]
            user= User.objects.create_user(nombre, email, clave)
            user.save()
            return render(request, 'catalogo/usuariocreado.html')
    else:
        form= UsuariosForm()
        return render(request, 'catalogo/crearusuario.html',{"form":form})

def login(request):
    if request.method=="POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data["nombre"]
            clave= form.cleaned_data["password"]
        
            user= authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request,user)
        return render(request, 'catalogo/bienvenido.html', {"user":user})
    else:
        form= LoginForm()
        return render(request, 'catalogo/login.html', {"form":form})
        
@login_required(login_url="/login")
def bienvenido(request):
    return render(request, 'catalogo/bienvenido.html')

def salir(request):
    logout(request)
    return redirect("/login")

def login2(request):
    if request.method=="POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data["nombre"]
            clave= form.cleaned_data["password"]
        
            user= myBackend.authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request,user)
        return render(request, 'catalogo/bienvenido.html', {"user":user})
    else:
        form= LoginForm()
        return render(request, 'catalogo/login.html', {"form":form})