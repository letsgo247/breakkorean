from django import forms
from .models import Inputs

class InputForm(forms.ModelForm):
    # text = forms.CharField(label='')
    text = forms.CharField(initial='문장을 입력하세요', widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), label='')
    class Meta:
        model = Inputs
        fields = ('text',)
