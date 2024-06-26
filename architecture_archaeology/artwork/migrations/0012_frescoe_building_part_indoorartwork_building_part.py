# Generated by Django 5.0 on 2024-04-10 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0011_alter_frescoe_options_alter_indoorartwork_options'),
        ('building', '0003_alter_building_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='frescoe',
            name='building_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='building.buildingpart', verbose_name='Элемент постройки'),
        ),
        migrations.AddField(
            model_name='indoorartwork',
            name='building_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='building.buildingpart', verbose_name='Элемент постройки'),
        ),
    ]
