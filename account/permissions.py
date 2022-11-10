from rest_framework.permissions import BasePermission

from account.models import CustomUser


class IsOwnerOrIsStaff(BasePermission):
    message = 'Пользователь не является Владельцом или Админом!'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_staff or request.user == obj:
            return True
        return False
