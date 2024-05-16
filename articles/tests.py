from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, ProductQuestion, ProductQuestionArticle
from questions.models import Question
from .models import Article
from configurations.models import Configuration


class ArticleTests(APITestCase):
    def test_get_articles(self):
        # todo: Use your factories
        #       ProductFactory()
        #       this allows you to automatically create a lot of the related objects.

        product = Product.objects.create(name='Product')
        configuration = Configuration.objects.create(product_id=product)
        question = Question.objects.create(name='Question')
        second_question = Question.objects.create(name='Question2')
        # todo: Lines are a little long. Can you configure your IDE to use max length
        #       120 line length and apply it throughout your code? Very useful for split
        #       screen.
        url = reverse('ArticleListView', kwargs={'configuration_id': configuration.id, 'question_id': question.id})

        product_question = ProductQuestion.objects.create(product_id=product, question_id=question)
        second_product_question = ProductQuestion.objects.create(product_id=product, question_id=second_question)
        article1 = Article.objects.create(name="Content of Article1")
        article2 = Article.objects.create(name="Content of Article2")
        ProductQuestionArticle.objects.create(product_question_id=product_question, article_id=article1, price=20)
        ProductQuestionArticle.objects.create(product_question_id=product_question, article_id=article2, price=70)
        ProductQuestionArticle.objects.create(product_question_id=second_product_question, article_id=article2, price=200)
 
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
