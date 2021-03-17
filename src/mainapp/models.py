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
        null=True,
        blank=True
    )
    
    cost = models.DecimalField(
        verbose_name='Цена (BYN)',
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    
    authors = ManyToManyField(
        'references.Authors',
        verbose_name='Авторы книги',
        blank=True
    )

    series = ForeignKey(
        'references.Series',
        on_delete = models.PROTECT,
        blank=True,
        null=True
    )

    genres = ManyToManyField(
        'references.Genres',
        verbose_name='Жанры',
        blank=True
    )

    year = models.SmallIntegerField(
        verbose_name='Год издания',
        default=1900
    )

    num_pages = models.SmallIntegerField(
        verbose_name='Количество страниц',
        default=0
    )

    book_format = ForeignKey(
        'references.BookFormats',
        on_delete = models.PROTECT,
        blank=True,
        null=True
    )

    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True,
        null=True
    )

    weight = models.SmallIntegerField(
        verbose_name='Вес (гр)',
        default=0
    )

    age_category = ForeignKey(
        'references.AgeCategories',
        on_delete = models.PROTECT,
        blank=True,
        null=True
    )

    publisher = ForeignKey(
        'references.Publishers',
        on_delete = models.PROTECT,
        blank=True,
        null=True
    )

    qty = models.SmallIntegerField(
        verbose_name='Наличие (шт)',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Доступен к заказу',
        default=True
    )

    rating = models.FloatField(
        verbose_name='Рейтинг',
        default=0.0  
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def get_authors(self):
        return "\n".join([p.name for p in self.authors.all()])
    
    def get_genres(self):
        return "\n".join([p.name for p in self.genres.all()])

    def __str__(self):
        return self.name
