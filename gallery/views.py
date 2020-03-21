from django.shortcuts import render

from .models import Category


def gallery(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, 'gallery.html', context)
