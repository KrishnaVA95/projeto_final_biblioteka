from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Account


class IsAccountOnwer(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account) -> bool:
        return request.user == obj or request.user.is_superuser
    

class IsUserStaff(permissions.BasePermission):
     def has_permission(self, request, view):        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )


class IsUserStaffOrAuth(permissions.BasePermission):
     def has_permission(self, request, view):        
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        
        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )