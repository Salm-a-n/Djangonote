from django import forms
class RegForm(forms.Form):
    movie=forms.CharField(max_length=100)
    year=forms.IntegerField()