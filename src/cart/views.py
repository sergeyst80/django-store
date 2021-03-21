from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import models as auth_models

from cart import models as cart_models
from mainapp import models as main_models
from users import utils as users_utils
from cart import utils as cart_utils
from orders import models as orders_models, utils as orders_utils

# Create your views here.
class AddToCartView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        book_pk = self.request.GET.get('book')

        if book_pk:
            current_cart = cart_utils.get_or_create_current_cart(self)
            
            cart_utils.add_item_in_current_cart(self, main_models.BookCard.objects.get(pk=book_pk))

        return self.request.GET.get('next')


class CartView(generic.DetailView):
    model = cart_models.CustomerCart
    template_name = 'cart/view_cart.html'

    def get_object(self):
        current_cart = cart_utils.get_current_cart(self)
        return current_cart


class DeleteFromCart(generic.DeleteView):
    model = cart_models.BooksInCart
    template_name = 'cart/delete_from_cart.html'
    success_url = reverse_lazy('cart:view-cart')

    def delete(self, request, *args, **kwargs):
        obj = super().delete(request)
        cart_utils.update_current_cart_items_count(self)
        return obj


class UpdateCart(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        action = cart_utils.update_current_cart(self)

        if action =='checkout':
            cart_utils.check_current_cart_owner(self)
            return reverse('orders:create-order')
        else:
            return reverse('cart:view-cart')
