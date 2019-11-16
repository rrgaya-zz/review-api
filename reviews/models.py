from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    pass


class Reviewer(models.Model):
    pass


class Review(models.Model):
    rating = models.PositiveIntegerField(
        "Rating", validators=(MinValueValidator(1), MaxValueValidator(5))
    )
    title = models.CharField(max_length=64)
    sumary = models.TextField(max_length=10000)
    ip_address = models.GenericIPAddressField()
    submited_date = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=255)
    reviewer = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.title
