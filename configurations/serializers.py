from .models import Configuration
from rest_framework import serializers

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'product_id', 'adress_id']
