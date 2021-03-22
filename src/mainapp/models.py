from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth import models as auth_models


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
        verbose_name='Серия',
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
        null=True,
        default=''
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


class BookComments(models.Model):
    bookcard = models.ForeignKey(
        'BookCard',
        on_delete=models.CASCADE,
        verbose_name='Книга',
        related_name='comments',
        blank=False,
        null=True
    )

    user = models.ForeignKey(
        auth_models.User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='book_comments',
        blank=False,
        null=True
    )

    comment = models.TextField(
        verbose_name='Комментарий',
        max_length=1000,
        blank=True,
        default=''
    )

    rating = models.FloatField(
        verbose_name='Рейтинг',
        default=None,
        null=True,
        blank=True  
    )

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f'Комментарий #{self.pk} пользователя {self.user.username} к книге {self.bookcard.pk}'
