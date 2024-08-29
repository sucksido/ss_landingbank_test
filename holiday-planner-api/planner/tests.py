# planner/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_weather_api_valid_request(self):
        response = self.client.get(reverse('weather'), {'latitude': '52.52', 'longitude': '13.41'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_weather_api_invalid_request(self):
        response = self.client.get(reverse('weather'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)