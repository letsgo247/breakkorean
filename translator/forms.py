from django import forms
from .models import Inputs

class InputForm(forms.ModelForm):
    # text = forms.CharField(label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), label='')
    class Meta:
        model = Inputs
        fields = ('text',)
