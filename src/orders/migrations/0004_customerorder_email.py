# Generated by Django 3.1.6 on 2021-03-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210318_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='email',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='e-mail'),
        ),
    ]
