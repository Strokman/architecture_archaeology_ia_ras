# Generated by Django 5.0 on 2024-02-01 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0029_building_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='creator',
        ),
    ]