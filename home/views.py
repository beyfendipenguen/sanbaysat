from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.models import Bayi

# Create your views here.

def home(request):
    return render(request, "home/index.html", {})

def bayilerimiz(request):
    bayiler = Bayi.objects.all()
    context={"bayiler":bayiler}
    return render(request, "home/bayilerimiz.html", context)

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

def signIn(request):
    return render(request,"home/bayikayit.html")
def cikisyap(request):
    logout(request)
    return redirect('home')