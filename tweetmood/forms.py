
from django import forms


class SubjectContent(forms.Form):
    sentence = forms.CharField(label='Enter the content analysed', max_length=200)
