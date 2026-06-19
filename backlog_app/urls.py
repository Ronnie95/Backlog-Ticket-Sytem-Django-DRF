from django.urls import path, include
from .views import TicketViewSet, ProjectViewSet, CommentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'comments', CommentsViewSet)



urlpatterns = [
    
    path('',include(router.urls)),
]