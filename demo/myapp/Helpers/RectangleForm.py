# RectangleForm.py
from django import forms

class RectangleForm(forms.Form):
    x = forms.IntegerField(label='X')
    y = forms.IntegerField(label='Y')
    width = forms.IntegerField(label='Width')
    height = forms.IntegerField(label='Height')
    color = forms.CharField(label='Color')
