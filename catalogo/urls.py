from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('', views.index),
    path('contacto/' , views.contacto),
    path('recibir/', views.recibir),
    path('sumar/<int:numero1>/<int:numero2>/', views.sumar)
]