from django.shortcuts import render,redirect

from core.models import Satış, Sipariş, Bakım
from .models import *
from .forms import SiparisForm



def bayi(request):
    bayisatis = Satış.objects.all()
    form = SiparisForm()
    return render(request, "bayi/bayi.html", {"bayisatis":bayisatis, "form":form})

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparisEt(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)

def siparisSil(request,id):
    satis= Satış.objects.get(pk=id)
    satis.delete()
    return redirect("bayi")

def bayiBakim(request):
    
    context = {}
    return render(request, 'bayi/bayiBakim.html',context)

def bakimSil(request,id):
    bakim = Bakım.objects.get(pk=id)
    bakim.delete()
    return redirect("bayi")