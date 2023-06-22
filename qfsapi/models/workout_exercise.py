from django.db import models
from django.contrib.auth.models import User
import datetime


class WorkoutExercise(models.Model):
    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    exercise = models.ForeignKey(
        "Exercise", on_delete=models.CASCADE, related_name="exercise_order"
    )
    order = models.IntegerField()
