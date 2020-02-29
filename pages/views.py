from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')