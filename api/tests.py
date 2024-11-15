from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Food

class FoodAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.food_url = '/food/'
        self.food_item = Food.objects.create(name="Pizza", description="Pizza margherita", price=12.5)

    def test_get_food_list(self):
        response = self.client.get(self.food_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_food_item(self):
        data = {
            "name": "Burger",
            "description": "Classic burger",
            "price": 10.0
        }
        response = self.client.post(self.food_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_food_item(self):
        update_url = f'{self.food_url}{self.food_item.id}/'
        data = {
            "name": "Pizza Updated",
            "description": "Updated pizza",
            "price": 13.0
        }
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_food_item(self):
        delete_url = f'{self.food_url}{self.food_item.id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)