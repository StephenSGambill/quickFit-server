from rest_framework import serializers
from qfsapi.models import Workout, WorkoutGroup, Exercise, Member
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer


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
    member = MemberSerializer(many=False)

    class Meta:
        model = Workout
        fields = ("id", "name", "description", "exercises", "workout_group", "member")
