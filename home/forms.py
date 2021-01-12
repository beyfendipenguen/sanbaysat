from django.forms import ModelForm
from django.contrib.auth.models import User

class createUser(ModelForm):
    class Meta: 
       model = User
       fields = '__all__'
       #['first_name','last_name','username','password','email']
