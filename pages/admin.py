from django.contrib import admin

from .models import HomeMessage
from .models import About
from .models import Services

admin.site.register(HomeMessage)
admin.site.register(About)
admin.site.register(Services)
