# Generated by Django 4.2.7 on 2023-12-20 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_filetype_alter_file_file_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_type',
            new_name='type',
        ),
    ]
