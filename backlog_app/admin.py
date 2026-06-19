from django.contrib import admin
from .models import Projects, Ticket_submissions, Comments

# Register your models here.


admin.site.register(Projects),
admin.site.register(Ticket_submissions),
admin.site.register(Comments)