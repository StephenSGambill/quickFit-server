"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member, Workout
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer, WorkoutSerializer


class WorkoutView(ViewSet):
    """QFS workout view"""

    def list(self, request):
        """Handle GET requests to get all workouts

        Returns:
            Response -- JSON serialized list of workouts
        """

        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests to get individual workout

        Returns:
            Response -- JSON serialized individual of workout
        """

        workout = Workout.objects.get(pk=pk)
        serializer = WorkoutSerializer(workout, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
