# Generated by Django 5.0 on 2024-02-01 11:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0032_remove_building_creator_remove_building_editor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='creator_core.models.slug_mixin+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='building',
            name='editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='editor_core.models.slug_mixin+', to=settings.AUTH_USER_MODEL),
        ),
    ]
