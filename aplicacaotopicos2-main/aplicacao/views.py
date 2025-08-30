from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def index(request):
    context = {
        'texto': "olá mundo",
    }
    return render(request, 'index.html', context)

def produto(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'produto.html', context)

def cadastro_produto(request):
    if request.method == "GET":
        return render(request, 'cadastro_produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',', '.')
        quantidade = request.POST.get('quantidade')

        produto = Produto(
            nome = nome,
            preco = preco,
            quantidade = quantidade,
        )
        produto.save()
        return redirect(('url_produto'))

def atualizar_produtos(request, id):
    #prod = Produto.objects.get(id = id)
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
            return HttpResponse("Usuário logado com sucesso")
        else:
            return HttpResponse("Falha no login")