from django import forms

from .models import Inputs

class InputForm(forms.ModelForm):
    class Meta:
        model = Inputs
        fields = ('text',)
