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


class CustomWorkoutView(ViewSet):
    """QFS custom workouts view"""

    def list(self, request):
        """Handle GET requests to get all custom workouts for current user

        Returns:
            Response -- JSON serialized list of workouts
        """

        custom_workouts = CustomWorkout.objects.filter(member=request.auth.user.id)
        serializer = CustomWorkoutSerializer(custom_workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests to get individual workout

        Returns:
            Response -- JSON serialized individual of workout
        """

        custom_workouts = CustomWorkout.objects.get(pk=pk)
        serializer = CustomWorkoutSerializer(custom_workouts, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete a workout"""
        try:
            custom_workout = CustomWorkout.objects.get(pk=pk)
            member = Member.objects.get(user_id=request.auth.user)
            workout = Workout.objects.get(pk=custom_workout.workout_id)

            if custom_workout.member_id == member.id:
                custom_workout.delete()
                workout.exercises.clear()
                workout.delete()

                return Response(
                    {"message": "Custom workout deleted."},
                    status=status.HTTP_204_NO_CONTENT,
                )
            else:
                return Response(
                    {
                        "message": "You do not have permission to delete this custom workout."
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )
        except CustomWorkout.DoesNotExist:
            return Response(
                {"message": "Custom workout not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def create(self, request):
        workout_group_id = request.data["workout_group"]
        workout_group = WorkoutGroup.objects.get(id=workout_group_id)
        member = Member.objects.get(user=request.auth.user)

        new_workout = Workout.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            workout_group=workout_group,
        )

        new_custom_workout = CustomWorkout.objects.create(
            member=member,
            workout=new_workout,
        )

        exercise_ids = request.data.get("exercises", [])
        exercises = Exercise.objects.filter(id__in=exercise_ids)
        new_workout.exercises.set(exercises)

        serializer = CustomWorkoutSerializer(new_custom_workout, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests to update an existing custom workout"""

        try:
            custom_workout = CustomWorkout.objects.get(pk=pk)
            member = Member.objects.get(user=request.auth.user)

            if custom_workout.member_id == member.id:
                workout_group_id = request.data["workout_group"]
                workout_group = WorkoutGroup.objects.get(id=workout_group_id)

                workout = custom_workout.workout
                workout.name = request.data["name"]
                workout.description = request.data["description"]
                workout.workout_group = workout_group
                workout.save()

                exercise_ids = request.data.get("exercises", [])
                exercises = Exercise.objects.filter(id__in=exercise_ids)
                workout.exercises.set(exercises)

                serializer = CustomWorkoutSerializer(custom_workout, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "message": "You do not have permission to update this custom workout."
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )
        except CustomWorkout.DoesNotExist:
            return Response(
                {"message": "Custom workout not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
