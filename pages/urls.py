from django.urls import path

from .views import home, contact, contact_sent, about, services

urlpatterns = [
    path('', home, name="home"),
    path('services/', services, name="services"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('contact_sent/', contact_sent, name="contact_sent"),
]