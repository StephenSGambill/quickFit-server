from rest_framework import serializers
from qfsapi.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises"""

    class Meta:
        model = Exercise
        fields = (
            "id",
            "name",
            "description",
            "gif",
            "workout_group",
        )
        depth = 1


class NewExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises"""

    class Meta:
        model = Exercise
        fields = (
            "id",
            "name",
            "description",
            "gif",
            "workout_group",
        )
        depth = 1
