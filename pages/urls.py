from django.urls import path

from .views import home, contact, gallery, about, services

urlpatterns = [
    path('', home, name="home"),
    path('gallery/', gallery, name="gallery"),
    path('services/', services, name="services"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]