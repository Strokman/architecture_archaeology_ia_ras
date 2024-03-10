# Generated by Django 5.0 on 2024-03-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archaeologicalsite',
            name='preservation',
            field=models.CharField(choices=[('P', 'сохранился'), ('D', 'не сохранился')], default='P', max_length=100, verbose_name='Сохранность'),
            preserve_default=False,
        ),
    ]
