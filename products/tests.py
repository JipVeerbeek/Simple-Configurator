from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase

from products.factories import ProductFactory
from products.models import Product

from products.serializers import ProductSerializer


class ProductTests(TransactionTestCase):
    def test_get_product(self):
        url = reverse("ProductListView")
        ProductFactory.create_batch(2)

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ProductSerializerTests(TestCase):
    def test_serializer(self):
        expected_data = [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]

        Product.objects.create(name="Product 1")
        Product.objects.create(name="Product 2")

        queryset = Product.objects.all()
        serialized_data = ProductSerializer(queryset, many=True).data

        self.assertEqual(serialized_data, expected_data)
