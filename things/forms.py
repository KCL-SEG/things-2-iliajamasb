"""Forms of the project."""
from django import forms
from things import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):

    #class Meta:

        #model = models.Thing
        #fields = ['name', 'description', 'quantity']


    name = forms.CharField(label='Name', max_length=35, required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', max_length=120, required=False)
    quantity = forms.IntegerField(
        widget=forms.NumberInput(),
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )


# Create your forms here.
