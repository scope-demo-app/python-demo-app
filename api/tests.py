import uuid

from django.test import TestCase, Client
from django.urls import reverse
import requests

from api.models import Rating


class RatingsTestCase(TestCase):
    def setUp(self):
        self.restaurant_id = uuid.uuid4()
        Rating.objects.create(restaurant=self.restaurant_id, rating=1)
        Rating.objects.create(restaurant=self.restaurant_id, rating=2)
        Rating.objects.create(restaurant=self.restaurant_id, rating=3)
        self.client = Client()

    def test_calculates_average(self):
        response = self.client.get(reverse('ratings', args=(self.restaurant_id,)))
        json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['rating'], 2)
        self.assertEqual(json['restaurant'], str(self.restaurant_id))


class RequestsTestCase(TestCase):
    def test_integration_test(self):
        response = requests.get('https://go-demo-app.undefinedlabs.dev/restaurants')
        self.assertEqual(response.status_code, 200)
