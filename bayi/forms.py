from django.forms import ModelForm
from core.models import  Sipariş_Ürün

class SiparisForm(ModelForm):
    class Meta: 
       model = Sipariş_Ürün
       fields = '__all__'

