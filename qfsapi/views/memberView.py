"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer


class MemberView(ViewSet):
    """QFS members view"""

    def list(self, request):
        """Handle GET requests to get all members

        Returns:
            Response -- JSON serialized list of members
        """

        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests to get individual member

        Returns:
            Response -- JSON serialized individual of members
        """

        member = Member.objects.get(user=pk)
        serializer = MemberSerializer(member, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
