"""Forms of the project."""
from django import forms

class ThingForm(forms.Form):

    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    quantity = forms.IntegerField(label='Quantity')
    widgets = { "bio": forms.Textarea() }

# Create your forms here.
