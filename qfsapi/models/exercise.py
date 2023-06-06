from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    gif = models.URLField("https://giphy.com/clips/theoffice-3rS8HpFMbQzQ7p925V")
