from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

from .models import Usuario
from django.contrib.auth.hashers import make_password

def telaLogin(request):
    return render(request, "usuarios/telaLogin.html")

def telaCadastro(request):
    return render(request, "usuarios/telaCadastro.html")


def login_view(request):
    if request.method == 'POST':
        email_cpf = request.POST.get('email_cpf')
        senha = request.POST.get('senha')

        print("Email/CPF:", email_cpf)
        print("Senha:", senha)


        user = authenticate(request, username=email_cpf, password=senha)
        print("User:", user)
        if user:
            login(request, user)
            messages.success(request, f"Bem-vindo {user.username}!")
            return redirect('telaCadastro')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'usuarios/telaLogin.html')


def telaCadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        confirmar_email = request.POST.get('confirmar_email')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validações
        if email != confirmar_email:
            messages.error(request, "Os e-mails não coincidem.")
            return redirect('telaCadastro')

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return redirect('telaCadastro')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado.")
            return redirect('telaCadastro')

        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado.")
            return redirect('telaCadastro')

        # Cria usuário
        user = Usuario.objects.create(
            username=email,  
            first_name=nome,
            last_name=sobrenome,
            email=email,
            cpf=cpf,
            password=make_password(senha)
        )

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('telaLogin')

    return render(request, 'usuarios/telaCadastro.html')