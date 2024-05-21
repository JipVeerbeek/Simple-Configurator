from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase
from configurations.factories import (
    ConfigurationFactory,
    ConfigurationLineFactory,
    AddressFactory,
)
from configurations.models import Configuration
from products.factories import (
    ProductFactory,
    ProductQuestionFactory,
    ProductQuestionArticleFactory,
)
from configurations.services import PriceService, DiscountPriceService


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
        product_question_article = ProductQuestionArticleFactory(product_question=product_question)

        url = reverse("AnswerCreateView")

        data = {
            "product_question_article": product_question_article.id,
            "configuration": configuration.id,
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PriceServiceTestCase(TransactionTestCase):
    def setUp(self):
        self.configuration = ConfigurationFactory()
        self.lines = ConfigurationLineFactory.create_batch(3, configuration=self.configuration)

    def test_get_order_lines(self):
        lines = PriceService(self.configuration.id).get_order_lines()
        self.assertEqual(len(lines), 3)

    def test_calculate_order_price(self):
        price = PriceService(self.configuration.id).calculate_order_price()
        self.assertIsInstance(price, int)

    def test_get_price(self):
        url = reverse("PriceListView", kwargs={"configuration_id": self.configuration.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_discounted_price(self):
        price = DiscountPriceService(self.configuration.id).calculate_discounted_price(order_price=30)
        price = int(price)

        self.assertEqual(price, 27)
        self.assertIsInstance(price, int)
