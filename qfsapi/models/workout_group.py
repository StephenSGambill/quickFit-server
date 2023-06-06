from django.db import models
from django.contrib.auth.models import User


class WorkoutGroup(models.Model):
    name = models.CharField(max_length=20)
    exercise = models.ForeignKey("Exercise", models.CASCADE)
