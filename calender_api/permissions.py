from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id is not None

