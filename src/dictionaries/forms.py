from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Authors
        fields = ['first_name', 'last_name', 'country', 'date_of_birth']