# Generated by Django 5.0 on 2024-04-10 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0010_alter_frescoe_code_alter_indoorartwork_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frescoe',
            options={'ordering': ('code', 'id'), 'verbose_name': 'Индивидуальная фреска', 'verbose_name_plural': 'Индивидуальные фрески'},
        ),
        migrations.AlterModelOptions(
            name='indoorartwork',
            options={'ordering': ('code', 'id'), 'verbose_name': 'Изображение в постройке', 'verbose_name_plural': 'Изображения в постройке'},
        ),
    ]
