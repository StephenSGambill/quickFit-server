from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    workout_group = models.ForeignKey("WorkoutGroup", on_delete=models.CASCADE)
    gif = models.URLField(
        default="https://giphy.com/clips/theoffice-3rS8HpFMbQzQ7p925V"
    )
    duration = models.IntegerField(default=30)
    rest = models.IntegerField(default=10)
    iterations = models.IntegerField(default=3)
