from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mainapp import models as mainapp_models


# Create your views here.
class HomePage(generic.TemplateView):
    model = mainapp_models.BookCard
    template_name = "mainapp/homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = mainapp_models.BookCard.objects.all()
        cards = []
        for book in books :
            cards.append([book, book.get_authors(), book.get_genres()])
        context['objects'] = cards
        return context