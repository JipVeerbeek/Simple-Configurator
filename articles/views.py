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
        #haalt ids op uit url
        configuration_id = self.kwargs.get('configuration_id')
        question_id = self.kwargs.get('question_id')

        # todo: captain obvious, think I can't read common code? ;)
        #       in other words, don't overuse comments, they don't add anything here.
        #       Also, comments should be in english.
        #configuration ophalen
        configuration = Configuration.objects.get(id=configuration_id)

        #haalt product question op waar je de articles van gaat krijgen
        product_question = ProductQuestion.objects.get(product_id=configuration.product_id, question_id=question_id)
        #serialize
        product_question_serializer = ProductQuestionSerializer(product_question)
        #pakt prod question id
        product_question_id = product_question_serializer.data['id']

        #haalt product question article(s) op
        product_question_article = ProductQuestionArticle.objects.filter(product_question_id=product_question_id)
        #serialize
        product_question_article_serializer = ProductQuestionArticleSerializer(product_question_article, many=True)

        #array waar articles in komen
        queryset = []

        #loop door de product question article(s)
        for item in product_question_article_serializer.data:
            article_id = item['article_id']

            #haalt de article(s) op op basis van id
            article = Article.objects.get(id=article_id)
            #pusht naar array
            queryset.append(article)

        return queryset
