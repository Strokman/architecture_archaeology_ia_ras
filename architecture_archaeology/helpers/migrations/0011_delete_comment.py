# Generated by Django 4.2.7 on 2023-12-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0010_comment_building_comment_site'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]