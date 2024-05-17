from rest_framework import generics
from .models import Article
from products.models import ProductQuestion, ProductQuestionArticle
from .serializers import ArticleSerializer
from products.serializers import ProductQuestionSerializer, ProductQuestionArticleSerializer
from configurations.models import Configuration


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # todo: get_queryset is only used for fetching the BASE queryset. You
        #       are doing way to much here. Move related logic to `get`.
        configuration_id = self.kwargs.get('configuration_id')
        question_id = self.kwargs.get('question_id')
        configuration = Configuration.objects.get(id=configuration_id)

        product_question = ProductQuestion.objects.get(product_id=configuration.product_id, question_id=question_id)
        product_question_serializer = ProductQuestionSerializer(product_question)
        product_question_id = product_question_serializer.data['id']

        product_question_article = ProductQuestionArticle.objects.filter(product_question_id=product_question_id)
        product_question_article_serializer = ProductQuestionArticleSerializer(product_question_article, many=True)

        queryset = []

        for item in product_question_article_serializer.data:
            article_id = item['article_id']

            article = Article.objects.get(id=article_id)
            queryset.append(article)

        return queryset
