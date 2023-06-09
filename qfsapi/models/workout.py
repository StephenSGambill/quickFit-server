from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    workout_group = models.ForeignKey("WorkoutGroup", on_delete=models.CASCADE)
    exercises = models.ManyToManyField("Exercise", related_name="workout_exercises")
