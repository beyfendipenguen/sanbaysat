from django.shortcuts import render
from django.views.generic import CreateView
from accounts.models import UserAccount
from .forms import CreateUserAccountForm
# Create your views here.


class AccountCreateView(CreateView):
    model = UserAccount
    form_class = CreateUserAccountForm
    template_name = "signup.html"
