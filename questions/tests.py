from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase

from products.factories import ProductFactory, ProductQuestionFactory
from configurations.factories import ConfigurationFactory


class QuestionTests(TransactionTestCase):
    def test_get_questions(self):
        product = ProductFactory()
        ProductQuestionFactory.create_batch(
            2,
            product=product
        )
        configuration = ConfigurationFactory(product=product)

        url = reverse("QuestionListView", kwargs={"configuration_id": configuration.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
