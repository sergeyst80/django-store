from cart import models
from users import utils as users_utils


def get_current_cart_pk(obj):
    return obj.request.session.get('current_cart_pk')


def set_current_cart_pk(obj, pk):
    obj.request.session['current_cart_pk'] = pk


def get_cart(pk):
    return models.CustomerCart.objects.filter(pk=pk).first()


def get_current_cart(obj):
    return get_cart(get_current_cart_pk(obj))


def get_or_create_cart(obj, pk, customer):
    cart, is_created = models.CustomerCart.objects.get_or_create(
                pk=pk,
                defaults={'customer': customer}
            )

    if is_created:
        cart.save()
        set_current_cart_pk(obj, cart.pk)
    
    return cart


def get_or_create_current_cart(obj):
    return get_or_create_cart(obj, get_current_cart_pk(obj), users_utils.get_current_customer(obj))


def check_cart_owner(current_cart, current_customer):
    if current_cart.customer != current_customer:
        current_cart.customer = current_customer
        current_cart.save()


def check_current_cart_owner(obj):
    cart = get_current_cart(obj)
    customer = users_utils.get_current_customer(obj)
    check_cart_owner(cart, customer)


def update_current_cart_items_count(obj):
    current_cart = get_current_cart(obj)
    
    if current_cart:
        obj.request.session['books_in_cart'] = current_cart.get_books_count
    else:
        obj.request.session['books_in_cart'] = None


def add_item_in_cart(cart, item):
    book_in_cart, created = models.BooksInCart.objects.get_or_create(
        customer_cart=cart,
        book_card=item,
        defaults={'qty': 1, 'price': item.cost}
    )

    if not created:
        book_in_cart.qty += 1
        book_in_cart.save()
    

def add_item_in_current_cart(obj, item):
    current_cart = get_current_cart(obj)
    add_item_in_cart(current_cart, item)
    update_current_cart_items_count(obj)


def update_cart(pk, obj):
    action = None
    cart = get_cart(pk)

    if not cart:
        return 

    cart_items = cart.books_in_cart.all()
    items = obj.request.GET.items()

    for item, value in obj.request.GET.items():

        if item =='btn':
            action = value
            continue

        cart_item = cart_items.get(pk=item)

        if item and int(value) > 0:
            cart_item.qty = value
            cart_item.save()
        else:
            cart_item.delete()

    return action


def update_current_cart(obj):
    action = None
    current_cart = get_current_cart(obj)

    if not current_cart:
        return 

    cart_items = current_cart.books_in_cart.all()

    for item, value in obj.request.GET.items():

        if item =='btn':
            action = value
            continue

        cart_item = cart_items.get(pk=item)

        if item and int(value) > 0:
            cart_item.qty = value
            cart_item.save()
        else:
            cart_item.delete()

    update_current_cart_items_count(obj)
    return action
