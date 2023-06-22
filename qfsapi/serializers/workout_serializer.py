from rest_framework import serializers
from qfsapi.models import Workout, WorkoutGroup, Exercise, Member, WorkoutExercise
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer


class WorkoutGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutGroup
        fields = ("id", "name")


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    # order = WorkoutExerciseOrderSerializer()

    class Meta:
        model = Exercise
        fields = ("id", "name", "description", "gif", "exercise_order")
        depth = 1


class WorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    exercises = WorkoutExerciseSerializer(many=True)
    member = MemberSerializer(many=False)

    class Meta:
        model = Workout
        fields = ("id", "name", "description", "exercises", "workout_group", "member")


class WorkoutPlainSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    class Meta:
        model = Workout
        fields = ("id", "name", "description", "exercises", "workout_group")
