from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.models import Bayi
from django.contrib.auth.forms import UserCreationForm

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
            if user.is_superuser:
                return redirect("firma")
            else:
                return redirect("bayi")
        else:
            cevap ={"cevap":"Kullanıcı adı veya Şifre hatalı"}

    return render(request, "home/login.html", cevap)


def signIn(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loginPage')
    else:
        form = UserCreationForm()
    return render(request,"home/bayikayit.html",{"form":form})

def cikisyap(request):
    logout(request)
    return redirect('home')