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
    Exercise,
    WorkoutExercise,
)
from django.contrib.auth.models import User
from qfsapi.serializers import (
    WorkoutSerializer,
    CompletedWorkoutSerializer,
    WorkoutPlainSerializer,
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

    def create(self, request):
        """Handle POST requests to create a new workout"""

        workout_group_id = request.data.get("workout_group")
        workout_group = WorkoutGroup.objects.get(id=workout_group_id)

        try:
            workout = Workout.objects.create(
                name=request.data.get("name"),
                description=request.data.get("description"),
                workout_group=workout_group,
                member=Member.objects.get(user_id=request.auth.user),
            )

            exercise_ids = request.data.get("exercises", [])
            exercises = Exercise.objects.filter(id__in=exercise_ids)

            for order, exercise_id in enumerate(exercise_ids, start=1):
                workout_exercise = WorkoutExercise()
                workout_exercise.workout = workout
                workout_exercise.exercise = Exercise.objects.get(id=exercise_id)
                workout_exercise.order = order
                workout_exercise.save()

            workout.exercises.set(exercises)

            serializer = WorkoutSerializer(workout)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except WorkoutGroup.DoesNotExist:
            return Response(
                {"message": "Workout Group not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, pk=None):
        """Handle PUT requests to update a workout"""

        workout_group_id = request.data.get("workout_group")
        workout_group = WorkoutGroup.objects.get(id=workout_group_id)

        try:
            workout = Workout.objects.get(pk=pk)

            workout_group_id = int(request.data["workout_group"])
            workout_group = WorkoutGroup.objects.get(id=workout_group_id)

            workout.name = request.data["name"]
            workout.description = request.data["description"]
            workout.workout_group = workout_group
            workout.save()

            exercise_ids = request.data.get("exercises", [])

            workout_exercises = WorkoutExercise.objects.filter(workout_id=pk)

            if workout_exercises.exists():
                workout_exercises.delete()

            for order, exercise_id in enumerate(exercise_ids, start=1):
                workout_exercise = WorkoutExercise()
                workout_exercise.workout = workout
                workout_exercise.exercise = Exercise.objects.get(id=exercise_id)
                workout_exercise.order = order
                workout_exercise.save()

            workout.exercises.set(exercise_ids)

            serializer = WorkoutPlainSerializer(workout, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Workout.DoesNotExist:
            return Response(
                {"message": "Workout not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete a workout"""

        try:
            workout = Workout.objects.get(pk=pk)
            workout.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Workout.DoesNotExist:
            return Response(
                {"message": "Workout not found"}, status=status.HTTP_404_NOT_FOUND
            )

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
