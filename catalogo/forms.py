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
