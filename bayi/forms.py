from django.forms import ModelForm
from core.models import  Sipariş

class SiparisForm(ModelForm):
    class Meta: 
       model = Sipariş
       fields = ['tutar']
