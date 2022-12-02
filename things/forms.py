"""Forms of the project."""
from django import forms
from things import models

class ThingForm(forms.Form):

    class Meta:

        model = models.Thing
        fields = ['name', 'description', 'quantity']
        widgets = { "description": forms.Textarea(), "quantity": forms.NumberInput() }

    name = forms.CharField(label='Name', validators=[])
    description = forms.CharField(label='Description')
    quantity = forms.IntegerField(label='Quantity')


# Create your forms here.
