import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from reviews.models import Review, Company


class IntegrationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testing"
        )
        self.token = Token.objects.create(user=self.user)
        self.company = baker.make(Company)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_should_post_review(self):
        data = {
            "rating": 5,
            "title": "Test Title",
            "sumary": "Test Sumary",
            "ip_address": "127.0.0.1",
            "submited_date": datetime.datetime.now(),
            "company": 1,
            "reviewer": 1,
        }

        response = self.client.post(reverse("review_create"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)

    def test_should_cant_create_review_with_rating_0(self):
        data = {
            "rating": 0,
            "title": "Test Title",
            "sumary": "Test Sumary",
            "ip_address": "127.0.0.1",
            "submited_date": datetime.datetime.now(),
            "company": 1,
            "reviewer": 1,
        }

        response = self.client.post(reverse("review_create"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Review.objects.count(), 0)