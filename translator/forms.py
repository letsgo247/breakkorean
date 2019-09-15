from django import forms
from django.forms import Textarea


from .models import Inputs

class InputForm(forms.ModelForm):
    # text = forms.CharField(label='')
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Inputs
        fields = ('text',)
        # widgets = {
        #     'text': Textarea(attrs={'cols': 20, 'rows': 20}),
        # }
