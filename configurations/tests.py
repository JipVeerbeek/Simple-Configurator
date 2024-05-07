from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from configurations.models import Configuration, Address
from products.models import Product


class ConfigurationTests(APITestCase):
    def test_get_Configuration(self):
        url = reverse('ConfigurationCreateView')
        product = Product.objects.create(name='Product')
        address1 = Address.objects.create(first_name='fname', last_name='lname', address='address', city="city", postal_code='0000AA')
        address2 = Address.objects.create(first_name='fname', middle_name='mname', last_name='lname', address='address', city="city", postal_code='0000AA')

        data1 = {'product_id': product.id, 'address_id': address1.id}
        data2 = {'product_id': product.id, 'address_id': address2.id}
        data3 = {'product_id': product.id}
        
        response1 = self.client.post(url, data1, format='json')
        response2 = self.client.post(url, data2, format='json')
        response3 = self.client.post(url, data3, format='json')

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Configuration.objects.count(), 3)
