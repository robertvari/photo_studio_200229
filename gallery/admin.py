from django.contrib import admin

from .models import Category, Photo

admin.site.register(Category)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "uploaded", "image"]
    search_fields = ["title", "comment"]

admin.site.register(Photo, PhotoAdmin)
