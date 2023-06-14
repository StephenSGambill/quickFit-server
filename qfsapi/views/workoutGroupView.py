"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member, Workout, CompletedWorkout, WorkoutGroup, Exercise
from django.contrib.auth.models import User
from qfsapi.serializers import (
    WorkoutSerializer,
    CompletedWorkoutSerializer,
    WorkoutGroupSerializer,
    ExerciseSerializer,
)
from rest_framework.decorators import action


class WorkoutGroupView(ViewSet):
    """QFS workout view"""

    def list(self, request):
        """Handle GET requests to get all workouts

        Returns:
            Response -- JSON serialized list of workouts
        """

        workout_groups = WorkoutGroup.objects.all()
        serializer = WorkoutGroupSerializer(workout_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a specific workout group

        Args:
            request (object): Django request object
            pk (int): Primary key of the workout group to retrieve

        Returns:
            Response -- JSON serialized workout group
        """
        try:
            workout_group = WorkoutGroup.objects.get(pk=pk)
        except WorkoutGroup.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Fetch exercises belonging to the workout group
        exercises = Exercise.objects.filter(workout_group=workout_group)
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
