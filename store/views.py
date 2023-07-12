from django.shortcuts import render
from store.models import Kategori, Urun
# Create your views here.


def Master(request):
    return render(request, 'master.html')

def Index(request):
    kategori = Kategori.objects.all()
    urun = Urun.objects.all()
    context = {
        'kategori':kategori,
        'urun':urun
    }
    return render(request, 'index.html', context)
