from rest_framework import generics
from rest_framework.response import Response
from configurations.models import Configuration
from articles.models import Article
from products.models import ProductQuestion, ProductQuestionArticle
from articles.serializers import ArticleSerializer

from .models import Article
from .serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request, configuration_id, question_id, *args, **kwargs):
        configuration = Configuration.objects.get(id=configuration_id)
        product_question = ProductQuestion.objects.get(product=configuration.product, question=question_id)

        product_question_articles = ProductQuestionArticle.objects.filter(
            product_question=product_question
        ).values_list("article__id", flat=True)

        articles = Article.objects.filter(id__in=product_question_articles)
        serializer = ArticleSerializer(data=articles, many=True)
        serializer.is_valid()

        return Response(serializer.data)
