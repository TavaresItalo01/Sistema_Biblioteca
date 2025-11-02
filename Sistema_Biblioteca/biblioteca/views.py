from django.shortcuts import render
from .models import Livro
from django.shortcuts import render, get_object_or_404


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

def detalhes_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'biblioteca/detalhesLivro.html', {'livro': livro})