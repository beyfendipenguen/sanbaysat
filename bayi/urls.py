from django.urls import path
from . import views

urlpatterns = [
    path('', views.bayi, name="bayi"),
    path('bayisatis/',views.bayisatis,name="bayisatis"),
    path('bayisiparis/',views.siparis_et,name="siparis_et"),
    path('bilgilendirme/', views.bilgilendirme, name = "bilgilendirme"),
    path('bayikayıt/', views.bayiKayıt, name="bayiKayıt"),
]