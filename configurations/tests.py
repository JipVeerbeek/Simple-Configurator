from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from configurations.models import Configuration, ConfigurationLine, Address
from products.models import Product, ProductQuestion, ProductQuestionArticle
from questions.models import Question
from articles.models import Article


class ConfigurationTests(APITestCase):

    # todo: use factories
    def setUp(self):
        self.product = Product.objects.create(name='Product')
        self.configuration = Configuration.objects.create(product_id=self.product)
        self.address1 = Address.objects.create(first_name='fname', last_name='lname', address='address', city="city")
        self.address2 = Address.objects.create(first_name='fname', middle_name='mname', last_name='lname', address='address', city="city")
        self.question = Question.objects.create(name='Question')
        self.second_question = Question.objects.create(name='Question2')
        self.product_question = ProductQuestion.objects.create(product_id=self.product, question_id=self.question)
        self.second_product_question = ProductQuestion.objects.create(product_id=self.product, question_id=self.second_question)
        self.article1 = Article.objects.create(name="Content of Article1")
        self.article2 = Article.objects.create(name="Content of Article2")
        self.product_question_article1 = ProductQuestionArticle.objects.create(product_question_id=self.product_question, article_id=self.article1, price=30)
        self.product_question_article2 = ProductQuestionArticle.objects.create(product_question_id=self.product_question, article_id=self.article2, price=70)
        self.product_question_article3 = ProductQuestionArticle.objects.create(product_question_id=self.second_product_question, article_id=self.article2, price=200)
        ConfigurationLine.objects.create(product_question_article_id=self.product_question_article1, configuration_id= self.configuration)
        ConfigurationLine.objects.create(product_question_article_id=self.product_question_article2, configuration_id= self.configuration)
        ConfigurationLine.objects.create(product_question_article_id=self.product_question_article3, configuration_id= self.configuration)


    def test_create_configuration(self):
        # todo: rewrite to factories with create_batch()
        url = reverse('ConfigurationCreateView')

        data1 = {'product_id': self.product.id, 'address_id': self.address1.id}
        data2 = {'product_id': self.product.id, 'address_id': self.address2.id}
        data3 = {'product_id': self.product.id}
        
        response1 = self.client.post(url, data1, format='json')
        response2 = self.client.post(url, data2, format='json')
        response3 = self.client.post(url, data3, format='json')

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Configuration.objects.count(), 4)

    def test_create_configuration_line_answer(self):
        url = reverse('AnswerCreateView')

        # todo: if you don't test a quantity response result, then just testing a
        #       single create action is sufficient
        data1 = {'product_question_article_id': self.product_question_article1.id, 'configuration_id': self.configuration.id}
        data2 = {'product_question_article_id': self.product_question_article2.id, 'configuration_id': self.configuration.id}
        data3 = {'product_question_article_id': self.product_question_article3.id, 'configuration_id': self.configuration.id}

        response1 = self.client.post(url, data1, format='json')
        response2 = self.client.post(url, data2, format='json')
        response3 = self.client.post(url, data3, format='json')        

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)

    def test_get_price_service(self):
        url = reverse('PriceListView', kwargs={'configuration_id': self.configuration.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 300)
