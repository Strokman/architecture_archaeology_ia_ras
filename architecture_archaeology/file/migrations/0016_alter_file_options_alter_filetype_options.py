# Generated by Django 5.0 on 2024-01-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0015_file_gc_ms_file_infrared_ramanov_file_roentgen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('type',), 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='filetype',
            options={'ordering': ('name',), 'verbose_name': 'Тип файла', 'verbose_name_plural': 'Типы файлов'},
        ),
    ]