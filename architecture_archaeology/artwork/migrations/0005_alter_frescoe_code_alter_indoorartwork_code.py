# Generated by Django 5.0 on 2024-03-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0004_alter_frescoe_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frescoe',
            name='code',
            field=models.IntegerField(default=1, verbose_name='Шифр'),

        ),
        migrations.AlterField(
            model_name='indoorartwork',
            name='code',
            field=models.IntegerField(default=1, verbose_name='Шифр'),
 
        ),
    ]