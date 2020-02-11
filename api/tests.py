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
        self.client = Client()

    def test_calculates_average(self):
        response = self.client.get(reverse('ratings', args=(self.restaurant_id,)))
        json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['rating'], 1.5)
        self.assertEqual(json['restaurant'], str(self.restaurant_id))


class RequestsTestCase(TestCase):
    def test_can_do_http_requests(self):
        response = requests.get('https://www.google.com')
        self.assertEqual(response.status_code, 200)
        response_json = requests.post(
            'https://jsonplaceholder.typicode.com/todos/',
            data={'payload': 'value'},
            headers={
                'content-type': 'json',
                'Authorization': 'secret_should_be_redacted',
            },
        )
        self.assertEqual(response.status_code, 200)
        response_json = requests.delete('https://jsonplaceholder.typicode.com/todos/1')
        self.assertEqual(response.status_code, 200)

    def test_integration_test(self):
        response = requests.get('https://go-demo-app.undefinedlabs.dev/restaurants')
        self.assertEqual(response.status_code, 200)
