from django.urls import path
from .views import review_list
from .views import review_create
from .views import review_detail


urlpatterns = [
    path("", review_list, name="review_list"),
    path("<int:pk>/", review_detail, name="review_detail"),
    path("create/", review_create, name="review_create"),
]
