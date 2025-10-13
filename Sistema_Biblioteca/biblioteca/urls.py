from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaInicial, name='telaInicial'),
]