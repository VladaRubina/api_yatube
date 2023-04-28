from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission is for check.

    In case authorised user created the object then to be able
    update the object.
    Otherwise authorised user that has not created the object
    will be able to request SAFE methods only.
    """

    message = 'It is prohibitted to change foreign content!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
