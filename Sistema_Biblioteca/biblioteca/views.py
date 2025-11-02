from django.shortcuts import render
from .models import Livro

def telaInicial(request):
    return render(request, "biblioteca/telaInicial.html")

def area_interesse(request):
    return render(request, 'biblioteca/telaAreaInteresse.html')

def lista_livros(request, categoria):
    livros_filtrados = Livro.objects.filter(categoria=categoria)
    categorias_dict = dict(Livro.CATEGORIAS_LIVRO)
    categoria_nome_formatado = categorias_dict.get(categoria, categoria)
    
    context = {
        'livros': livros_filtrados,
        'categoria_nome': categoria_nome_formatado
    }
    return render(request, 'biblioteca/telaLivros.html', context)
