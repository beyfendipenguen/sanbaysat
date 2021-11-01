from django.urls import path, include
from django.views.generic import TemplateView
from accounts.views import AccountCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('signup/', AccountCreateView.as_view()),
]
