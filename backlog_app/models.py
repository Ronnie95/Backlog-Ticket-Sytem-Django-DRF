from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ticket_submissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    priority_choices = (

        ("LOW", "low"),
        ("MEDIUM", "medium"),
        ("HIGH", "high"),
    )
    priority = models.CharField(max_length=20, choices=priority_choices, default='Low')

    def __str__(self):
        return self.date


class projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
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
    tickets = models.ForeignKey(ticket_submissions, on_delete=models.CASCADE, related_name="projects") #watch for this

    #add the models to admin.py when complete 