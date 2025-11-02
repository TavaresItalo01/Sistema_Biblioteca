from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaInicial, name='telaInicial'),
    path('interesse/', views.area_interesse, name='telaAreaInteresse'),
    path('livros/<str:categoria>/', views.lista_livros, name='telaLivros'),
    path('livro/<int:id>/', views.detalhes_livro, name='detalhesLivro'),
    path('contato', views.telaContato, name='telaContato'),

]