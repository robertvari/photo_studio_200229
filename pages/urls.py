from django.urls import path

from .views import home, contact, about, services

urlpatterns = [
    path('', home, name="home"),
    path('services/', services, name="services"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]