from django import forms
from django.db.models import fields
from .models  import Cliente

class ReclamoForm(forms.Form):
    email= forms.CharField(widget= forms.EmailInput)
    reclamo= forms.CharField(widget= forms.Textarea)

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields=('rut','nombre','apellido','edad')

class UsuariosForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    nombre= forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
