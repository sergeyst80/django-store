# Generated by Django 3.1.5 on 2021-01-30 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Country name')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Book genre name')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Book series name')),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Publisher name')),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dictionaries.countries', verbose_name="Publisher's country")),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name="Author's first name")),
                ('last_name', models.CharField(max_length=80, verbose_name="Author's last name")),
                ('date_of_birth', models.DateField(default=datetime.datetime(1900, 1, 1, 0, 0), verbose_name="Author's birthday")),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dictionaries.countries', verbose_name="Author's country")),
            ],
        ),
    ]
