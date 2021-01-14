from django.forms import ModelForm
from core.models import Ürün, Ödeme
from django import forms
"""
class modelAdıEkleForm(ModelForm):
    class Meta:
        model = modelAdı
        fields = "__all__"
"""

class ürünEkleForm(ModelForm):
    class Meta:
        model = Ürün
        fields = "__all__"


class ödemeEkleForm(ModelForm):
    class Meta:
        model = Ödeme
        fields = "__all__"