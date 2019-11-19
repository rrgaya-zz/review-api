from django.test import TestCase
from reviews.models import Company
from model_bakery import baker


class TestReview(TestCase):
    """Test Company model using baker"""

    def setUp(self):
        self.company = baker.make(Company)

    def test_should_create_company(self):
        self.assertEqual(1, Company.objects.all().count())

    def test_should_return_name_in_str_method(self):
        result = self.company.__str__()
        self.assertEqual(result, self.company.name)