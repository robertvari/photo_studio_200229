from django.urls import path

from .views import home, contact, gallery

urlpatterns = [
    path('', home),
    path('gallery/', gallery),
    path('contact/', contact),
]