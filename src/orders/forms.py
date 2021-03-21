from django import forms
from orders import models


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = models.CustomerOrder
        fields = ('email', 'phone', 'country', 'city', 'post_index', 'address1', 'address2', 'additional')


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = models.CustomerOrder
        fields = ('phone', 'country', 'city', 'post_index', 'address1', 'address2')