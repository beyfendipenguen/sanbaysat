from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Sipariş, Ürün, Ödeme, Bayi, Sipariş_Ürün

# Create your views here.
def firma(request):
    #TODO kullanıcı girişi
    user = User.objects.get(pk=request.user.pk)
    if user is not None:
        if user.is_superuser:
            print("buyur reis şöyle geç")
        else:
            return redirect('home')
    siparişler = Sipariş.objects.all()
    ürünler = Ürün.objects.all()
    bayiler = Bayi.objects.all()
    ödemeler = Ödeme.objects.all()


    return render(request, "firma/firma.html", {"siparişler":siparişler, "ürünler":ürünler, "bayiler":bayiler,"ödemeler":ödemeler})


def bayiSil(request,id):
    bayi = Bayi.objects.get(pk=id)
    bayi.delete()
    return redirect("firma")

def nesneSil(request,nesneadı,id):
    nesne = nesneadı.objects.get(pk=id)
    nesne.delete()
    return redirect("firma")

def bayiOnayla(request,id):
    bayi = Bayi.objects.get(pk=id)
    bayi.aktif = True
    bayi.save()

    return redirect("firma")

def siparisler(request):
    return render(request, "firma/siparisler.html", {})

def odemeler(request):
    return render(request, "firma/odemeler.html", {})

def bayiler(request):
    return render(request, "firma/bayiler.html", {})

def urunler(request):
    return render(request, "firma/urunler.html", {})


def siparisEkle(request):
    s = Sipariş()
    context = {}
    return render(request, "firma/siparisler.html", context)
