from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    description = models.CharField(max_length=400)
    time_required = models.CharField(max_length=15)
    instructions = models.TextField()
