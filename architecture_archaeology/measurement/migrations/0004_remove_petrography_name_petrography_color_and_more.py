# Generated by Django 5.0 on 2024-04-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0003_delete_indextable'),
        ('measurement', '0003_remove_gaschromatographymassspectrometry_site_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petrography',
            name='name',
        ),
        migrations.AddField(
            model_name='petrography',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='helpers.color', verbose_name='Цвета'),
        ),
        migrations.AlterField(
            model_name='petrography',
            name='binder_description',
            field=models.TextField(blank=True, null=True, verbose_name='Вяжущее описание'),
        ),
        migrations.AlterField(
            model_name='petrography',
            name='binder_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вяжущее название'),
        ),
        migrations.AlterField(
            model_name='petrography',
            name='filler_contains',
            field=models.ManyToManyField(blank=True, null=True, to='helpers.filler', verbose_name='Заполнитель состав'),
        ),
        migrations.AlterField(
            model_name='petrography',
            name='filler_description',
            field=models.TextField(blank=True, null=True, verbose_name='Заполнитель описание'),
        ),
    ]
