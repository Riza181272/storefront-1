from django.shortcuts import render
from . import views
# Create your views here.
def x(request):
    context = {
        'a' : 'Kelas Terbuka',
        'b' : 'Riza Raharja'
    }
    return render(request, 'z.html', context)
