from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase
from articles.models import Article
from configurations.factories import ConfigurationFactory, ConfigurationLineFactory, AddressFactory
from configurations.models import Address, Configuration, ConfigurationLine
from products.factories import ProductFactory, ProductQuestionFactory, ProductQuestionArticleFactory
from questions.factories import QuestionFactory


class ConfigurationTests(TransactionTestCase):
    def test_create_configuration(self):
        product = ProductFactory()
        address = AddressFactory()
        
        url = reverse("ConfigurationCreateView")

        data1 = {"product": product.id, "address": address.id}
        data2 = {"product": product.id}

        response1 = self.client.post(url, data1, format="json")
        response2 = self.client.post(url, data2, format="json")

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Configuration.objects.count(), 2)

    def test_create_configuration_line_answer(self):
        product = ProductFactory()
        configuration = ConfigurationFactory(product=product)
        product_question = ProductQuestionFactory(product=product)
        product_question_article = ProductQuestionArticleFactory(
            product_question=product_question
        )

        url = reverse("AnswerCreateView")

        # todo: if you don't test a quantity response result, then just testing a
        #       single create action is sufficient
        data = {
            "product_question_article": product_question_article.id,
            "configuration": configuration.id,
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_price_service(self):
        product = ProductFactory()
        product_question = ProductQuestionFactory(product=product)
        configuration = ConfigurationFactory(product=product)
        product_question_article = ProductQuestionArticleFactory(
            product_question=product_question
        )
        ConfigurationLineFactory(
            product_question_article=product_question_article,
            configuration=configuration,
        )
        url = reverse("PriceListView", kwargs={"configuration_id": configuration.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, 300)
