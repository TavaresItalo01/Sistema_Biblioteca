from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class EmailOrCpfBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta buscar por emails
            user = Usuario.objects.get(email=username)
        except Usuario.DoesNotExist:
            try:
                # Tenta buscar por CPF
                user = Usuario.objects.get(cpf=username)
            except Usuario.DoesNotExist:
                return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
