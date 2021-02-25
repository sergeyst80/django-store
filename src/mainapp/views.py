from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mainapp import models


# Create your views here.
class HomePage(generic.TemplateView):
    template_name = "mainapp/homepage.html"