# Generated by Django 5.0.4 on 2024-05-06 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0008_rename_configuration_line_configurationline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='adress_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.adress'),
        ),
    ]
