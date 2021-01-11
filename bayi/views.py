from django.shortcuts import render
from django.contrib.auth.models import User

from core.models import Satış, Sipariş, Bayi
from .models import *
from .forms import SiparisForm



def bayi(request):
    bayisatis = Satış.objects.all()
    form = SiparisForm()
    luser = User.objects.get(pk=request.user.pk)
    print(luser)
    bayiler = Bayi.objects.filter(user=luser)
    print(bayiler)
    return render(request, "bayi/bayi.html", {"bayisatis":bayisatis, "form":form})

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparis_et(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)