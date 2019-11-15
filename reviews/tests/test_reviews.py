from django.test import TestCase
from reviews.models import Review
from model_mommy import mommy

class TestReview(TestCase):

    def test_verifica_review_model(self):
        mommy.make(Review)
        self.assertEqual(1, Review.objects.all().count())