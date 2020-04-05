from django.contrib import admin

from .models import HomeMessage
admin.site.register(HomeMessage)

from .models import About
admin.site.register(About)
