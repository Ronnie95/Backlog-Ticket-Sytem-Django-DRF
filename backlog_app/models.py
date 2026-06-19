from django.db import models
from django.contrib.auth.models import User


class projects(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dueDate = models.DateField()
    status_choices = (
        ('complete', 'Complete'),
        ('in_progress', 'In Progress'),
        ('not_complete', 'Not Complete'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='not_complete')

    #add the models to admin.py when complete 


# Create your models here.
class ticket_submissions(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    priority_choices = (

        ("LOW", "low"),
        ("MEDIUM", "medium"),
        ("HIGH", "high"),
    )
    priority = models.CharField(max_length=20, choices=priority_choices, default='Low')
    project = models.ForeignKey(projects, on_delete=models.CASCADE, related_name="projects") #watch for this


    def __str__(self):
        return self.date


class Comments(models.Model):
    ticket_submission = models.ForeignKey(ticket_submissions, on_delete=models.CASCADE, related_name="ticket_submission") #watch for this
    authors = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
