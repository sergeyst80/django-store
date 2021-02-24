from django.shortcuts import render
from . import models
from . import forms
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
# Dictionaries ListViews
class AuthorsList(generic.ListView):
    model = models.Authors
    template_name = 'dictionaries/list_authors.html'
    

class GenresList(generic.ListView):
    model = models.Genres
    template_name = 'dictionaries/list_genres.html'
    

class SeriesList(generic.ListView):
    model = models.Series
    template_name = 'dictionaries/list_series.html'


class PublishersList(generic.ListView):
    model = models.Publishers
    template_name = 'dictionaries/list_publishers.html'


# Dictionaries generic.DeleteViews
class AuthorsDelete(generic.DeleteView):
    model = models.Authors
    template_name = 'dictionaries/form_confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(generic.DeleteView):
    model = models.Genres
    template_name = 'dictionaries/form_confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(generic.DeleteView):
    model = models.Series
    template_name = 'dictionaries/form_confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(generic.DeleteView):
    model = models.Publishers
    template_name = 'dictionaries/form_confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries UpdateViews
class AuthorsUpdate(generic.UpdateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(generic.UpdateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(generic.UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(generic.UpdateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries CreateViews
class AuthorsCreate(generic.CreateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(generic.CreateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(generic.CreateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'dictionaries/form_create_update.html'
    success_url = reverse_lazy('publishers-list')
