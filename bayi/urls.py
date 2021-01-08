from django.urls import path
from . import views

urlpatterns = [
    path('', views.bayi, name="bayi"),
    
]