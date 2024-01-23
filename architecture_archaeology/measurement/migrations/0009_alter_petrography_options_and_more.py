# Generated by Django 5.0 on 2024-01-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_petrography'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petrography',
            options={'verbose_name': 'Петрография', 'verbose_name_plural': 'Петрография'},
        ),
        migrations.RemoveField(
            model_name='gaschromatographymassspectrometry',
            name='description',
        ),
        migrations.RemoveField(
            model_name='infraredramanmicroscopy',
            name='description',
        ),
        migrations.RemoveField(
            model_name='petrography',
            name='description',
        ),
        migrations.RemoveField(
            model_name='rfa',
            name='description',
        ),
        migrations.RemoveField(
            model_name='roentgen',
            name='description',
        ),
        migrations.RemoveField(
            model_name='scanningelectronmicroscopy',
            name='description',
        ),
        migrations.AddField(
            model_name='petrography',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
    ]
