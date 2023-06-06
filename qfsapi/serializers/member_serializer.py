from rest_framework import serializers
from qfsapi.models import Member
from django.contrib.auth.models import User


class MemberUserSerializer(serializers.ModelSerializer):
    """JSON serialzer for user details for members"""

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class MemberSerializer(serializers.ModelSerializer):
    """JSON serializer for members"""

    user = MemberUserSerializer()

    class Meta:
        model = Member
        fields = ("id", "pic", "user")
