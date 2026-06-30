from rest_framework.serializers import ModelSerializer
from .models import Ticket_submissions, Projects, Comments, UserProfile
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



# class RegisterSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "email",
#             "password"
#         ]
#         extra_kwargs = {
#             "password": {"write_only": True}
#         }

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


class RegisterSerializer(ModelSerializer):

    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "role"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):

        role = validated_data.pop("role")

        user = User.objects.create_user(
            **validated_data
        )

        UserProfile.objects.create(
            user=user,
            role=role
        )

        return user
    

    

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket_submissions
        fields = ('id','created_by','date', 'title', 'description', 'priority', 'project') 



class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'created_by', 'date', 'project_name', 'description', 'dueDate', 'status',) 



class CommentsSerializer(ModelSerializer):
    model = Comments
    fields = ('id', 'ticket_submission', 'authors', 'text', 'created_at')