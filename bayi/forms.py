from django import forms
from django.forms import ModelForm
from core.models import  Sipariş_Ürün, Bayi

class nameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)


class SiparisForm(ModelForm):
    class Meta: 
       model = Sipariş_Ürün
       fields = '__all__'


class createBayi(ModelForm):
    class Meta:
        model = Bayi
        fields = ['adı','şehir','telefon','adres','ülke']
    