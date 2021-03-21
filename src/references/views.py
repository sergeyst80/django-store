from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from references import models, forms
from users.utils import MyLoginRequiredMixin
# Create your views here.

# Dictionaries ListViews
class AuthorsList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_authors'
    model = models.Authors
    template_name = 'references/list_authors.html'
    

class GenresList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_genres'
    model = models.Genres
    template_name = 'references/list_genres.html'
    

class SeriesList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_series'
    model = models.Series
    template_name = 'references/list_series.html'


class PublishersList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_publishers'
    model = models.Publishers
    template_name = 'references/list_publishers.html'


class AgeCategoriesList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_agecategories'
    model = models.AgeCategories
    template_name = 'references/list_age_categories.html'


class BookFormatsList(MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    permission_required = 'references.view_bookformats'
    model = models.BookFormats
    template_name = 'references/list_book_formats.html'


# references generic.DeleteViews
class AuthorsDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_authors'
    model = models.Authors
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_genres'
    model = models.Genres
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_series'
    model = models.Series
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_publishers'
    model = models.Publishers
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_agecategories'
    model = models.AgeCategories
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsDelete(MyLoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'references.delete_bookformats'
    model = models.BookFormats
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('boo_formats-list')


# references UpdateViews
class AuthorsUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsUpdate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'references.change_bookformats'
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')


# references CreateViews
class AuthorsCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsCreate(MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'references.add_bookformats'
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')
