from rest_framework import serializers
from qfsapi.models import WorkoutGroup


class WorkoutGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutGroup
        fields = ("id", "name")
        depth = 1
