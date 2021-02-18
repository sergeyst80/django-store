from django import forms
from . import models
from crispy_forms.helper import FormHelper

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Authors
        fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Countries
        fields = ['name']


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genres
        fields = ['name']


class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = ['name']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publishers
        fields = ['name', 'country']
