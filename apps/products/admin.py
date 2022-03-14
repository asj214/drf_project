from django.conf import settings
from django.contrib import admin
from django.utils import timezone
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = settings.REST_FRAMEWORK.get('PAGE_SIZE', 10)
    list_display = (
        'id',
        'category',
        'user',
        'name',
        'amount',
        'description',
        'created_at',
        'updated_at',
    )
    exclude = ('deleted_at',)
    list_select_related = ('user', 'category',)

    def delete_queryset(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
