# Generated by Django 3.1.6 on 2021-03-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210319_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuserdata',
            name='phone',
            field=models.CharField(max_length=80, verbose_name='Телефон'),
        ),
    ]
