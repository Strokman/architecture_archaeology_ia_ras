# Generated by Django 5.0 on 2023-12-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0024_alter_building_year_max_alter_building_year_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='year_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='building',
            name='year_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='От'),
        ),
    ]