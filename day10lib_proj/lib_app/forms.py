from django import forms
from  .models import Lib_manage

class lib_form(forms.ModelForm):
    class Meta:
        model=Lib_manage
        fields=['title','author','year']
        