from rest_framework import generics
from .models import Article
from products.models import ProductQuestion, ProductQuestionArticle
from .serializers import ArticleSerializer
from products.serializers import ProductQuestionSerializer, ProductQuestionArticleSerializer


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        #haalt ids op uit url
        product_id = self.kwargs.get('product_id')
        question_id = self.kwargs.get('question_id')

        #haalt product question op waar je de articles van gaat krijgen
        product_question = ProductQuestion.objects.get(product_id=product_id, question_id=question_id)
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