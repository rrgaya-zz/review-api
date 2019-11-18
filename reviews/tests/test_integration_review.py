from django.test import TestCase
from reviews.models import Review
from model_bakery import baker


class TestReview(TestCase):
    """Test Review model using baker"""

    def test_should_create_review(self):
        baker.make(Review)
        self.assertEqual(1, Review.objects.all().count())
