from django.shortcuts import render

def index(request):
    context = {
        "texto": "Olá mundo!",
    }
    return render(request,'index.html',context)

def produtos(request):
    return render(request, 'produto.html')

