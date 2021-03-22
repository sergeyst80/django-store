# Generated by Django 3.1.6 on 2021-03-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210320_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Телефон'),
        ),
    ]