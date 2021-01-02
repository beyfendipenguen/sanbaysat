from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "home/index.html", {})

def loginPage(request):
    cevap = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('firma')
            # if user.superuser:
            #   return redirect("firma")
            # else:

            #    return redirect("bayi")
        else:
            cevap ={"cevap":"Kullanıcı adı veya Şifre hatalı"}

    return render(request, "home/login.html", cevap)


def firma(request):
    #TODO kullanıcı girişi
    """if user is not None:
        if user.super_user_status:
        else:
            return redirect('home')
"""
    return render(request, "core/firma.html", {})

def bayi(request):
    return render(request, "core/bayi.html", {})

def siparisler(request):
    return render(request, "core/siparisler.html", {})

def odemeler(request):
    return render(request, "core/siparisler.html", {})

def bayiler(request):
    return render(request, "core/siparisler.html", {})

def urunler(request):
    return render(request, "core/siparisler.html", {})

def cikisyap(request):
    logout(request)
    return redirect('home')