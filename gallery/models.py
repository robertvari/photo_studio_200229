from django.db import models
from django.db.models.signals import post_delete
import os


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

    def __str__(self):
        return self.title


def photo_cleanup(sender, instance, **kwargs):
    os.remove(instance.image.path)


post_delete.connect(photo_cleanup, sender=Photo)
