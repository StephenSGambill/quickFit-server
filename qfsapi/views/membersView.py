"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer


class MembersView(ViewSet):
    """QFS members view"""

    def list(self, request):
        """Handle GET requests to member profile

        Returns:
            Response -- JSON serialized member profile
        """

        try:
            members = Member.objects.all()
            serializer = MemberSerializer(members, many=True)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
