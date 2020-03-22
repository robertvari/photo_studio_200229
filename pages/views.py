from django.shortcuts import render
import random

from .models import HomeMessage
from gallery.models import Photo

def home(request):
    message_object = HomeMessage.objects.all()

    if message_object:
        message_object = message_object[0]

    context = {
        "object": message_object,
        "photo": random.choice(Photo.objects.all())
    }

    return render(request, 'home.html', context)


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')