# Generated by Django 5.0 on 2024-04-30 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_alter_file_options_remove_file_type_foto_artefact_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileType',
        ),
    ]
