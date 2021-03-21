from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from mainapp import models as main_models
from users import utils as users_utils
from storemanager import forms

# Create your views here.
class CreateBookCardView(users_utils.MyLoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'mainapp.add_bookcard'
    model = main_models.BookCard
    template_name = 'storemanager/create_bookcard.html'
    form_class = forms.BookCardForm
    success_url = reverse_lazy('manager:create-bookcard')


class UpdateBookCardView(users_utils.MyLoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'mainapp.change_bookcard'
    model = main_models.BookCard
    template_name = 'storemanager/update_bookcard.html'
    form_class = forms.BookCardForm
    success_url = reverse_lazy('manager:update-bookcard')


class ListBookCardsView(users_utils.MyLoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'mainapp.view_bookcard'
    paginate_by = 20
    model = main_models.BookCard
    template_name = 'storemanager/list_bookcards.html'


class DetailBookCardView(generic.DetailView):
    model = main_models.BookCard
    template_name = "storemanager/detail_bookcard.html"


