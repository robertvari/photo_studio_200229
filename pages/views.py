from django.shortcuts import render


def home(request):
    context = {
        "title": "Wellcome on my page!",
        "message": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. A debitis deleniti inventore numquam.",
        "image": "https://source.unsplash.com/1600x900/?nature,water"
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