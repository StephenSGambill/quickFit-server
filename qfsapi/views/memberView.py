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

    def update(self, request, pk):
        """Handle PUT requests for a member

        Returns:
            Response -- Empty body with 204 status code
        """

        member = Member.objects.get(user=pk)
        member.motivation = request.data["motivation"]
        member.public = request.data["public"]
        member.pic = request.data["pic"]

        user = User.objects.get(pk=member.user_id)
        user.username = request.data["username"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.email = request.data["email"]

        member.save()
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for members
        Returns:
            Response: None with 204 status code
        """

        try:
            member = Member.objects.get(user=pk)
            member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
