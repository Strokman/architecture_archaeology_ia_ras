# Generated by Django 5.0 on 2024-04-10 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0005_alter_element_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='element',
            options={'ordering': ('name',)},
        ),
    ]
