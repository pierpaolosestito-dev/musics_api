#Il nostro permesso:
from rest_framework import permissions
class IsPublisherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Quindi vuole leggere
            return True
        if request.method == "PUT" or request.method == "DELETE":
            return request.user.groups.filter(name='publishers').exists()
        if request.method == "POST":
            return request.user.groups.filter(
                name='publishers').exists()
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #Quindi vuole leggere
            return True
        return obj.published_by == request.user