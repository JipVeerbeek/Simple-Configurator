# Generated by Django 5.0.4 on 2024-04-30 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0007_rename_product_question_article_configuration_line_product_question_article_id'),
        ('products', '0006_product_question_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Configuration_line',
            new_name='ConfigurationLine',
        ),
    ]
