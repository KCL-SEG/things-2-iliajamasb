"""Forms of the project."""
from django import forms

class ThingForm(forms.Form):

    name = forms.CharField(label='Name', max_length=35, blank=False, unique=True)
    description = forms.CharField(label='Description', blank=False)
    quantity = forms.IntegerField(
        label='Quantity', validators=[
            MinValueValidator(0),
            MaxValueValidator(50)])
    widgets = { "description": forms.Textarea(), "quantity": forms.NumberInput() }

# Create your forms here.
