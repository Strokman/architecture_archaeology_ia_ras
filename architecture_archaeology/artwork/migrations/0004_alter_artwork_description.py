# Generated by Django 4.2.7 on 2023-12-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_alter_artwork_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]