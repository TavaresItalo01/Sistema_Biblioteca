from django.shortcuts import render
from django.http import HttpResponse

def telaLogin(request):
    return render(request, "usuarios/telaLogin.html")
