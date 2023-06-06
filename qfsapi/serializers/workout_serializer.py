from rest_framework import serializers
from qfsapi.models import Workout, WorkoutGroup
from django.contrib.auth.models import User


class WorkoutGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutGroup
        fields = ("id", "name", "exercise")


class WorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    workout_group = WorkoutGroupSerializer(serializers.ModelSerializer)

    class Meta:
        model = Workout
        fields = ("id", "name", "description", "workout_group")
