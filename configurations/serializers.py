from .models import Configuration, ConfigurationLine
from rest_framework import serializers

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'product', 'address']

class ConfigurationLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationLine
        fields = ['id', 'product_question_article', 'configuration']


class PriceSerializer(serializers.Serializer):
    
    price = serializers.IntegerField()
