from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        if hasattr(obj, 'user'):
            return obj.user == request.user
        return obj == request.user


class BelongToUser(permissions.BasePermission):
    message = 'Not your survey, wen dont allow it'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
