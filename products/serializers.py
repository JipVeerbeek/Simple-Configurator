from .models import Product, ProductQuestion, ProductQuestionArticle
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class ProductQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestion
        fields = ['id', 'product', 'question']


class ProductQuestionArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestionArticle
        fields = ['id', 'product_question', 'article', 'price']
