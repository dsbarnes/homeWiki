from django import forms
from django.forms import ModelForm
from .models import Grocery


class DateInput(forms.DateInput):
    input_type = 'date'


class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = ['item', 'name', 'quantity', 'cost', 'date']

        # The default form is input:text,
        # that is dumb af - it's a dateField
        widgets = {
            'date': DateInput(),
        }