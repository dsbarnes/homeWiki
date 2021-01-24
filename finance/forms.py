from django import forms
from django.forms import ModelForm
from .models import Finance 


class DateInput(forms.DateInput):
    input_type = 'date'


class FinanceForm(ModelForm):
    class Meta:
        model = Finance
        fields = ['user', 'name', 'amount', 'date', 'finance_type']

        # The default form is input:text,
        # that is dumb af - it's a dateField
        widgets = {
            'date': DateInput(),
        }