from rest_framework import serializers

from .models import Product, ProductQuestion, ProductQuestionArticle


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"]


class ProductQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestion
        fields = ["id", "product", "question"]


class ProductQuestionArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestionArticle
        fields = ["id", "product_question", "article", "price"]
