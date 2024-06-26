# Generated by Django 5.0 on 2024-04-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_remove_file_lotok'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('filename', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=255)),
                ('original_name', models.CharField(max_length=255)),
                ('object_storage_key', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ('id',),
            },
        ),
    ]
