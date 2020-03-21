from django.shortcuts import render

from .models import Category
from utilities.gallery_generator import create_gallery


def gallery(request):
    # temp function for creating random images
    photos = create_gallery(num=100)

    context = {
        "categories": Category.objects.all(),
        "photos": photos
    }
    return render(request, 'gallery.html', context)
