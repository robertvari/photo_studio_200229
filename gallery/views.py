from django.shortcuts import render

from .models import Category
from utilities.gallery_generator import create_gallery


def gallery(request):
    # temp function for creating random images
    photos = create_gallery(num=20)

    category = request.GET.get("category")
    if category:
        photos = [i for i in photos if i["category"].title == category]

    context = {
        "categories": Category.objects.all(),
        "photos": photos
    }
    return render(request, 'gallery.html', context)
