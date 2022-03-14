from django.urls import path
from .views import PurchaseListCreateView


urlpatterns = [
    path(r'purchases', PurchaseListCreateView.as_view()),
]
