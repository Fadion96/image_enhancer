from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
import json
# Create your tests here.

class AccountTests(APITestCase):

    def setUp(self):
        User.objects.create_user("testuser", "test@example.com", "testpassword123")


    def test_register(self):
        url = reverse('accounts:rest_register')
        data = {
            "username": "johndoe",
            "email" : "john@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_register_unmatched_passwords(self):
        url = reverse('accounts:rest_register')
        data = {
            "username": "johndoe",
            "email" : "john@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword1234",
        }
        response = self.client.post(url, data)
        self.assertContains(response, "The two password fields didn\'t match.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_register_existent_username(self):
        url = reverse('accounts:rest_register')
        data = {
            "username" : "testuser",
            "email" : "test2@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword123",
        }
        response = self.client.post(url, data)
        self.assertContains(response, "A user with that username already exists.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_register_existent_email(self):
        url = reverse('accounts:rest_register')
        data = {
            "username" : "testuser2",
            "email" : "test@example.com",
            "password1" : "testpassword123",
            "password2" : "testpassword123",
        }
        response = self.client.post(url, data)
        self.assertContains(response, "A user is already registered with this e-mail address.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        url = reverse("accounts:rest_login")
        data = {
            "username" : "testuser",
            "email" : "test@example.com",
            "password" : "testpassword123"
        }
        response = self.client.post(url, data)
        self.assertContains(response, "key")

    def test_login_nonexistent_user(self):
        url = reverse("accounts:rest_login")
        data = {
            "username" : "testuser2",
            "email" : "test@example.com",
            "password" : "testpassword123"
        }
        response = self.client.post(url, data)
        self.assertContains(response, "Unable to log in with provided credentials.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_login_wrong_password(self):
        url = reverse("accounts:rest_login")
        data = {
            "username" : "testuser",
            "email" : "test@example.com",
            "password" : "testpassword1234"
        }
        response = self.client.post(url, data)
        self.assertContains(response, "Unable to log in with provided credentials.", status_code=status.HTTP_400_BAD_REQUEST)

    def test_user_details(self):
        self.client.login(username="testuser", password="testpassword123")
        url = reverse("accounts:rest_user_details")
        response = self.client.get(url)
        self.assertContains(response, "pk")        

    def test_user_details_not_logged_in(self):
        url = reverse("accounts:rest_user_details")
        response = self.client.get(url)
        self.assertContains(response, "Authentication credentials were not provided.", status_code = status.HTTP_403_FORBIDDEN)

    def test_logout(self):
        self.client.login(username="testuser", password="testpassword123")
        url = reverse("accounts:rest_logout")
        response = self.client.post(url)
        self.assertContains(response, "Successfully logged out.")
        
        url = reverse("accounts:rest_user_details")
        response = self.client.get(url)
        self.assertContains(response, "Authentication credentials were not provided.", status_code = status.HTTP_403_FORBIDDEN)
