from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user == obj.user:
            return True

    
class IsAdminUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
    