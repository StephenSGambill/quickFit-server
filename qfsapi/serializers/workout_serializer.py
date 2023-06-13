from rest_framework import serializers
from qfsapi.models import Workout, WorkoutGroup, Exercise


class WorkoutGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutGroup
        fields = ("id", "name")


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ("id", "name", "description", "gif", "duration", "rest", "iterations")


class WorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    exercises = WorkoutExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = ("id", "name", "description", "exercises", "workout_group")
