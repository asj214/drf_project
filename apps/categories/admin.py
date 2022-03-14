from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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

    def absolute_path(self, obj):
        return ' > '.join(obj.path)

    absolute_path.short_description = '경로'
