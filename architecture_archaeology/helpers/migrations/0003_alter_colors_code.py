# Generated by Django 4.2.7 on 2023-11-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='code',
            field=models.CharField(max_length=7, verbose_name='16-ный код'),
        ),
    ]
