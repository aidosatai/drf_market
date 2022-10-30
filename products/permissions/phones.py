from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    message = 'Пользователь не является Владельцем или Админом'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):

        if hasattr(request.user, 'is_superuser') or hasattr(request.user, 'is_staff') or \
                hasattr(request.user, 'role'):
            if request.user.is_staff or request.user.is_superuser:
                return True
            else:
                if request.user.role == 'admin' or request.user.role == 'manager':
                    return True
                return False
        else:
            return False
