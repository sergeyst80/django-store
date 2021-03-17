from django.db import models
from django.contrib.auth import models as auth_models
from mainapp import models as main_models


# Create your models here.
class CustomerCart(models.Model):
    customer = models.ForeignKey(
        auth_models.User,
        on_delete=models.PROTECT,
        verbose_name='Покупатель',
        related_name='cutomer_carts',
        blank=False,
        null=True
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    @property
    def get_books_count(self):
        count = 0
        
        for book in self.books_in_cart.all():
            count += book.qty
        
        return count

    @property
    def get_total_price(self):
        total_price = 0
        
        for book in self.books_in_cart.all():
            total_price += book.get_total_price
        
        return total_price

    def __str__(self):
        return f'Корзина #{self.pk}'

class BooksInCart(models.Model):
    customer_cart = models.ForeignKey(
        'CustomerCart',
        on_delete=models.PROTECT,
        verbose_name='Корзина товаров',
        related_name='books_in_cart',
        blank=False,
        null=True   
    )

    book_card = models.ForeignKey(
        main_models.BookCard,
        on_delete=models.PROTECT,
        verbose_name='Книга',
        related_name='book_cards'
    )

    qty = models.IntegerField(
        verbose_name='Количество'
    )

    price = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=5,
        decimal_places=2
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    @property
    def get_total_price(self):
        return self.qty * self.price

    def __str__(self):
        return f'{self.book_card}, {self.qty} шт., {self.price} BYN'
