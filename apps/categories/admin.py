from django.conf import settings
from django.contrib import admin
from django.utils import timezone
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = settings.REST_FRAMEWORK.get('PAGE_SIZE', 10)
    list_display = (
        'id',
        'parent',
        'user',
        'name',
        'absolute_path',
        'depth',
        'order',
        'created_at',
        'updated_at',
    )
    list_select_related = ('user', 'parent',)
    exclude = ('path', 'deleted_at',)

    def delete_queryset(self, request, queryset):
        queryset.update(deleted_at=timezone.now())

    def absolute_path(self, obj):
        return ' > '.join(obj.path)

    absolute_path.short_description = '경로'

