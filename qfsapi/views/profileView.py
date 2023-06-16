"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer
from rest_framework.decorators import action


class ProfileView(ViewSet):
    """QFS members view"""

    def list(self, request):
        """Handle GET requests to member profile

        Returns:
            Response -- JSON serialized member profile
        """

        try:
            user = User.objects.get(id=request.auth.user.id)
            member = Member.objects.get(user_id=user.id)
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["PUT"])
    def edit(self, request):
        """Handle PUT requests for member profile

        Returns:
            Response -- Empty body with 204 status code
        """
        print(request)
        user = User.objects.get(id=request.auth.user.id)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        # user.username = request.data["username"]
        # user.email = request.data["email"]

        member = Member.objects.get(user_id=user.id)
        member.motivation = request.data["motivation"]
        member.pic = request.data["pic"]
        # member.public = request.data["public"]

        user.save()
        member.save()

        serializer = MemberSerializer(member)
        return Response(serializer.data)
