from rest_framework.permissions import BasePermission



class IsSupervisor(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "SUPERVISOR"
        )


class IsSoftwareEngineer(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "SWE "
        )
    

class IsTeamMember(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "TEAM_MEMBER"
        )