# Generated by Django 5.0.4 on 2024-04-30 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0005_alter_product_question_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("middle_name", models.CharField(max_length=100, null=True)),
                ("second_name", models.CharField(max_length=100)),
                ("adress", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(default="draft", max_length=100)),
                (
                    "adress_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configurations.adress",
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
