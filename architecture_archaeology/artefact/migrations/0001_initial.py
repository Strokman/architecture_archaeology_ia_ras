# Generated by Django 5.0 on 2024-03-06 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arch_site', '0001_initial'),
        ('helpers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('year_min', models.IntegerField(blank=True, null=True, verbose_name='Датировка от:')),
                ('year_max', models.IntegerField(blank=True, help_text='Даты до н.э. должны быть отрицательными', null=True, verbose_name='до:')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('code', models.CharField(max_length=100, verbose_name='Шифр')),
                ('find_date_from', models.IntegerField(blank=True, null=True, verbose_name='Год находки от:')),
                ('find_date_to', models.IntegerField(blank=True, null=True, verbose_name='до:')),
                ('comment', models.TextField(null=True, verbose_name='Примечание')),
                ('square_number', models.CharField(max_length=255, null=True, verbose_name='Номер квадрата/участка/пласта по археологическим отчетам')),
                ('museum_code', models.CharField(max_length=255, verbose_name='Музейный шифр')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creator+', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='editor+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arch_site.archaeologicalsite', verbose_name='Памятник')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helpers.storage', verbose_name='Место хранения')),
            ],
            options={
                'verbose_name': 'Находка',
                'verbose_name_plural': 'Находки',
            },
        ),
    ]
