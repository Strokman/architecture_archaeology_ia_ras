# Generated by Django 5.0 on 2024-04-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefact', '0003_alter_artefact_comment_alter_artefact_museum_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
