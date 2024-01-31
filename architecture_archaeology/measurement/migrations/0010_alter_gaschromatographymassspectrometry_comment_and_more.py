# Generated by Django 5.0 on 2024-01-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0009_alter_petrography_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaschromatographymassspectrometry',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='infraredramanmicroscopy',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='rfa',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='roentgen',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='scanningelectronmicroscopy',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
    ]
