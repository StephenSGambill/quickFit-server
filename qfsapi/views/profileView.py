"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from qfsapi.models import Member
from django.contrib.auth.models import User
from qfsapi.serializers import MemberSerializer, MemberUserSerializer
from rest_framework.decorators import action


class ProfileView(ViewSet):
    """QFS members view"""

    @action(methods=["GET"], detail=False, url_path="profile")
    def my_profile(self, request):
        """Get the current user's profile"""
        try:
            user = User.objects.get(id=request.auth.user.id)
            member = Member.objects.get(user_id=user.id)
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # START HERE
    # def update(self, request, pk):
    #     """Handle PUT requests for a member

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     print(request.data)
    #     member = Member.objects.get(user=pk)
    #     member.motivation = request.data["motivation"]
    #     # member.public = request.data["public"]
    #     member.pic = request.data["pic"]

    #     user = User.objects.get(pk=member.user_id)
    #     # user.username = request.data["username"]
    #     user.first_name = request.data["first_name"]
    #     user.last_name = request.data["last_name"]
    #     # user.email = request.data["email"]

    #     member.save()
    #     user.save()

    #     serializer = MemberSerializer(member)
    #     return Response(serializer.data)
