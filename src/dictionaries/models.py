from django.db import models
import datetime
# Create your models here.


class Authors(models.Model):
    name = models.CharField(
        verbose_name='Author\'s first name',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name='Book series name',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        verbose_name='Book genre name',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(
        verbose_name='Publisher name',
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.name
