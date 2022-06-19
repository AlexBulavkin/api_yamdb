from rest_framework import permissions


class PostUsersPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
            or request.user.is_superuser)


class PatchUsersPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if obj.role is not None:
            return(
                request.user.role == 'admin'
                and obj.username == request.user.username
            )
        return obj.username == request.user.username
