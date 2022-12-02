"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class ThingForm(forms.Form):

    name = forms.CharField(label='Name')
    #max_length=35,
    #blank=False,
    #unique=True)
    description = forms.CharField(label='Description')
    quantity = forms.IntegerField(label='Quantity', validators=[MinValueValidator(0),MaxValueValidator(50)])
    widgets = { "description": forms.Textarea(), "quantity": forms.NumberInput() }

# Create your forms here.
