# Generated by Django 5.0.4 on 2024-04-30 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0006_configuration_line_product_question_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration_line',
            old_name='product_question_article',
            new_name='product_question_article_id',
        ),
    ]