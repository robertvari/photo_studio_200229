from django.shortcuts import render

from .models import Category, Photo
from utilities.gallery_generator import create_gallery

# temp function for creating random images
# photos = create_gallery(num=20)


def gallery(request):
    photo_list = Photo.objects.all()

    category = request.GET.get("category")
    if category:
        photo_list = [i for i in photo_list if i.category.title == category]

    context = {
        "categories": Category.objects.all(),
        "photos": photo_list
    }
    return render(request, 'gallery.html', context)


def photo_details_view(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photo_details.html', {"photo": photo})
