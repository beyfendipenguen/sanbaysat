from django.shortcuts import render

from core.models import Satış, Sipariş
from .models import *
from .forms import SiparisForm



def bayi(request):
    bayisatis = Satış.objects.all()
    form = SiparisForm()
    return render(request, "bayi/bayi.html", {"bayisatis":bayisatis, "form":form})

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparis_et(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)