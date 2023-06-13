"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Exercise, WorkoutGroup
from django.contrib.auth.models import User
from qfsapi.serializers import (
    ExerciseSerializer,
    NewExerciseSerializer,
)


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
            Response -- JSON serialized individual exercise
        """

        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests to create individual exercise

        Returns:
            Response -- JSON serialized individual exercise
        """
        workout_group = WorkoutGroup.objects.get(id=request.data["workout_group"])

        new_exercise = Exercise.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            workout_group=workout_group,
            gif=request.data["gif"],
            duration=request.data["duration"],
            rest=request.data["rest"],
            iterations=request.data["iterations"],
        )
        serialized = NewExerciseSerializer(new_exercise, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an exercise

        Returns:
            Response -- updated exercise
        """

        workout_group = WorkoutGroup.objects.get(id=request.data["workout_group"])
        updated_exercise = Exercise.objects.get(pk=pk)

        updated_exercise.name = request.data["name"]
        updated_exercise.description = request.data["description"]
        updated_exercise.workout_group = workout_group
        updated_exercise.gif = request.data["gif"]
        updated_exercise.duration = request.data["duration"]
        updated_exercise.rest = request.data["rest"]
        updated_exercise.iterations = request.data["iterations"]

        updated_exercise.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy individual exercise

        Returns:
            Response -- JSON response confirming delete or not found
        """

        try:
            exercise = Exercise.objects.get(pk=pk)
            exercise.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exercise.DoesNotExist:
            return Response(
                {"message": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND
            )
