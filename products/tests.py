from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product
from products.serializers import ProductSerializer


class ProductTests(APITestCase):
    def test_get_product(self):
        url = reverse('ProductListView')
        Product.objects.create(name='Product 1')
        Product.objects.create(name='Product 2')
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data[0]['name'], 'Product 1')
        self.assertEqual(response.data[1]['name'], 'Product 2')

    def test_serializer(self):
        expected_data = [{'id': 1, 'name': 'Product 1'}, {'id': 2, 'name': 'Product 2'}]

        Product.objects.create(name='Product 1')
        Product.objects.create(name='Product 2')

        queryset = Product.objects.all()
        serialized_data = ProductSerializer(queryset, many=True).data

        self.assertEqual(serialized_data, expected_data)
