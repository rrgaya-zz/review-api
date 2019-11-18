from rest_framework import serializers
from reviews.models import Review, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "name",
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        depth = 1
        fields = (
            "id",
            "rating",
            "title",
            "sumary",
            "ip_address",
            "submited_date",
            "company",
            "reviewer",
        )
