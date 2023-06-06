from rest_framework import serializers
from qfsapi.models import Workout, WorkoutGroup, Exercise
from django.contrib.auth.models import User


class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises"""

    class Meta:
        model = Exercise
        fields = ("id", "name", "description", "gif")
