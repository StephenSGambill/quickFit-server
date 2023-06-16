"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member, Workout, CompletedWorkout
from django.contrib.auth.models import User
from qfsapi.serializers import (
    CompletedWorkoutSerializer,
)
from rest_framework.decorators import action


class CompletedWorkoutView(ViewSet):
    """QFS custom workouts view"""

    def list(self, request):
        """Handle GET requests to get all custom workouts for current user

        Returns:
            Response -- JSON serialized list of workouts
        """
        user = User.objects.get(id=request.auth.user.id)
        member = Member.objects.get(user_id=user.id)
        completed_workouts = CompletedWorkout.objects.filter(member_id=member.id)
        serializer = CompletedWorkoutSerializer(completed_workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        member = Member.objects.get(user=request.auth.user)
        workout = Workout.objects.get(id=request.data["workout"])

        new_completed_workout = CompletedWorkout.objects.create(
            member=member,
            workout=workout,
        )

        serializer = CompletedWorkoutSerializer(new_completed_workout, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
