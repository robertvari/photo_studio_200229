from django.db import models


class HomeMessage(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.title