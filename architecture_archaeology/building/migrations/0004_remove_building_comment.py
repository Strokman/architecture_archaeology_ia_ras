# Generated by Django 4.2.7 on 2023-12-01 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_building_comment_building_date_building_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='comment',
        ),
    ]