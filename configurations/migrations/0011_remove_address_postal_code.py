# Generated by Django 5.0.4 on 2024-05-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0010_rename_adress_address_alter_address_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="postal_code",
        ),
    ]
