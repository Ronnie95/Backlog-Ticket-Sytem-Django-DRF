from django.shortcuts import render
from .models import Projects, Comments, Ticket_submissions, User
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, TicketSerializer, CommentsSerializer, RegisterSerializer
from rest_framework import generics
from .permissions import IsSoftwareEngineer, IsSupervisor, IsTeamMember
from rest_framework.permissions import IsAuthenticated





class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsSupervisor]
    

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsSoftwareEngineer]
    permission_class = [IsTeamMember]



# class TicketViewSet(ModelViewSet):
#     queryset = Ticket_submissions.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = [IsTeamMember]

class TicketViewSet(ModelViewSet):
    queryset = Ticket_submissions.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.userprofile.role

        if role == "SUPERVISOR":
            return Ticket_submissions.objects.all()

        if role == "SWE":
            return Ticket_submissions.objects.filter(
                assigned_to=user
            )
        
        if role == "TEAM_MEMBER":
            return Ticket_submissions.objects.filter(
                created_by=user
            )

        # return Ticket_submissions.objects.filter(
        #     created_by=user
        # )

        return Ticket_submissions.objects.none()