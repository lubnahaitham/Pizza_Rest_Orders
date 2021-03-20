from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pizza_Rest, Customers
# Create your tests here.

class Pizaa_RestTest(APITestCase):
    def test_create_pizza(self):
        url = reverse('pizza-list')
        data = {'pizza': 'Pizza_Rest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza_Rest.objects.count(), 1)
        self.assertEqual(Pizza_Rest.objects.get().status_customer, 'Pizza_Rest')


class CustomersTest(APITestCase):
    def test_create_customer(self):
        url = reverse('customer-list')
        data = {'customer': 'Customers'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customers.objects.count(), 1)
        self.assertEqual(Customers.objects.get().customer_id, 'Customers')