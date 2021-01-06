from django.shortcuts import render
from core.models import Sipariş
# Create your views here.
def firma(request):
    #TODO kullanıcı girişi
    siparişler = Sipariş.objects.all()
    """if user is not None:
        if user.super_user_status:
        else:
            return redirect('home')
"""
    return render(request, "firma/firma.html", {"siparişler":siparişler})



def siparisler(request):
    return render(request, "firma/siparisler.html", {})

def odemeler(request):
    return render(request, "firma/odemeler.html", {})

def bayiler(request):
    return render(request, "firma/bayiler.html", {})

def urunler(request):
    return render(request, "firma/urunler.html", {})


def siparisEkle(request):
    context = {}
    return render(request, "firma/siparisler.html", context)
