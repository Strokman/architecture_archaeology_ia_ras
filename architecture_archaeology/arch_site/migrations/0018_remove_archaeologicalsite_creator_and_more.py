# Generated by Django 5.0 on 2024-02-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arch_site', '0017_alter_archaeologicalsite_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archaeologicalsite',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='archaeologicalsite',
            name='editor',
        ),
    ]