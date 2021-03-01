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
        books = mainapp_models.BookCard.objects.all().order_by('-pk')[0:9]
        context['objects'] = books
        return context