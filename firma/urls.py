from django.urls import path
from . import views

urlpatterns= [
    path('', views.firma, name="firma"),
    path('siparisler/', views.siparisler, name="siparisler"),
    path('odemeler/', views.odemeler, name="odemeler"),
    path('urunler/', views.urunler, name="urunler"),
    path('bayiler/', views.bayiler, name="bayiler"),
    path("siparisEkle/", views.siparisEkle, name="siparisEkle"),
    path("bayiSil/<int:id>", views.bayiSil, name="bayiSil"),
    path("bayiOnayla/<int:id>", views.bayiOnayla, name="bayiOnayla"),
    path("ürünGöster/<int:id>", views.siparişÜrün, name="siparişÜrün"),
    path("ürünEkle/", views.ürünEkle, name="ürünEkle"),
    path("ödemeEkle/", views.ödemeEkle, name="ödemeEkle"),

]