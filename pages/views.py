from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
import random

from .models import HomeMessage
from gallery.models import Photo


from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        message_object = HomeMessage.objects.all()
        if message_object:
            message_object = message_object[0]

        context.update({
            "object": message_object,
            "photo": random.choice(Photo.objects.all())
        })

        return context


class ServicesView(TemplateView):
    template_name = 'services.html'


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_sent")

    def form_valid(self, form):
        name = form.data["name"]
        email = form.data["email"]
        subject = form.data["subject"]
        message = form.data["message"]

        print(name, email, subject, message)
        return super().form_valid(form)


class ContactSentView(TemplateView):
    template_name = 'email_sent.html'


class AboutView(TemplateView):
    template_name = 'about.html'
