from rest_framework.serializers import ModelSerializer
from .models import ticket_submissions, projects, Comments

class TicketSerializer(ModelSerializer):
    class Meta:
        model = ticket_submissions
        fields = ('id','created_by','date', 'title', 'description', 'priority', 'project') 



class ProjectSerializer(ModelSerializer):
    class Meta:
        model = projects
        fields = ('id', 'created_by', 'date', 'project_name', 'description', 'due_date', 'status',) 



class CommentsSerializer(ModelSerializer):
    model = Comments
    fields = ('id', 'ticket_submission', 'authors', 'text', 'created_at')