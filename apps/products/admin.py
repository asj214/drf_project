from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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
