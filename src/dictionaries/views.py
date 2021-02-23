from django.shortcuts import render
from . import models
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
# Dictionaries ListViews
class AuthorsList(ListView):
    model = models.Authors
    context_object_name = 'Authors'
    template_name = 'dict-list.html'
    

class GenresList(ListView):
    model = models.Genres
    context_object_name = 'Genres'
    template_name = 'dict-list.html'
    

class SeriesList(ListView):
    model = models.Series
    context_object_name = 'Series'
    template_name = 'dict-list.html'


class PublishersList(ListView):
    model = models.Publishers
    context_object_name = 'Publishers'
    template_name = 'dict-list.html'


# Dictionaries DetailViews
class AuthorsDetail(DetailView):
    model = models.Authors


class GenresDetail(DetailView):
    model = models.Genres


class SeriesDetail(DetailView):
    model = models.Series


class PublishersDetail(DetailView):
    model = models.Publishers


# Dictionaries DeleteViews
class AuthorsDelete(DeleteView):
    model = models.Authors
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(DeleteView):
    model = models.Genres
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(DeleteView):
    model = models.Series
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(DeleteView):
    model = models.Publishers
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries UpdateViews
class AuthorsUpdate(UpdateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(UpdateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(UpdateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('publishers-list')


# Dictionaries CreateViews
class AuthorsCreate(CreateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(CreateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(CreateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'main_form.html'
    success_url = reverse_lazy('publishers-list')
