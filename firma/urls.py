from django.urls import path
from . import views

urlpatterns= [
    path('', views.firma, name="firma"),
    path('siparisler/', views.siparisler, name="siparisler"),
    path('odemeler/', views.odemeler, name="odemeler"),
    path('urunler/', views.urunler, name="urunler"),
    path('bayiler/', views.bayiler, name="bayiler"),
    path("bayiSil/<int:id>", views.bayiSil, name="bayiSil"),
    path("bayiOnayla/<int:id>", views.bayiOnayla, name="bayiOnayla"),
    path("ürünGöster/<int:id>", views.siparişÜrün, name="siparişÜrün"),
    path('firmaSiparisSil/<int:id>', views.firmaSiparisSil,name="firmaSiparisSil"),
    path('firmaUrunSil/<int:id>',views.firmaUrunSil,name="firmaUrunSil"),
    path('firmaOdemeSil/<int:id>',views.firmaOdemeSil,name="firmaOdemeSil"),
    path("ürünEkle/", views.ürünEkle, name="ürünEkle"),
    path("ödemeEkle/", views.ödemeEkle, name="ödemeEkle"),
]