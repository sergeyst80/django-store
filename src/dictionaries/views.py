from django.shortcuts import render
from . import models
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
# Dictionaries ListViews
class AuthorsList(ListView):
    model = models.Authors
    

class GenresList(ListView):
    model = models.Genres
    

class SeriesList(ListView):
    model = models.Series


class PublishersList(ListView):
    model = models.Publishers


# Dictionaries DeleteViews
class AuthorsDelete(DeleteView):
    model = models.Authors
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(DeleteView):
    model = models.Genres
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(DeleteView):
    model = models.Series
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(DeleteView):
    model = models.Publishers
    template_name = 'dictionaries/confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries UpdateViews
class AuthorsUpdate(UpdateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(UpdateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(UpdateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries CreateViews
class AuthorsCreate(CreateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(CreateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(CreateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'dictionaries/main_form.html'
    success_url = reverse_lazy('publishers-list')
