# Generated by Django 5.0.4 on 2024-05-17 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0011_remove_address_postal_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='configuration',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='configurationline',
            old_name='configuration_id',
            new_name='configuration',
        ),
        migrations.RenameField(
            model_name='configurationline',
            old_name='product_question_article_id',
            new_name='product_question_article',
        ),
    ]
