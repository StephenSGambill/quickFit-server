from django.db import models
from django.contrib.auth.models import User
import datetime


class CustomWorkout(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    workout = models.ForeignKey("Workout", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
