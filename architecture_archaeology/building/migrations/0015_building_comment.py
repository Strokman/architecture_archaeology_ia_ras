# Generated by Django 4.2.7 on 2023-12-12 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0009_remove_comment_building'),
        ('building', '0014_building_age_max_building_age_min_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buildings', to='helpers.comment'),
        ),
    ]