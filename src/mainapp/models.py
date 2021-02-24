from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.
class BookCard(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=80
    )
    
    picture = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='uploads/',
    )
    
    # upload = models.FileField()
    
    cost = models.DecimalField(
        verbose_name='Цена (BYN)',
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    
    authors = ManyToManyField(
        'dictionaries.Authors',
        verbose_name='Авторы книги'
    )

    series = ForeignKey(
        'dictionaries.Series',
        on_delete = models.PROTECT,
        null=True
    )

    genres = ManyToManyField(
        'dictionaries.Genres',
        verbose_name='Жанры'
    )

    year = models.SmallIntegerField(
        verbose_name='Год издания',
        blank=True
    )

    num_pages = models.SmallIntegerField(
        verbose_name='Количество страниц',
        blank=True
    )

    book_format = ForeignKey(
        'dictionaries.BookFormats',
        on_delete = models.PROTECT,
        null=True
    )

    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True
    )

    weight = models.SmallIntegerField(
        verbose_name='Вес (гр)',
        blank=True
    )

    age_category = ForeignKey(
        'dictionaries.AgeCategories',
        on_delete = models.PROTECT,
        null=True
    )

    publisher = ForeignKey(
        'dictionaries.Publishers',
        on_delete = models.PROTECT,
        null=True
    )

    qty = models.SmallIntegerField(
        verbose_name='Наличие (шт)',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Доступен к заказу',
        default=False
    )

    rating = models.FloatField(
        verbose_name='Рейтинг',
        default=0.0   
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания карточки',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Дата изменения карточки',
        auto_now=True
    )