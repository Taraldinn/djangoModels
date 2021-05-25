from django import forms
from django.core import validators
from appone import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

# class user_form(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
#     number_field = forms.IntegerField(validators=[validators.MaxValueValidator(15), validators.MinValueValidator(5)])
