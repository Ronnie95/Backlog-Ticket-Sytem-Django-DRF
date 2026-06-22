from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    ROLE_CHOICES = (
        ("SUPERVISOR", "Supervisor"),
        ("SWE", "Software Engineer"),
        ("TEAM_MEMBER", "Team Member"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username

class Projects(models.Model):
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
class Ticket_submissions(models.Model):
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
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="projects") #watch for this


    def __str__(self):
        return self.date


class Comments(models.Model):
    ticket_submission = models.ForeignKey(Ticket_submissions, on_delete=models.CASCADE, related_name="ticket_submission") #watch for this
    authors = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
