from django.db import models
import datetime
# Create your models here.


class Authors(models.Model):
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия книг',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        verbose_name='Жанр книги',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(
        verbose_name='Название издателя',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name
