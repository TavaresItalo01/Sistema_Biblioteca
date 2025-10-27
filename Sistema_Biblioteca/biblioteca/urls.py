from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaInicial, name='telaInicial'),
    path('interesse/', views.area_interesse, name='telaAreaInteresse'),
    # path('livros/', views.lista_livros, name='lista_livros'),
]