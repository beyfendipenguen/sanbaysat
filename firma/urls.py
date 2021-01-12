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
    #path("nesneSil/<str:nesneadı>/<int:id>", views.nesneSil, name="nesneSil"),
    path("bayiOnayla/<int:id>", views.bayiOnayla, name="bayiOnayla"),


]