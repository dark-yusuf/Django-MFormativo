from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import Cliente


class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            cliente= Cliente.objects.filter(rut=username, password=password).get()
            return cliente
        except:
            return None

    def get_user(sefl, user_id):
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None