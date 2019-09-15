from django import forms

from .models import Inputs

class InputForm(forms.ModelForm):
    # text = forms.CharField(label='')
    class Meta:
        model = Inputs
        fields = ('text',)
