from django import forms

from mainapp import models

class BookCardForm(forms.ModelForm):
    class Meta:
        model = models.BookCard
        fields = (
            'name',
            'picture',
            'cost',
            'authors',
            'series',
            'genres',
            'year',
            'num_pages',
            'book_format',
            'isbn',
            'weight',
            'age_category',
            'publisher',
            'qty',
            'is_active',
            'rating'
        )
