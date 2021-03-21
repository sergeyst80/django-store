from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse

from orders import models, forms, utils
from users import utils as users_utils
from cart import models as cart_models, utils as cart_utils


# Create your views here.
class CreateOrderView(generic.CreateView):
    model = models.CustomerOrder
    form_class = forms.CreateOrderForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        customer = users_utils.get_current_customer(self)
        
        if customer:
            form = forms.CreateOrderForm(
                initial={
                    'email': customer.email,
                    'phone': customer.extuserdata.phone,
                    'country': customer.extuserdata.country,
                    'city': customer.extuserdata.city,
                    'post_index': customer.extuserdata.post_index,
                    'address1': customer.extuserdata.address1,
                    'address2': customer.extuserdata.address2
                    }
                )
            
            context['form'] = form
        
        return context

    def get_success_url(self):
        utils.finish_order(self)
        return super().get_success_url()

    def get_object(self, queryset=None):
        return models.CustomerOrder.objects.create(pk=cart_utils.get_current_cart_pk(self))


class ListOrdersView(users_utils.MyLoginRequiredMixin, generic.ListView):
    paginate_by = 20
    model = models.CustomerOrder
    template_name = 'orders/view_orders.html'
    ordering = '-pk'

    def get_queryset(self):
        customer = users_utils.get_current_customer(self)

        if not customer.is_staff:
            queryset = self.model.objects.filter(customer_cart__customer=customer)
        else:
            queryset = super().get_queryset()

        return queryset


class DetailOrderView(users_utils.MyLoginRequiredMixin, generic.DetailView):
    model = models.CustomerOrder
    template_name = 'orders/detail_order.html'


class UpdateOrderView(users_utils.MyLoginRequiredMixin, generic.UpdateView):
    model = models.CustomerOrder
    form_class = forms.UpdateOrderForm
    permission_required = 'orders.change_customerorder'
    template_name = 'orders/update_order.html'
    # success_url = reverse_lazy('orders:update-order')
    def get_object(self, queryset=None):
        obj = super().get_object()
        user = users_utils.get_current_customer(self)

        if user.is_staff or user == obj.customer_cart.customer:
            return obj
        else:
            return None 

    def get_success_url(self):
        obj = self.get_object()
        if obj:
            return reverse('orders:update-order', args=[obj.pk])
        else:
            return reverse('homepage')

class UpdateOrderCartView(users_utils.MyLoginRequiredMixin, generic.RedirectView):
    # permission_required = 'orders.change_customerorder'

    def get_redirect_url(self, *args, **kwargs):
        pk = self.request.GET.get('btn')
        
        if pk:
            cart_utils.update_cart(pk, self)
            return reverse('orders:update-order', args=[pk])
        else:
            return reverse('homepage')


class SendOrderCommentView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        comment = self.request.POST.get('comment')
        pk = self.request.POST.get('pk')
        rating = self.request.POST.get('rating')

        if comment and pk:
            comments = models.OrderComments.objects.create(
                customer_order=models.CustomerOrder.objects.filter(pk=pk).first(),
                user=users_utils.get_current_customer(self),
                comment=comment,
                rating = rating
            )
            comments.save()
        
        return reverse('orders:detail-order', args=[pk])


class CancelOrderView(users_utils.MyLoginRequiredMixin, generic.detail.SingleObjectMixin, generic.TemplateView):
    template_name = 'orders/cancel_order.html'
    model = models.CustomerOrder

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data()
        context['object'] = super().get_object()
        return context
