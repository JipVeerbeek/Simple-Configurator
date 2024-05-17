from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product, ProductQuestion
from .models import Question
from configurations.models import Configuration

class ArticleTests(APITestCase):
    def test_get_articles(self):

        product = Product.objects.create(name='Product')
        configuration = Configuration.objects.create(product=product)
        question = Question.objects.create(name='Question')
        second_question = Question.objects.create(name='Question2')
        
        url = reverse('QuestionListView', kwargs={'configuration': configuration.id})

        ProductQuestion.objects.create(product=product, question=question)
        ProductQuestion.objects.create(product=product, question=second_question)
 
        response = self.client.get(url)
 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
