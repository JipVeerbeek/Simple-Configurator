# Generated by Django 5.0.4 on 2024-04-30 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0003_alter_adress_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="adress",
            options={"verbose_name_plural": "Adresses"},
        ),
    ]
