from rest_framework.permissions import BasePermission


class NotAdminUser(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_staff
