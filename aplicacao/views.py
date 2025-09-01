from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def index(request):
    context = {
        'texto': "olá mundo",
    }
    return render(request, 'index.html', context)
@login_required(login_url="url_entrar")
def produto(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'produto.html', context)

def cadastro_produto(request):
    if request.user.is_authenticated:
        if request.method =='GET':
            return render(request, 'cadastro_produto.html')
        elif request.method == "POST":
            nome = request.POST.get('nome')
            preco = request.POST.get('preco').replace(',', '.')
            quantidade = request.POST.get('quantidade')

            produto = Produto(
                nome = nome,
                preco = preco,
                quantidade = quantidade
            )
            produto.save()
            return redirect('url_produto')
    else:
        return redirect('url_entrar')
    
def atualizar_produtos(request, id):
    prod = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        context = {
            'prod': prod,
        }
    
        return render(request, 'atualizar_produtos.html', context)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',', '.')
        quantidade = request.POST.get('quantidade')

        prod.nome = nome
        prod.preco = preco
        prod.quantidade = quantidade
        prod.save()
    return redirect('url_produto')

def apagar_produto(request, id):
    prod = get_object_or_404(Produto, id=id)
    prod.delete()
    return redirect('url_produto')

def entrar(request):
    if request.method == "GET":
        return render(request, "entrar.html")
    else:
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("url_produto")
        else:
            return HttpResponse("Falha no login")
        
def cad_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        usuario_existente = User.objects.filter(username=nome).first()
        
        if usuario_existente:
            return HttpResponse("Usuário já existe")


        User = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        mensages.sucess (request,"cad_user.html")
        
        return HttpResponse("Usuário criado com sucesso!")
    else:
        return render(request, 'cad_user.html')
    
def sair(request):
    logout(request)
    return redirect('url_entrar')