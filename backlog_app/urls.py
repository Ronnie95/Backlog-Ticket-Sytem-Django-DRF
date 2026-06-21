from django.urls import path, include
from .views import TicketViewSet, ProjectViewSet, CommentsViewSet, UserViewSet, RegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', UserViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'comments', CommentsViewSet)


urlpatterns = [

    path('',include(router.urls)),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
]