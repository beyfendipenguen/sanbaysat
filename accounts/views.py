from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import UserAccount
# Create your views here.


class AccountCreateView(CreateView):
    model = UserAccount
    template_name = "signup.html"
    fields = ['email', 'first_name', 'last_name', 'password', 'date_of_birth']
