from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator 

from .models import AwesomeLink


class RatingForm(forms.Form):
    pk = forms.IntegerField()
    rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])