from rest_framework import serializers
from qfsapi.models import CompletedWorkout, WorkoutGroup


class CompletedWorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for custom workouts"""

    class Meta:
        model = CompletedWorkout
        fields = ("id", "member", "workout", "date")
        depth = 1
