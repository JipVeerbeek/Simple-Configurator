from .models import Configuration, ConfigurationLine
from rest_framework import serializers

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'product_id', 'address_id']

class ConfigurationLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationLine
        fields = ['id', 'product_question_article_id', 'configuration_id']
