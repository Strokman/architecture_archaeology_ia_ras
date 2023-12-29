# Generated by Django 4.2.7 on 2023-12-20 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_alter_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='file.filetype'),
            preserve_default=False,
        ),
    ]