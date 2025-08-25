from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    context = {
        'texto': "Olá mundo!",
    }
    return render(request, 'index.html', context)

def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos,
    }
    return render(request, 'produto.html', context)

def cad_produto(request):

    if request.method == "GET":
        return render(request, 'cad_produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',', '.')
        qtde = request.POST.get('qtde')

        produto = Produto(
            nome = nome,
            preco = preco,
            qtde = qtde
        )
        produto.save()
        return redirect('url_produtos')
    
def atualizar_produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        context = {
            'prod': prod,
        }
        return render(request, 'atualizar_produto.html', context)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',', '.')
        qtde = request.POST.get('qtde')

        prod.nome = nome
        prod.preco = preco
        prod.qtde = qtde
        prod.save()

    return redirect('url_produtos')

def apagar_produto(request):
    pass