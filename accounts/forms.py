from django import forms

ACCOUNT_TYPE = [
    ('fm', 'Factory Manager'),
    ('dm', 'Dealer Manager'),
    ('cm', 'Customer')
]


class CreateUserAccountForm(forms.Form):
    email = forms.EmailField(label="Your Email Address", required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=True)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE, required=True)
    password = forms.PasswordInput()
