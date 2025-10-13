from django.shortcuts import render

def telaInicial(request):
    return render(request, "biblioteca/telaInicial.html")
