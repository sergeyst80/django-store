from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mainapp import models


# Create your views here.
class HomePage(generic.TemplateView):
    model = models.BookCard
    template_name = "mainapp/homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.model.objects.all().order_by('-pk')[0:9]
        context['objects'] = books
        return context


class BooksCatalog(generic.ListView):
    paginate_by = 3
    model = models.BookCard
    ordering = ['-pk']
    template_name = "mainapp/books_catalog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_books = self.model.objects.all().order_by('-pk')[0:9]
        context['new_books'] = new_books
        return context
