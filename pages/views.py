from django.shortcuts import render
import random

from .models import HomeMessage
from gallery.models import Photo


from .forms import ContactForm

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
    form = ContactForm()
    return render(request, 'contact.html', {"form": form})


def about(request):
    return render(request, 'about.html')