from django.urls import path

from .views import login_view, telaLogin, telaCadastro

urlpatterns = [
    path("/login", login_view, name="telaLogin"),
    path("/cadastro", telaCadastro, name="telaCadastro"),
]
