# Generated by Django 3.1.6 on 2021-03-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210319_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='email',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='E-mail'),
        ),
    ]
