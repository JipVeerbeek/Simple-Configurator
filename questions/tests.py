from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product, ProductQuestion
from .models import Question


class ArticleTests(APITestCase):
    def test_get_articles(self):

        product = Product.objects.create(name='Product')
        second_product = Product.objects.create(name='Product2')

        question = Question.objects.create(name='Question')
        second_question = Question.objects.create(name='Question2')
        third_question = Question.objects.create(name='Question3')
        
        url = reverse('QuestionListView', kwargs={'product_id': product.id})

        ProductQuestion.objects.create(product_id=product, question_id=question)
        ProductQuestion.objects.create(product_id=product, question_id=second_question)
        ProductQuestion.objects.create(product_id=second_product, question_id=third_question)
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
