# Generated by Django 5.0 on 2023-12-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0011_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]