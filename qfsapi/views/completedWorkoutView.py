"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import (
    Member,
    Workout,
    CompletedWorkout,
    WorkoutGroup,
    CustomWorkout,
    Exercise,
)
from django.contrib.auth.models import User
from qfsapi.serializers import (
    MemberSerializer,
    WorkoutSerializer,
    CompletedWorkoutSerializer,
    CustomWorkoutSerializer,
)
from rest_framework.decorators import action


class CompletedWorkoutView(ViewSet):
    """QFS custom workouts view"""

    def list(self, request):
        """Handle GET requests to get all custom workouts for current user

        Returns:
            Response -- JSON serialized list of workouts
        """

        custom_workouts = CompletedWorkout.objects.filter(member=request.auth.user.id)
        serializer = CompletedWorkoutSerializer(custom_workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
