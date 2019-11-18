from django.test import TestCase
from reviews.models import Company
from model_bakery import baker


class TestReview(TestCase):
    """Test Company model using baker"""

    def test_should_create_company(self):
        baker.make(Company)
        self.assertEqual(1, Company.objects.all().count())
