from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, blank=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'  # mantém o username como campo obrigatório para autenticação
    REQUIRED_FIELDS = ['email']  # email será obrigatório ao criar superuser

    def __str__(self):
        return self.username