from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Satış, Sipariş, Bayi
from .models import *
from .forms import SiparisForm, createBayi, nameForm


def bayi(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except:
        return redirect('loginPage') 
    bayisatis = Satış.objects.all()
    form = SiparisForm()
    context = {"bayisatis":bayisatis, "form":form}
    #bayiler = Bayi.objects.filter(user=luser)
    if user is not None:
        if user.is_staff:
            return render(request, "bayi/bayi.html", context)
        else:
            return redirect('bilgilendirme')

def bilgilendirme(request):
    return render(request, "bayi/bilgilendirme.html")

def bayiKayıt(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except:
        return redirect('loginPage') 
    if request.method == 'POST':
        form = createBayi(request.POST)
        if form.is_valid():
            adı = form.cleaned_data['adı']
            şehir = form.cleaned_data['şehir']      
            telefon = form.cleaned_data['telefon']      
            adres = form.cleaned_data['adres']
            ülke = form.cleaned_data['ülke'] 
            bayi = Bayi(
                adı=adı,
                şehir=şehir,
                telefon=telefon,
                adres = adres,
                ülke = ülke,
                user=user
            )     
            try:
                bayi.save()
                return redirect('home')
            except:
                print("kayıt hatası")
    else:
        form = createBayi()
    context = {'form':form} 
    return render(request, "bayi/bayikayıt.html",context)

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparis_et(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)