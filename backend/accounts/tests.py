from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class AccountTests(APITestCase):

    def test_register(self):
        url = reverse('accounts:rest_register')
        data = {
            "username": "johndoe",
            "email" : "john@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword123",
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_register_(self):
        url = reverse('accounts:rest_register')
        data = {
            "username": "johndoe",
            "email" : "john@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword1234",
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
