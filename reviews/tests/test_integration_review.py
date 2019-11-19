from django.test import TestCase
from reviews.models import Review
from model_bakery import baker


class TestReview(TestCase):
    """Test Review model using baker"""
    def setUp(self):
        self.review = baker.make(Review)

    def test_should_create_review(self):
        self.assertEqual(1, Review.objects.all().count())

    def test_should_return_title_in_str_method(self):
        result = self.review.__str__()
        self.assertEqual(result, self.review.title)