"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member, Workout, Exercise
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer, WorkoutSerializer, ExerciseSerializer


class ExerciseView(ViewSet):
    """QFS exercise view"""

    def list(self, request):
        """Handle GET requests to get all exercises

        Returns:
            Response -- JSON serialized list of exercises
        """

        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests to get individual exercise

        Returns:
            Response -- JSON serialized individual of exercise
        """

        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
