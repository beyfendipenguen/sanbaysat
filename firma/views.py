from django.shortcuts import render

from core.models import Sipariş, Ürün, Ödeme, Bayi 

# Create your views here.
def firma(request):
    #TODO kullanıcı girişi
    siparişler = Sipariş.objects.all()
    ürünler = Ürün.objects.all()
    bayiler = Bayi.objects.all()
    ödemeler = Ödeme.objects.all()

    """if user is not None:
        if user.super_user_status:
        else:
            return redirect('home')
"""

    return render(request, "firma/firma.html", {"siparişler":siparişler, "ürünler":ürünler, "bayiler":bayiler,"ödemeler":ödemeler})




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
