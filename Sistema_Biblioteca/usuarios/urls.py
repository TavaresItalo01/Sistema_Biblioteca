from django.urls import path

from .views import login_view, telaLogin, telaCadastro, telaPerfil, atualizar_perfil

urlpatterns = [
    path("login/", login_view, name="telaLogin"),
    path("cadastro/", telaCadastro, name="telaCadastro"),
    path("perfil/", telaPerfil, name="telaPerfil"),
    path('perfil/atualizar/', atualizar_perfil, name='atualizar_perfil'),

]
