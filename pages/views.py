from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1> Hello World! This is my new Django project </h1>")


def gallery(request):
    return HttpResponse("<h1>Gallery Page</h1>")


def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")
