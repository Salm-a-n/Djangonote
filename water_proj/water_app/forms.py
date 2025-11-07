from django import forms
from .models import WaterIntakeModel

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntakeModel
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WaterIntakeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        intake = super().save(commit=False)
        intake.user = self.user
        if commit:
            intake.save()
        return intake

class DateRangeForm(forms.Form):
    start_date = forms.DateField(label="Start Date", widget=forms.Select)
    end_date = forms.DateField(label="End Date", widget=forms.Select)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            dates = WaterIntakeModel.objects.filter(user=user).order_by('-date').values_list('date', flat=True)
            choices = [(date, date.strftime('%Y-%m-%d')) for date in dates]
            self.fields['start_date'].widget.choices = choices
            self.fields['end_date'].widget.choices = choices
