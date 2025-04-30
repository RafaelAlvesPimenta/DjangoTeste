from django.shortcuts import render, redirect
from .models import Usuario

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Usuario.objects.create(
            nome=nome,
            senha=senha,
            cpf_cnpj=cpf_cnpj,
            email=email,
            telefone=telefone
        )
        return redirect('home')  # Redireciona para a página de sucesso após salvar

    return render(request, 'cadastro/cadastrar.html')  # Só mostra o formulário se for GET

def Telainicial_home(request):
    return render(request, 'cadastro/home.html')

def Login_usuario(request):
    return render(request, 'cadastro/login.html')

