from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField("Company name", max_length=255)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.PositiveIntegerField(
        "Rating", validators=(MinValueValidator(1), MaxValueValidator(5))
    )
    title = models.CharField(max_length=64)
    sumary = models.TextField(max_length=10000)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    submited_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review", null=True,
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["submited_date"]

    def __str__(self):
        return self.title
