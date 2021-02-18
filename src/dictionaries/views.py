from django.shortcuts import render
from . import models
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


views_dicts = [
    'Authors',
    'Countries',
    'Genres',
    'Series',
    'Publishers'
]


# Create your views here.
def main_dicts(request):
    return render(request, template_name='main_dicts.html', context={'view_dicts': views_dicts})


class AuthorsList(ListView):
    model = models.Authors


class CountriesList(ListView):
    model = models.Countries


class GenresList(ListView):
    model = models.Genres
    

class SeriesList(ListView):
    model = models.Series


class PublishersList(ListView):
    model = models.Publishers


class AuthorsDetail(DetailView):
    model = models.Authors


class AuthorsDelete(DeleteView):
    model = models.Authors
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class CountriesDelete(DeleteView):
    model = models.Countries
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('countries-list')


class AuthorsUpdate(UpdateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'main_form.html'
    # fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('authors-list')


class CountriesUpdate(UpdateView):
    model = models.Countries
    form_class = forms.CountryForm
    template_name = 'main_form.html'
    # fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('countries-list')


class AuthorsCreate(CreateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'main_form.html'
    # fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('authors-list')


class CountriesCreate(CreateView):
    model = models.Countries
    form_class = forms.CountryForm
    template_name = 'main_form.html'
    # fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('countries-list')
