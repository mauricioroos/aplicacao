from django.shortcuts import render, redirect
from .models import Produto
from django.http.response import HttpResponse

def index(request):
    context = {
        "texto": "Olá mundo!",
    }
    return render(request,'index.html', context)

def produtos(request):
    produtos = Produto.objects.all()
    context ={
        'produtos': produtos
        
    }
    return render(request, 'produto.html', context)

def cad_produto(request):
    if request.method == "GET":
        return render(request,'cad_produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',','.')
        qtde = request.POST.get('qtde')
    
        produtos =  Produto(
            nome = nome,
            preco = preco,
            qtde = qtde,
        )
        produtos.save()
        return redirect('url_produtos')



