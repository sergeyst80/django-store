from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.
class BookCard(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=80,
        unique=True
    )
    
    picture = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='uploads/'
    )
    
    # upload = models.FileField()
    
    cost = models.DecimalField(
        verbose_name='Цена (BYN)',
        max_digits=10,
        decimal_places=2
    )
    
    authors = ManyToManyField(
        'dictionaries.Authors',
        verbose_name='Авторы книги'
    )

    series = ForeignKey(
        'dictionaries.Series',
        on_delete = models.PROTECT,
        default = 1
    )

    genres = ManyToManyField(
        'dictionaries.Genres',
        verbose_name='Жанры'
    )

