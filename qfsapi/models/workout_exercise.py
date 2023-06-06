from django.db import models
from django.contrib.auth.models import User


class WorkoutExercise(models.Model):
    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
