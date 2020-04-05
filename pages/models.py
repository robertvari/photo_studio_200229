from django.db import models
from django.db.models.signals import post_delete
from PIL import Image
import os


class HomeMessage(models.Model):
    title = models.CharField("Cím", max_length=200)
    message = models.TextField("Üzenet")

    class Meta:
        verbose_name_plural = "Home oldal"

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField("Név", max_length=200)
    phone = models.CharField("Telefon", max_length=200)
    profile_pic = models.ImageField("Profilkép", upload_to="media/about")
    message = models.TextField("Magamról")

    class Meta:
        verbose_name_plural = "Magamról"

    def save(self, *args, **kwargs):
        # if photo is being replaced
        self.replace_image()

        super().save(*args, **kwargs)

        # resize uploaded image
        self.resize_image()

    def replace_image(self):
        try:
            about = About.objects.get(id=self.id)
            if about.profile_pic.name != self.profile_pic.name:
                about.profile_pic.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.profile_pic.path
        img = Image.open(image_path)
        max_size = 1500

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self):
        return self.name


def photo_cleanup(sender, instance, **kwargs):
    os.remove(instance.profile_pic.path)


post_delete.connect(photo_cleanup, sender=About)