from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Livro
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


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

def telaContato(request):
    return render(request, "biblioteca/telaContato.html")

def pedido(request):
    livro_id = request.GET.get('livro_id')
    quantidade = int(request.GET.get('quantidade', 1))

    livro = None
    if livro_id:
        livro = get_object_or_404(Livro, id=livro_id)

    if 'aumentar' in request.GET:
        quantidade += 1
    elif 'diminuir' in request.GET and quantidade > 1:
        quantidade -= 1

    if 'finalizar' in request.GET:
        if livro:
            messages.success(request, 'Pedido realizado com sucesso!')
        else:
            messages.warning(request, 'Nenhum livro selecionado.')

    return render(request, 'biblioteca/pedido.html', {
        'livro': livro,
        'quantidade': quantidade
    })
