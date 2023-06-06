from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    name = models.CharField(max_length=30)
    source = models.URLField()
    credits = models.CharField(max_length=30)
