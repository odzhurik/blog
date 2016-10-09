from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def get_absolute_url(self):
     return reverse_lazy("app:test")

    def __str__(self):
        return str(self.date)


class Category(models.Model):
    pass
