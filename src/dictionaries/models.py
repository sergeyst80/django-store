from django.db import models
import datetime
# Create your models here.


class Countries(models.Model):
    name = models.CharField(
        verbose_name='Country name',
        max_length=80,
        unique=True)

    def __str__(self):
        return self.name


class Authors(models.Model):
    first_name = models.CharField(
        verbose_name='Author\'s first name',
        max_length=80)

    last_name = models.CharField(
        verbose_name='Author\'s last name',
        max_length=80)

    country = models.ForeignKey(
        'Countries',
        on_delete=models.PROTECT,
        verbose_name='Author\'s country',
        default=1)

    date_of_birth = models.DateField(
        verbose_name='Author\'s birthday',
        default=datetime.datetime(1900, 1, 1))

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.date_of_birth}, {self.country}'


class Series(models.Model):
    name = models.CharField(
        verbose_name='Book series name',
        max_length=80)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        verbose_name='Book genre name',
        max_length=80)

    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(
        verbose_name='Publisher name',
        max_length=80)

    country = models.ForeignKey(
        'Countries',
        on_delete=models.PROTECT,
        verbose_name='Publisher\'s country',
        default=1)

    def __str__(self):
        return f'{self.name}, {self.country}'
