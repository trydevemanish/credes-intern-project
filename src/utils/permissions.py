from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_authenticated and request.user.role=='Admin')


class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active)

class IsTaskAssignedToMeOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == "Admin":
            return True
        else:
            return getattr(obj,"assigned_to",None) == request.user.id