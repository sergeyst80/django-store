from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from references import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
# Dictionaries ListViews
class AuthorsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_authors'
    model = models.Authors
    template_name = 'references/list_authors.html'
    

class GenresList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_genres'
    model = models.Genres
    template_name = 'references/list_genres.html'
    

class SeriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_series'
    model = models.Series
    template_name = 'references/list_series.html'


class PublishersList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_publishers'
    model = models.Publishers
    template_name = 'references/list_publishers.html'


class AgeCategoriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_agecategories'
    model = models.AgeCategories
    template_name = 'references/list_age_categories.html'


class BookFormatsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_bookformats'
    model = models.BookFormats
    template_name = 'references/list_book_formats.html'


# references generic.DeleteViews
class AuthorsDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_authors'
    model = models.Authors
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('authors-list')


class GenresDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_genres'
    model = models.Genres
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('genres-list')


class SeriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_series'
    model = models.Series
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('series-list')


class PublishersDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_publishers'
    model = models.Publishers
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_agecategories'
    model = models.AgeCategories
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_bookformats'
    model = models.BookFormats
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('boo_formats-list')


# references UpdateViews
class AuthorsUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_bookformats'
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')


# references CreateViews
class AuthorsCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_authors'
    model = models.Authors
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors-list')


class GenresCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_genres'
    model = models.Genres
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres-list')


class SeriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series-list')


class PublishersCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_publishers'
    model = models.Publishers
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers-list')


class AgeCategoriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_agecategories'
    model = models.AgeCategories
    form_class = forms.AgeCategoriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('age_categories-list')


class BookFormatsCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_bookformats'
    model = models.BookFormats
    form_class = forms.BookFormatsForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('book_formats-list')
