# Generated by Django 5.0 on 2024-01-18 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_gaschromatographymassspectrometry_site_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gaschromatographymassspectrometry',
            name='site',
        ),
        migrations.RemoveField(
            model_name='infraredramanmicroscopy',
            name='site',
        ),
        migrations.RemoveField(
            model_name='rfa',
            name='site',
        ),
        migrations.RemoveField(
            model_name='roentgen',
            name='site',
        ),
        migrations.RemoveField(
            model_name='scanningelectronmicroscopy',
            name='site',
        ),
    ]
