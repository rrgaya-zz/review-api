from django.test import TestCase
from reviews.models import Review
from model_bakery import baker

class TestReview(TestCase):
    def test_verifica_review_model(self):
        baker.make(Review)
        self.assertEqual(1, Review.objects.all().count())
