from rest_framework import permissions


class StaffOnly(permissions.BasePermission):
    message = 'You Don\'t Have Permission!!'

    def has_permission(self, request, view):
        return self.chk_permission(request)

    def has_object_permission(self, request, view, obj):
        return self.chk_permission(request)

    def chk_permission(self, request):
        is_authentication = False
        if request.user.is_authenticated and request.user.is_staff:
            is_authentication = True

        return is_authentication


class StaffOrReadOnly(permissions.BasePermission):
    message = 'You Don\'t Have Permission!!'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return self.chk_permission(request)

    def chk_permission(self, request):
        is_authentication = False
        if request.user.is_authenticated and request.user.is_staff:
            is_authentication = True

        return is_authentication
