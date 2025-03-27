from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'


class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Editor'


class IsLimitedEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'LimitedEditor'
