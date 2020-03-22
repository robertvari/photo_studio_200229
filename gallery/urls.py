from django.urls import path

from .views import gallery, photo_details_view

urlpatterns = [
    path('', gallery, name="gallery"),
    path('<int:pk>/', photo_details_view, name="photo_details"),
]