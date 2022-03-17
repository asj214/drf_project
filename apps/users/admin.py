from django.conf import settings
from django.contrib import admin
from django.utils import timezone
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = settings.REST_FRAMEWORK.get('PAGE_SIZE', 10)
    list_display = (
        'id',
        'email',
        'name',
        'is_staff',
        'is_superuser',
        'last_login',
        'created_at',
        'updated_at',
    )
    exclude = ('last_login', 'deleted_at',)

    def delete_queryset(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
