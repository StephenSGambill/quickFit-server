"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member, Workout, CompletedWorkout, WorkoutGroup
from django.contrib.auth.models import User
from qfsapi.serializers import (
    MemberSerializer,
    WorkoutSerializer,
    CompletedWorkoutSerializer,
)
from rest_framework.decorators import action


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

    @action(detail=True, methods=["post"], url_path="complete")
    def complete(self, request, pk):
        """Save current workout as complete for member"""

        try:
            member = Member.objects.get(user=request.auth.user)
            workout = Workout.objects.get(pk=pk)
            completed_workout = CompletedWorkout.objects.create(
                member=member, workout=workout
            )
            completed_workout.save()
            return Response({"message": "Workout marked as complete"})

        except Member.DoesNotExist:
            return Response(
                {"message": "Member not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except Workout.DoesNotExist:
            return Response(
                {"message": "Workout not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @action(methods=["get"], detail=False)
    def completed(self, request):
        """Get the member's completed workouts"""

        try:
            workouts = CompletedWorkout.objects.filter(member_id=request.auth.user.id)
            serializer = CompletedWorkoutSerializer(workouts, many=True)
            return Response(serializer.data)
        except CompletedWorkout.DoesNotExist:
            return Response(
                {"message": "No completed workouts."},
                status=status.HTTP_404_NOT_FOUND,
            )

    @action(detail=False, methods=["get"], url_path="group")
    def workout_group(self, request):
        """Retrieve workout groups based on the id of workout group"""

        group_id = request.query_params.get("id")
        group_id = int(group_id)
        workouts = Workout.objects.filter(workout_group_id=group_id)
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
