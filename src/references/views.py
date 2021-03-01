from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from references import models, forms


# Create your views here.
# Dictionaries ListViews
class AuthorsList(generic.ListView):
    model = models.Authors
    template_name = 'references/list_authors.html'
    

class GenresList(generic.ListView):
    model = models.Genres
    template_name = 'references/list_genres.html'
    

class SeriesList(generic.ListView):
    model = models.Series
    template_name = 'references/list_series.html'


class PublishersList(generic.ListView):
    model = models.Publishers
    template_name = 'references/list_publishers.html'


class AgeCategoriesList(generic.ListView):
    model = models.AgeCategories
    template_name = 'references/list_age_categories.html'


class BookFormatsList(generic.ListView):
    model = models.BookFormats
    template_name = 'references/list_book_formats.html'


# references generic.DeleteViews
class AuthorsDelete(generic.DeleteView):
    model = models.Authors
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(generic.DeleteView):
    model = models.Genres
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(generic.DeleteView):
    model = models.Series
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(generic.DeleteView):
    model = models.Publishers
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesDelete(generic.DeleteView):
    model = models.AgeCategories
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsDelete(generic.DeleteView):
    model = models.BookFormats
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('boo_formats-list')


# references UpdateViews
class AuthorsUpdate(generic.UpdateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(generic.UpdateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(generic.UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(generic.UpdateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesUpdate(generic.UpdateView):
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsUpdate(generic.UpdateView):
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')


# references CreateViews
class AuthorsCreate(generic.CreateView):
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(generic.CreateView):
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(generic.CreateView):
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesCreate(generic.CreateView):
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsCreate(generic.CreateView):
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')
