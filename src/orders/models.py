from django.db import models
from django.contrib.auth import models as auth_models
from cart import models as cart_models

# Create your models here.
class OrderStatuses(models.Model):
    status = models.CharField(
        verbose_name='Статус заказа',
        max_length=50
    )

    def __str__(self):
        return self.status


class CustomerOrder(models.Model):
    customer_cart = models.OneToOneField(
        cart_models.CustomerCart,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='Корзина товаров'
    )

    status = models.ForeignKey(
        'OrderStatuses',
        verbose_name='Статус заказа',
        on_delete=models.PROTECT
    )

    phone = models.CharField(
        verbose_name='Телефон',
        max_length=80,
        blank=True,
        default=''
    )
    
    country = models.CharField(
        verbose_name='Страна',
        max_length=80,
        blank=True,
        default='Беларусь'
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=80,
        blank=True,
        default=''
    )

    post_index = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=80,
        blank=True,
        default=''
    )

    address1 = models.CharField(
        verbose_name='Адрес 1',
        max_length=120,
        blank=True,
        default=''
    )

    address2 = models.CharField(
        verbose_name='Адрес 2',
        max_length=120,
        blank=True,
        default=''
    )

    comments = models.TextField(
        verbose_name='Комментарий',
        max_length=1000,
        blank=True,
        default=''
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'Заказ #{self.pk}'
