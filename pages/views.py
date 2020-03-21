from django.shortcuts import render

from .models import HomeMessage


def home(request):
    message_object = HomeMessage.objects.all()

    if message_object:
        message_object = message_object[0]

    context = {
        "object": message_object
    }

    return render(request, 'home.html', context)


def gallery(request):
    return render(request, 'gallery.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')