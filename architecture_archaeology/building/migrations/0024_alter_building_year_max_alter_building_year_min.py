# Generated by Django 5.0 on 2023-12-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0023_remove_buildingpart_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='year_max',
            field=models.IntegerField(null=True, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='building',
            name='year_min',
            field=models.IntegerField(null=True, verbose_name='От'),
        ),
    ]
