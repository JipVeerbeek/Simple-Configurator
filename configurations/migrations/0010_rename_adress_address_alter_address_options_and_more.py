# Generated by Django 5.0.4 on 2024-05-06 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0009_alter_configuration_adress_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Adress",
            new_name="Address",
        ),
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Addresses"},
        ),
        migrations.RenameField(
            model_name="address",
            old_name="adress",
            new_name="address",
        ),
        migrations.RenameField(
            model_name="configuration",
            old_name="adress_id",
            new_name="address_id",
        ),
    ]
