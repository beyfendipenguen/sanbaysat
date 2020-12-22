from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="loginPage"),
    path('firma/', views.firma, name="firma"),
    path('bayi/', views.bayi, name="bayi"),


]
