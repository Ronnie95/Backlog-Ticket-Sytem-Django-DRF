from django.shortcuts import render
from .models import Projects, Comments, Ticket_submissions, User
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, TicketSerializer, CommentsSerializer, RegisterSerializer
from rest_framework import generics



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket_submissions.objects.all()
    serializer_class = TicketSerializer