from django import forms
from .models import Car

class CarForm(forms.Form):
    product = forms.ModelChoiceField(Car.objects.all(), required=False)


