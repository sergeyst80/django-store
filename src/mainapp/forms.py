from django import forms


class CatalogSearchForm(forms.Form):
    search = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Поиск по каталогу...'}),
        required=False
    )