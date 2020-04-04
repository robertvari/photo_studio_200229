from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Photo


class GalleryView(ListView):
    model = Photo
    template_name = "gallery.html"
    context_object_name = "photos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "categories": Category.objects.all(),
        })
        return context
    
    def get_queryset(self):
        category_name = self.request.GET.get("category")
        photos = Photo.objects.all()

        if category_name:
            photos = Photo.objects.filter(category__title=category_name)

        return photos


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = "photo_details.html"
    context_object_name = "photo"