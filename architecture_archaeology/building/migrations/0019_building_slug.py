# Generated by Django 4.2.7 on 2023-12-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0018_remove_building_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='slug',
            field=models.SlugField(default='test-slug-kek'),
            preserve_default=False,
        ),
    ]