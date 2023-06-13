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
