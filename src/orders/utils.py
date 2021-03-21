from cart import utils as cart_utils
from orders import models


def get_or_create_order(cart, initial=None):
    order, is_created = models.CustomerOrder.objects.get_or_create(
                customer_cart=cart,
                initial = initial
            )

    if is_created:
        order.save()
            
    return cart


def get_or_create_current_order(obj):
    customer = users_utils.get_current_customer(obj)
    initial={
                    'email': customer.email,
                    'phone': customer.extuserdata.phone,
                    'country': customer.extuserdata.country,
                    'city': customer.extuserdata.city,
                    'post_index': customer.extuserdata.post_index,
                    'address1': customer.extuserdata.address1,
                    'address2': customer.extuserdata.address2
                    }
    return get_or_create_order(cart_utils.get_current_cart(obj), initial)


def finish_order(obj):
    cart_utils.set_current_cart_pk(obj, None)
    cart_utils.update_current_cart_items_count(obj)