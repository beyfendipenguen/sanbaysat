from django.urls import path
from . import views

urlpatterns= [
    path('', views.firma, name="firma"),
    path('siparisler/', views.siparisler, name="siparisler"),
    path('odemeler/', views.odemeler, name="odemeler"),
    path('urunler/', views.urunler, name="urunler"),
    path('bayiler/', views.bayiler, name="bayiler"),
    path("siparis_ekle/", views.siparisEkle, name="siparisEkle"),

]