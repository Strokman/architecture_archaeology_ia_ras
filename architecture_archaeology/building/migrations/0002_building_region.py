# Generated by Django 4.2.7 on 2023-12-01 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0001_initial'),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helpers.region'),
        ),
    ]