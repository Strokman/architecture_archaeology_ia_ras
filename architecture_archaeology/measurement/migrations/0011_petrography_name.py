# Generated by Django 5.0 on 2024-04-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0010_remove_scanningelectronmicroscopy_elements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='petrography',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
