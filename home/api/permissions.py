from rest_framework import permissions

class MyPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user.id == request.user.id:
            return True
        return request.method in permissions.SAFE_METHODS or request.user.is_staff
    
        # return super().has_object_permission(request, view, obj)