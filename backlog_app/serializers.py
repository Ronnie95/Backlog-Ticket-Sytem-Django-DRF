from rest_framework.serializers import ModelSerializer
from .models import Ticket_submissions, Projects, Comments

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket_submissions
        fields = ('id','created_by','date', 'title', 'description', 'priority', 'project') 



class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'created_by', 'date', 'project_name', 'description', 'due_date', 'status',) 



class CommentsSerializer(ModelSerializer):
    model = Comments
    fields = ('id', 'ticket_submission', 'authors', 'text', 'created_at')