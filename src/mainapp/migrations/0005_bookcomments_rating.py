# Generated by Django 3.1.6 on 2021-03-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_bookcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomments',
            name='rating',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Рейтинг'),
        ),
    ]
