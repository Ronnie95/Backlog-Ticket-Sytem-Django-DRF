from django.contrib import admin
from .models import projects, ticket_submissions

# Register your models here.


admin.site.register(projects),
admin.site.register(ticket_submissions),