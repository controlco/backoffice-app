from rest_framework import permissions


class IsPostOrOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST" or request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
