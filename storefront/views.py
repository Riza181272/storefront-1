from django.shortcuts import render

def index(request):
    context = {
        'title': 'Welcome in | Anavrin Inc.',
        'heading': 'Selamat Datang di Blog',

    }
    return render(request, 'index.html',context)




