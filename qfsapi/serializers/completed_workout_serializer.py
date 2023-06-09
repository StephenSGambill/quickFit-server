from rest_framework import serializers
from qfsapi.models import (
    Workout,
    WorkoutGroup,
    Exercise,
    CompletedWorkout,
    CustomWorkout,
)
from django.contrib.auth.models import User


class CompletedWorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for custom workouts"""

    class Meta:
        model = CompletedWorkout
        fields = ("id", "workout")
        depth = 2
