from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="loginPage"),
    path('firma/', views.firma, name="firma"),
    path('bayi/', views.bayi, name="bayi"),
    path('firma/siparisler/', views.siparisler, name="siparisler"),
    path('firma/odemeler/', views.odemeler, name="odemeler"),
    path('firma/urunler/', views.urunler, name="urunler"),
    path('firma/bayiler/', views.bayiler, name="bayiler"),
    path('cikisyap/', views.cikisyap, name="cikisyap"),



]
