from django.urls import path

from .views import home, contact, gallery, about

urlpatterns = [
    path('', home, name="home"),
    path('gallery/', gallery, name="gallery"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
]