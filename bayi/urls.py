from django.urls import path
from . import views

urlpatterns = [
    path('', views.bayi, name="bayi"),
    path('bayisatis/',views.bayisatis,name="bayisatis"),
    path('bayisiparis/',views.siparisEt,
    name="siparisEt"),
    path('siparisSil/<int:id>', views.siparisSil,name="siparisSil"),
    path('bayibakim/',views.bayiBakim, name="bayiBakim"),
    path('bakimSil/<int:id>', views.bakimSil,name="bakimSil"),
]