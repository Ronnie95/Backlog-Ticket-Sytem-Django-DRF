from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ticket_submissions, projects

class TicketSerializer(ModelSerializer):
    class Meta:
        model = ticket_submissions
        fields = ('id', 'date', 'title', 'description', 'priority', 'user') 



class ProjectSerializer(ModelSerializer):
    class Meta:
        model = projects
        fields = ('id', 'date', 'project_name', 'description', 'due_date', 'status', 'tickets' 'user') 


#add user serializer