from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError

def validate_not_gmail(value):
    if value.find('@gmail') != -1:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value': value},
        )
class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,min_length=6, validators=[validate_email,validate_not_gmail])
    password = forms.CharField(max_length=50,min_length=6)