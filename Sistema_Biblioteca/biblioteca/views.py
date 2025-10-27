from django.shortcuts import render

def telaInicial(request):
    return render(request, "biblioteca/telaInicial.html")

def area_interesse(request):
    return render(request, 'biblioteca/telaAreaInteresse.html')

def lista_livros(request):
    return render(request, 'biblioteca/telaLivros.html')