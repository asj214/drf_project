from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
