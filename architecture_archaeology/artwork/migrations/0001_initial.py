# Generated by Django 4.2.7 on 2023-12-01 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helpers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('code', models.CharField(max_length=100)),
                ('preservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.preservation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
