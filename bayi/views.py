from django.shortcuts import render
from django.contrib.auth.models import User

from core.models import Satış, Sipariş, Bayi
from .models import *
from .forms import SiparisForm



def bayi(request):
    bayisatis = Satış.objects.all()
    form = SiparisForm()
    context = {"bayisatis":bayisatis, "form":form}
    #bayiler = Bayi.objects.filter(user=luser)
    user = User.objects.get(pk=request.user.pk)
    if user is not None:
        if user.is_staff:
            return render(request, "bayi/bayi.html", context)
        else:
            return render(request, "bayi/bilgilendirme.html")

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparis_et(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)