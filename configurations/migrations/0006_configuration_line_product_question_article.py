# Generated by Django 5.0.4 on 2024-04-30 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0005_alter_adress_middle_name_configuration_line'),
        ('products', '0006_product_question_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration_line',
            name='product_question_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_question_article'),
        ),
    ]
