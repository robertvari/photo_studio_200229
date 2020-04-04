from django.shortcuts import render, redirect
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
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            print(name, email, subject, message)
            return redirect("contact_sent")

    return render(request, 'contact.html', {"form": form})


def contact_sent(request):
    return render(request, 'email_sent.html')


def about(request):
    return render(request, 'about.html')