from django import forms
class RegForm(forms.Form):
    movie=forms.CharField(max_length=100)
    year=forms.IntegerField()
class ContactForm(forms.Form):
    full_name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    phone=forms.CharField(max_length=13)                                                                                                          