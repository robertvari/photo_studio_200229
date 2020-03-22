from django.db import models
from django.db.models.signals import post_delete
import os
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="media")
    comment = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # if photo is being replaced
        self.replace_image()

        super(Photo, self).save(*args, **kwargs)

        # resize uploaded image
        self.resize_image()

    def replace_image(self):
        try:
            photo = Photo.objects.get(id=self.id)
            if photo.image.name != self.image.name:
                photo.image.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 1500

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self):
        return self.title


def photo_cleanup(sender, instance, **kwargs):
    os.remove(instance.image.path)


post_delete.connect(photo_cleanup, sender=Photo)
