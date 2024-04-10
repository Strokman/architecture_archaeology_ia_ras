# Generated by Django 5.0 on 2024-04-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0004_element'),
        ('measurement', '0008_petrography_artefact_petrography_frescoe_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gaschromatographymassspectrometry',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'Газовая хроматография и масс-спектрометрия', 'verbose_name_plural': 'Газовая хроматография и масс-спектрометрия'},
        ),
        migrations.AlterModelOptions(
            name='infraredramanmicroscopy',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'ИК и рамановская спектроскопия', 'verbose_name_plural': 'ИК и рамановская спектроскопия'},
        ),
        migrations.AlterModelOptions(
            name='petrography',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'Петрография', 'verbose_name_plural': 'Петрография'},
        ),
        migrations.AlterModelOptions(
            name='rfa',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'РФА', 'verbose_name_plural': 'РФА'},
        ),
        migrations.AlterModelOptions(
            name='roentgen',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'Рентгенофазовый и рентгеноструктурный анализ', 'verbose_name_plural': 'Рентгенофазовый и рентгеноструктурный анализы'},
        ),
        migrations.AlterModelOptions(
            name='scanningelectronmicroscopy',
            options={'ordering': ('created_at', 'id'), 'verbose_name': 'Растровая электронная микроскопия', 'verbose_name_plural': 'Растровая электронная микроскопия'},
        ),
        migrations.RemoveField(
            model_name='rfa',
            name='elements',
        ),
        migrations.AddField(
            model_name='rfa',
            name='elements',
            field=models.ManyToManyField(blank=True, to='helpers.element', verbose_name='Элементы периодической таблицы'),
        ),
    ]