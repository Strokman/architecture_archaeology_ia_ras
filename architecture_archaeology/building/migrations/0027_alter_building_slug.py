# Generated by Django 5.0 on 2023-12-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0026_alter_building_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
    ]