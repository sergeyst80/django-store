from . import models
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
class AuthorsList(ListView):
    model = models.Authors


class AuthorsDetail(DetailView):
    model = models.Authors


class AuthorsDelete(DeleteView):
    model = models.Authors
    success_url = reverse_lazy('authors-list')


class AuthorsUpdate(UpdateView):
    model = models.Authors
    fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('authors-list')



class AuthorsCreate(CreateView):
    model = models.Authors
    fields = ['first_name', 'last_name', 'country', 'date_of_birth']
    success_url = reverse_lazy('authors-list')
