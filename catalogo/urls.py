from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('', views.index),
    path('contacto/' , views.contacto),
    path('recibir/', views.recibir),
    path('sumar/<int:numero1>/<int:numero2>/', views.sumar),
    path('clientes', views.clientes),
    path('recibirReclamo', views.reclamo),
    path('reclamov2', views.reclamo2),
    path('cliente2', views.clientes2),
    path('crearusuario', views.crearUsuario),
    path('login', views.login),
    path('bienvenido', views.bienvenido),
    path('salir', views.salir)

]