from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAuthor(BasePermission):
    def has_object_permissions(self, request,view,obj):
        return request.user == obj.owner
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user