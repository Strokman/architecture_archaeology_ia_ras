# Generated by Django 5.0 on 2024-04-24 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0014_frescoe_building_indoorartwork_building_and_more'),
        ('building', '0003_alter_building_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frescoe',
            name='building_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='building.buildingpart', verbose_name='Элемент постройки'),
        ),
        migrations.AlterField(
            model_name='indoorartwork',
            name='building_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='building.buildingpart', verbose_name='Элемент постройки'),
        ),
    ]
