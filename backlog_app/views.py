from django.shortcuts import render
from .models import Projects, Comments, Ticket_submissions
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, Ticket_submissions, CommentsSerializer


# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket_submissions.objects.all()
    serializer_class = Ticket_submissions