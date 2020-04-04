from django.urls import path

from .views import HomeView, ContactView, ContactSentView, AboutView, ServicesView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('services/', ServicesView.as_view(), name="services"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('contact_sent/', ContactSentView.as_view(), name="contact_sent"),
]