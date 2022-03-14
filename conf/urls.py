from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.categories.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.purchases.urls')),
]
