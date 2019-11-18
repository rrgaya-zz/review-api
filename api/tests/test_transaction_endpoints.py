import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from reviews.models import Review, Company


class TransactionsUrlsTestCase(APITestCase):

    list_url = reverse("review_list")

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@test.com", password="testing"
        )
        self.token = Token.objects.create(user=self.user)
        self.company = baker.make(Company)
        self.review = baker.make(Review)
        self.client = APIClient()
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_should_review_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_review_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_retrive_review_detail(self):
        response = self.client.get(reverse("review_detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_retrive_review_detail_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse("review_detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_retrive_review_detail_non_exist(self):
        response = self.client.get(reverse("review_detail", kwargs={"pk": 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_post_review(self):
        postData = {
            "rating": 2,
            "title": "Test Title",
            "sumary": "Test Sumary",
            "ip_address": "127.0.0.1",
            "submited_date": datetime.datetime.now(),
            "company": 1,
            "reviewer": 1,
        }
        response = self.client.post(reverse("review_create"), postData)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_post_review_with_invalid_data(self):
        postData = {
            "rating": 0,
            "title": "Test Title",
            "sumary": "Test Sumary",
            "ip_address": "127.0.0.1",
            "submited_date": datetime.datetime.now(),
            "company": 1,
            "reviewer": 1,
        }
        response = self.client.post(reverse("review_create"), postData)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_post_review_un_authenticated(self):
        self.client.force_authenticate(user=None)
        postData = {
            "rating": 2,
            "title": "Test Title",
            "sumary": "Test Sumary",
            "ip_address": "127.0.0.1",
            "submited_date": datetime.datetime.now(),
            "company": 1,
            "reviewer": 1,
        }
        response = self.client.post(reverse("review_create"), postData)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_delete_review_authenticated(self):
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_should_delete_review_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
