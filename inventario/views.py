from django.shortcuts import render


def inventario(request):
    return render(request, 'home.html')

def imagem(request):
    return render(request, 'imagem.html')
