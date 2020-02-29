from django.urls import path

from .views import home, contact, gallery, about

urlpatterns = [
    path('', home),
    path('gallery/', gallery),
    path('contact/', contact),
    path('about/', about),
]