from django.urls import path

from .views import telaLogin

urlpatterns = [
    path("/login", telaLogin, name="telaLogin"),
]
