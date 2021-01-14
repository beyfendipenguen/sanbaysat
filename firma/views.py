from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ürünEkleForm, ödemeEkleForm
from core.models import Sipariş, Ürün, Ödeme, Bayi, Sipariş_Ürün
"""
def modelAdıEkle(request):
    if request.method == "POST":
        form = modelAdıEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            return redirect("Yönlendirilecek Sayfa")
    
    else:
        form = modelAdıEkleForm()
    context = {"form":form}
    return render(request,"tempalteAdı",context)
""" 
def ödemeEkle(request):
    if request.method == "POST":
        form = ödemeEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = ödemeEkleForm()
    context = {"form":form}
    return render(request,"firma/ödemeEkle.html",context)

def ürünEkle(request):
    if request.method == "POST":
        form = ürünEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = ürünEkleForm()
    context = {"form":form}
    return render(request, "firma/ürünEkle.html", context)
        



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


def siparişÜrün(request,id):
    s_ü = Sipariş_Ürün.objects.filter(sipariş_id=id)
    context = {'ürünler':s_ü}
    return render(request,"firma/urungoster.html",context)

def bayiSil(request,id):
    bayi = Bayi.objects.get(pk=id)
    kullanıcı = bayi.user
    bayi.delete()
    if Bayi.objects.filter(user_id=kullanıcı.id).__bool__() == False:
        kullanıcı.is_staff = False
        kullanıcı.save()
    return redirect("firma")
"""
def nesneSil(request,nesneadı,id):
    nesne = nesneadı.objects.get(pk=id)
    nesne.delete()
    return redirect("firma")
"""
def bayiOnayla(request,id):
    bayi = Bayi.objects.get(pk=id)
    kullanıcı = User.objects.get(pk=bayi.user.pk)
    kullanıcı.is_staff=True
    kullanıcı.save()
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

def firmaSiparisSil(request):
    firmaSiparis= Sipariş.objects.get(pk=id)
    firmaSiparis.delete()
    return redirect("firma")

def firmaUrunSil(request):
    firmaUrun = Ürün.objects.get(pk=id)
    firmaUrun.delete()
    return redirect("firma")

def firmaOdemeSil(request):
    firmaOdeme = Ödeme.objects.get(pk=id)
    firmaOdeme.delete()
    return redirect("firma")