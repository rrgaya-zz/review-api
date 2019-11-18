from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reviews.models import Company
from reviews.models import Review
from .serializers import ReviewSerializer


@api_view(["GET"])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def review_list(request):
    try:
        reviews = Review.objects.filter(reviewer=request.user)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def review_create(request):
    if request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            company_data = int(request.data["company"])
            company = Company.objects.get(pk=company_data)
            serializer.save(reviewer=request.user)
            serializer.save(ip_address=request.META["REMOTE_ADDR"])
            serializer.save(company=company)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def review_detail(request, pk):
    """ Retrieve, a review instance.
    """
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
