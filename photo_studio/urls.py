from django.contrib import admin
from django.urls import path

from pages.views import home, contact, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact),
    path('gallery/', gallery),
]
