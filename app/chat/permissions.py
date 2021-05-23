from rest_framework import permissions


class IsSenderOrReceiver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.to_user == request.user or obj.from_user == request.user
        return obj.from_user == request.user
