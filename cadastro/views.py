from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario
from django.contrib.auth import authenticate, login
def Telainicial_home(request):
    return render(request, 'cadastro/home.html')



def resetpassword_email(request):
     return render(request, 'resetsenha/restpassword_form_email.html')


#start cadastro usuários
def cadastrar_usuario(request):
    if request.method == 'POST':
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            cpf_cnpj = request.POST.get('cpf_cnpj')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Este e-mail já está cadastrado.')
                return redirect('cadastro')

            if Usuario.objects.filter(cpf_cnpj=cpf_cnpj).exists():
                messages.error(request, 'Este CPF/CNPJ já está cadastrado.')
                return redirect('cadastro')
            
            if Usuario.objects.filter(nome=nome).exists():
                messages.error(request, 'Este Nome já está cadastrado.')
                return redirect('cadastro')
            
            else:
                Usuario.objects.create(
                nome=nome,
                senha=make_password(senha),
                cpf_cnpj=cpf_cnpj,
                email=email,
                telefone=telefone
                )
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return render(request, 'cadastro/home.html')
            
    return render(request, 'cadastro/cadastrar.html')
#end cadastro usuários

#start login
def Login_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        
        try:
            usuario = Usuario.objects.get(cpf_cnpj=cpf_cnpj)

        except Usuario.DoesNotExist:
                messages.error(request, 'CPF/CNPJ não encontrado.')
                return redirect('login')
        
        if check_password(senha, usuario.senha):
            # Login válido, você pode salvar sessão ou redirecionar
            request.session['usuario_id'] = usuario.id
            messages.success(request, 'Login realizado com sucesso!')
            return render(request, 'cadastro/home.html')
        else:
            messages.error(request, 'Senha incorreta.')
            return redirect('login')

    return render(request, 'cadastro/login.html')

#end login
